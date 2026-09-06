---
title: "KG Context — Semantic Context Injection for LLMs"
semantic_class: Concept
tags:
  - knowledge-graph
  - semantic-web
  - llm
  - sparql
  - rag
aliases:
  - KG Context
  - KG Context Graph
  - sparql_bridge
Topics:
  - Knowledge Graphs
  - Semantic Web
  - LLM Context Engineering
publish: true
description: "How the YellowVault AI system injects live knowledge-graph context into LLM prompts — the sparql_bridge, hybrid KG+RAG fusion, and the anti-hallucination disambiguation work."
reading_time: 3
type: tool-guide
lang: en
created: 2026-08-17
---

## What it is

**KG Context** is the mechanism that turns a knowledge graph into *live context* for an LLM. Instead of asking the model to reason from memory, the system queries the graph at prompt time and injects a structured block of real, verifiable facts — tags, backlinks, and neighboring notes — so the model answers from the vault's actual data, not from what it guesses.

It is the bridge between a **static RDF triplestore** (GraphDB) and a **generative model** that has no native access to it.

## The pipeline

| Stage | Tool | What it produces |
|---|---|---|
| Graph build | `parse_vault_to_rdf.py` | RDF triples from every Obsidian note (51,811 triples) |
| Store | GraphDB (RDF triplestore) | SPARQL endpoint + OWL reasoning |
| Query | `sparql_bridge.py` | 3 SPARQL queries → context block |
| Fusion | `hybrid_context.py` | KG + vector RAG merged, 0.5s cache |
| Injection | Prompt Runner | `> [!info]+ KG Context` callout in the prompt |

## The three SPARQL queries

`sparql_bridge --kg-context "NOTE"` runs three queries and merges the results:

| Query | Question it answers |
|---|---|
| **Tags** | What topics does this note carry? |
| **Backlinks** | Which notes link *to* this one? |
| **Neighbors** | Which notes share tags (same-tags)? |

The output is a markdown block with `**Note:**`, `**Tags:**`, and `**Same tags:**` sections — ready to inject into any prompt.

## The anti-hallucination fix (v3)

The original bridge resolved notes **by name only** (`CONTAINS` on the label). With 14 notes named "Untitled", that produced a real failure mode:

| Symptom | Root cause |
|---|---|
| Irrelevant context returned | Name collision across homonyms |
| Mixed-up tags | Tags joined from *all* matching notes |
| Wrong folder | First row's folder used |

**Fix:** a `--folder` flag filters by directory across all four queries. Without it, the bridge now emits a `⚠️ Ambigüedad: N carpetas` warning instead of silently merging. The rule of thumb: *every name query must carry `--folder`.*

## Connection discovery (v3.1)

The bridge used to only *read* existing links. `--suggest-links` makes it *discover* missing ones:

```bash
python sparql_bridge.py --suggest-links "NOTE" --folder "FOLDER" --timeout 60
```

It finds notes that share **≥1 tag** but have **no edge yet** (`FILTER NOT EXISTS`), ranks by shared-tag count, and returns a `> [!tip]+ Suggested links` block ready to inject into `see_also:`. Each run densifies the graph with discovered connections, not just hand-written ones.

## Why it matters

A knowledge graph is only useful if a model can *use* it. KG Context closes that gap: the graph becomes a **grounding layer** that prevents hallucination, because every claim the model makes is backed by a triple that physically exists in the vault.

> [!note] RA
> The graph doesn't invent connections. It only surfaces the ones you already made — and shows you the ones you haven't yet.

---

## Related

- [GraphDB — RDF Triplestore](/Semantic-Web/GraphDB)
- [SPARQL — Query Language](/Semantic-Web/SPARQL)
- [Knowledge Graphs](/Semantic-Web/Knowledge-Graphs)
- [AI Ecosystem — Data Pipeline](/Projekte/AI-Ecosystem-Data-Pipeline)
