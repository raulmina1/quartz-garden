---
title: "KGE Link Prediction — YellowVault Knowledge Graph"
tags:
  - ai
  - knowledge-graph
  - embeddings
  - kge
  - ra-blog
description: "Knowledge Graph Embeddings (TransE) para predecir conexiones faltantes en un vault de 4.660 notas. MRR 0.1985 (1.49x sobre baseline) y 266 wikilinks densificados automáticamente, 0 corruptos."
reading_time: "4 min"
type: showcase
lang: de
publish: true
created: 2026-08-26
status: draft
semantic_class: showcase
see_also:
  - "[[AI Ecosystem]]"
  - "[[Projekte/AI Ecosystem Data Pipeline]]"
  - "[[Semantic Web/KG-Context-vs-RAG]]"
  - "[[Semantic Web/Knowledge-Graphs]]"
---

# KGE Link Prediction — YellowVault Knowledge Graph

> Ein Vault ist kein statisches Archiv — es ist ein Graph, der lernen kann.

Das YellowVault-Projekt ging einen Schritt weiter: statt den **Knowledge Graph** nur abzufragen, lernt ein **Knowledge Graph Embedding (TransE)** aus den realen Triples und **sagt fehlende Verbindungen voraus**. Das Modell densifizierte 1.925 verwaiste Notizen und schrieb 266 semantisch plausible Wikilinks automatisch — ohne einen einzigen korrupten Frontmatter.

## Das komplette Diagramm

<iframe src="/static/mental-maps/kge-link-prediction.html" style="width:100%;height:720px;border:1px solid #3a3a3a;border-radius:8px;background:#000" title="KGE Link Prediction Pipeline"></iframe>

## Was ist das Problem?

Im Vault hatten **48 % der Notizen keinen einzigen Wikilink** — sie hingen als Inseln im Graph. KGE löst das als **Link Prediction**: gegeben ein Triple `(h, r, ?)`, lernt das Modell `h + r ≈ t` und schlägt den plausibelsten Objektknoten vor.

| Konzept | In diesem Projekt |
|---|---|
| Triples | **27.726** extrahiert aus `yellowvault_export.ttl` |
| Wichtigste Relationen | `wikilink` 12.885 · `mentions` 7.525 · `hasTag` 7.316 |
| Entitäten | **7.055** (Notizen, Tags, NER-Entitäten) |
| Modell | **TransE** (dim 100, margin 1.0, torch) |
| Split | 90/5/5 **ohne Entity-Leak** |

## Die Pipeline

```
yellowvault_export.ttl
  → kge_export.py        (rdflib → triples.csv + Mappings + Split ohne Leak)
  → kge_train.py         (TransE, early stopping, Embeddings)
  → kge_baseline.py      (Co-Occurrence-Baseline zum Vergleich)
  → kge_predict.py       (Link Prediction → Wikilink-Vorschläge)
  → kge_hybrid_filter.py (semantischer Filter, e5-small)
  → kge_validate.py      (5 SPARQL-Regeln gegen den echten Graphen)
  → kge_apply_frontmatter.py v2 (ruamel + Backup + Revert)
  → sparql_bridge.py --predict-links
```

## Ergebnisse (TEST, filtered)

| Metrik | **TransE** | Baseline Co-Occ. | Gewinn |
|---|---|---|---|
| **MRR** | **0.1985** | 0.1330 | **1.49×** |
| **Hits@1** | **0.1162** | 0.0000 | **~3×** |
| Hits@10 | 0.3424 | 0.4743 | B2 gewinnt rohes Recall |

> [!tip] Experten-Fazit
> TransE gewinnt klar beim **präzisen Ranking** (MRR, Hits@1). Das Baseline-Modell gewinnt nur rohes Hits@10, weil es Co-Occurrents **ohne Sortierung** listet — hohes Recall, schlechtes Ranking. Für *Verbindungen vorschlagen* ist TransE das richtige Modell: **Das Embedding liefert echten gelernten Strukturwert, kein Frequenz-Rauschen.**

## Densifizierung (der produktive Teil)

- **1.925 verwaiste Notizen** → **9.625 Vorschläge** (top-5, `--diversity 20`), über **532 eindeutige Ziele**.
- **Semantischer Filter** (`kge_hybrid_filter.py`, multilingual-e5-small): 9.625 strukturelle → **4.175 semantisch plausibel**, Ziele 4 → **320 eindeutige**. Paare wie `Reflexive Verben → Dativ`, `SQLite → AI Hook - Prompt Runner Watcher`.
- **Validierung** (`kge_validate.py`, 5 Regeln): 9.625 → **9.622 gültig** (nur 3 durch inverse Kante abgelehnt).
- **Angewendet (hohe Konfidenz):** **266 Top-1-Links** mit Cosinus-Ähnlichkeit ≥ 0.85 als `see_also` geschrieben — **264/264 Dateien OK, 0 korrupt, 0 dangling**. Backups in `state/kge_frontmatter_backup_v2/`.

## Warum TransE und nicht RotatE?

| Modell | MRR (TEST) | Hits@1 | Hits@10 | Urteil |
|---|---|---|---|---|
| **TransE** | **0.2044** | 0.1451 | 0.3417 | ✅ Generalisiert |
| RotatE | 1.0000 | 1.0000 | 1.0000 | ⚠️ Überanpassung |

RotatE **memorisiert** den kleinen Graphen (nur 3 Relationen) und liefert perfekte 1.0 — ein Warnsignal, kein Sieg. **TransE ist das richtige Modell für einen Graphen dieser Größe.**

## Zahlen hinter dem Projekt

| Etappe | Live-Kennzahlen |
|---|---|
| 📦 Datenquelle | 27.726 Triples · TTL-Master · GraphDB nur Ontologie |
| ⚙️ Export | 7.055 Entitäten · 3 Relationen · Split ohne Leak |
| 🧠 Training | TransE dim 100 · Early stopping · ~Minuten auf CPU/GPU |
| 📈 Evaluation | MRR 0.1985 · Hits@1 0.1162 · **1.49× Baseline** |
| 🔮 Densifizierung | 1.925 Waisen-Notizen → 266 Links hochvertraulich, 0 korrupt |
| 🛡️ Integration | `sparql_bridge.py --predict-links` · Cron re-train So 06:00 |

> [!note] RA
> Ein Embedding ist kein Zauber — es ist der Graph, der aufhört, still zu sein.

---

*Was passiert mit deinen Notizen, wenn der Graph sie von selbst verbindet? Schreib mir → raul.mina1@outlook.com*
