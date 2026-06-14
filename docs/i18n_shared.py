"""Shared language list and HTML helpers for Moni docs generators."""

from __future__ import annotations

LANG_PAGES: list[tuple[str, str, str, str]] = [
    ("en", "index.html", "English", "🇺🇸"),
    ("ko", "ko.html", "한국어", "🇰🇷"),
    ("zh", "zh.html", "中文", "🇨🇳"),
    ("ja", "ja.html", "日本語", "🇯🇵"),
    ("es", "es.html", "Español", "🇪🇸"),
    ("de", "de.html", "Deutsch", "🇩🇪"),
    ("fr", "fr.html", "Français", "🇫🇷"),
]

MANUAL_PAGES: list[tuple[str, str]] = [
    ("index", "index.html"),
    ("custom-buttons", "custom-buttons.html"),
    ("settings", "settings.html"),
    ("settings-ai", "settings-ai.html"),
]


def landing_lang_href(target_lang: str) -> str:
    if target_lang == "en":
        return "index.html"
    return f"{target_lang}.html"


def manual_lang_href(current_lang: str, target_lang: str, page_file: str) -> str:
    """Relative href from manual/{lang}/page to the same page in target_lang."""
    if current_lang == "en":
        if target_lang == "en":
            return page_file
        return f"{target_lang}/{page_file}"
    if target_lang == "en":
        return f"../{page_file}"
    if target_lang == current_lang:
        return page_file
    return f"../{target_lang}/{page_file}"


def lang_flag_label(flag: str, label: str) -> str:
    return (
        f'<span class="lang-flag" aria-hidden="true">{flag}</span>'
        f'<span class="lang-name">{label}</span>'
    )


def lang_menu_html(
    *,
    menu_label: str,
    menu_aria: str,
    links: list[tuple[str, str, str, bool]],
    current_flag: str = "🌐",
) -> str:
    items = []
    for href, flag, label, active in links:
        cls = ' class="active"' if active else ""
        items.append(
            f'          <a href="{href}" role="menuitem"{cls}>{lang_flag_label(flag, label)}</a>'
        )
    dropdown = "\n".join(items)
    return f"""      <li class="language-menu">
        <button type="button" class="language-button" aria-label="{menu_aria}" title="{menu_label}" aria-expanded="false" aria-haspopup="true">
          <span class="language-emoji" aria-hidden="true">{current_flag}</span>
        </button>
        <div class="language-dropdown" role="menu" aria-label="{menu_aria}">
{dropdown}
        </div>
      </li>"""


def lang_grid_html() -> str:
    chips = []
    for _code, _fname, label, flag in LANG_PAGES:
        chips.append(
            f'      <span class="lang-chip">{lang_flag_label(flag, label)}</span>'
        )
    return "\n".join(chips)
