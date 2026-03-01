from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

from scripts.http_client import fetch_text
from scripts.utils import parse_human_date, parse_money


def _clean(text: str) -> str:
    return " ".join(re.sub(r"<[^>]+>", " ", text).split())


def _extract_basic_details(html: str, section_id: str) -> List[Dict[str, Optional[str]]]:
    idx = html.find(f'id="{section_id}"')
    if idx == -1:
        return []
    after = html[idx:]
    ul_start = after.find("<ul>")
    ul_end = after.find("</ul>")
    if ul_start == -1 or ul_end == -1:
        return []
    block = after[ul_start:ul_end]
    items = re.findall(r"<li[^>]*>.*?</li>", block, re.S)
    results = []
    for item in items:
        label_match = re.search(r"basic_detail_label\">\s*(.*?)\s*</span>", item, re.S)
        value_match = re.search(r"basic_detail_value[^>]*>\s*(.*?)\s*</span>", item, re.S)
        date_match = re.search(r"basic_detail_date\">\s*\(([^)]+)\)", item, re.S)
        if not label_match or not value_match:
            continue
        results.append(
            {
                "label": _clean(label_match.group(1)),
                "value": _clean(value_match.group(1)),
                "date": date_match.group(1).strip() if date_match else None,
            }
        )
    return results


def _parse_distribution(value: str) -> tuple[Optional[float], Optional[str]]:
    amount = parse_money(value)
    freq = None
    lower = value.lower()
    if "mo" in lower or "month" in lower:
        freq = "monthly"
    elif "q" in lower or "quarter" in lower:
        freq = "quarterly"
    return amount, freq


def _parse_percent(value: str) -> Optional[float]:
    if not value:
        return None
    match = re.search(r"[-+]?(?:\d*\.\d+|\d+)", value.replace(",", ""))
    if not match:
        return None
    try:
        return float(match.group(0)) / 100.0
    except ValueError:
        return None


def load_brompton_etfs(cfg: Dict[str, Any]) -> Dict[str, Any]:
    pages = cfg.get(
        "pages",
        [
            "https://www.bromptongroup.com/product/brompton-split-corp-enhanced-equity-income-etf/",
            "https://www.bromptongroup.com/product/brompton-split-corp-preferred-share-etf/",
        ],
    )
    preferred_tickers = {t.upper() for t in (cfg.get("preferred_tickers") or ["SPLT"])}

    funds: List[Dict[str, Any]] = []

    for url in pages:
        page = fetch_text(url)

        title_match = re.search(r"<title>(.*?)</title>", page, re.S | re.I)
        title = _clean(title_match.group(1)) if title_match else ""
        ticker = title.split("|", 1)[0].strip().upper() if title else ""
        theme = title.split("|", 1)[-1].strip() if title and "|" in title else (title or None)

        if not ticker:
            continue

        security_type = "PREFERRED" if ticker in preferred_tickers else "CLASS_A"

        basic = _extract_basic_details(page, "basic_detail_1")
        nav = None
        nav_asof = None
        dist_amt = None
        dist_freq = None
        dist_rate = None

        for item in basic:
            label = item.get("label") or ""
            value = item.get("value") or ""
            if label == "NAV":
                nav = parse_money(value)
                if item.get("date"):
                    date = parse_human_date(item["date"])
                    nav_asof = date.isoformat() if date else nav_asof
            elif label == "Distribution":
                dist_amt, dist_freq = _parse_distribution(value)
            elif label.startswith("Distribution Rate"):
                dist_rate = _parse_percent(value)

        fund = {
            "fund_id": ticker,
            "issuer_manager": "Brompton ETF",
            "theme": theme,
            # For ETFs, treat Unit NAV as the reported NAV per unit so the existing UI
            # and flags show a usable NAV value without requiring extra columns.
            "unit_nav": nav,
            "nav_asof_date": nav_asof,
            "securities": [
                {
                    "security_type": security_type,
                    "ticker": ticker,
                    "nav_self": nav,
                }
            ],
        }

        security = fund["securities"][0]
        if security_type == "CLASS_A":
            security["dist_amt"] = dist_amt
            security["dist_freq"] = dist_freq
        else:
            # Map ETF distribution to the preferred cashflow fields so the preferred
            # table can show yield in a consistent way.
            security["pref_div_amt"] = dist_amt
            security["pref_div_freq"] = dist_freq
            security["pref_yield_current"] = dist_rate

        funds.append(fund)

    return {"funds": funds}

