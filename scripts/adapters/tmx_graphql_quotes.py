from __future__ import annotations

from typing import Any, Dict, Iterable, List

from scripts.http_client import post_json

QUERY = """
query getQuoteBySymbol($symbol: String, $locale: String) {
  getQuoteBySymbol(symbol: $symbol, locale: $locale) {
    symbol
    name
    price
    volume
    weeks52high
    weeks52low
    close
  }
}
"""


def _chunk(items: List[str], size: int) -> Iterable[List[str]]:
    for i in range(0, len(items), size):
        yield items[i : i + size]


def load_tmx_quotes(payload: Dict[str, Any]) -> Dict[str, Any]:
    tickers = payload.get("tickers") or []
    if not tickers:
        return {"asof": payload.get("asof"), "rows": [], "tr_method": None}

    locale = payload.get("locale", "en")
    chunk_size = int(payload.get("chunk_size", 20))

    rows: List[Dict[str, Any]] = []
    endpoint = "https://app-money.tmx.com/graphql"
    headers = {
        "Origin": "https://money.tmx.com",
        "Referer": "https://money.tmx.com/",
    }

    for group in _chunk(list(tickers), chunk_size):
        for ticker in group:
            variables = {"symbol": ticker, "locale": locale}
            payload_body = {"query": QUERY, "variables": variables}
            data = post_json(endpoint, payload_body, headers=headers)
            quote = (data.get("data") or {}).get("getQuoteBySymbol")
            if not quote:
                continue
            rows.append(
                {
                    "ticker": quote.get("symbol") or ticker,
                    "price": quote.get("price"),
                    "volume": quote.get("volume"),
                    "low_52w": quote.get("weeks52low"),
                    "high_52w": quote.get("weeks52high"),
                    "price_kind": "last",
                    "price_asof": payload.get("asof"),
                    "source_price": "tmx_graphql",
                }
            )

    return {"asof": payload.get("asof"), "rows": rows, "tr_method": None}
