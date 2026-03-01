from __future__ import annotations

import re
import urllib.parse
from typing import Any, Dict, List, Optional

from scripts.http_client import fetch_text
from scripts.utils import parse_human_date, parse_money


def _clean(text: str) -> str:
    return " ".join(re.sub(r"<[^>]+>", " ", text).split())


def _extract_basic_details(html: str, section_id: str) -> List[Dict[str, Optional[str]]]:
    idx = html.find(f'id="{section_id}"')
    if idx == -1:
        return []
    after = html[idx:]
    ul_start = after.find("<ul>")
    ul_end = after.find("</ul>")
    if ul_start == -1 or ul_end == -1:
        return []
    block = after[ul_start:ul_end]
    items = re.findall(r"<li[^>]*>.*?</li>", block, re.S)
    results = []
    for item in items:
        label_match = re.search(r"basic_detail_label\">\s*(.*?)\s*</span>", item, re.S)
        value_match = re.search(r"basic_detail_value[^>]*>\s*(.*?)\s*</span>", item, re.S)
        date_match = re.search(r"basic_detail_date\">\s*\(([^)]+)\)", item, re.S)
        if not label_match or not value_match:
            continue
        results.append(
            {
                "label": _clean(label_match.group(1)),
                "value": _clean(value_match.group(1)),
                "date": date_match.group(1).strip() if date_match else None,
            }
        )
    return results


def _parse_distribution(value: str) -> tuple[Optional[float], Optional[str]]:
    amount = parse_money(value)
    freq = None
    lower = value.lower()
    if "mo" in lower or "month" in lower:
        freq = "monthly"
    elif "q" in lower or "quarter" in lower:
        freq = "quarterly"
    return amount, freq


def _parse_percent(value: str) -> Optional[float]:
    if not value:
        return None
    match = re.search(r"[-+]?(?:\d*\.\d+|\d+)", value.replace(",", ""))
    if not match:
        return None
    try:
        return float(match.group(0)) / 100.0
    except ValueError:
        return None


def _parse_fund_facts(html: str) -> Dict[str, str]:
    facts: Dict[str, str] = {}
    match = re.search(r"FUND FACTS</h3>(.*?)</ul>", html, re.S | re.I)
    if not match:
        return facts
    for item in re.findall(r"<li>(.*?)</li>", match.group(1), re.S):
        text = _clean(item)
        if not text:
            continue
        if "Ticker (Class A" in text:
            facts["class_a_ticker"] = text.split()[-1]
        elif "Ticker (Preferred" in text:
            facts["pref_ticker"] = text.split()[-1]
    return facts


def _parse_unit_nav(html: str) -> tuple[Optional[float], Optional[str]]:
    items = re.findall(r"<li[^>]*>.*?</li>", html, re.S)
    for item in items:
        text = _clean(item)
        match = re.search(r"Unit NAV \(([^)]+)\) \$([0-9.]+)", text, re.I)
        if match:
            nav = parse_money(match.group(2))
            date = parse_human_date(match.group(1))
            return nav, date.isoformat() if date else None
    return None, None


def _parse_maturity_date(html: str) -> Optional[str]:
    items = re.findall(r"<li[^>]*>.*?</li>", html, re.S)
    for item in items:
        text = _clean(item)
        if text.startswith("Maturity Date"):
            parts = text.split("Maturity Date", 1)[-1].strip()
            # Brompton often annotates the label with a footnote like "(2)".
            parts = re.sub(r"\(\d+\)", "", parts).strip()
            date = parse_human_date(parts)
            return date.isoformat() if date else None
    return None


def _parse_extendable(html: str) -> tuple[bool, Optional[str]]:
    bullets = re.findall(r"<li>\s*(.*?)\s*</li>", html, re.S)
    for bullet in bullets:
        text = _clean(bullet)
        if "extend" in text.lower():
            return True, text
    return False, None


