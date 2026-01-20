from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from scripts.utils import read_json


def load_quotes(source: Any) -> Dict[str, Any]:
    """Load quote data from a local JSON file.

    Expected shape:
    {
      "asof": "2026-01-02T20:00:00Z",
      "tr_method": "total_return",
      "rows": [
        {
          "ticker": "DFN",
          "price": 7.8,
          "price_kind": "close",
          "volume": 123456,
          "high_52w": 9.2,
          "low_52w": 5.6,
          "price_asof": "2026-01-02T20:00:00Z",
          "tr_1y": 0.12,
          "tr_3y": 0.25,
          "tr_5y": 0.41,
          "tr_10y": 0.85
        }
      ]
    }
    """
    path = None
    if isinstance(source, dict):
        path_value = source.get("path")
        if path_value:
            path = Path(path_value)
    else:
        path = Path(source)

    if not path:
        return {"asof": None, "tr_method": None, "rows": []}
    data = read_json(path)
    if not data:
        return {"asof": None, "tr_method": None, "rows": []}
    return data
