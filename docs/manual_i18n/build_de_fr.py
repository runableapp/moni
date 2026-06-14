#!/usr/bin/env python3
"""Build de/fr manual bodies: start from es where complete, else en; apply locale maps."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "bodies"

PRE_RE = re.compile(r"<pre class=\"manual-code\">.*?</pre>", re.S)


def protect(html: str) -> tuple[str, list[str]]:
    blocks: list[str] = []

    def stash(m: re.Match[str]) -> str:
        blocks.append(m.group(0))
        return f"@@PRE{len(blocks) - 1}@@"

    return PRE_RE.sub(stash, html), blocks


def restore(html: str, blocks: list[str]) -> str:
    for i, b in enumerate(blocks):
        html = html.replace(f"@@PRE{i}@@", b)
    return html


def apply_map(html: str, mapping: dict[str, str]) -> str:
    protected, blocks = protect(html)
    for src, dst in sorted(mapping.items(), key=lambda x: -len(x[0])):
        protected = protected.replace(src, dst)
    return restore(protected, blocks)


# Maps Spanish (complete es bodies) → target locale for pages translated via es pipeline.
ES_TO_DE: dict[str, str] = {
    "Guía de usuario": "Benutzerhandbuch",
    "En esta página": "Auf dieser Seite",
    "La barra de pestañas": "Die Tab-Leiste",
    "Pestaña": "Tab",
    "Propósito": "Zweck",
    "Ajustes": "Einstellungen",
    "Secciones": "Abschnitte",
    "Guía completa:": "Ausführliche Anleitung:",
    "Resumen de Settings": "Einstellungsübersicht",
    "Guía de usuario →": "Benutzerhandbuch →",
    "← Guía de usuario": "← Benutzerhandbuch",
    "← Resumen de Settings": "← Einstellungsübersicht",
    "Siguiente: Botones personalizados (YAML) →": "Weiter: Eigene Schaltflächen (YAML) →",
    "Botones personalizados (YAML) →": "Eigene Schaltflächen (YAML) →",
    "Consejo:": "Tipp:",
    "Elegir proveedor": "Anbieter wählen",
    "Proveedor": "Anbieter",
    "Privacidad": "Datenschutz",
    "Uso típico": "Typische Nutzung",
    "Chat desactivado": "Chat deaktiviert",
    "Solo libro mayor": "Nur Ledger-Workflow",
    "Totalmente local": "Vollständig lokal",
    "Servidor gestionado, descarga de modelo, soporte GPU": "Verwalteter Server, Modell-Download, GPU-Unterstützung",
    "Local (daemon Ollama)": "Lokal (Ollama-Daemon)",
    "Si ya ejecutas modelos Ollama": "Wenn Sie bereits Ollama-Modelle nutzen",
    "API en la nube": "Cloud-API",
    "Modelos potentes con hardware local limitado": "Starke Modelle bei begrenzter lokaler Hardware",
    "Vía app de escritorio Runable": "Über Runable-Desktop-App",
    "Puente de extensión o Electron a servicios externos": "Extension- oder Electron-Brücke zu externen Diensten",
    "Controles clave": "Wichtige Steuerelemente",
    "Resolución de problemas": "Fehlerbehebung",
    "Comportamiento del chat en Main": "Chat-Verhalten auf Main",
    "Comportamiento del chat": "Chat-Verhalten",
    "Documentación hledger (RAG)": "hledger-Dokumentation (RAG)",
    "Proveedores en la nube": "Cloud-Anbieter",
    "Proveedores en la nube (OpenAI, Claude, Gemini)": "Cloud-Anbieter (OpenAI, Claude, Gemini)",
    "IA local (llama.cpp)": "Lokale KI (llama.cpp)",
    "Dónde viven las recetas": "Wo Rezepte liegen",
    "Receta mínima": "Minimales Rezept",
    "Tablas de texto delimitado": "Tabelle aus begrenztem Text",
    "Recetas de varios pasos": "Mehrstufige Rezepte",
    "Fechas por defecto": "Standarddaten",
    "Transformaciones": "Transformationen",
    "Varias tablas": "Mehrere Tabellen",
    "Programas externos": "Externe Programme",
    "Tubería y salida vacía": "Pipe und leere Ausgabe",
    "Marcadores integrados": "Eingebaute Platzhalter",
    "Gráficos opcionales": "Optionale Diagramme",
    "Conectar en Settings": "In Einstellungen verbinden",
    "Ubicación": "Speicherort",
    "← Guía de usuario": "← Benutzerhandbuch",
}

ES_TO_FR: dict[str, str] = {
    "Guía de usuario": "Guide utilisateur",
    "En esta página": "Sur cette page",
    "La barra de pestañas": "La barre d'onglets",
    "Pestaña": "Onglet",
    "Propósito": "Objectif",
    "Ajustes": "Paramètres",
    "Secciones": "Sections",
    "Guía completa:": "Guide complet :",
    "Resumen de Settings": "Vue d'ensemble des paramètres",
    "Guía de usuario →": "Guide utilisateur →",
    "← Guía de usuario": "← Guide utilisateur",
    "← Resumen de Settings": "← Vue d'ensemble des paramètres",
    "Siguiente: Botones personalizados (YAML) →": "Suivant : Boutons personnalisés (YAML) →",
    "Botones personalizados (YAML) →": "Boutons personnalisés (YAML) →",
    "Consejo:": "Astuce :",
    "Elegir proveedor": "Choisir un fournisseur",
    "Proveedor": "Fournisseur",
    "Privacidad": "Confidentialité",
    "Uso típico": "Usage typique",
    "Chat desactivado": "Chat désactivé",
    "Solo libro mayor": "Workflow ledger uniquement",
    "Totalmente local": "Entièrement local",
    "Resolución de problemas": "Dépannage",
    "Dónde viven las recetas": "Où vivent les recettes",
    "Receta mínima": "Recette minimale",
    "Tablas de texto delimitado": "Tableaux texte délimité",
    "Recetas de varios pasos": "Recettes multi-étapes",
    "Fechas por defecto": "Dates par défaut",
    "Transformaciones": "Transformations",
    "Varias tablas": "Plusieurs tableaux",
    "Programas externos": "Programmes externes",
    "Tubería y salida vacía": "Pipe et sortie vide",
    "Marcadores integrados": "Espaces réservés intégrés",
    "Gráficos opcionales": "Graphiques optionnels",
    "Conectar en Settings": "Brancher dans Paramètres",
    "Ubicación": "Emplacement",
}

# English → locale for pages still generated from en (fallback) and extra coverage.
EN_TO_DE: dict[str, str] = {
    "User guide": "Benutzerhandbuch",
    "Settings": "Einstellungen",
    "On this page": "Auf dieser Seite",
    "Custom buttons (YAML)": "Eigene Schaltflächen (YAML)",
    "Settings → AI": "Einstellungen → KI",
}

EN_TO_FR: dict[str, str] = {
    "User guide": "Guide utilisateur",
    "Settings": "Paramètres",
    "On this page": "Sur cette page",
    "Custom buttons (YAML)": "Boutons personnalisés (YAML)",
    "Settings → AI": "Paramètres → IA",
}


def build_lang(lang: str, es_map: dict[str, str], en_map: dict[str, str]) -> None:
    for name in ("index.html", "settings.html", "settings-ai.html", "custom-buttons.html"):
        es_src = ROOT / "es" / name
        en_src = ROOT / "en" / name
        src = es_src if es_src.is_file() and lang in ("de", "fr") else en_src
        html = src.read_text(encoding="utf-8")
        if src == es_src:
            html = apply_map(html, es_map)
        else:
            html = apply_map(html, en_map)
        # Also apply English map for leftover English fragments
        html = apply_map(html, en_map)
        (ROOT / lang / name).write_text(html, encoding="utf-8")
        print(f"wrote {lang}/{name}")


def main() -> None:
    build_lang("de", ES_TO_DE, EN_TO_DE)
    build_lang("fr", ES_TO_FR, EN_TO_FR)


if __name__ == "__main__":
    main()
