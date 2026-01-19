from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from scripts.utils import read_json


def load_issuer(path: Path) -> Dict[str, Any]:
    """Load issuer NAV/terms updates from a local JSON file.

    Expected shape:
    {
      "asof_date": "2026-01-01",
      "funds": [
        {
          "fund_id": "DFN",
          "unit_nav": 15.8,
          "nav_asof_date": "2026-01-01",
          "securities": [
            {"ticker": "DFN", "nav_self": 5.8, "dist_status": "paying"},
            {"ticker": "DFN.PR.A", "nav_self": 10.0}
          ]
        }
      ]
    }
    """
    data = read_json(path)
    if not data:
        return {"asof_date": None, "funds": []}
    return data