def load_brompton(cfg: Dict[str, Any]) -> Dict[str, Any]:
    base_url = cfg.get("base_url", "https://www.bromptongroup.com/funds")
    pref_par_default = cfg.get("pref_par_default", 10.0)
    gate_nav_default = cfg.get("gate_nav_default", 15.0)

    html = fetch_text(base_url)
    links = set(re.findall(r'href="([^"]+)"', html))

    fund_urls = []
    for link in links:
        if "/product/" not in link:
            continue
        if "split" not in link.lower():
            continue
        if "etf" in link.lower():
            continue
        clean_link = link.split("?")[0]
        fund_urls.append(urllib.parse.urljoin(base_url, clean_link))

    funds: List[Dict[str, Any]] = []

    for url in sorted(set(fund_urls)):
        page = fetch_text(url)
        title_match = re.search(r"<title>(.*?)</title>", page, re.S | re.I)
        title = _clean(title_match.group(1)) if title_match else ""

        class_ticker = None
        pref_ticker = None
        title_match = re.match(r"\s*([A-Z0-9.]+)\s*\|\s*([A-Z0-9.]+)\s*\|", title)
        if title_match:
            class_ticker = title_match.group(1)
            pref_ticker = title_match.group(2)
        else:
            facts = _parse_fund_facts(page)
            class_ticker = facts.get("class_a_ticker")
            pref_ticker = facts.get("pref_ticker")

        if not class_ticker or not pref_ticker:
            continue

        basic_class = _extract_basic_details(page, "basic_detail_1")
        basic_pref = _extract_basic_details(page, "basic_detail_2")

        class_nav = None
        pref_nav = None
        dist_amt = None
        dist_freq = None
        pref_div_amt = None
        pref_div_freq = None
        pref_yield_current = None
        nav_date = None

        for item in basic_class:
            if item["label"] == "NAV":
                class_nav = parse_money(item["value"])
                if item["date"]:
                    date = parse_human_date(item["date"])
                    nav_date = date.isoformat() if date else nav_date
            if item["label"] == "Distribution":
                dist_amt, dist_freq = _parse_distribution(item["value"])

        for item in basic_pref:
            if item["label"] == "NAV":
                pref_nav = parse_money(item["value"])
                if item["date"]:
                    date = parse_human_date(item["date"])
                    nav_date = date.isoformat() if date else nav_date
            if item["label"] == "Distribution":
                pref_div_amt, pref_div_freq = _parse_distribution(item["value"])
            # Preferred pages usually show a percentage "Distribution Rate" rather than a cash amount.
            if item["label"].startswith("Distribution Rate"):
                # Store as a current yield (decimal), so downstream scoring can use it.
                # Example: "5.96%" -> 0.0596
                pref_yield_current = _parse_percent(item["value"])

        unit_nav, unit_nav_date = _parse_unit_nav(page)
        nav_asof_date = unit_nav_date or nav_date

        maturity_date = _parse_maturity_date(page)
        extendable, extend_terms = _parse_extendable(page)

        fund = {
            "fund_id": class_ticker.split(".")[0],
            "issuer_manager": "Brompton",
            "theme": title.split("|")[-1].strip() if title else None,
            "maturity_date": maturity_date,
            "extendable": extendable,
            "extend_terms_text": extend_terms,
            "pref_par": pref_par_default,
            "gate_nav": gate_nav_default,
            "unit_nav": unit_nav,
            "nav_asof_date": nav_asof_date,
            "securities": [
                {
                    "security_type": "CLASS_A",
                    "ticker": class_ticker,
                    "nav_self": class_nav,
                    "dist_amt": dist_amt,
                    "dist_freq": dist_freq,
                },
                {
                    "security_type": "PREFERRED",
                    "ticker": pref_ticker,
                    "nav_self": pref_nav,
                    "pref_div_amt": pref_div_amt,
                    "pref_div_freq": pref_div_freq,
                    "pref_yield_current": pref_yield_current,
                },
            ],
        }
        funds.append(fund)

    return {"funds": funds}
