from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.compute_metrics import compute_metrics
from scripts.scoring import score_rows
from scripts.sitegen.render_index import render_site
from scripts.utils import (
    asof_timestamp,
    load_adapter,
    load_config,
    parse_iso_date,
    safe_float,
    write_json,
)
from scripts.validate import validate_rows


OUTPUT_FIELDS = [
    "fund_id",
    "security_type",
    "ticker",
    "asof",
    "issuer_manager",
    "theme",
    "holdings_hint",
    "maturity_date",
    "final_maturity_date",
    "extendable",
    "extend_terms_text",
    "pref_par",
    "gate_nav",
    "gate_rule_text",
    "unit_nav",
    "nav_self",
    "nav_asof_date",
    "price",
    "price_kind",
    "price_asof",
    "volume",
    "high_52w",
    "low_52w",
    "tr_1y",
    "tr_3y",
    "tr_5y",
    "tr_10y",
    "tr_method",
    "dist_amt",
    "dist_freq",
    "dist_status",
    "roc_flag",
    "roc_ratio",
    "pref_div_amt",
    "pref_div_freq",
    "pref_div_cash_annual",
    "pref_div_kind",
    "pref_yield_issue",
    "pref_yield_current",
    "source_price",
    "source_nav",
    "source_terms",
    "cushion",
    "coverage",
    "distance_to_gate",
    "classa_intrinsic",
    "leverage_th",
    "leverage_mkt",
    "discount_to_nav",
    "discount_to_par",
    "discount_to_intrinsic",
    "annualized_discount_to_nav",
    "annualized_discount_to_par",
    "annualized_discount_to_intrinsic",
    "years_to_maturity",
    "years_to_first_maturity",
    "years_to_final_maturity",
    "score_conservative",
    "score_aggressive",
    "flags",
    "near_gate",
    "nav_missing",
    "intrinsic_le_0",
    "dist_suspended",
    "low_liquidity",
]


def _merge_security(existing: Dict[str, Any], incoming: Dict[str, Any]) -> Dict[str, Any]:
    merged = existing.copy()
    for key, value in incoming.items():
        if merged.get(key) is None and value is not None:
            merged[key] = value
    return merged


def _merge_fund(existing: Dict[str, Any], incoming: Dict[str, Any]) -> Dict[str, Any]:
    merged = existing.copy()
    for key, value in incoming.items():
        if key == "securities":
            continue
        if merged.get(key) is None and value is not None:
            merged[key] = value
    merged["fund_id"] = incoming.get("fund_id") or merged.get("fund_id")

    securities: Dict[str, Dict[str, Any]] = {}
    for item in existing.get("securities", []) + incoming.get("securities", []):
        ticker = item.get("ticker")
        if not ticker:
            continue
        current = securities.get(ticker, {})
        securities[ticker] = _merge_security(current, item)
    merged["securities"] = list(securities.values())
    return merged


