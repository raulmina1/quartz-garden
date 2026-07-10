---
tags:
  - semantic-web
  - ontology
  - owl
  - w3c
aliases:
  - Web Ontology Language
  - OWL 2
description: OWL is the W3C ontology language for formal knowledge representation. Learn classes, properties, axioms, reasoning, and how to build ontologies that machines can reason over.
reading_time: "4 min"
lang: en
publish: true
type: concept-guide
date: 2026-07-09
---

# OWL — Web Ontology Language

> **OWL (Web Ontology Language)** is a W3C-standardized ontology language built on top of RDF. It provides rich formal semantics for defining classes, properties, individuals, and logical axioms — enabling automated reasoning, consistency checking, and inference of implicit knowledge.

---

## Key components

| Component | Description | Example |
|---|---|---|
| **Classes** | Sets of individuals sharing characteristics | `Person`, `Organization`, `Software` |
| **Object properties** | Relationships between individuals | `worksFor(Person, Organization)` |
| **Data properties** | Attributes with literal values | `hasAge(Person, integer)` |
| **Individuals** | Concrete instances | `RaulMina: Person` |
| **Restrictions** | Class definitions via property constraints | `hasAge only xsd:integer` |
| **Axioms** | Logical statements about the ontology | `Person ⊑ hasName exactly 1` |
| **Reasoners** | Inference engines (HermiT, Pellet, ELK) | Classify, check consistency, materialize |

---

## Comparison: OWL vs RDFS vs Relational Schema

| Aspect | OWL (Full/DL) | RDFS | Relational Schema |
|---|---|---|---|
| **Expressivity** | High — cardinality, disjointness, equivalence | Low — subclass, subproperty | Medium — FK, NOT NULL |
| **Reasoning** | Automatic classification, consistency | Minimal (subclass propagation) | None built-in |
| **Open World** | Yes — absence ≠ falsehood | Yes | No — closed world |
| **Use case** | Complex domains, AI, biomedical | Simple taxonomies | Transactional data |

---

## How to apply it

1. **Scope** — define the domain and competency questions (e.g., *"Which skills transfer between job titles?"*).
2. **Classes** — model taxonomies with `owl:subClassOf`, use `owl:equivalentClass` for synonyms.
3. **Properties** — define object/data properties with domain, range, and cardinality restrictions.
4. **Axioms** — add `owl:disjointWith`, `owl:hasValue`, or `owl:someValuesFrom` to enforce logic.
5. **Individuals** — populate with concrete data.
6. **Reason** — run a reasoner to infer subsumptions, detect inconsistencies, and materialize new facts.
7. **Publish** — serialize to OWL/XML or Turtle, document with standard annotations.

### Real-world example

Build a job-skill ontology: class `JobTitle` with subclasses `DataArchitect`, `DataEngineer`; property `requiresSkill(Skill)` with cardinality restrictions; reason over it to answer *"Which job titles require both SPARQL and Python?"* using SPARQL + OWL reasoning.

### Turtle serialization example

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix yv: <http://yellowvault.example/ontology/> .

yv:Position rdfs:subClassOf owl:Class .
yv:requiresSkill rdfs:domain yv:Position ;
                  rdfs:range yv:Skill .

yv:SemanticDataArchitect rdfs:subClassOf yv:Position .
yv:SemanticDataArchitect yv:requiresSkill yv:RDF ,
                                           yv:SPARQL ,
                                           yv:OWL .
```

---

## OWL profiles

| Profile | Complexity | Use case |
|---------|-----------|----------|
| **OWL 2 EL** | Low | Biomedical ontologies (large class hierarchies) |
| **OWL 2 QL** | Low | Ontology-based data access, query rewriting |
| **OWL 2 RL** | Medium | Rule-based reasoning, scalable |
| **OWL 2 DL** | High | Maximum expressivity, decidability guaranteed |
| **OWL 2 Full** | Highest | Undecidable but most expressive |

---

## Related

- [RDF — Resource Description Framework](/Semantic-Web/RDF)
- [SPARQL — Query Language for RDF](/Semantic-Web/SPARQL)
- [Knowledge Graphs — Architecture Guide](/Semantic-Web/Knowledge-Graphs)
- [Ontology Engineering — A Practical Guide](/Semantic-Web/Ontology-Engineering)
- [Linked Data Principles](/Semantic-Web/Linked-Data)
