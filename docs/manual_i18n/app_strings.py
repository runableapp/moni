"""Load Moni app UI strings from accounting/moni/locales for manual docs."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

LOCALES_DIR = (
    Path(__file__).resolve().parents[2].parent / "accounting" / "moni" / "locales"
)

MANUAL_LANGS = ("ko", "zh", "ja", "es", "de", "fr")

EMOJI_PREFIX = re.compile(
    r"^[\U0001F300-\U0001FAFF\U00002600-\U000027BF\ufe0f\u200d\s]+"
)


def strip_emoji(text: str) -> str:
    return EMOJI_PREFIX.sub("", text).strip()


@lru_cache(maxsize=8)
def load_locale(lang: str) -> dict[str, str]:
    path = LOCALES_DIR / f"{lang}.json"
    if not path.is_file():
        raise FileNotFoundError(f"app locale not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


class AppStrings:
    """Resolved UI labels for one locale (fallback to English)."""

    def __init__(self, lang: str) -> None:
        self.lang = lang
        self.en = load_locale("en")
        self.loc = load_locale(lang) if lang != "en" else self.en

    def t(self, key: str) -> str:
        return self.loc.get(key) or self.en[key]

    def en_t(self, key: str) -> str:
        return self.en[key]

    @property
    def settings_name(self) -> str:
        return self.t("settings.panelTitle")

    def settings_path(self, section_key: str) -> str:
        return f"{self.settings_name} → {self.t(section_key)}"

    def tab_label(self, tab_key: str, *, with_emoji: bool = False) -> str:
        if tab_key == "tab.data" and not with_emoji:
            return self.t("tab.dataTitle")
        value = self.t(tab_key)
        return value if with_emoji else strip_emoji(value)

    def main_chat_path(self) -> str:
        return f"{self.tab_label('tab.main')} → {self.t('chat.title')}"

    def help_topic_path(self, topic_key: str) -> str:
        return f"{self.tab_label('tab.help')} → {self.t(topic_key)}"


TAB_KEYS = (
    "tab.main",
    "tab.accounts",
    "tab.payees",
    "tab.reports",
    "tab.data",
    "tab.settings",
    "tab.help",
)

SETTINGS_PATH_KEYS = (
    "settings.general",
    "settings.ai",
    "settings.accounts",
    "settings.mcp",
    "settings.advanced",
    "settings.agents",
    "settings.customButtons",
    "settings.appearance",
    "settings.backup.title",
    "settings.hledger.title",
    "settings.import.title",
    "settings.logs.title",
)

SETTINGS_SECTION_LIST_KEYS = (
    "settings.general",
    "settings.ai",
    "settings.accounts",
    "settings.mcp",
    "settings.advanced",
    "settings.agents",
    "settings.customButtons",
    "settings.appearance",
    "settings.backup.title",
    "settings.hledger.title",
    "settings.import.title",
    "settings.logs.title",
)


def tab_list_plain(lang: str) -> str:
    app = AppStrings(lang)
    names = [app.tab_label(key) for key in TAB_KEYS]
    if lang == "en":
        return ", ".join(names[:-1]) + f", and {names[-1]}"
    return "、".join(names) if lang in ("zh", "ja") else ", ".join(names)


def settings_section_list(lang: str) -> str:
    app = AppStrings(lang)
    names = [app.t(key) for key in SETTINGS_SECTION_LIST_KEYS]
    if lang == "en":
        return ", ".join(names[:-1]) + f", and {names[-1]}"
    if lang in ("zh", "ja"):
        return "、".join(names)
    return ", ".join(names)


def ledger_panel_label(app: AppStrings) -> str:
    label = app.t("settings.logs.interactionLedgerPanel")
    for suffix in (" results", " result", " 결과", " Ergebnisse", " resultados"):
        if label.endswith(suffix):
            return label[: -len(suffix)]
    return label


def _add_pair(rep: dict[str, str], en_text: str, loc_text: str) -> None:
    if en_text and en_text != loc_text:
        rep[en_text] = loc_text


def _add_key(
    rep: dict[str, str],
    en: AppStrings,
    app: AppStrings,
    key: str,
    *,
    strip_emoji_value: bool = False,
) -> None:
    en_text = en.t(key)
    loc_text = app.t(key)
    if strip_emoji_value:
        en_text = strip_emoji(en_text)
        loc_text = strip_emoji(loc_text)
    _add_pair(rep, en_text, loc_text)


# Locale keys referenced by English manual bodies (UI labels only).
MANUAL_LOCALE_KEYS = (
    "settings.ai.none",
    "settings.ai.llamacpp",
    "settings.ai.ollama",
    "settings.ai.openai",
    "settings.ai.claude",
    "settings.ai.gemini",
    "settings.ai.aiWrapper",
    "settings.ai.llamaSetupLocalAI",
    "settings.ai.llamaServerStart",
    "settings.ai.llamaUseGpu",
    "settings.ai.llamaDisableReasoning",
    "settings.ai.llamaRouterMode",
    "settings.ai.llamaAutoStartServer",
    "settings.ai.llamaChatMaxTokens",
    "settings.ai.llamaChatTimeoutSeconds",
    "settings.ai.llamaApplyDefaults",
    "settings.ai.llamaModelPreset",
    "settings.ai.llamaBinInstallDir",
    "settings.ai.llamaModelDir",
    "settings.ai.serviceLogs",
    "settings.ai.ragTitle",
    "settings.ai.ragSummaryMissing",
    "settings.ai.ragSummaryPending",
    "settings.ai.ragSummaryReady",
    "settings.ai.aiWrapperConnect",
    "settings.ai.aiWrapperExperimental",
    "settings.ai.aiWrapperViaElectron",
    "settings.ai.aiWrapperViaChrome",
    "settings.ai.provider",
    "settings.ai.statusCheckingTitle",
    "settings.hledger.chatVerifyAssistantCommands",
    "settings.logs.appDebug",
    "settings.backup.backupNow",
    "settings.backup.fileEnabled",
    "settings.backup.gitEnabled",
    "settings.customButtons",
    "chat.noAiEmptyTitle",
    "import.title",
)

# Manual English phrases that differ from locale values but map to a key.
MANUAL_PHRASE_KEYS: dict[str, str] = {
    "None": "settings.ai.none",
    "Local llama.cpp": "settings.ai.llamacpp",
    "Set up local AI": "settings.ai.llamaSetupLocalAI",
    "Use GPU if available": "settings.ai.llamaUseGpu",
    "Disable model reasoning": "settings.ai.llamaDisableReasoning",
    "Router mode": "settings.ai.llamaRouterMode",
    "Auto-start local AI on launch": "settings.ai.llamaAutoStartServer",
    "Reset paths to defaults": "settings.ai.llamaApplyDefaults",
    "Verify hledger commands in AI replies": "settings.hledger.chatVerifyAssistantCommands",
    "Connect": "settings.ai.aiWrapperConnect",
    "Logs": "settings.ai.serviceLogs",
    "OpenAI": "settings.ai.openai",
    "Claude": "settings.ai.claude",
    "Gemini": "settings.ai.gemini",
    "Model preset": "settings.ai.llamaModelPreset",
    "Binary and model directories": "settings.ai.llamaBinInstallDir",
}


def _rag_status_replacements(en: AppStrings, app: AppStrings) -> dict[str, str]:
    rep: dict[str, str] = {}
    missing = app.t("settings.ai.ragSummaryMissing")
    pending = app.t("settings.ai.ragSummaryPending").rstrip(".")
    ready = app.t("settings.ai.ragSummaryReady").replace("{chunks}", "N").rstrip(".")
    missing_label = missing.split("(")[0].strip() if "(" in missing else missing.rstrip(".")
    en_missing = en.t("settings.ai.ragSummaryMissing")
    en_pending = en.t("settings.ai.ragSummaryPending").rstrip(".")
    en_ready = en.t("settings.ai.ragSummaryReady").replace("{chunks}", "N").rstrip(".")
    en_missing_label = en_missing.split("(")[0].strip()

    _add_pair(rep, en_missing, missing)
    _add_pair(rep, en_pending, pending)
    _add_pair(rep, en_ready, ready)
    _add_pair(rep, en_missing_label, missing_label)
    _add_pair(rep, "<strong>Not available</strong>", f"<strong>{missing_label}</strong>")
    _add_pair(
        rep,
        "<strong>Found on disk; loads on first chat</strong>",
        f"<strong>{pending}</strong>",
    )
    _add_pair(rep, "<strong>Ready — N doc chunks</strong>", f"<strong>{ready}</strong>")
    return rep


def _strong_wrapped(label: str) -> str:
    return f"<strong>{label}</strong>"


def _ui_label_replacements(app: AppStrings) -> dict[str, str]:
    """English UI labels (often in &lt;strong&gt;) → app locale strings."""
    rep: dict[str, str] = {}
    pairs = (
        ("None", "settings.ai.none"),
        ("Local llama.cpp", "settings.ai.llamacpp"),
        ("Set up local AI", "settings.ai.llamaSetupLocalAI"),
        ("Use GPU if available", "settings.ai.llamaUseGpu"),
        ("Disable model reasoning", "settings.ai.llamaDisableReasoning"),
        ("Router mode", "settings.ai.llamaRouterMode"),
        ("Auto-start local AI on launch", "settings.ai.llamaAutoStartServer"),
        ("Reset paths to defaults", "settings.ai.llamaApplyDefaults"),
        (
            "Verify hledger commands in AI replies",
            "settings.hledger.chatVerifyAssistantCommands",
        ),
        ("Connect", "settings.ai.aiWrapperConnect"),
        ("Debug", "settings.logs.appDebug"),
        ("OpenAI", "settings.ai.openai"),
        ("Claude", "settings.ai.claude"),
        ("Gemini", "settings.ai.gemini"),
    )
    for phrase, key in pairs:
        loc = app.t(key)
        _add_pair(rep, phrase, loc)
        _add_pair(rep, _strong_wrapped(phrase), _strong_wrapped(loc))

    start = strip_emoji(app.t("settings.ai.llamaServerStart"))
    _add_pair(rep, _strong_wrapped("Start server"), _strong_wrapped(start))

    preset = app.t("settings.ai.llamaModelPreset").rstrip(":：")
    _add_pair(rep, "Model preset", preset)
    _add_pair(rep, _strong_wrapped("Model preset"), _strong_wrapped(preset))

    logs = strip_emoji(app.t("settings.ai.serviceLogs"))
    _add_pair(rep, "Logs", logs)

    wrapper = app.t("settings.ai.aiWrapper")
    _add_pair(rep, _strong_wrapped("AI Wrapper"), _strong_wrapped(wrapper))

    server_bad = app.t("settings.ai.llamaServerStatusBad")
    _add_pair(rep, _strong_wrapped("Server not reachable"), _strong_wrapped(server_bad))
    return rep


def build_replacements(lang: str) -> dict[str, str]:
    """Map English UI labels to the app's localized strings."""
    if lang == "en":
        return {}
    app = AppStrings(lang)
    en = AppStrings("en")
    rep: dict[str, str] = {}

    for key in TAB_KEYS:
        rep[en.t(key)] = app.t(key)
        en_plain = en.tab_label(key)
        loc_plain = app.tab_label(key)
        if en_plain != loc_plain:
            rep[en_plain] = loc_plain
            rep[f"{loc_plain} ({en_plain})"] = loc_plain

    rep[en.t("tab.dataTitle")] = app.t("tab.dataTitle")

    for key in SETTINGS_PATH_KEYS:
        en_path = en.settings_path(key)
        loc_path = app.settings_path(key)
        if en_path != loc_path:
            rep[en_path] = loc_path

    # Manual prose uses "Settings → Import"; app label is settings.import.title.
    import_path_en = f"{en.settings_name} → {en.t('tab.dataTitle')}"
    rep[import_path_en] = app.settings_path("settings.import.title")
    wrong_import = f"{app.settings_name} → {app.t('tab.dataTitle')}"
    if wrong_import != app.settings_path("settings.import.title"):
        rep[wrong_import] = app.settings_path("settings.import.title")

    for key in SETTINGS_SECTION_LIST_KEYS:
        en_label = en.t(key)
        loc_label = app.t(key)
        if en_label != loc_label:
            rep[en_label] = loc_label

    if en.settings_name != app.settings_name:
        rep[en.settings_name] = app.settings_name

    for key in ("ledger.title", "chat.title", "common.clear"):
        if en.t(key) != app.t(key):
            rep[en.t(key)] = app.t(key)

    for key in MANUAL_LOCALE_KEYS:
        _add_key(rep, en, app, key)
        if key in ("settings.ai.llamaServerStart", "settings.ai.serviceLogs"):
            _add_key(rep, en, app, key, strip_emoji_value=True)

    for phrase, key in MANUAL_PHRASE_KEYS.items():
        if phrase == "Binary and model directories":
            loc_dirs = (
                f"{app.t('settings.ai.llamaBinInstallDir')} / "
                f"{app.t('settings.ai.llamaModelDir')}"
            )
            _add_pair(rep, phrase, loc_dirs)
            continue
        loc = app.t(key)
        if key == "settings.ai.llamaServerStart":
            loc = strip_emoji(loc)
        elif key == "settings.ai.llamaModelPreset":
            loc = loc.rstrip(":：")
        elif key == "settings.ai.serviceLogs":
            loc = strip_emoji(loc)
        _add_pair(rep, phrase, loc)

    cloud_en = f"{en.t('settings.ai.openai')} / {en.t('settings.ai.claude')} / {en.t('settings.ai.gemini')}"
    cloud_loc = f"{app.t('settings.ai.openai')} / {app.t('settings.ai.claude')} / {app.t('settings.ai.gemini')}"
    _add_pair(rep, cloud_en, cloud_loc)

    rep.update(_rag_status_replacements(en, app))
    rep.update(_ui_label_replacements(app))

    rep[en.main_chat_path()] = app.main_chat_path()
    rep[en.help_topic_path("help.topic.import")] = app.help_topic_path(
        "help.topic.import"
    )

    if en.t("import.smart.title") != app.t("import.smart.title"):
        rep[en.t("import.smart.title")] = app.t("import.smart.title")

    ledger_panel_en = ledger_panel_label(en)
    ledger_panel_loc = ledger_panel_label(app)
    if ledger_panel_en != ledger_panel_loc:
        rep[ledger_panel_en] = ledger_panel_loc
        rep[ledger_panel_en.replace("panel", "Panel")] = ledger_panel_loc

    for suffix in (" panel", " Panel", " 패널", " 面板", " パネル", " panel", " Panel"):
        en_ai = f"{en.settings_path('settings.ai')}{suffix}"
        loc_ai = f"{app.settings_path('settings.ai')}{suffix}"
        if en_ai != loc_ai:
            rep[en_ai] = loc_ai

    rep[settings_section_list("en")] = settings_section_list(lang)

    # Manual page titles / links that embed English section names.
    rep["Settings manual"] = {
        "ko": "설정 설명서",
        "zh": "设置手册",
        "ja": "設定マニュアル",
        "es": "Manual de Ajustes",
        "de": "Einstellungen-Handbuch",
        "fr": "Manuel Paramètres",
    }.get(lang, app.settings_name)
    rep["Settings overview →"] = {
        "ko": f"{app.settings_name} 개요 →",
        "zh": f"{app.settings_name} 概览 →",
        "ja": f"{app.settings_name} 概要 →",
        "es": f"Resumen de {app.settings_name} →",
        "de": f"{app.settings_name}-Übersicht →",
        "fr": f"Aperçu {app.settings_name} →",
    }[lang]
    rep["Settings overview"] = rep["Settings overview →"].replace(" →", "")

    # Mixed lists from older partial translations (e.g. Korean index settings paragraph).
    mixed_lists = {
        "ko": "General, AI, 계정, MCP, Advanced, AI Agents, Buttons, Appearance, Backup, hledger, 가져오기, Logs",
        "zh": "General, AI, 账户, MCP, Advanced, AI Agents, Buttons, Appearance, Backup, hledger, 导入, Logs",
        "ja": "General, AI, アカウント, MCP, Advanced, AI Agents, Buttons, Appearance, Backup, hledger, インポート, Logs",
        "es": "General, AI, Cuentas, MCP, Advanced, AI Agents, Buttons, Appearance, Backup, hledger, Importación, Logs",
    }
    if lang in mixed_lists:
        rep[mixed_lists[lang]] = settings_section_list(lang)

    lang_fixes = {
        "ko": {
            "리포트 (보고서)": app.tab_label("tab.reports"),
            "Settings 설명서": f"{app.settings_name} 설명서",
            f"{app.settings_name}는": f"{app.settings_name}은",
            "계정 탐색, 리포트,": "계정 탐색, 보고서,",
        },
    }
    rep.update(lang_fixes.get(lang, {}))

    return rep