def _merge_funds(primary: List[Dict[str, Any]], secondary: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged: Dict[str, Dict[str, Any]] = {}
    for fund in primary:
        fund_id = fund.get("fund_id")
        if fund_id:
            merged[fund_id] = fund
    for fund in secondary:
        fund_id = fund.get("fund_id")
        if not fund_id:
            continue
        if fund_id in merged:
            merged[fund_id] = _merge_fund(merged[fund_id], fund)
        else:
            merged[fund_id] = fund
    return list(merged.values())


def resolve_universe(universe_cfg: Dict[str, Any]) -> Dict[str, Any]:
    adapter_path = universe_cfg.get("adapter")
    adapter_args = universe_cfg.get("adapter_args", {})
    static_funds = universe_cfg.get("funds", [])

    if adapter_path:
        adapter = load_adapter(adapter_path)
        if isinstance(adapter_args, dict):
            dynamic = adapter(**adapter_args)
        else:
            dynamic = adapter(adapter_args)
        dynamic_funds = dynamic.get("funds", [])
        merged = _merge_funds(dynamic_funds, static_funds)
        return {"funds": merged}

    return universe_cfg


def build_base_rows(universe_cfg: Dict[str, Any], asof: str, source_terms: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for fund in universe_cfg.get("funds", []):
        fund_base = {
            "fund_id": fund.get("fund_id"),
            "issuer_manager": fund.get("issuer_manager"),
            "theme": fund.get("theme"),
            "holdings_hint": fund.get("holdings_hint"),
            "maturity_date": fund.get("maturity_date"),
            "final_maturity_date": fund.get("final_maturity_date"),
            "extendable": fund.get("extendable", False),
            "extend_terms_text": fund.get("extend_terms_text"),
            "pref_par": fund.get("pref_par"),
            "gate_nav": fund.get("gate_nav"),
            "gate_rule_text": fund.get("gate_rule_text"),
            "source_terms": source_terms,
        }
        for security in fund.get("securities", []):
            row = {
                **fund_base,
                "security_type": security.get("security_type"),
                "ticker": security.get("ticker"),
                "dist_amt": security.get("dist_amt"),
                "dist_freq": security.get("dist_freq"),
                "dist_status": security.get("dist_status"),
                "roc_flag": security.get("roc_flag"),
                "roc_ratio": security.get("roc_ratio"),
                "pref_div_amt": security.get("pref_div_amt"),
                "pref_div_freq": security.get("pref_div_freq"),
                "pref_div_kind": security.get("pref_div_kind"),
                "pref_yield_issue": security.get("pref_yield_issue"),
                "nav_self": security.get("nav_self"),
                "price": security.get("price"),
                "price_asof": security.get("price_asof"),
                "asof": asof,
            }
            rows.append(row)
    return rows


def _merge_row(target: Dict[str, Any], source: Dict[str, Any]) -> None:
    for key, value in source.items():
        if target.get(key) is None and value is not None:
            target[key] = value


def augment_rows_from_funds(rows: List[Dict[str, Any]], funds: List[Dict[str, Any]], asof: str, source_terms: str) -> None:
    extra_rows = build_base_rows({"funds": funds}, asof, source_terms)
    row_by_ticker = {row.get("ticker"): row for row in rows if row.get("ticker")}
    for row in extra_rows:
        ticker = row.get("ticker")
        if not ticker:
            continue
        existing = row_by_ticker.get(ticker)
        if existing is None:
            rows.append(row)
            row_by_ticker[ticker] = row
        else:
            _merge_row(existing, row)


def apply_issuer(rows: List[Dict[str, Any]], issuer_data: Dict[str, Any], source_name: str) -> None:
    fund_lookup = {fund["fund_id"]: fund for fund in issuer_data.get("funds", []) if fund.get("fund_id")}
    row_by_ticker = {row["ticker"]: row for row in rows if row.get("ticker")}

    for fund_id, fund in fund_lookup.items():
        for row in rows:
            if row.get("fund_id") != fund_id:
                continue
            for key in [
                "issuer_manager",
                "theme",
                "holdings_hint",
                "maturity_date",
                "final_maturity_date",
                "extendable",
                "extend_terms_text",
                "pref_par",
                "gate_nav",
                "gate_rule_text",
            ]:
                if fund.get(key) is not None:
                    row[key] = fund.get(key)
            if fund.get("unit_nav") is not None:
                row["unit_nav"] = fund.get("unit_nav")
                row["nav_asof_date"] = fund.get("nav_asof_date") or issuer_data.get("asof_date")
                row["source_nav"] = source_name
        for security in fund.get("securities", []):
            ticker = security.get("ticker")
            if not ticker:
                continue
            row = row_by_ticker.get(ticker)
            if not row:
                continue
            if security.get("nav_self") is not None:
                row["nav_self"] = security.get("nav_self")
                row["source_nav"] = source_name
            if security.get("dist_status") is not None:
                row["dist_status"] = security.get("dist_status")
            if security.get("dist_amt") is not None:
                row["dist_amt"] = security.get("dist_amt")
            if security.get("dist_freq") is not None:
                row["dist_freq"] = security.get("dist_freq")
            if security.get("pref_div_amt") is not None:
                row["pref_div_amt"] = security.get("pref_div_amt")
            if security.get("pref_div_freq") is not None:
                row["pref_div_freq"] = security.get("pref_div_freq")
            if security.get("price") is not None:
                row["price"] = security.get("price")
            if security.get("price_asof") is not None:
                row["price_asof"] = security.get("price_asof")


def apply_quotes(rows: List[Dict[str, Any]], quote_data: Dict[str, Any], source_name: str) -> None:
    quote_map = {item["ticker"]: item for item in quote_data.get("rows", []) if item.get("ticker")}
    for row in rows:
        ticker = row.get("ticker")
        if not ticker:
            continue
        quote = quote_map.get(ticker)
        if not quote:
            continue
        row["price"] = quote.get("price")
        row["price_kind"] = quote.get("price_kind") or "close"
        row["price_asof"] = quote.get("price_asof") or quote_data.get("asof")
        row["volume"] = quote.get("volume")
        row["high_52w"] = quote.get("high_52w")
        row["low_52w"] = quote.get("low_52w")
        row["tr_1y"] = quote.get("tr_1y")
        row["tr_3y"] = quote.get("tr_3y")
        row["tr_5y"] = quote.get("tr_5y")
        row["tr_10y"] = quote.get("tr_10y")
        row["tr_method"] = quote.get("tr_method") or quote_data.get("tr_method")
        row["source_price"] = source_name


def propagate_pref_yield(rows: List[Dict[str, Any]]) -> None:
    pref_yield_by_fund = {}
    for row in rows:
        if row.get("security_type") == "PREFERRED":
            yield_current = safe_float(row.get("pref_yield_current"))
            if yield_current is not None:
                pref_yield_by_fund[row.get("fund_id")] = yield_current

    for row in rows:
        if row.get("security_type") == "CLASS_A":
            if row.get("pref_yield_current") is None:
                row["pref_yield_current"] = pref_yield_by_fund.get(row.get("fund_id"))


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        for row in rows:
            flat_row = row.copy()
            if isinstance(flat_row.get("flags"), list):
                flat_row["flags"] = ";".join(flat_row.get("flags"))
            writer.writerow({field: flat_row.get(field) for field in OUTPUT_FIELDS})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config", help="Config directory")
    parser.add_argument("--output", default="site", help="Output directory")
    parser.add_argument("--asof", default=None, help="Override asof timestamp (ISO8601)")
    args = parser.parse_args()

    root = Path.cwd()
    config_dir = root / args.config
    output_dir = root / args.output

    universe_cfg = resolve_universe(load_config(config_dir / "universe.yaml"))
    sources_cfg = load_config(config_dir / "sources.yaml")
    scoring_cfg = load_config(config_dir / "scoring.yaml")

    now = datetime.now(timezone.utc)
    if args.asof:
        try:
            now = datetime.fromisoformat(args.asof.replace("Z", "+00:00"))
        except ValueError:
            raise SystemExit("Invalid --asof timestamp")

    asof = asof_timestamp(now)

    quotes_path = root / sources_cfg.get("paths", {}).get("quotes", "data/source/quotes.json")
    issuer_path = root / sources_cfg.get("paths", {}).get("issuer", "data/source/issuer_daily.json")

    quote_adapter_path = sources_cfg.get("quote_adapter", "scripts.adapters.local_quotes:load_quotes")
    issuer_adapter_path = sources_cfg.get("issuer_adapter", "scripts.adapters.local_issuer:load_issuer")

    quote_loader = load_adapter(quote_adapter_path)
    issuer_loader = load_adapter(issuer_adapter_path)

    quote_data = quote_loader(quotes_path)
    issuer_data = issuer_loader(issuer_path)

    rows = build_base_rows(universe_cfg, asof, sources_cfg.get("terms_source", "config"))
    augment_rows_from_funds(rows, issuer_data.get("funds", []), asof, sources_cfg.get("terms_source", "config"))

    apply_quotes(rows, quote_data, sources_cfg.get("price_source", "local_quotes"))
    apply_issuer(rows, issuer_data, sources_cfg.get("nav_source", "local_issuer"))

    asof_date = parse_iso_date(asof)
    if asof_date is None:
        asof_date = now.date()

    compute_metrics(rows, asof_date)
    propagate_pref_yield(rows)
    score_rows(rows, scoring_cfg)
    report = validate_rows(rows)

    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    write_json(data_dir / "latest.json", rows)
    write_csv(data_dir / "latest.csv", rows)
    write_json(root / "data" / "run_report.json", report)

    render_site(output_dir)


if __name__ == "__main__":
    main()
