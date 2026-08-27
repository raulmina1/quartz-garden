---
title: "Ein Blick ins Innere: mein KI-Ökosystem auf einer Seite"
tags:
  - ai
  - ecosystem
  - architecture
  - ra-blog
description: "Sechs Schichten, 16 Knoten, kein toter Raum: was wirklich in meinem KI-Ökosystem steckt — von der Quelle bis zum Betrieb, mit echten Zahlen."
reading_time: "4 min"
type: showcase
lang: de
publish: true
created: 2026-08-14
status: published
---

# Ein Blick ins Innere: mein KI-Ökosystem auf einer Seite

> Ein KI-Ökosystem — eine Seite, sechs Schichten, null toter Raum.

So sieht mein System von innen aus — in einem einzigen Diagramm, 16 Knoten, alles lokal, kein SaaS:

<iframe src="/static/mental-maps/ecosystem-one-pager.html" style="width:100%;height:720px;border:1px solid #3a3a3a;border-radius:8px;background:#000" title="AI-Ökosystem One-Pager"></iframe>

## Die sechs Schichten

### 📁 Quelle — 4.063 Notizen

Alles beginnt im Obsidian-Vault. Jede Notiz mit `run_prompt: true` aktiviert die Pipeline — bewacht von einem **dualen Watchdog** (1s-Polling, gemeinsames Registry, 104+ Runs).

### ⚙️ Automatisierung — alle 30 Minuten

Der Orchestrator `vault_structure_sync.py` läuft im 30-Minuten-Takt:

| Schritt | Skript | Kennzahl |
|---------|--------|----------|
| NER | `ner_extract.py` | 6.210 Mentions · 74 Entitäten |
| Anreicherung | `frontmatter_enricher.py` | Tags · created · aliases |
| Parse | `parse_vault_to_rdf.py` | inkrementell · 5 Uhr Voll-Build |
| Embeddings | `vault_rag.py` | e5-small |

### 🗄️ Zwei Gehirne

| Gehirn | Was es speichert | Stand |
|--------|------------------|-------|
| 🕸️ **GraphDB** | Struktur (Triples) | 51.811 Triples · 4.063 Notizen · 226K 2-Hop |
| 🧠 **ChromaDB** | Bedeutung (Chunks) | 14.180 Chunks · 5.810 Dateien |

### 🔌 Zugriff — drei Abfrage-Pfade

`sparql_bridge` (KG-Kontext), `hybrid_context` (KG + RAG fusioniert), `qa_kg` (natürliche Sprache → SPARQL) — alle speisen **Prompt Runner v3.17**.

### 👁️ Visualisierung & Monitoring

WebVOWL (Ontologie-Browser), Grafana (5 SPARQL-Panels), RA Log Viewer (30s Refresh).

### 🛡️ Betrieb

Backup sonntags 4 Uhr, Health-Check mit 35K-Schwelle, Keep-alive 8–22 Uhr, Auto-Start 30–90s.

> [!note] RA
> Jedes System, das ich gebaut habe, ist ein Spiegel einer Lücke, die ich gefunden habe — nicht in den Tools, sondern darin, wie ich sie benutzt habe.

---

*Wenn ein System so komplex ist, dass es nicht mehr auf eine Seite passt — verstehst du es dann wirklich? Schreib mir → raul.mina1@outlook.com*
