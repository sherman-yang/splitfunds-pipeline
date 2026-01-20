from __future__ import annotations

import urllib.parse
from typing import Any, Dict, List

from scripts.http_client import fetch_json


def _infer_security_type(ticker: str) -> str:
    upper = ticker.upper()
    if ".PR" in upper:
        return "PREFERRED"
    return "CLASS_A"


def _merge_security(securities: List[Dict[str, Any]], security: Dict[str, Any]) -> None:
    existing = {item.get("ticker"): item for item in securities}
    ticker = security.get("ticker")
    if not ticker:
        return
    if ticker in existing:
        return
    securities.append(security)


def load_universe(
    exchange: str = "tsx",
    queries: List[str] | None = None,
    require_preferred: bool = True,
    exclude_keywords: List[str] | None = None,
) -> Dict[str, Any]:
    queries = queries or ["split"]
    exclude_keywords = [word.lower() for word in (exclude_keywords or ["etf"])]

    funds: Dict[str, Dict[str, Any]] = {}

    for query in queries:
        safe_query = urllib.parse.quote(query)
        url = f"https://www.tsx.com/json/company-directory/search/{exchange}/{safe_query}"
        data = fetch_json(url)
        for result in data.get("results", []):
            name = result.get("name") or ""
            if any(word in name.lower() for word in exclude_keywords):
                continue
            instruments = result.get("instruments", [])
            if require_preferred and not any(
                ".PR" in (instrument.get("symbol") or "").upper() for instrument in instruments
            ):
                continue
            fund_id = result.get("symbol") or ""
            if not fund_id:
                continue
            fund = funds.setdefault(
                fund_id,
                {
                    "fund_id": fund_id,
                    "theme": name,
                    "securities": [],
                },
            )
            for instrument in instruments:
                ticker = instrument.get("symbol")
                if not ticker:
                    continue
                security = {
                    "security_type": _infer_security_type(ticker),
                    "ticker": ticker,
                }
                _merge_security(fund["securities"], security)

    return {"funds": list(funds.values())}
