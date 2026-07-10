---
title: "RDF — Resource Description Framework"
tags:
  - semantic-web
  - rdf
  - data-modeling
  - w3c
description: RDF (Resource Description Framework) is the W3C standard for representing web data as triples. Learn how to model, serialize, and query interconnected data.
reading_time: "4 min"
lang: en
publish: true
type: concept-guide
date: 2026-07-09
---

# RDF — Resource Description Framework

> **RDF (Resource Description Framework)** is a W3C standard for representing information about resources on the web. It models data as **triples** — `(subject, predicate, object)` statements — where each element is identified by a URI.

This enables machine-readable, interconnected data across different sources without a fixed schema.

---

## Key components

| Component | Description | Example |
|---|---|---|
| **Subject** | The resource being described | `https://example.org/RaulMina` |
| **Predicate** | The property or relationship | `https://xmlns.com/foaf/0.1/knows` |
| **Object** | The value or target resource | `https://example.org/Berlin` |
| **IRI/URI** | Global identifier for resources | `http://www.w3.org/2001/XMLSchema#string` |
| **Literal** | Concrete values (strings, numbers, dates) | `"Raul"^^xsd:string` |
| **Blank node** | Anonymous resource without explicit IRI | `[] a foaf:Person` |
| **Serialization** | Concrete syntax for writing RDF | Turtle, JSON-LD, RDF/XML, N-Triples |

---

## Comparison: RDF vs Relational Database

| Aspect | Relational Database | RDF |
|---|---|---|
| **Schema** | Fixed, must be defined upfront | Schema-on-read — flexible, extensible |
| **Identity** | Row IDs (surrogate keys) | Global IRIs — linked across datasets |
| **Join** | SQL JOIN on foreign keys | Graph pattern matching via SPARQL |
| **Extensibility** | ALTER TABLE required | Add triples freely, no migration |
| **Interoperability** | Siloed per DB vendor | Standards-based, web-native |

---

## How to apply it

1. **Identify resources** — assign IRIs to real-world entities (people, documents, places).
2. **Model relationships** — define predicates using existing vocabularies (FOAF, Dublin Core, Schema.org) or create custom ones.
3. **Write triples** — serialize in Turtle or JSON-LD format.
4. **Store** — load into an RDF store (Apache Jena, GraphDB, Amazon Neptune).
5. **Query** — use SPARQL to traverse relationships across datasets.
6. **Link** — connect your triples to external datasets (DBpedia, Wikidata) via `owl:sameAs`.

### Real-world example

Convert an Obsidian vault to RDF — each note gets an IRI, each `[[wikilink]]` becomes an RDF triple `NoteA → foaf:topic → NoteB`. Load into GraphDB and query: "Which notes connect through two hops to my job-search notes?" via SPARQL.

### Turtle syntax example

```turtle
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix schema: <http://schema.org/> .

<https://raulmina1.github.io/#me>
  a foaf:Person ;
  foaf:name "Raul Mina" ;
  foaf:knows <https://example.org/berlin> ;
  schema:knowsAbout <https://example.org/knowledge-graphs> .
```

---

## Related

- [Knowledge Graphs — Architecture Guide](/Semantic-Web/Knowledge-Graphs)
- [SPARQL — Query Language for RDF](/Semantic-Web/SPARQL)
- [OWL — Web Ontology Language](/Semantic-Web/OWL)
- [Linked Data Principles](/Semantic-Web/Linked-Data)
- [Semantic Web Standards Overview](/Semantic-Web/Semantic-Web-Standards)
- [Ontology Engineering Guide](/Semantic-Web/Ontology-Engineering)
