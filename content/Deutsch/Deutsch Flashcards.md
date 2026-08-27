---
title: "Deutsch Flashcards — Interaktive Lernspiele"
date: 2026-07-09
tags:
  - deutsch
  - flashcards
  - vhs
  - spiel
  - lernen
description: "Drei interaktive Lernspiele aus meinem VHS-Deutschkurs: Matching Pairs, Flash Cards und Multiple Choice für Vokabeln, Grammatik und Phrasen."
reading_time: "2 min"
type: showcase
lang: de
publish: true
---

# 🃏 Deutsch Flashcards

_Drei Spiele — Vokabeln und Grammatik aus meinem VHS-Kurs B1.1/B1.2_

---

## 🃏 Matching Pairs — Vokabeln

Finde die Paare: deutsches Wort ↔ englische Übersetzung. Trainiert Artikel, Plural und Kontext.

> [!tip] So funktioniert's
>
> 1. **Deck wählen** — jedes Deck entspricht einer Unterrichtseinheit
> 2. **Spielfeldgröße wählen** — 4×4 (8 Paare) oder 6×6 (18 Paare)
> 3. **Karten umdrehen** — klicke auf zwei Karten. Gleiches Paar? Sie bleiben offen. Unterschiedlich? Sie drehen sich zurück.
> 4. **Alle Paare finden** — schaffe es in möglichst wenigen Zügen!

<iframe src="/static/flashcards/matching-pairs.html"
  style="width:100%;height:620px;border:1px solid #e0e0d8;border-radius:12px;background:#0d0d0d;">
</iframe>

---

## 📇 Flash Cards — Grammatik & Phrasen

Lies die Frage, überlege die Antwort, decke auf und bewerte dich selbst. Perfekt für Grammatik-Regeln, Verben mit Präpositionen, Eselsbrücken und Phrasen.

> [!tip] So funktioniert's
>
> 1. **Deck wählen** und auf **Start** klicken
> 2. **Frage lesen** — überlege dir die Antwort
> 3. **Karte antippen** — die Antwort erscheint
> 4. **Selbst bewerten:** ✓ Gewusst oder ✗ Wiederholen
> 5. Am Ende: alle ✗-Karten kommen in eine Wiederholungsrunde
>
> **Tastatur**: Leertaste = aufdecken · ← = wiederholen · → = gewusst

<iframe src="/static/flashcards/flash-cards.html"
  style="width:100%;height:680px;border:1px solid #e0e0d8;border-radius:12px;background:#0d0d0d;">
</iframe>

---

## 🎯 Multiple Choice — Wortschatz

Lies das Wort, wähle die richtige Übersetzung aus vier Optionen. Sofortiges Feedback mit Beispielsatz — perfekt für schnelle Wiederholungsrunden.

> [!tip] So funktioniert's
>
> 1. **Deck wählen** und Richtung wählen: Deutsch → Englisch oder Englisch → Deutsch
> 2. **Frage lesen** — vier Antworten stehen zur Auswahl
> 3. **Antwort wählen** — sofortiges Feedback: ✓ Richtig oder ✗ Falsch
> 4. **Am Ende:** dein Ergebnis in Prozent — wiederhole die Runde, bis du 100 % erreichst

<iframe src="/static/flashcards/multiple-choice.html"
  style="width:100%;height:680px;border:1px solid #e0e0d8;border-radius:12px;background:#0d0d0d;">
</iframe>

---

## Technische Umsetzung

Die Spiele werden als standalone HTML-Widgets in Quartz eingebettet (`<iframe>`). Die Vokabeldaten werden automatisch aus meinen Anki-Notizen im YellowVault extrahiert:

```
01_DATABASE/*.md  →  extract_flashcards.py  →  vhs-decks.json  →  matching-pairs.html / flash-cards.html / multiple-choice.html
```

- **Extraction:** Python-Script parst `:::` (Vokabeln) und `::` (Grammatik) aus den Markdown-Notizen
- **Game engines:** Vanilla JS + CSS 3D transforms — keine externen Abhängigkeiten
- **Speicherung:** `localStorage` für Session-Persistenz
- **Deployment:** Automatisch via `quartz sync` → GitHub Actions → GitHub Pages

> [!note] Über die Karten
> Die Vokabeln und Grammatik-Karten stammen aus meinem Deutschkurs an der VHS (B1.1 und B1.2). Sie werden automatisch aus meinen Anki-Notizen extrahiert — jede Karte enthält den Artikel, die Pluralform und einen Beispielsatz im Originalkontext. Mehr dazu: [[Kolumnen/Deutsch lernen als Ingenieur]].

## Verwandte Notizen

- [[Kolumnen/Deutsch lernen als Ingenieur]] — Hintergrund zu meinem Lernsystem
- [[Kolumnen/Die Werkzeuge, die ich mir selbst gebaut habe]] — Übersicht meiner Automatisierungen

---

_Hast du ein Deck, das ich hinzufügen soll? Schick mir deine Vokabeln — ich baue ein Spiel daraus. → [raul.mina1@outlook.com](mailto:raul.mina1@outlook.com)_
