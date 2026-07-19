---
title: "Linked Data Principles"
tags:
  - linked-data
  - semantic-web
  - rdf
  - open-data
description: "Linked data principles for publishing structured data so it can be interlinked and queried. Learn the 4 rules, 5-star deployment, and how to connect to the global graph."
reading_time: "4 min"
lang: en
publish: true
type: concept-guide
date: 2026-07-09
---

# Linked Data Principles

> **Linked data** is a set of principles for publishing structured data on the web so it can be interlinked and queried across sources. Coined by Tim Berners-Lee, the four rules are: (1) use URIs as names for things, (2) use HTTP URIs for lookup, (3) provide useful information via standard formats (RDF, SPARQL), (4) include links to other URIs for discovery.

---

## Key components

| Component | Description |
|---|---|
| **HTTP URIs** | Globally unique, dereferenceable identifiers |
| **RDF** | Standard data model for statements |
| **Content negotiation** | Serve HTML for humans, RDF for machines from the same URI |
| **SPARQL** | Query across linked datasets |
| **VoID** | Vocabulary of Interlinked Datasets — metadata about datasets |
| **LOD cloud** | The global graph of linked open datasets (DBpedia, Wikidata, GeoNames) |
| **5-star deployment** | 1★ (open license) → 5★ (linked RDF) |

---

## Comparison: Traditional API vs Linked Data

| Aspect | Traditional API | Linked Data |
|---|---|---|
| **Data model** | JSON, XML — fixed per API | RDF — uniform across all sources |
| **Discovery** | API documentation, Swagger | Follow-your-nose — follow URIs |
| **Integration** | Custom clients per API | Generic SPARQL or graph traversal |
| **Granularity** | Endpoints return fixed objects | Dereference any URI, get triples |
| **Interlinking** | Not inherent | Built-in via owl:sameAs, rdfs:seeAlso |

---

## How to apply it

1. **Assign URIs** — each entity (person, job, skill) gets a stable HTTP URI.
2. **Decide vocabularies** — reuse FOAF, Schema.org, or Dublin Core; extend with custom terms.
3. **Publish RDF** — serve Turtle or JSON-LD via content negotiation.
4. **Link outward** — connect entities to DBpedia, Wikidata, or industry vocabularies via `owl:sameAs`.
5. **Expose SPARQL** — provide a public endpoint for cross-dataset queries.

### Real-world example

Publish your job-search data as linked data — each company gets a URI linked to Wikidata, each skill linked to DBpedia.

A query across datasets:

```sparql
SELECT ?job ?skill WHERE {
  ?job :requiresSkill ?skill .
  ?skill owl:sameAs <http://dbpedia.org/resource/Python_(programming_language)> .
}
```

---

## The 5-star deployment scheme

| ★ | Requirement | Example |
|---|---|---|
| ★ | Data available on the web (any format) | PDF spreadsheet |
| ★★ | Machine-readable structured data | Excel file |
| ★★★ | Non-proprietary format | CSV |
| ★★★★ | W3C standard (RDF) to identify things | RDF/Turtle |
| ★★★★★ | Link your data to others' data | Linked RDF to DBpedia |

---

## Why linked data matters

- **Serendipitous discovery**: Follow URIs to find related data you didn't know existed
- **Decentralized**: No single point of control — anyone can publish and link
- **Cross-domain queries**: One SPARQL query can span scientific, geographic, and corporate data
- **Future-proof**: W3C standards ensure decades of compatibility

---

## Related

- [RDF — Resource Description Framework](/Semantic-Web/RDF)
- [SPARQL — Query Language for RDF](/Semantic-Web/SPARQL)
- [OWL — Web Ontology Language](/Semantic-Web/OWL)
- [Knowledge Graphs — Architecture Guide](/Semantic-Web/Knowledge-Graphs)
- [Semantic Web Standards Overview](/Semantic-Web/Semantic-Web-Standards)
- [Ontology Engineering Guide](/Semantic-Web/Ontology-Engineering)

---
*Linked data is the bridge between isolated datasets and a global graph. See how everything connects in the Semantic Web Standards overview.*
