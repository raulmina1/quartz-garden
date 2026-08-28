---
title: "KG Context vs RAG — zwei Quellen, ein Gedächtnis"
tags:
  - knowledge-graph
  - rag
  - semantic-web
  - ra-blog
description: "Der Unterschied zwischen Knowledge-Graph-Kontext und Vektor-RAG: zwei Quellen, die zusammen die vollständige, optimierte Erinnerung ergeben."
reading_time: "3 min"
type: showcase
lang: de
publish: true
created: 2026-08-20
status: draft
semantic_class: showcase
see_also:
  - "[[Semantic Web/Knowledge-Graphs]]"
  - "[[Semantic Web/RDF]]"
  - "[[Semantic Web/SPARQL]]"
  - "[[Projekte/AI Ecosystem Data Pipeline]]"
  - "[[AI Ecosystem]]"
---

# KG Context vs RAG — zwei Quellen, ein Gedächtnis

> Ein Knowledge Graph kennt die Struktur. Ein Vektor-RAG kennt die Bedeutung. Beide zusammen ergeben die vollständige, optimierte Erinnerung.

<iframe src="/static/mental-maps/kg-context-vs-rag.html" style="width:100%;height:720px;border:1px solid #3a3a3a;border-radius:8px;background:#000" title="KG Context vs RAG — zwei Quellen, ein Gedächtnis"></iframe>

## Zwei Gehirne, zwei Fragen

Das System fragt denselben Wissensbestand mit **zwei unterschiedlichen "Gehirnen"**. Keines deckt allein das ganze Bild ab:

| Gehirn | Engine | Was es beantwortet | Natur |
|---|---|---|---|
| 🕸️ **Knowledge Graph (KG)** | GraphDB (SPARQL) | *Wie ist diese Notiz verbunden?* — Backlinks, Tags, Nachbarn mit gleichem Tag, Strong Ties, 2-Hop | **Struktur** — exakt, deterministisch, null Halluzination |
| 🧠 **Vektor-RAG** | ChromaDB + e5-small | *Worum geht es?* Notizen, die semantisch ähnlich sind | **Bedeutung** — vage, nach Embedding-Ähnlichkeit |

**Faustregel:** Der KG antwortet *"wie ist etwas verbunden"* (Kanten, Labels, Fakten); das RAG antwortet *"was bedeutet etwas"* (Inhalt, Ähnlichkeit). Keines allein ist das vollständige Bild — genau dafür gibt es die Fusion.

## Warum man BEIDE braucht

- **Der KG ist exakt, aber auf das Explizite begrenzt:** Er sieht nur Verbindungen, die schon existieren (Wikilinks, Tags). Wenn eine Notiz *ähnlich* ist, aber keinen Tag oder Link teilt, **findet der KG sie nicht**. Das ist das "strukturelle Gedächtnis".
- **Das RAG ist flexibel, aber ungenau:** Es findet Ähnliches nach Bedeutung, auch wenn sich Ordner/Tags/Links unterscheiden. Aber es ist **verschwommen** (Ähnlichkeit, kein Fakt) und kann Rauschen mitreißen.
- **Jedes deckt die Blindheit des anderen ab:**
  - Der KG liefert **verifizierbare Fakten** (Backlinks, Tags), die das RAG semantisch nicht kann.
  - Das RAG liefert **konzeptionelle Nachbarn**, die der KG nie sieht (andere Ordner, andere Tags).

## Der Wert der Fusion

`hybrid_context.py` **verschmilzt** beide in **einem** Callout, der in den Prompt eingespielt wird:

```
> [!info]+ Hybrid Context (KG + RAG)
> 🕸️ Knowledge Graph: Notiz · Tags · Verlinkt von · Gleiche Tags
> 🔍 Semantic (RAG): verwandte Notizen nach Ähnlichkeit (sim: 0.x)
```

Das Modell sieht gleichzeitig **wo die Notiz im Netz lebt** (Struktur) und **worum es geht** (Semantik). Das ist das vollständige, optimierte Gedächtnis.

## Aktuelle Zahlen (live 17.08.26)

| Quelle | Metrik | Wert |
|---|---|---|
| 🕸️ KG (GraphDB) | Triples | 57.964 |
| | Notizen indexiert | 4.063 |
| | Wikilinks | 18.672 (30% auf echte IRIs aufgelöst) |
| | hasTag | 4.745 |
| | Mentions NER | 6.210 · 74 Entitäten |
| | 2-Hop / Strong Ties | 226.001 / 1.030 |
| 🧠 RAG (ChromaDB) | Chunks | 15.076 (14.180 beim Re-Index 13.08) |
| | Dateien | 5.810 |
| | Embeddings | e5-small + Cross-Encoder-Rerank |

## Noch offene Verbesserungen

| Offen | Status | Hinweis |
|---|---|---|
| **Graph-Embeddings (node2vec)** | ⏳ Offen | Einzige nicht umgesetzte Roadmap-Idee: "ähnliche Notizen" über geteilte Tags hinaus. Aufwendig und spekulativ — neu bewerten, sobald der Rest stabil ist. |
| **Token-Tracking** | ⏳ Offen | Noch kein Session-Token-Zähler, der den realen Einspar-Effekt des Kontexts misst. Ohne das gibt es keine bezifferte €-Angabe. |
| **Notizen ohne Tags** | 1.804 (44%) | Der Enricher ist additiv und erstellt kein neues Frontmatter; der Cron baut den Rückstau schrittweise ab. |
| **Gelöschte / stark geänderte Notizen** | ⚠️ | Der KG-Increment fügt nur hinzu; Löschungen/Änderungen bereinigt der 5-Uhr-Rebuild. |

## Der potenzielle Nutzen

**Bereits gemessen und gewonnen:**
- **Kontext-Latenz:** Context-Cache **60s → 0,5s** für unveränderte Notizen.
- **RAG-Qualität:** Der Cross-Encoder-Reranker entfernte einen **falschen Positiv** — ein Chunk gab sim 0,963 (irrelevantes Rauschen) und der Reranker senkte ihn auf **0,243**, wodurch das korrekte Ergebnis aufstieg.
- **Anti-Halluzination:** KG-Kontext exakt, ohne erfundene Verbindungen.
- **Disambiguierung:** `--folder` löst Homonyme (14 "Untitled"-Notizen), kein vermischter Kontext.

**Potenzial (zu messen mit Token-Tracking):**
- Präziserer **und kürzerer** Kontext = weniger Re-Run-Tokens des LLM (weniger Nacharbeit, weniger Kontext-Müll, den er filtern muss).
- **Ehrliche Angabe:** Noch gibt es keine gemessene €-Zahl, weil TSK-113 (Token-Tracking) fehlt. Erst wenn die Messung existiert, lässt sich der Euro-Betrag beziffern — vorher wäre es erfunden.

---

*Erst mit beiden Quellen wird die Erinnerung vollständig — Struktur plus Bedeutung. Schreib mir → raul.mina1@outlook.com*
