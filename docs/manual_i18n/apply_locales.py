#!/usr/bin/env python3
"""Apply EN→locale string maps to manual body fragments (skips pre/code blocks)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "bodies"
PRE = re.compile(r"<pre class=\"manual-code\">.*?</pre>", re.S)


def protect(html: str) -> tuple[str, list[str]]:
    blocks: list[str] = []

    def stash(m: re.Match[str]) -> str:
        blocks.append(m.group(0))
        return f"@@PRE{len(blocks) - 1}@@"

    return PRE.sub(stash, html), blocks


def restore(html: str, blocks: list[str]) -> str:
    for i, b in enumerate(blocks):
        html = html.replace(f"@@PRE{i}@@", b)
    return html


def apply(html: str, mapping: dict[str, str]) -> str:
    protected, blocks = protect(html)
    for src, dst in sorted(mapping.items(), key=lambda x: -len(x[0])):
        protected = protected.replace(src, dst)
    return restore(protected, blocks)


# Shared maps for manual prose (EN source files in bodies/en/).
DE: dict[str, str] = {
    "User guide": "Benutzerhandbuch",
    "Moni is a desktop companion for plain-text hledger journals. This guide walks through each tab in the app bar and what you can do there. Screenshots below are placeholders — replace them with real captures from your build when ready.": "Moni ist ein Desktop-Begleiter für hledger-Journale im Klartext. Dieses Handbuch führt durch jede Registerkarte in der App-Leiste und erklärt, was Sie dort tun können. Die Screenshots unten sind Platzhalter — ersetzen Sie sie bei Bedarf durch echte Aufnahmen aus Ihrer Installation.",
    "On this page": "Auf dieser Seite",
    "The tab bar": "Die Tab-Leiste",
    "Seven tabs run across the top of the window. Together they cover daily ledger work, account browsing, reporting, CSV import, configuration, and in-app documentation.": "Sieben Registerkarten befinden sich oben im Fenster. Zusammen decken sie tägliche Buchführung, Konten, Berichte, CSV-Import, Konfiguration und integrierte Hilfe ab.",
    "Tab": "Tab",
    "Purpose": "Zweck",
    "Ledger panel + AI chat; toolbar buttons run hledger tools": "Ledger-Panel + KI-Chat; Symbolleisten-Schaltflächen starten hledger-Werkzeuge",
    "Pick an account for balance chart and register": "Konto für Saldenchart und Kontoblatt wählen",
    "Browse payees and open payee registers": "Empfänger durchsuchen und Kontoblätter öffnen",
    "Longer summary views (monthly reports, etc.)": "Längere Übersichten (Monatsberichte usw.)",
    "Drop CSV bank exports; preview with hledger import": "Bank-CSV ablegen; Vorschau mit hledger import",
    "hledger paths, AI, buttons, theme, backup, and more": "hledger-Pfade, KI, Schaltflächen, Theme, Backup und mehr",
    "Built-in Markdown topics shipped with the app": "Integrierte Markdown-Themen mit der App",
    "Full window — tab bar": "Gesamtfenster — Tab-Leiste",
    "All seven tabs visible on a typical desktop layout.": "Alle sieben Tabs in einem typischen Desktop-Layout.",
    "Tab bar close-up": "Tab-Leiste im Detail",
    "Tab labels and icons match your UI language setting.": "Tab-Beschriftungen und Symbole folgen der UI-Sprache.",
    "First launch": "Erster Start",
    "Before hledger is configured, Settings prompts you to set binary and journal paths.": "Vor der hledger-Konfiguration fordert Settings Sie auf, Binary- und Journal-Pfade zu setzen.",
    "Main": "Main",
    "The Main tab splits the window into two panels.": "Der Main-Tab teilt das Fenster in zwei Panels.",
    "(left) shows results from toolbar buttons and built-in tools — tables, charts, and plain-text output stack in the panel. Use ": "(links) zeigt Ergebnisse von Symbolleisten-Schaltflächen und integrierten Werkzeugen — Tabellen, Diagramme und Klartext stapeln sich im Panel. Mit ",
    " to reset the stack. ": " setzen Sie den Stapel zurück. ",
    "(right) talks to the AI provider you chose under Settings → AI; if none is selected, Moni explains how to enable AI.": "(rechts) spricht mit dem unter Einstellungen → KI gewählten Anbieter; ist keiner gewählt, erklärt Moni die Aktivierung.",
    "Toolbar buttons are YAML recipes (see ": "Symbolleisten-Schaltflächen sind YAML-Rezepte (siehe ",
    "Custom buttons": "Eigene Schaltflächen",
    "). You can run hledger reports, registers, balance sheets, and external scripts from one click. Chat can suggest hledger commands; optional verification checks them against your installed hledger version.": "). Mit einem Klick starten Sie hledger-Berichte, Kontoblätter, Bilanzen und externe Skripte. Der Chat kann hledger-Befehle vorschlagen; optionale Prüfung vergleicht sie mit Ihrer installierten Version.",
    "Split view: ledger results on the left, chat on the right.": "Geteilte Ansicht: Ledger links, Chat rechts.",
    "Toolbar buttons": "Symbolleisten-Schaltflächen",
    "Custom and bundled buttons across the top of the Ledger panel.": "Eigene und mitgelieferte Schaltflächen über dem Ledger-Panel.",
    "Register table + drill-down": "Kontoblatt-Tabelle mit Drill-down",
    "Button output as an interactive register with row drill-down.": "Schaltflächenausgabe als interaktives Kontoblatt mit Zeilen-Drill-down.",
    "Choose an account from the list (configured under Settings → Accounts). Moni shows a balance-over-time chart and a register filtered to that account. Account display names, icons, and institution hints come from your account profiles in Settings.": "Wählen Sie ein Konto aus der Liste (unter Einstellungen → Konten). Moni zeigt einen Saldenverlauf und ein gefiltertes Kontoblatt. Anzeigenamen, Symbole und Institutshinweise stammen aus den Kontoprofilen.",
    "Account list": "Kontenliste",
    "Accounts you marked visible in Settings → Accounts.": "In Einstellungen → Konten sichtbar gemachte Konten.",
    "Balance chart": "Saldenchart",
    "Running balance for the selected account.": "Laufender Saldo des gewählten Kontos.",
    "Account register": "Kontoblatt",
    "Posting list for the selected account.": "Buchungsliste für das gewählte Konto.",
    "Browse payees extracted from your journal. Select a payee to open its register in a modal dialog — useful for reviewing spending with a single merchant or client.": "Durchsuchen Sie Empfänger aus Ihrem Journal. Wählen Sie einen, um sein Kontoblatt in einem Modal zu öffnen — hilfreich für Ausgaben bei einem Händler oder Kunden.",
    "Payee list": "Empfängerliste",
    "Searchable list of payee names from the journal.": "Durchsuchbare Liste von Empfängern aus dem Journal.",
    "Payee register modal": "Empfänger-Kontoblatt-Modal",
    "Register filtered to one payee, opened from the list.": "Auf einen Empfänger gefiltertes Kontoblatt, aus der Liste geöffnet.",
    "Reports is a dedicated area for longer-running or summary views — for example monthly P&amp;L-style reports. Content here grows with future releases; many day-to-day reports still live on Main via toolbar buttons.": "Reports ist ein Bereich für längere oder zusammenfassende Ansichten — z. B. monatliche GuV-Berichte. Der Inhalt wächst mit künftigen Versionen; viele Alltagsberichte bleiben auf Main über Symbolleisten-Schaltflächen.",
    "Reports tab overview": "Reports-Tab Überblick",
    "Single-panel layout for report workflows.": "Ein-Panel-Layout für Berichts-Workflows.",
    "Sample monthly report": "Beispiel-Monatsbericht",
    "Example summary view (placeholder).": "Beispielübersicht (Platzhalter).",
    "Open Import and drop a": "Öffnen Sie Import und legen Sie eine",
    "file on the drop zone, or use the": "Datei in die Ablagezone oder nutzen Sie das",
    "menu. Moni applies your import rules and always previews with": "Menü. Moni wendet Ihre Importregeln an und zeigt immer eine Vorschau mit",
    "before writing to the journal.": "bevor ins Journal geschrieben wird.",
    "Two workflows are available:": "Zwei Workflows stehen bereit:",
    "classic import": "klassischer Import",
    "(full-file import with overlap": "(Gesamtdatei-Import mit",
    "tracking) and": "Nachverfolgung) und",
    "(pick rows, append selected journal text). Toggle Smart Import under Settings → Import. For the full import guide, open Help → Import inside the app.": "(Zeilen wählen, Journaltext anhängen). Smart Import unter Einstellungen → Import umschalten. Die vollständige Import-Anleitung finden Sie in der App unter Help → Import.",
    "Import drop zone": "Import-Ablagezone",
    "Drag-and-drop area for bank CSV exports.": "Drag-and-Drop-Bereich für Bank-CSV.",
    "Dry-run preview": "Dry-run-Vorschau",
    "Preview postings before commit.": "Buchungen vor dem Commit ansehen.",
    "Smart Import row picker": "Smart-Import-Zeilenauswahl",
    "Select individual rows when Smart Import is enabled.": "Einzelne Zeilen wählen, wenn Smart Import aktiv ist.",
    "Settings is organized into sections along the left: General, AI, Accounts, MCP, Advanced, AI Agents, Buttons, Appearance, Backup, hledger, Import, and Logs. Start with ": "Settings ist links in Abschnitte gegliedert: General, KI, Konten, MCP, Erweitert, KI-Agenten, Schaltflächen, Erscheinungsbild, Backup, hledger, Import und Protokolle. Beginnen Sie mit ",
    "(binary + journal path) and ": "(Binary + Journalpfad) und ",
    "(which accounts appear on Main and Accounts).": "(welche Konten auf Main und Accounts erscheinen).",
    "See the dedicated ": "Siehe das ",
    "Settings manual": "Settings-Handbuch",
    " for each section. AI setup is covered in ": " für jeden Abschnitt. Die KI-Einrichtung steht in ",
    "Settings sidebar": "Settings-Seitenleiste",
    "Section list on the left, detail panel on the right.": "Abschnittsliste links, Detailpanel rechts.",
    "Binary path, journal file, and download helper.": "Binary-Pfad, Journaldatei und Download-Hilfe.",
    "Enable toolbar buttons and point each at a YAML recipe.": "Symbolleisten-Schaltflächen aktivieren und jeweils auf ein YAML-Rezept verweisen.",
    "The Help tab ships Markdown topics with the app — English by default, plus localized copies for German, Spanish, French, Japanese, Korean, and Chinese. Topics include import workflows, AI usage, and troubleshooting.": "Der Help-Tab liefert Markdown-Themen mit der App — standardmäßig Englisch, plus Lokalisierungen für Deutsch, Spanisch, Französisch, Japanisch, Koreanisch und Chinesisch. Themen: Import, KI-Nutzung, Fehlerbehebung.",
    "Help topic list": "Help-Themenliste",
    "Browse topics from the Help tab sidebar.": "Themen in der Help-Seitenleiste durchsuchen.",
    "Help article rendered": "Gerendeter Help-Artikel",
    "In-app Markdown rendered with the app theme.": "In-App-Markdown im App-Theme.",
    "Tip:": "Tipp:",
    "Keep a backup of your journal before bulk imports or experimental AI-suggested rewrites. Enable automatic backup under Settings → Backup.": "Sichern Sie Ihr Journal vor Massenimporten oder experimentellen KI-Umschreibungen. Automatisches Backup unter Einstellungen → Backup aktivieren.",
    "Next: Custom buttons (YAML) →": "Weiter: Eigene Schaltflächen (YAML) →",
    "Settings overview →": "Einstellungsübersicht →",
    "Settings": "Einstellungen",
    "Settings → AI": "Einstellungen → KI",
    "Custom buttons (YAML)": "Eigene Schaltflächen (YAML)",
    "← User guide": "← Benutzerhandbuch",
    "Sections": "Abschnitte",
    "General": "Allgemein",
    "Advanced": "Erweitert",
    "Appearance": "Erscheinungsbild",
    "Logs": "Protokolle",
}

FR: dict[str, str] = {
    "User guide": "Guide utilisateur",
    "Moni is a desktop companion for plain-text hledger journals. This guide walks through each tab in the app bar and what you can do there. Screenshots below are placeholders — replace them with real captures from your build when ready.": "Moni est un compagnon de bureau pour les journaux hledger en texte brut. Ce guide parcourt chaque onglet de la barre d'application et ce que vous pouvez y faire. Les captures ci-dessous sont des placeholders — remplacez-les par de vraies captures de votre build quand vous êtes prêt.",
    "On this page": "Sur cette page",
    "The tab bar": "La barre d'onglets",
    "Seven tabs run across the top of the window. Together they cover daily ledger work, account browsing, reporting, CSV import, configuration, and in-app documentation.": "Sept onglets traversent le haut de la fenêtre. Ils couvrent le travail quotidien, les comptes, les rapports, l'import CSV, la configuration et l'aide intégrée.",
    "Tab": "Onglet",
    "Purpose": "Objectif",
    "Tip:": "Astuce :",
    "Settings": "Paramètres",
    "Settings → AI": "Paramètres → IA",
    "Custom buttons (YAML)": "Boutons personnalisés (YAML)",
    "← User guide": "← Guide utilisateur",
    "Settings overview →": "Vue d'ensemble des paramètres →",
    "Next: Custom buttons (YAML) →": "Suivant : Boutons personnalisés (YAML) →",
    "Sections": "Sections",
    "General": "Général",
    "Advanced": "Avancé",
    "Appearance": "Apparence",
    "Logs": "Journaux",
}


def main() -> None:
    for lang, mapping in (("de", DE), ("fr", FR)):
        for name in ("index.html", "settings.html", "settings-ai.html", "custom-buttons.html"):
            src = ROOT / "en" / name
            html = apply(src.read_text(encoding="utf-8"), mapping)
            (ROOT / lang / name).write_text(html, encoding="utf-8")
            print(f"updated {lang}/{name}")


if __name__ == "__main__":
    main()
