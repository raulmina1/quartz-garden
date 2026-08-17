---
title: "Der Weg einer Notiz: meine Daten-Pipeline"
tags:
  - ai
  - ecosystem
  - data-pipeline
  - ra-blog
description: "Was passiert mit einer Notiz, nachdem du sie geschrieben hast? NER → Knowledge Graph (51.811 Triples) → RAG (14.180 Chunks). Meine lokale Daten-Pipeline, alle 30 Minuten."
reading_time: "4 min"
type: showcase
lang: de
publish: true
created: 2026-08-17
status: published
---

# Der Weg einer Notiz: meine Daten-Pipeline

> Ich schreibe eine Notiz. Dann passiert etwas — ohne dass ich einen Finger rühre.

Jede Notiz in meinem Obsidian-Vault durchläuft eine Daten-Pipeline: **Entitäten werden erkannt, Metadaten angereichert, alles wird in einen Knowledge Graph (51.811 Triples) und parallel in einen Vektor-Index (14.180 Chunks) verwandelt.** Alle 30 Minuten, automatisch, lokal — ohne SaaS.

## Das komplette Diagramm

<iframe src="/static/mental-maps/ecosystem-data-pipeline.html" style="width:100%;height:720px;border:1px solid #3a3a3a;border-radius:8px;background:#000" title="Daten-Pipeline AI-Ökosystem"></iframe>

## DP-1 · Ingesta & Anreicherung

Ein Orchestrator (`vault_structure_sync.py`) tickt alle 30 Minuten und koordiniert:

| Schritt | Werkzeug | Ergebnis |
|---------|----------|----------|
| Entity-Erkennung | `ner_extract.py` (lokal, Wörterbuch) | 6.210 Mentions · 74 Entitäten |
| Zwischenspeicher | `ner_cache.ndjson` + `mentions.ttl` | Input für den RDF-Parser |
| Anreicherung | `frontmatter_enricher.py` | Tags, created, Aliase — mit Backup + Changelog |

## DP-2 · Knowledge Graph

- **`parse_vault_to_rdf.py`** baut inkrementell (`--since` + State-File) RDF-Triples; um 5 Uhr ein kompletter Rebuild (`--replace`).
- **`yellowvault_export.ttl`** — 51.811 Triples — wird in **11 Chunks** nach **GraphDB** geladen.
- Stündlich hält **`kg_incremental_sync.py`** den Graph frisch (inkl. WebVOWL-Refresh).
- Drei Dashboards lesen direkt vom Graph: **WebVOWL :3000** (Ontologie), **Grafana :4000** (5 SPARQL-Panels), **RA Log Viewer :8485** (Ecosistema-Tab).

## DP-3 · Vektor-RAG

Notizen werden mit **e5-small** eingebettet → **ChromaDB** (14.180 Chunks, 5.810 Dateien). Ein optionaler **Cross-Encoder** re-rankt die Treffer. `hybrid_context.py` fusioniert KG- und Vektor-Ergebnisse — mit 0,5s Cache.

## DP-4 · Konsumenten

Drei Abfrage-Pfade speisen den **Prompt Runner**:

| Agent | Funktion |
|-------|----------|
| `sparql_bridge --kg-context` | 3 SPARQL-Queries: Tags, Backlinks, Nachbarn → Kontextblock |
| `qa_kg` | Natürliche Sprache → SPARQL |
| `hybrid_context` | KG + RAG fusioniert |

## DP-5 · Betrieb — die langweilige Schicht

| Komponente | Job |
|------------|-----|
| `backup_graphdb.py` | Backup So 4 Uhr → OneDrive, Retention 7 |
| `sync_health_check.py` | Alarm unter 35K Triples |
| `keep-alive cron` | GraphDB 8–22 Uhr am Leben halten, Auto-Start 30–90s |
| `ecosystem_status.py` | Status → Grafana + Telegram |

## Zahlen hinter der Pipeline

| Etappe | Live-Kennzahlen |
|--------|-----------------|
| 📁 Quelle | 4.063 Notizen |
| ⚙️ Ingesta | 6.210 Mentions · 74 Entitäten · 30-Min-Tick |
| 🕸️ Knowledge Graph | 51.811 Triples · 11 Chunks · stündlicher Sync |
| 🧠 Vektor-RAG | 14.180 Chunks · 5.810 Dateien · Cache 0,5s |
| 🛡️ Betrieb | Backup So 4 Uhr · 35K-Schwelle · Keep-alive 8–22 Uhr |

> [!note] RA
> Eine Pipeline ist erst dann fertig, wenn du aufhören kannst, sie zu beobachten.

---

*Was passiert mit deinen Notizen, wenn du nicht hinsiehst? Schreib mir → raulmina13@gmail.com*
