from __future__ import annotations

import urllib.parse
from typing import Any, Dict, Iterable, List

from scripts.http_client import fetch_json


def _to_decimal(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value) / 100
    except (TypeError, ValueError):
        return None


def _chunk(items: List[str], size: int) -> Iterable[List[str]]:
    for i in range(0, len(items), size):
        yield items[i : i + size]


def load_stockanalysis(payload: Dict[str, Any]) -> Dict[str, Any]:
    tickers = payload.get("tickers") or []
    if not tickers:
        return {"asof": payload.get("asof"), "rows": [], "tr_method": "total_return"}

    exchange = payload.get("exchange", "TSX")
    chunk_size = int(payload.get("chunk_size", 50))
    columns = payload.get(
        "columns",
        [
            "price",
            "volume",
            "low52",
            "high52",
            "tr1y",
            "tr3y",
            "tr5y",
            "tr10y",
        ],
    )

    rows: List[Dict[str, Any]] = []

    for chunk in _chunk(list(tickers), chunk_size):
        symbols = [f"@{exchange}:{ticker}" for ticker in chunk]
        params = urllib.parse.urlencode({
            "symbols": ",".join(symbols),
            "columns": ",".join(columns),
        })
        url = f"https://stockanalysis.com/api/watchlist/?{params}"
        data = fetch_json(url)
        for item in data.get("data", []):
            symbol = item.get("s") or ""
            ticker = symbol.split(":", 1)[-1] if ":" in symbol else symbol
            row = {
                "ticker": ticker,
                "price": item.get("price"),
                "volume": item.get("volume"),
                "low_52w": item.get("low52"),
                "high_52w": item.get("high52"),
                "tr_1y": _to_decimal(item.get("tr1y")),
                "tr_3y": _to_decimal(item.get("tr3y")),
                "tr_5y": _to_decimal(item.get("tr5y")),
                "tr_10y": _to_decimal(item.get("tr10y")),
                "price_kind": "last",
                "price_asof": payload.get("asof"),
            }
            rows.append(row)

    return {
        "asof": payload.get("asof"),
        "rows": rows,
        "tr_method": "total_return",
    }
