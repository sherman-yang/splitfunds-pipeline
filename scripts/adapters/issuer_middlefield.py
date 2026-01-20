from __future__ import annotations

import re
import urllib.parse
from typing import Any, Dict, List

from scripts.http_client import fetch_text
from scripts.utils import parse_money


def _clean(text: str) -> str:
    return " ".join(re.sub(r"<[^>]+>", " ", text).split())


def _parse_distribution(label: str, value: str) -> tuple[float | None, str | None]:
    amount = parse_money(value)
    freq = None
    label_lower = label.lower()
    if "monthly" in label_lower:
        freq = "monthly"
    elif "quarterly" in label_lower:
        freq = "quarterly"
    return amount, freq


def load_middlefield(cfg: Dict[str, Any]) -> Dict[str, Any]:
    base_url = cfg.get("base_url", "https://www.middlefield.com/funds")
    pref_par_default = cfg.get("pref_par_default", 10.0)
    gate_nav_default = cfg.get("gate_nav_default", 15.0)

    html = fetch_text(base_url)
    links = set(re.findall(r'href="([^"]+)"', html))

    fund_urls = []
    for link in links:
        if "split-share-funds" not in link:
            continue
        fund_urls.append(urllib.parse.urljoin(base_url, link))

    funds: List[Dict[str, Any]] = []

    for url in sorted(set(fund_urls)):
        page = fetch_text(url)
        title_match = re.search(r"<title>(.*?)</title>", page, re.S | re.I)
        title = _clean(title_match.group(1)) if title_match else ""

        pairs = re.findall(
            r'order-text\">\s*(.*?)\s*</div>\s*<span class="f-600">\s*(.*?)\s*</span>',
            page,
            re.S,
        )

        class_ticker = None
        pref_ticker = None
        dist_amt = None
        dist_freq = None
        pref_div_amt = None
        pref_div_freq = None

        for label_raw, value_raw in pairs:
            label = _clean(label_raw)
            value = _clean(value_raw)
            if label.startswith("Ticker/CUSIP (Class A"):
                class_ticker = value.split("/")[0].strip()
            elif label.startswith("Ticker/CUSIP (Preferred"):
                pref_ticker = value.split("/")[0].strip()
            elif "Distribution" in label and "Class A" in label:
                dist_amt, dist_freq = _parse_distribution(label, value)
            elif "Distribution" in label and "Preferred" in label:
                pref_div_amt, pref_div_freq = _parse_distribution(label, value)

        if not class_ticker or not pref_ticker:
            continue

        fund = {
            "fund_id": class_ticker.split(".")[0],
            "issuer_manager": "Middlefield",
            "theme": title.split("|")[0].strip() if title else None,
            "pref_par": pref_par_default,
            "gate_nav": gate_nav_default,
            "securities": [
                {
                    "security_type": "CLASS_A",
                    "ticker": class_ticker,
                    "dist_amt": dist_amt,
                    "dist_freq": dist_freq,
                },
                {
                    "security_type": "PREFERRED",
                    "ticker": pref_ticker,
                    "pref_div_amt": pref_div_amt,
                    "pref_div_freq": pref_div_freq,
                },
            ],
        }
        funds.append(fund)

    return {"funds": funds}
