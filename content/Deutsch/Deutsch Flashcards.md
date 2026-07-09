---
title: "Deutsch Flashcards — Interaktives Lernspiel"
date: 2026-07-09
tags:
  - deutsch
  - flashcards
  - vhs
  - spiel
  - lernen
description: "Interaktives Memory-Spiel mit Vokabeln aus meinem VHS-Deutschkurs. Finde die Paare — deutsches Wort und englische Übersetzung."
reading_time: "1 min"
type: showcase
lang: de
publish: true
---

# 🃏 Deutsch Flashcards

*Interaktives Memory-Spiel — Vokabeln aus meinem VHS-Kurs*

---

Wähle ein Deck, finde die passenden Paare aus deutschen Wörtern und ihren englischen Übersetzungen. Das Spiel speichert deinen Fortschritt lokal im Browser — kein Login, keine App.

> [!tip] So funktioniert's
> 1. **Deck wählen** — jedes Deck entspricht einer Unterrichtseinheit
> 2. **Spielfeldgröße wählen** — 4×4 (8 Paare) oder 6×6 (18 Paare)
> 3. **Karten umdrehen** — klicke auf zwei Karten. Gleiches Paar? Sie bleiben offen. Unterschiedlich? Sie drehen sich zurück.
> 4. **Alle Paare finden** — schaffe es in möglichst wenigen Zügen!

---

## Technische Umsetzung

Das Spiel wird als standalone HTML-Widget in Quartz eingebettet (`<iframe>`). Die Vokabeldaten werden automatisch aus meinen Anki-Notizen im YellowVault extrahiert:

```
01_DATABASE/*.md  →  extract_flashcards.py  →  vhs-decks.json  →  matching-pairs.html
```

- **Extraction:** Python-Script parst `:::` (Vokabeln) und `::` (Grammatik) aus den Markdown-Notizen
- **Game engine:** Vanilla JS + CSS 3D transforms — keine externen Abhängigkeiten
- **Speicherung:** `localStorage` für Session-Persistenz
- **Deployment:** Automatisch via `quartz sync` → GitHub Actions → GitHub Pages

## Verwandte Notizen

- [[Deutsch lernen als Ingenieur]] — Hintergrund zu meinem Lernsystem
- [[Die Werkzeuge, die ich mir selbst gebaut habe]] — Übersicht meiner Automatisierungen
