---
title: "FAIR — First Article Inspection (AS9102)"
date: 2026-08-05
publish: true
description: "First Article Inspection (FAIR) per AS9102 — process flow, dimensional reports, material certification, and how FAIR gates serial production in aerospace."
tags:
  - FAIR
  - AS9102
  - quality
  - aerospace
  - manufacturing
reading_time: "3 min"
type: concept-guide
lang: en
---




## FAIR — First Article Inspection

### What It Is

**FAIR** (First Article Inspection) is a formal verification process required by **AS9102** — the aerospace standard for First Article Inspection. It ensures that the *first* production unit of a new part (or after a design change) meets all engineering and quality specifications before serial production begins.

In the F-35 context at NAXCON: every new bracket, rib, or fitting that starts production must pass FAIR before Lockheed Martin or the customer accepts it.

### Key Components of AS9102 FAIR

| Component | What It Verifies | NAXCON Relevance |
|-----------|-----------------|------------------|
| **Part Number & Revision** | Correct drawing revision, material spec, process spec | F-35 parts change revisions with engineering orders |
| **Dimensional Report** | Every critical dimension measured and recorded (± tolerance) | AS9100 requires ±0.05mm on critical features |
| **Material Certification** | Raw material batch, heat treat cert, coating cert | Aerospace material traceability per batch |
| **Process Specification** | All process steps documented per work instruction | Drilling, milling, heat treat parameters |
| **Functional Test** | Assembly fits, moving parts cycle correctly | Bracket-to-bracket fit in wing assembly |
| **Characteristics Classification** | Critical, major, minor characteristics per drawing | Critical = safety of flight → 100% inspection |

### FAIR Process Flow

```
New Part / Change Order
    ↓
FAIR Planning → Identify characteristics, define measurement method
    ↓
Produce First Article (1–5 units, same tooling/procedure as serial)
    ↓
Inspect & Measure → Dimensional, material, functional
    ↓
Complete AS9102 Form (3 parts: Part Number, Material, Process)
    ↓
Customer (Lockheed) Review & Approval
    ↓
✅ FAIR Passed → Serial Production Released
    ↓
❌ Non-Conformance → Root Cause → Corrective Action → Re-inspection
```

### Comparison: What You Know vs. FAIR

| Aspect | Oil & Gas (Your Experience) | Aerospace FAIR (NAXCON) |
|--------|-----------------------------|-------------------------|
| **First unit** | First barrel through new separator = demo/test run | First article = physical part with AS9102 documentation |
| **Specification** | API / ASME design code | AS9102 + customer (Lockheed) drawing |
| **Documentation** | Test report (pressure, temperature, flow) | 3-part form: part, material, process + dimensional report |
| **Approval** | Client engineer signs off | Customer QA + NAXCON QA sign off |
| **Trigger** | New equipment commissioned | New part number, design change, process change, tooling change |
| **Rework** | Adjust process parameters and re-test | Complete new FAIR for the change |

### How to Apply It (Step-by-Step)

**Step 1 — Understand FAIR triggers at NAXCON**
FAIR is required for:
- New part number
- Design change (drawing revision)
- Process change (new tooling, new routing)
- Material change (new alloy, new coating)
- After a production hiatus >2 years

**Step 2 — Learn to read an AS9102 form**
During onboarding, request a completed FAIR package. The form has 3 parts:
- **Part 1:** Part number, revision, drawing number, serial number
- **Part 2:** Material certification, special processes (heat treat, coating)
- **Part 3:** Dimensional report — every characteristic measured

**Step 3 — Participate in FAIR as Junior Process Engineer**
Your role:
- Review work instructions against drawing (are the process steps correct?)
- Witness dimensional inspection of first article
- Verify MES data matches AS9102 documentation
- Log FAIR results in quality system

**Real-world example (F-35 wing rib change):**
- **Change:** Customer updated drilling pattern (3 holes → 5 holes for new bracket)
- **Trigger:** Drawing revision A → B
- **FAIR required:** Yes — design change
- **Your action:** Verify work instruction updated → witness first article production → check 5 holes dimensional report → sign off
- **Result:** FAIR passed → 500 units released to new revision

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Treating FAIR as a paperwork exercise | FAIR is the *last chance* to catch issues before 500 parts are made wrong |
| Rushing FAIR to start serial production | An extra day on FAIR can save weeks of rework |
| Not involving inspection team early | FAIR planning should include metrology (how to measure each feature) |
| Assuming FAIR passes automatically | 30-40% of first articles fail initially — plan for re-inspection |
| FAIR only for new parts | FAIR also required for: tooling transfer, supplier change, process change |

¿Preguntas sobre First Article Inspection o control de calidad? Escríbeme → [raul.mina1@outlook.com](mailto:raul.mina1@outlook.com)


