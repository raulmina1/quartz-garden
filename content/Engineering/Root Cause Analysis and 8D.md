---
title: "Root Cause Analysis & 8D Methodology"
date: 2026-08-05
publish: true
description: "8D problem-solving methodology and Root Cause Analysis tools (5 Whys, Fishbone, FMEA) for aerospace manufacturing — AS9100 non-conformance resolution at NAXCON."
tags:
  - engineering
  - RCA
  - 8D
  - quality
  - problem-solving
  - aerospace
reading_time: "4 min"
type: concept-guide
lang: en
semantic_class: concept-guide
---




## Root Cause Analysis & 8D Methodology

### What It Is

**Root Cause Analysis (RCA)** is a systematic process for identifying the *underlying* cause of a problem — not just the symptoms. **8D** (Eight Disciplines) is the standard problem-solving methodology used in aerospace and automotive manufacturing, required by AS9100.

When a non-conformance occurs at NAXCON (e.g., a batch of F-35 brackets fails dimensional inspection), an 8D report is opened, and the process engineer leads or supports the investigation.

### The 8 Disciplines

| D# | Discipline | What It Involves | Timeframe |
|----|------------|------------------|-----------|
| **D1** | Team Formation | Assemble cross-functional team (quality, production, engineering) | Day 1 |
| **D2** | Problem Description | Define the problem — what, where, when, how big? (5W2H) | Day 1-2 |
| **D3** | Interim Containment | Protect the customer — quarantine suspect parts, sort, re-inspect | Day 1-2 |
| **D4** | Root Cause Analysis | Identify root cause (5 Whys, Fishbone, Fault Tree) | Day 3-7 |
| **D5** | Corrective Action | Choose and implement permanent fix | Day 7-14 |
| **D6** | Verify Effectiveness | Monitor after fix — did OEE/quality improve? | Day 14-30 |
| **D7** | Prevent Recurrence | Update FMEA, work instructions, training | Day 30-45 |
| **D8** | Closure & Recognition | Close the 8D, celebrate team, document lessons learned | Day 45 |

### RCA Tools You Should Know

| Tool | When to Use | How It Works |
|------|-------------|--------------|
| **5 Whys** | Simple problems with clear cause chain | Ask "Why?" 5 times to drill from symptom to root cause |
| **Fishbone / Ishikawa** | Complex problems with multiple possible causes | Organize causes into categories: Man, Machine, Material, Method, Measurement, Environment |
| **Fault Tree Analysis** | Safety-critical failures (aerospace) | Top-down logic: system failure → sub-failures → component failures |
| **FMEA** | Before the problem occurs (preventive) | Failure Modes & Effects Analysis — score severity, occurrence, detection |
| **Pareto Analysis** | Multiple problems — which one to fix first | 80% of effects come from 20% of causes |

### Comparison: RCA in Your Background vs. Aerospace

| Aspect | Oil & Gas (Your Experience) | Aerospace (NAXCON) |
|--------|-----------------------------|--------------------|
| **Problem type** | Process upset, equipment failure, quality deviation | Dimensional non-conformance, material defect, process deviation |
| **Method** | HAZOP, Root Cause Analysis (RCA) | 8D (AS9100 requirement), FMEA, Fault Tree |
| **Documentation** | Incident report, HAZOP action log | Formal 8D report with customer visibility |
| **Customer involvement** | Internal (client may review) | Lockheed Martin QA reviews and approves 8D |
| **Urgency** | Fix process → resume production → formal RCA later | Customer may stop shipments until 8D is accepted |
| **Regulatory** | Internal or client standards | AS9100 + FAA/EASA regulatory oversight |

### How to Apply It (Step-by-Step)

**Step 1 — Recognize you already do RCA**
Every HAZOP you participated in is structured RCA. Every time you investigated why a Red Eye meter drifted, you did root cause analysis. The terminology is the same — only the format changes.

**Step 2 — Learn the 8D template at NAXCON**
During onboarding, ask for a completed 8D example. Notice:
- How detailed is the problem description? (5W2H format)
- What is the containment action? (Inspect WIP? Sort finished goods?)
- How is root cause validated? (Data? Experiment? Simulation?)

**Step 3 — Lead or support 8Ds as Junior Process Engineer**
Your role in an 8D:
- **D2:** Help define the problem (MES data, OEE trends, inspection reports)
- **D4:** Lead the technical RCA for process-related issues (tooling, parameters, method)
- **D5:** Propose corrective actions (adjust process, change tooling, update work instruction)
- **D6:** Verify the fix — pull OEE data before and after

**Real-world example (F-35 bracket hole misalignment):**
- **Problem:** 12% of brackets at Station 4 show hole misalignment >0.1mm
- **D2:** Brackets serial #NAX-2401 to NAX-2480 — hole position deviation in Y-axis
- **D3:** Containment — sort all WIP, re-inspect last 200 parts, notify Lockheed
- **D4 (RCA):** Fishbone analysis → **Root cause:** Drill bushing wear after 1,200 cycles (expected life 5,000)
- **D5:** Change drill bushing earlier (preventive replacement at 800 cycles)
- **D6:** After fix: defect rate drops to 0.3% — verified over 3 weeks
- **D7:** Update PM schedule in CMMS, add bushing wear check to work instruction
- **D8:** Document in 8D report, close out

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Stopping at "operator error" as root cause | Ask 5 Whys: Why did the operator make the error? (training? tooling? fatigue? process design?) |
| Jumping to corrective action before finding root cause | D3 = contain, D4 = analyze, D5 = fix — never skip D4 |
| Writing vague problem descriptions ("quality issue") | Specific: "Hole position Y-axis deviation >0.1mm on bracket A-12, affecting 12% of parts since 15 Jul" |
| Not validating the fix before closing 8D | Run the process for 30 days post-fix — if defect returns, the root cause was wrong |
| Forgetting to update FMEA | Every non-conformance is data for FMEA — update occurrence and detection scores |


