from __future__ import annotations

import importlib
import json
import re
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


def load_config(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
        if data is None:
            return {}
        return data
    except Exception:
        return json.loads(text)


def read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")


def parse_iso_date(value: Optional[str]) -> Optional[date]:
    if not value:
        return None
    try:
        if "T" in value:
            return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
        return date.fromisoformat(value)
    except ValueError:
        return None


def parse_iso_datetime(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def asof_timestamp(now: Optional[datetime] = None) -> str:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    return now.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def clamp(value: float, min_value: float, max_value: float) -> float:
    return max(min_value, min(max_value, value))


def safe_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None




def parse_money(value: Any) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text:
        return None
    # Many issuer pages embed the amount inside a richer string, e.g.:
    #   "$0.10000/mo." or "$0.125 quarterly"
    # Extract the first numeric token rather than requiring a clean float string.
    cleaned = text.replace("$", "").replace(",", "").strip()
    match = re.search(r"[-+]?(?:\d*\.\d+|\d+)", cleaned)
    if not match:
        return None
    return safe_float(match.group(0))


def parse_human_date(value: Optional[str]) -> Optional[date]:
    if not value:
        return None
    value = value.strip()
    if not value:
        return None
    iso = parse_iso_date(value)
    if iso:
        return iso
    cleaned = value.replace(",", "")
    parts = cleaned.split()
    if len(parts) < 3:
        return None
    month_token = parts[0].lower()
    day_token = parts[1].rstrip(",")
    year_token = parts[2]
    months = {
        "jan": 1,
        "january": 1,
        "feb": 2,
        "february": 2,
        "mar": 3,
        "march": 3,
        "apr": 4,
        "april": 4,
        "may": 5,
        "jun": 6,
        "june": 6,
        "jul": 7,
        "july": 7,
        "aug": 8,
        "august": 8,
        "sep": 9,
        "sept": 9,
        "september": 9,
        "oct": 10,
        "october": 10,
        "nov": 11,
        "november": 11,
        "dec": 12,
        "december": 12,
    }
    month = months.get(month_token)
    if not month:
        return None
    try:
        day = int(day_token)
        year = int(year_token)
    except ValueError:
        return None
    try:
        return date(year, month, day)
    except ValueError:
        return None


def ensure_list(value: Any) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]

def load_adapter(adapter_path: str):
    if ":" not in adapter_path:
        raise SystemExit(f"Adapter path must be module:callable, got {adapter_path!r}")
    module_path, func_name = adapter_path.split(":", 1)
    module = importlib.import_module(module_path)
    adapter = getattr(module, func_name, None)
    if adapter is None:
        raise SystemExit(f"Adapter {func_name!r} not found in {module_path!r}")
    return adapter
