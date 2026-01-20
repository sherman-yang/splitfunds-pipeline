from __future__ import annotations

import json
import ssl
import urllib.request
from typing import Any, Dict, Optional

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36",
    "Accept": "text/html,application/json",
}


def fetch_text(url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 20) -> str:
    merged = DEFAULT_HEADERS.copy()
    if headers:
        merged.update(headers)
    req = urllib.request.Request(url, headers=merged)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def fetch_json(url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 20) -> Dict[str, Any]:
    text = fetch_text(url, headers=headers, timeout=timeout)
    return json.loads(text)

def post_json(url: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None, timeout: int = 20) -> Dict[str, Any]:
    merged = DEFAULT_HEADERS.copy()
    merged["Content-Type"] = "application/json"
    if headers:
        merged.update(headers)
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=merged)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))

