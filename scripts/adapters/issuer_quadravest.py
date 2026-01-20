from __future__ import annotations

import re
from typing import Any, Dict, List

from scripts.http_client import fetch_text


def _clean(text: str) -> str:
    return " ".join(re.sub(r"<[^>]+>", " ", text).split())


def _extract_tickers(text: str) -> List[str]:
    return re.findall(r"TSX:\s*([A-Z0-9\.]+)", text)


def load_quadravest(cfg: Dict[str, Any]) -> Dict[str, Any]:
    pages = cfg.get(
        "pages",
        [
            "https://www.quadravest.com/commerce-split-home",
            "https://www.quadravest.com/lifesplit-home",
            "https://www.quadravest.com/m-split-home",
            "https://www.quadravest.com/tdb-split-home",
        ],
    )
    pref_par_default = cfg.get("pref_par_default", 10.0)
    gate_nav_default = cfg.get("gate_nav_default", 15.0)

    funds: List[Dict[str, Any]] = []

    for url in pages:
        page = fetch_text(url)
        title_match = re.search(r"<title>(.*?)</title>", page, re.S | re.I)
        title = _clean(title_match.group(1)) if title_match else ""
        tickers = _extract_tickers(page)
        class_ticker = None
        pref_ticker = None
        for ticker in tickers:
            if ".PR" in ticker and pref_ticker is None:
                pref_ticker = ticker
            elif ".PR" not in ticker and class_ticker is None:
                class_ticker = ticker
        if not class_ticker or not pref_ticker:
            continue

        fund = {
            "fund_id": class_ticker.split(".")[0],
            "issuer_manager": "Quadravest",
            "theme": title.split("|")[0].strip() if title else None,
            "pref_par": pref_par_default,
            "gate_nav": gate_nav_default,
            "securities": [
                {
                    "security_type": "CLASS_A",
                    "ticker": class_ticker,
                },
                {
                    "security_type": "PREFERRED",
                    "ticker": pref_ticker,
                },
            ],
        }
        funds.append(fund)

    return {"funds": funds}
