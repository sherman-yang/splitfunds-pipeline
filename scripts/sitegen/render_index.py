from __future__ import annotations

from pathlib import Path


TEMPLATE_FILES = {
    "index.html": "index.html",
    "assets/app.js": "app.js",
    "assets/app.css": "app.css",
    ".github/workflows/deploy-pages.yml": "deploy-pages.yml",
}


def render_site(output_dir: Path) -> None:
    template_dir = Path(__file__).parent / "templates"
    for dest, src in TEMPLATE_FILES.items():
        source_path = template_dir / src
        target_path = output_dir / dest
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(source_path.read_text(encoding="utf-8"), encoding="utf-8")
