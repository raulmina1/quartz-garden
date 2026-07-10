---
tags:
  - knowledge-engineering
  - semantic-web
  - ontology
aliases:
  - Ontology Engineering
  - OE
description: Ontology engineering defines methods for building formal, shared conceptualizations. This guide covers methodology, components, practical steps, and a real-world movie ontology example.
reading_time: "5 min"
lang: en
publish: true
type: concept-guide
date: 2026-07-09
---

# Ontology Engineering — A Practical Guide

> **Ontology engineering** (ontology building) is a subfield of knowledge representation concerned with methods for constructing ontologies — formal, explicit specifications of a shared conceptualization of a domain (Gruber 1993, Borst 1997).

An ontology defines: **classes** (concepts), **individuals** (instances), **attributes** (properties), **relations** (connections), and **axioms** (logical constraints).

---

## Key components

| Component | Role | Example |
|---|---|---|
| **Class hierarchy** | Taxonomical structure | `Vehicle` → `Car`, `Truck` |
| **Object properties** | Inter-class relations | `drives(Person, Vehicle)` |
| **Data properties** | Attribute values | `hasSpeed(Car, integer)` |
| **Individuals** | Concrete instances | `myCar: Car` |
| **Axioms** | Logical constraints | `Car ⊑ Vehicle` |

---

## With vs. Without Ontology Engineering

| Criterion | Without OE | With OE |
|---|---|---|
| Data integration | Manual per source | Automated via shared schema |
| Query consistency | Ad-hoc, drift-prone | Formal, verifiable |
| Reasoning | Custom code required | Built-in reasoners (HermiT, Pellet) |
| Reusability | Low — siloed | High — shareable domain ontologies |

---

## How to apply it — 8-step methodology

1. **Scope** — define domain, users, competency questions
2. **Concepts** — identify classes and relationships
3. **Hierarchy** — organize general-to-specific
4. **Properties** — define attributes, domain, range, cardinality
5. **Individuals** — populate with concrete examples
6. **Axioms** — enforce disjointness, equivalence, consistency
7. **Evaluate** — run a reasoner, refine with domain experts
8. **Publish** — serialize to OWL/RDF, link to FOAF, SKOS, Dublin Core

---

## Example: Movie Ontology

Classes: `Movie`, `Actor`, `Director`, `Genre`, `Platform`.

Properties: `actedIn(Actor, Movie)`, `directedBy(Movie, Director)`, `hasGenre(Movie, Genre)`.

Individuals: `TheMatrix: Movie`, `KeanuReeves: Actor`, `SciFi: Genre`.

Axiom: `SciFi ⊑ Genre`.

Query: "Which SciFi movies directed by the Wachowskis are on Netflix?" → SPARQL over the ontology.

### Turtle serialization

```turtle
@prefix movie: <http://example.org/movie-ontology/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

movie:Movie a owl:Class .
movie:Actor a owl:Class .
movie:actedIn a owl:ObjectProperty ;
              rdfs:domain movie:Actor ;
              rdfs:range movie:Movie .
```

---

## Competency questions — the key first step

Competency questions define what your ontology must answer:

1. "Which skills transfer between job titles?"
2. "Which notes reference both SPARQL and RDF?"
3. "What job positions require knowledge graph experience in Berlin?"
4. "Which companies in my vault are in the energy sector?"
5. "What prerequisites does the Data Architect role require?"

If your ontology can't answer your competency questions, it's not complete.

---

## Related

- [OWL — Web Ontology Language](/Semantic-Web/OWL)
- [RDF — Resource Description Framework](/Semantic-Web/RDF)
- [SPARQL — Query Language](/Semantic-Web/SPARQL)
- [Knowledge Graphs — Architecture Guide](/Semantic-Web/Knowledge-Graphs)
- [Semantic Web Standards Overview](/Semantic-Web/Semantic-Web-Standards)
