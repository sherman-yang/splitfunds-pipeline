from __future__ import annotations

from datetime import date
from typing import Dict, Any, Iterable, Optional

from scripts.utils import safe_float, parse_iso_date


PAYMENTS_PER_YEAR = {
    "monthly": 12,
    "quarterly": 4,
}


def _years_between(start: date, end: date) -> Optional[float]:
    if not start or not end:
        return None
    delta = end - start
    return delta.days / 365.25


def _annualized_pull(anchor: Optional[float], price: Optional[float], years: Optional[float]) -> Optional[float]:
    if anchor is None or price is None or years is None:
        return None
    if anchor <= 0 or price <= 0 or years <= 0:
        return None
    try:
        return (anchor / price) ** (1 / years) - 1
    except (ZeroDivisionError, ValueError, OverflowError):
        return None


def compute_metrics(rows: Iterable[Dict[str, Any]], asof_date: date) -> None:
    for row in rows:
        unit_nav = safe_float(row.get("unit_nav"))
        pref_par = safe_float(row.get("pref_par"))
        gate_nav = safe_float(row.get("gate_nav"))
        price = safe_float(row.get("price"))
        nav_self = safe_float(row.get("nav_self"))

        if unit_nav is not None and pref_par is not None and pref_par > 0:
            row["cushion"] = unit_nav - pref_par
            row["coverage"] = unit_nav / pref_par
        else:
            row["cushion"] = None
            row["coverage"] = None

        if unit_nav is not None and gate_nav is not None:
            row["distance_to_gate"] = unit_nav - gate_nav
        else:
            row["distance_to_gate"] = None

        if unit_nav is not None and pref_par is not None:
            intrinsic = max(unit_nav - pref_par, 0)
            row["classa_intrinsic"] = intrinsic
        else:
            intrinsic = None
            row["classa_intrinsic"] = None

        if unit_nav is not None and pref_par is not None and unit_nav > pref_par:
            row["leverage_th"] = unit_nav / (unit_nav - pref_par)
        else:
            row["leverage_th"] = None

        if unit_nav is not None and price is not None and price > 0:
            row["leverage_mkt"] = unit_nav / price
        else:
            row["leverage_mkt"] = None

        if nav_self is not None and price is not None and nav_self > 0:
            row["discount_to_nav"] = (nav_self - price) / nav_self
        else:
            row["discount_to_nav"] = None

        if row.get("security_type") == "PREFERRED":
            if pref_par is not None and price is not None and pref_par > 0:
                row["discount_to_par"] = (pref_par - price) / pref_par
            else:
                row["discount_to_par"] = None
        else:
            row["discount_to_par"] = None

        if row.get("security_type") == "CLASS_A":
            if intrinsic is not None and price is not None and intrinsic > 0:
                row["discount_to_intrinsic"] = (intrinsic - price) / intrinsic
            else:
                row["discount_to_intrinsic"] = None
        else:
            row["discount_to_intrinsic"] = None

        maturity_date = parse_iso_date(row.get("maturity_date"))
        if maturity_date:
            years_to_first = _years_between(asof_date, maturity_date)
        else:
            years_to_first = None

        row["years_to_first_maturity"] = years_to_first

        final_maturity = parse_iso_date(row.get("final_maturity_date"))
        if final_maturity:
            row["years_to_final_maturity"] = _years_between(asof_date, final_maturity)
        else:
            row["years_to_final_maturity"] = None

        if row.get("extendable"):
            row["years_to_maturity"] = years_to_first
        else:
            row["years_to_maturity"] = years_to_first

        anchor_years = row.get("years_to_maturity")
        if row.get("security_type") == "PREFERRED":
            row["annualized_discount_to_par"] = _annualized_pull(pref_par, price, anchor_years)
        else:
            row["annualized_discount_to_par"] = None

        if row.get("security_type") == "CLASS_A":
            row["annualized_discount_to_intrinsic"] = _annualized_pull(intrinsic, price, anchor_years)
        else:
            row["annualized_discount_to_intrinsic"] = None
        row["annualized_discount_to_nav"] = _annualized_pull(nav_self, price, anchor_years)

        if row.get("security_type") == "PREFERRED":
            pref_div_amt = safe_float(row.get("pref_div_amt"))
            pref_div_freq = row.get("pref_div_freq")
            payments = PAYMENTS_PER_YEAR.get(pref_div_freq, None)
            existing_yield = safe_float(row.get("pref_yield_current"))
            if pref_div_amt is not None and payments is not None:
                row["pref_div_cash_annual"] = pref_div_amt * payments
                if price is not None and price > 0:
                    row["pref_yield_current"] = row["pref_div_cash_annual"] / price
                else:
                    row["pref_yield_current"] = None
            elif existing_yield is not None:
                # Some issuer pages publish a current yield (%) but not the cash distribution amount.
                # Preserve that value so scoring can incorporate the financing cost.
                row["pref_yield_current"] = existing_yield
                if price is not None and price > 0:
                    row["pref_div_cash_annual"] = existing_yield * price
                else:
                    row["pref_div_cash_annual"] = None
            else:
                row["pref_div_cash_annual"] = None
                row["pref_yield_current"] = None
        else:
            row["pref_div_cash_annual"] = None
            row["pref_yield_current"] = row.get("pref_yield_current")
