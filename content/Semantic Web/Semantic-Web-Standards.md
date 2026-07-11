---
title: "Semantic Web Standards — W3C Stack Overview"
tags:
  - semantic-web
  - w3c
  - standards
  - linked-data
description: The Semantic Web stack is a layered set of W3C standards — from URIs and RDF to OWL and SPARQL. This overview covers each layer and how they work together.
reading_time: "4 min"
lang: en
publish: true
type: concept-guide
date: 2026-07-09
---

# Semantic Web Standards — W3C Stack Overview

> **Semantic web standards** are a set of W3C specifications that enable machine-readable, interlinked data across the web. They form a layered stack — from unique identifiers (IRI) and data formats (RDF) to schema languages (RDFS, OWL) and query (SPARQL) — allowing data from different sources to be combined and reasoned over automatically.

---

## The W3C Semantic Web Stack

```
┌─────────────────────────────────────┐
│          User Interface              │
├─────────────────────────────────────┤
│  ┌───────────────────────────────┐  │
│  │      Trust / Proof            │  │
│  ├───────────────────────────────┤  │
│  │  ┌─────────────────────────┐  │  │
│  │  │   Unifying Logic        │  │  │
│  │  ├─────────────────────────┤  │  │
│  │  │  OWL (Ontology)         │  │  │
│  │  │  RDFS (Schema)          │  │  │
│  │  │  RIF (Rules)            │  │  │
│  │  ├─────────────────────────┤  │  │
│  │  │  SPARQL (Query)         │  │  │
│  │  ├─────────────────────────┤  │  │
│  │  │  RDF (Data Model)       │  │  │
│  │  ├─────────────────────────┤  │  │
│  │  │     XML / Turtle        │  │  │
│  │  ├─────────────────────────┤  │  │
│  │  │     URI / IRI           │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

---

## Key components

| Standard | Purpose | Example |
|---|---|---|
| **IRI / URI** | Globally unique resource identifiers | `http://example.org/people/Raul` |
| **RDF** | Data model — triples (subject-predicate-object) | `<Raul> <knows> <Berlin>` |
| **RDFS** | Lightweight schema — class/subclass, property domain/range | `rdfs:subClassOf`, `rdfs:domain` |
| **OWL** | Expressive ontology language with logic | Cardinality, disjointness, equivalence |
| **SPARQL** | Query language for RDF | `SELECT ?x WHERE {?x :type :DataArchitect}` |
| **SHACL** | Shape constraint language — validation | Validate that a Person `foaf:name` exists |
| **SKOS** | Simple Knowledge Organization System — taxonomies/thesauri | Concept schemes, broader/narrower terms |
| **RIF** | Rule interchange format for custom inference | If-then rules over RDF data |

---

## Comparison

| Aspect | Without Semantic Web | With Semantic Web |
|---|---|---|
| **Identity** | Local keys, collisions across systems | Global IRIs — unique across the web |
| **Schema** | Siloed per system | Shared ontologies, mapping via OWL |
| **Query** | Per-system APIs or SQL | SPARQL federation across endpoints |
| **Reasoning** | Custom code | Built-in OWL/RDFS inference |
| **Discovery** | Documentation, data dictionaries | VoID descriptions, content negotiation |

---

## How to apply it

1. **Identify your IRIs** — each real-world entity gets a stable HTTP IRI.
2. **Model with RDF** — represent data as triples using existing vocabularies (FOAF, Schema.org, Dublin Core).
3. **Layer schema** — use RDFS for taxonomies, OWL for complex constraints.
4. **Validate** — define SHACL shapes and run validation on your data.
5. **Expose** — publish data via a SPARQL endpoint or as Linked Data (content negotiation).
6. **Connect** — use `owl:sameAs` to link your entities to Wikidata, DBpedia, or other LOD sources.

### Real-world example

Publish an Obsidian vault as linked data — assign IRIs to notes, use FOAF for people and Schema.org for documents. Enable a SPARQL endpoint that lets others query "Which notes link to both 'SPARQL' and 'RDF'?".

---

## Related

- [RDF — Resource Description Framework](/Semantic-Web/RDF)
- [SPARQL — Query Language for RDF](/Semantic-Web/SPARQL)
- [OWL — Web Ontology Language](/Semantic-Web/OWL)
- [Knowledge Graphs — Architecture Guide](/Semantic-Web/Knowledge-Graphs)
- [Linked Data Principles](/Semantic-Web/Linked-Data)
- [Ontology Engineering Guide](/Semantic-Web/Ontology-Engineering)

---
*The semantic web stack is deep but coherent. Pick one layer and master it — the rest will connect naturally.*
