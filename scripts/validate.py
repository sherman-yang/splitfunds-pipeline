from __future__ import annotations

from typing import Dict, Any, Iterable

from scripts.utils import safe_float


LOW_LIQUIDITY_THRESHOLD = 5000
DISCOUNT_EXTREME_HIGH = 0.8
DISCOUNT_EXTREME_LOW = -0.5


def validate_rows(rows: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    report = {
        "invalid": 0,
        "warnings": 0,
        "flag_counts": {},
    }

    for row in rows:
        flags = []

        price = safe_float(row.get("price"))
        pref_par = safe_float(row.get("pref_par"))
        unit_nav = safe_float(row.get("unit_nav"))
        coverage = safe_float(row.get("coverage"))
        volume = safe_float(row.get("volume"))
        distance_to_gate = safe_float(row.get("distance_to_gate"))
        intrinsic = safe_float(row.get("classa_intrinsic"))
        discount_to_intrinsic = safe_float(row.get("discount_to_intrinsic"))
        discount_to_par = safe_float(row.get("discount_to_par"))

        if price is None or price <= 0:
            flags.append("price_invalid")
        instrument_kind = (row.get("instrument_kind") or "split").lower()
        is_etf = instrument_kind == "etf"
        if not is_etf and (pref_par is None or pref_par <= 0):
            flags.append("pref_par_invalid")
        if unit_nav is None or unit_nav <= 0:
            flags.append("nav_missing")
        if coverage is not None and coverage < 1.0:
            flags.append("coverage_lt_1")
        if discount_to_intrinsic is not None:
            if discount_to_intrinsic > DISCOUNT_EXTREME_HIGH or discount_to_intrinsic < DISCOUNT_EXTREME_LOW:
                flags.append("discount_extreme")
        if discount_to_par is not None:
            if discount_to_par > DISCOUNT_EXTREME_HIGH or discount_to_par < DISCOUNT_EXTREME_LOW:
                flags.append("discount_extreme")

        if volume is None:
            flags.append("liquidity_unknown")
        elif volume <= LOW_LIQUIDITY_THRESHOLD:
            flags.append("low_liquidity")

        if distance_to_gate is not None and distance_to_gate < 1.0:
            flags.append("near_gate")

        if row.get("dist_status") == "suspended":
            flags.append("dist_suspended")

        if intrinsic is not None and intrinsic <= 0:
            flags.append("intrinsic_le_0")

        row["flags"] = flags
        row["near_gate"] = "near_gate" in flags
        row["nav_missing"] = "nav_missing" in flags
        row["intrinsic_le_0"] = "intrinsic_le_0" in flags
        row["dist_suspended"] = "dist_suspended" in flags
        row["low_liquidity"] = "low_liquidity" in flags

        if "price_invalid" in flags or "pref_par_invalid" in flags:
            report["invalid"] += 1
        if flags:
            report["warnings"] += 1

        for flag in flags:
            report["flag_counts"][flag] = report["flag_counts"].get(flag, 0) + 1

    return report
