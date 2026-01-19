from __future__ import annotations

from typing import Dict, Any, Iterable, Optional

from scripts.utils import clamp, safe_float


def _normalize(value: Optional[float], min_value: float, max_value: float) -> Optional[float]:
    if value is None:
        return None
    if max_value == min_value:
        return None
    return clamp((value - min_value) / (max_value - min_value), 0.0, 1.0)


def _maturity_score(years: Optional[float], ideal_low: float, ideal_high: float, max_years: float) -> Optional[float]:
    if years is None:
        return None
    if years <= 0:
        return 0.0
    if ideal_low <= years <= ideal_high:
        return 1.0
    if years < ideal_low:
        return clamp(years / ideal_low, 0.0, 1.0)
    if years <= max_years:
        return clamp((max_years - years) / (max_years - ideal_high), 0.0, 1.0)
    return 0.0


def _weighted_score(components: Dict[str, Optional[float]], weights: Dict[str, float]) -> Optional[float]:
    total_weight = 0.0
    total = 0.0
    for key, weight in weights.items():
        value = components.get(key)
        if value is None:
            continue
        total_weight += weight
        total += value * weight
    if total_weight == 0:
        return None
    return total / total_weight


def _build_components(row: Dict[str, Any], normalization: Dict[str, Any]) -> Dict[str, Optional[float]]:
    coverage = safe_float(row.get("coverage"))
    distance = safe_float(row.get("distance_to_gate"))
    cushion = safe_float(row.get("cushion"))
    discount = safe_float(row.get("discount_to_intrinsic"))
    years = safe_float(row.get("years_to_maturity"))
    pref_yield = safe_float(row.get("pref_yield_current"))

    coverage_norm = _normalize(coverage, normalization["coverage"]["min"], normalization["coverage"]["max"])
    distance_norm = _normalize(distance, normalization["distance_to_gate"]["min"], normalization["distance_to_gate"]["max"])
    cushion_norm = _normalize(cushion, normalization["cushion"]["min"], normalization["cushion"]["max"])

    safety_parts = [v for v in [coverage_norm, distance_norm, cushion_norm] if v is not None]
    safety = sum(safety_parts) / len(safety_parts) if safety_parts else None

    valuation = _normalize(discount, normalization["discount_to_intrinsic"]["min"], normalization["discount_to_intrinsic"]["max"])

    maturity = _maturity_score(
        years,
        normalization["years_to_maturity"]["ideal_low"],
        normalization["years_to_maturity"]["ideal_high"],
        normalization["years_to_maturity"]["max"],
    )

    if pref_yield is not None:
        cost_norm = _normalize(pref_yield, normalization["pref_yield_current"]["min"], normalization["pref_yield_current"]["max"])
        cost = None if cost_norm is None else 1.0 - cost_norm
    else:
        cost = None

    return {
        "safety": safety,
        "valuation": valuation,
        "maturity": maturity,
        "cost": cost,
    }


def _passes_hard_filters(row: Dict[str, Any], hard_filters: Dict[str, Any]) -> bool:
    coverage = safe_float(row.get("coverage"))
    distance = safe_float(row.get("distance_to_gate"))
    intrinsic = safe_float(row.get("classa_intrinsic"))

    if coverage is None or coverage < hard_filters["coverage_min"]:
        return False
    if distance is not None and distance < hard_filters["distance_to_gate_min"]:
        return False
    if intrinsic is None or intrinsic <= hard_filters["classa_intrinsic_min"]:
        return False
    return True


def score_rows(rows: Iterable[Dict[str, Any]], scoring_cfg: Dict[str, Any]) -> None:
    conservative_cfg = scoring_cfg["conservative"]
    aggressive_cfg = scoring_cfg["aggressive"]

    for row in rows:
        if row.get("security_type") != "CLASS_A":
            continue

        components = _build_components(row, conservative_cfg["normalization"])
        row["score_components"] = components

        if _passes_hard_filters(row, conservative_cfg["hard_filters"]):
            score = _weighted_score(components, conservative_cfg["weights"])
            row["score_conservative"] = None if score is None else round(score * 100, 2)
        else:
            row["score_conservative"] = None

        components_aggr = _build_components(row, aggressive_cfg["normalization"])
        if _passes_hard_filters(row, aggressive_cfg["hard_filters"]):
            score_aggr = _weighted_score(components_aggr, aggressive_cfg["weights"])
            row["score_aggressive"] = None if score_aggr is None else round(score_aggr * 100, 2)
        else:
            row["score_aggressive"] = None

        row["score_components_aggressive"] = components_aggr
