---
semantic_class: Concept
tags:
  - graph-database
  - semantic-web
  - rdf
  - graphdb
aliases:
  - GraphDB
  - Ontotext GraphDB
Topics:
  - Graph Databases
  - Semantic Web
  - RDF Stores
publish: true
description: "GraphDB by Ontotext is a semantic RDF triplestore with SPARQL, OWL reasoning, and enterprise knowledge graph capabilities. Compare it with Neo4j and learn how to apply it."
reading_time: 2
type: tool-guide
lang: en
---

## What it is

**GraphDB** is a semantic graph database (RDF triplestore) by Ontotext. It stores data as RDF triples and supports SPARQL querying with built-in OWL 2 and RDFS reasoning. It is designed for enterprise knowledge graphs, data integration, and linked data applications.

## Key components

| Component | Description |
|---|---|
| **RDF store** | Native storage for subject-predicate-object triples |
| **SPARQL endpoint** | Query interface over HTTP (REST + HTML UI) |
| **Reasoner** | Built-in OWL 2 RL / RDFS rule engine — classifies, infers, validates |
| **Connectors** | Elasticsearch, Kafka, Lucene, Solr for full-text and index sync |
| **Workbench** | Web admin UI for queries, imports, monitoring |
| **Repository types** | In-memory, persistent, and Ontop (virtual RDF over SQL) |
| **SHACL validation** | Validate RDF graphs against shape constraints |

## Comparison

| Aspect | GraphDB | Neo4j |
|---|---|---|
| **Model** | RDF (triples) | Property graph (nodes + edges) |
| **Query** | SPARQL | Cypher |
| **Reasoning** | Built-in OWL 2 + RDFS | Application-level only |
| **Schema** | Ontology (OWL, RDFS) | Optional constraints |
| **Best for** | Data integration, inference, linked data | Application graphs, OLTP |
| **License** | Free (limited) / Enterprise | Community / Enterprise |

## How to apply it

1. **Set up** — download GraphDB Free or run via Docker: `docker run -p 7200:7200 ontotext/graphdb`.
2. **Create repository** — choose persistent or in-memory with ruleset (OWL-Horst, RDFS, custom).
3. **Load ontologies** — import OWL files, RDF data, or connect to external sources.
4. **Query** — use SPARQL via Workbench or API.
5. **Reason** — enable inference to materialize implicit triples.
6. **Connect** — index with Elasticsearch for hybrid graph + full-text search.

**Real-world example:** Load a job-skills ontology (RDF) into GraphDB, enable OWL reasoning, and query: *Which job titles subsume both Python and SPARQL skills?* — the reasoner infers subclass relationships automatically.
