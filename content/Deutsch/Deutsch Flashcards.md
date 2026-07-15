---
title: "Deutsch Lernkarten"
date: 2026-07-09
tags:
  - deutsch
  - lernkarten
  - vhs
  - spiel
  - lernen
description: "Drei interaktive Lernspiele mit Vokabeln und Grammatik aus meinem VHS-Deutschkurs. Multiple Choice, Paare finden und Lernkarten zum Selbsttesten."
reading_time: "2 min"
type: showcase
lang: de
publish: true
---

# Lernkarten & Spiele

*Vokabeln und Grammatik aus meinem VHS-Kurs B1.1/B1.2*

---

## Multiple Choice

Wähle die richtige Übersetzung aus vier Optionen. Schnelles Feedback, Punkte-Zählung und Fortschrittsbalken. Wechsle zwischen DE → EN und EN → DE.

> [!tip] So funktioniert's
> 1. **Deck wählen** und auf **Start** klicken
> 2. **Deutsches Wort erscheint** — wähle die richtige englische Übersetzung
> 3. **Richtige Antwort** = grün ✓ · **Falsche Antwort** = rot ✗ mit Korrektur
> 4. **Tastatur**: 1–4 = Option wählen · Enter/→ = nächste Frage
> 5. Wechsle die Richtung mit **DE → EN / EN → DE**

<iframe src="/static/flashcards/multiple-choice.html"
  style="width:100%;height:620px;border:1px solid #c4ab00;border-radius:12px;background:#0d0d0d;">
</iframe>

---

## Paarspiel

Finde die Paare: deutsches Wort und englische Übersetzung. Trainiert Artikel, Plural und Kontext.

> [!tip] So funktioniert's
> 1. **Deck wählen** — jedes Deck entspricht einer Unterrichtseinheit
> 2. **Spielfeldgröße wählen** — 4×4 (8 Paare) oder 6×6 (18 Paare)
> 3. **Karten umdrehen** — klicke auf zwei Karten. Gleiches Paar? Sie bleiben offen. Unterschiedlich? Sie drehen sich zurück.
> 4. **Alle Paare finden** — schaffe es in möglichst wenigen Zügen!

<iframe src="/static/flashcards/matching-pairs.html"
  style="width:100%;height:620px;border:1px solid #c4ab00;border-radius:12px;background:#0d0d0d;">
</iframe>

---

## Selbsttest

Lies die Frage, überlege die Antwort, decke auf und bewerte dich selbst. Perfekt für Grammatik-Regeln, Verben mit Präpositionen, Eselsbrücken und Phrasen.

> [!tip] So funktioniert's
> 1. **Deck wählen** und auf **Start** klicken
> 2. **Frage lesen** — überlege dir die Antwort
> 3. **Karte antippen** — die Antwort erscheint
> 4. **Selbst bewerten:** ✓ Gewusst oder ✗ Wiederholen
> 5. Am Ende: alle ✗-Karten kommen in eine Wiederholungsrunde
>
> **Tastatur**: Leertaste = aufdecken · ← = wiederholen · → = gewusst

<iframe src="/static/flashcards/flash-cards.html"
  style="width:100%;height:680px;border:1px solid #c4ab00;border-radius:12px;background:#0d0d0d;">
</iframe>

---

## Technik

Die Spiele werden als standalone HTML-Widgets in Quartz eingebettet (`<iframe>`). Die Vokabeldaten werden automatisch aus meinen Anki-Notizen im YellowVault extrahiert:

```
01_DATABASE/*.md  →  extract_flashcards.py  →  vhs-decks.json  →  multiple-choice.html / matching-pairs.html / flash-cards.html
```

- **Extraktion:** Python-Skript parst `:::` (Vokabeln) und `::` (Grammatik) aus den Markdown-Notizen
- **Spiele-Engine:** Vanilla JS + CSS 3D-Transformationen — keine externen Abhängigkeiten
- **Speicherung:** `localStorage` für Sitzungs-Persistenz
- **Bereitstellung:** Automatisch über `quartz sync` → GitHub Actions → GitHub Pages

> [!note] Über die Karten
> Die Vokabeln und Grammatik-Karten stammen aus meinem Deutschkurs an der VHS (B1.1 und B1.2). Sie werden automatisch aus meinen Anki-Notizen extrahiert — jede Karte enthält den Artikel, die Pluralform und einen Beispielsatz im Originalkontext. Mehr dazu: [[Kolumnen/Deutsch lernen als Ingenieur]].

---

*Hast du ein Deck, das ich hinzufügen soll? Schick mir deine Vokabeln — ich baue ein Spiel daraus. → [raulmina13@gmail.com](mailto:raulmina13@gmail.com)*
