"""Render the Flask pages as a static site for GitHub Pages."""
from pathlib import Path
import os
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app import app


def main():
    # GitHub project sites live under /repository-name/ rather than the domain root.
    prefix = os.getenv("SITE_BASE_PATH", "/Ev-market-analysis").rstrip("/")
    output = ROOT / "dist"
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    routes = {"/": "index.html", "/dashboard": "dashboard/index.html", "/about": "about/index.html"}
    from app import STORY_URL
    if STORY_URL:
        routes["/story"] = "story/index.html"

    with app.test_client() as client:
        for route, name in routes.items():
            response = client.get(route)
            if response.status_code != 200:
                raise RuntimeError(f"Could not render {route}: {response.status_code}")
            html = response.get_data(as_text=True)
            html = re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{prefix}/', html)
            target = output / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(html, encoding="utf-8")
            print(f"Rendered {name}")
    shutil.copytree(ROOT / "static", output / "static")
    (output / ".nojekyll").touch()
    print(f"Static site ready in dist/ with base path {prefix or '/'}")


if __name__ == "__main__":
    main()
