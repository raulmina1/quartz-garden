---
title: "🔗 Neo4j — Property Graphs vs RDF Stores"
date: 2026-08-09
tags:
  - semantic-web
  - neo4j
  - graph-database
  - cypher
  - knowledge-graphs
description: "Neo4j property graphs vs RDF stores — data models, query languages, and when to choose each. With a real-world example in Cypher."
reading_time: "4 min"
lang: en
publish: true
type: concept-guide
semantic_class: concept-guide
see_also:
  - "[[Semantic Web/Knowledge-Graphs]]"
  - "[[Semantic Web/RDF]]"
  - "[[Semantic Web/GraphDB]]"
  - "[[Semantic Web/SPARQL]]"
---

# 🔗 Neo4j — Property Graphs vs RDF Stores

> Neo4j is the leading property graph database. It stores data as nodes, relationships, and properties — with **relationships as first-class citizens**. Queries use **Cypher**, a declarative graph query language designed for intuitive pattern matching.

---

## Key Components

| Component | Description |
|---|---|
| **Node** | Entity with zero or more labels (`:Person`, `:Job`) |
| **Relationship** | Directed, typed edge between nodes (`[:WORKS_AT]`) |
| **Property** | Key-value on nodes and relationships |
| **Label** | Tag for grouping/classifying nodes |
| **Cypher** | Declarative graph query language |
| **APOC** | Standard library of procedures and functions |
| **Indexes** | B-tree or full-text for fast lookups |
| **Bolt protocol** | Binary, efficient client-server communication |

---

## Property Graph vs RDF — The Comparison

| Aspect | Neo4j (Property Graph) | RDF Store (GraphDB) |
|---|---|---|
| **Data model** | Nodes + labeled relationships | Triples (subject–predicate–object) |
| **Query language** | Cypher | SPARQL |
| **Reasoning** | Application-level | Built-in OWL reasoner |
| **Schema** | Optional (can enforce via constraints) | Ontology-based (RDFS/OWL) |
| **Graph types** | Labeled Property Graph (LPG) | RDF (semantic) |
| **Best for** | Application graphs, recommendations, routing | Knowledge graphs, data integration, inference |

The core difference: an RDF store treats data as **statements about the world** that can be reasoned over (inference, consistency checking), while a property graph treats data as **connected application entities** that are fast to traverse.

---

## How to Apply It

1. **Install** — Neo4j Desktop, or via Docker: `docker run -p 7474:7474 -p 7687:7687 neo4j`
2. **Model** — identify node labels, relationship types, and properties
3. **Create constraints** — uniqueness on key properties (`CREATE CONSTRAINT FOR (p:Person) REQUIRE p.email IS UNIQUE`)
4. **Load data** — `LOAD CSV` or `apoc.load.json` for bulk import
5. **Query** — `MATCH (p:Person)-[:WORKS_AT]->(c:Company) RETURN p, c`
6. **Index** — create indexes on frequently filtered properties

---

## Real-World Example

Model a professional network:

```
(:Person {name:'Ana'})-[:WORKS_AT]->(:Company {name:'SAP'})
(:Person)-[:HAS_SKILL]->(:Skill {name:'Python'})
```

Query: *find connections who work at companies hiring data architects*

```cypher
MATCH (p:Person)-[:WORKS_AT]->(c:Company)<-[:HIRES_FOR]-(:Job {title:'Data Architect'})
RETURN p, c
```

This pattern-based thinking is the bridge between application graphs (Neo4j) and semantic knowledge graphs (RDF) — the two worlds every graph practitioner should understand. For the RDF side, see the [Knowledge Graphs guide](/Semantic-Web/Knowledge-Graphs) and [RDF](/Semantic-Web/RDF).

---

> [!note] RA
> Neo4j asks "who is connected to whom?" RDF asks "what can we infer?" — learn both questions, and you can answer any graph problem.
