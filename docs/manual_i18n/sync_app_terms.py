#!/usr/bin/env python3
"""Replace English UI labels in manual bodies with strings from Moni app locales."""

from __future__ import annotations

import re
from pathlib import Path

from app_strings import MANUAL_LANGS, AppStrings, build_replacements

ROOT = Path(__file__).resolve().parent / "bodies"
PAGES = ("index.html", "settings.html", "settings-ai.html", "custom-buttons.html")

PAREN_EN = re.compile(
    r"([\u0080-\uFFFF]+)\s*\((Main|Accounts|Payees|Reports|Import|Settings|Help)\)"
)

SETTINGS_TAIL = re.compile(r"\bSettings(?=[에서의\s]|$)")


def apply_replacements(html: str, mapping: dict[str, str], settings_name: str | None = None) -> str:
    for src, dst in sorted(mapping.items(), key=lambda item: -len(item[0])):
        html = html.replace(src, dst)
    html = PAREN_EN.sub(r"\1", html)
    if settings_name:
        html = SETTINGS_TAIL.sub(settings_name, html)
    return html


def main() -> None:
    for lang in MANUAL_LANGS:
        mapping = build_replacements(lang)
        settings_name = AppStrings(lang).settings_name
        for name in PAGES:
            path = ROOT / lang / name
            if not path.is_file():
                continue
            updated = apply_replacements(
                path.read_text(encoding="utf-8"),
                mapping,
                settings_name=settings_name,
            )
            path.write_text(updated, encoding="utf-8")
            print(f"synced app terms: {lang}/{name}")


if __name__ == "__main__":
    main()
