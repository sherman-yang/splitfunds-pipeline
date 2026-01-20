from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from scripts.utils import load_adapter, load_config


def _merge_security_list(primary: List[Dict[str, Any]], secondary: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged: Dict[str, Dict[str, Any]] = {}
    for item in primary + secondary:
        ticker = item.get("ticker")
        if not ticker:
            continue
        existing = merged.get(ticker, {})
        for key, value in item.items():
            if existing.get(key) is None and value is not None:
                existing[key] = value
        merged[ticker] = existing
    return list(merged.values())


def _merge_funds(primary: List[Dict[str, Any]], secondary: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged: Dict[str, Dict[str, Any]] = {}
    for fund in primary + secondary:
        fund_id = fund.get("fund_id")
        if not fund_id:
            continue
        existing = merged.get(fund_id, {})
        for key, value in fund.items():
            if key == "securities":
                continue
            if existing.get(key) is None and value is not None:
                existing[key] = value
        existing["fund_id"] = fund_id
        existing["securities"] = _merge_security_list(existing.get("securities", []), fund.get("securities", []))
        merged[fund_id] = existing
    return list(merged.values())


def load_issuer(config_path: Path) -> Dict[str, Any]:
    cfg = load_config(config_path)
    funds: List[Dict[str, Any]] = []

    for issuer_cfg in cfg.get("issuers", []):
        adapter_path = issuer_cfg.get("adapter")
        if not adapter_path:
            continue
        adapter = load_adapter(adapter_path)
        data = adapter(issuer_cfg)
        funds = _merge_funds(funds, data.get("funds", []))

    asof_date = datetime.now(timezone.utc).date().isoformat()
    return {"asof_date": asof_date, "funds": funds}
