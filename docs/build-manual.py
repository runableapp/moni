#!/usr/bin/env python3
"""Generate Moni manual pages (one HTML file per language per topic)."""

from __future__ import annotations

from pathlib import Path

from i18n_shared import LANG_PAGES, MANUAL_PAGES, lang_menu_html, manual_lang_href
from manual_i18n.ui import PAGE_META_KEYS, UI

BODIES_DIR = Path(__file__).resolve().parent / "manual_i18n" / "bodies"


def asset_prefix(lang: str) -> str:
    return ".." if lang == "en" else "../.."


def manual_home_link(lang: str) -> str:
  prefix = asset_prefix(lang)
  return f"{prefix}/index.html" if lang == "en" else f"{prefix}/{lang}.html"


def sidebar_link(lang: str, slug: str, page_file: str, active_slug: str) -> str:
    cls = ' class="active"' if slug == active_slug else ""
    if slug == "settings-ai":
        cls = (' class="sub active"' if slug == active_slug else ' class="sub"')
    href = page_file
    labels = {
        "index": "sidebar_user_guide",
        "custom-buttons": "sidebar_custom_buttons",
        "settings": "sidebar_settings",
        "settings-ai": "sidebar_settings_ai",
    }
    return f'      <a href="{href}"{cls}>{UI[lang][labels[slug]]}</a>'


def load_body(lang: str, slug: str) -> str:
    path = BODIES_DIR / lang / f"{slug}.html"
    if not path.is_file():
        raise FileNotFoundError(f"missing manual body: {path}")
    return path.read_text(encoding="utf-8").strip()


def render(lang: str, slug: str, page_file: str) -> str:
    u = UI[lang]
    prefix = asset_prefix(lang)
    title_key, desc_key = PAGE_META_KEYS[slug]
    lang_links = [
        (
            manual_lang_href(lang, code, page_file),
            flag,
            label,
            code == lang,
        )
        for code, _landing, label, flag in LANG_PAGES
    ]
    sidebar = "\n".join(
        sidebar_link(lang, s, pf, slug) for s, pf in MANUAL_PAGES
    )
    body = load_body(lang, slug)
    return f"""<!DOCTYPE html>
<html lang="{lang if lang != 'zh' else 'zh'}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{u[title_key]}</title>
  <meta name="description" content="{u[desc_key]}">
  <link rel="icon" href="https://runableapp.github.io/i/favicon.ico" type="image/x-icon">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}/css/style.css">
  <link rel="stylesheet" href="{"css/manual.css" if lang == "en" else "../css/manual.css"}">
</head>
<body class="manual-page">

<nav>
  <div class="inner">
    <a href="{manual_home_link(lang)}" class="brand">
      <img src="{prefix}/i/moni-wave.webp" alt="Moni logo">
      <span>Moni</span>
    </a>
    <ul>
{lang_menu_html(
    menu_label=u["lang_menu_label"],
    menu_aria=u["lang_menu_aria"],
    links=lang_links,
    current_flag=next(flag for code, _landing, _label, flag in LANG_PAGES if code == lang),
)}
      <li><a href="{manual_home_link(lang)}">{u["nav_home"]}</a></li>
      <li><a href="index.html" class="nav-cta">{u["nav_manual"]}</a></li>
      <li><a href="{prefix}/feedback.html">{u["nav_feedback"]}</a></li>
    </ul>
  </div>
</nav>

<div class="manual-layout">
  <aside class="manual-sidebar">
    <p class="manual-sidebar-title">{u["sidebar_title"]}</p>
    <nav>
{sidebar}
    </nav>
    <a href="{manual_home_link(lang)}" class="manual-back">{u["back_home"]}</a>
  </aside>

  <main class="manual-content">
{body}
  </main>
</div>

<footer>
  <p>
    {u["footer_rights"]}
  </p>
</footer>

<script src="{prefix}/js/main.js"></script>
</body>
</html>
"""


def main() -> None:
    out = Path(__file__).resolve().parent / "manual"
    for lang_code, _landing, _label, _flag in LANG_PAGES:
        for slug, page_file in MANUAL_PAGES:
            html = render(lang_code, slug, page_file)
            if lang_code == "en":
                path = out / page_file
            else:
                path = out / lang_code / page_file
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(html, encoding="utf-8")
            rel = path.relative_to(out.parent)
            print(f"wrote {rel}")


if __name__ == "__main__":
    main()
