---
title: "Ein KI-System, das sich selbst überwacht"
tags:
  - ai
  - ecosystem
  - automation
  - ra-blog
description: "Mein komplettes KI-Ökosystem auf einer Seite: 4.063 Notizen, dualer Watchdog, zwei Gehirne (GraphDB + ChromaDB), alles lokal — ein System, das sich selbst überwacht."
reading_time: "4 min"
type: showcase
lang: de
publish: true
created: 2026-08-14
status: published
---

# Ein KI-System, das sich selbst überwacht

> Ich habe kein Produktivitätssystem gekauft — ich habe mir eines gebaut, das sich selbst überwacht.

Mein Obsidian-Vault ist in den letzten Monaten zu einem vollständigen KI-Ökosystem gewachsen: **130+ Komponenten, 12 autonome Agenten, 44 Prompts, 5 Hooks** — alles lokal, 24/7, ohne SaaS-Lock-in.

Der One-Pager dahinter ist brutal in seiner Einfachheit: **4.063 Notizen → dualer Watchdog + Orchestrator alle 30 Minuten → zwei parallele Gehirne → Agenten → zurück zu den Notizen.**

## Das komplette Diagramm

<iframe src="/static/mental-maps/ecosystem-one-pager.html" style="width:100%;height:720px;border:1px solid #3a3a3a;border-radius:8px;background:#000" title="AI-Ökosystem One-Pager"></iframe>

## Zwei Gehirne, ein System

| Gehirn | Speichert | Stand |
|--------|-----------|-------|
| 🕸️ **GraphDB** | Struktur — wer mit wem verbunden ist | 51.811 Triples |
| 🧠 **ChromaDB** | Bedeutung — was ähnlich zu was ist | 14.180 Chunks |

Alle 30 Minuten organisiert sich der Vault neu: Tags, Links, Entitäten (6.210 Mentions erkannt), Knowledge-Graph-Sync, semantischer Index. Kein manueller Aufwand.

## Das System heilt sich selbst

Wenn ein Watcher stirbt, repariert sich das System selbst — ich schaue nicht mehr zu. **Es überwacht sich selbst.**

## Zahlen hinter dem One-Pager

| Ebene | Komponenten | Live-Kennzahlen |
|-------|-------------|-----------------|
| 📁 Quelle | Obsidian-Vault, `run_prompt: true` | 4.063 Notizen |
| ⚙️ Automatisierung | `vault_structure_sync.py` alle 30 Min., NER, RDF-Parse, Embeddings | 6.210 Mentions · 74 Entitäten |
| 🗄️ Zwei Gehirne | GraphDB (Triples) + ChromaDB (Chunks) | 51.811 Triples · 14.180 Chunks · 5.810 Dateien |
| 🔌 Zugriff | `sparql_bridge`, `hybrid_context`, `qa_kg` | Prompt Runner v3.17 |
| 👁️ Visualisierung & Monitoring | WebVOWL · Grafana · RA Log Viewer | 5 SPARQL-Panels · 30s Refresh |
| 🛡️ Betrieb | Backup · Health · Keep-alive · Auto-Start | Backup So 4 Uhr · 35K-Schwelle |

> [!note] RA
> Jedes System, das ich gebaut habe, ist ein Spiegel einer Lücke, die ich gefunden habe — nicht in den Tools, sondern darin, wie ich sie benutzt habe.

---

*Was würde dein eigenes System aussehen, wenn du aufhören würdest, Tools zu kaufen? Schreib mir → raul.mina1@outlook.com*
