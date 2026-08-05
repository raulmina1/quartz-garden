---
title: "KPI & OEE — Manufacturing Performance Metrics"
date: 2026-08-05
publish: true
description: "Overall Equipment Effectiveness (OEE) and KPIs for discrete manufacturing — Availability × Performance × Quality formula, world-class benchmarks, and OEE-driven process improvement at NAXCON."
tags:
  - OEE
  - KPI
  - manufacturing
  - lean
  - performance
reading_time: "3 min"
type: concept-guide
lang: en
---




## KPI / OEE — Key Performance Indicators & Overall Equipment Effectiveness

### What It Is

**KPI** (Key Performance Indicator) is a measurable value that shows how effectively a process or operation is achieving key business objectives. In manufacturing, KPIs focus on production output, quality, cost, and safety.

**OEE** (Overall Equipment Effectiveness) is the gold-standard KPI in manufacturing — a single percentage that measures how well a production machine or line runs relative to its full potential. It combines three factors: **Availability**, **Performance**, and **Quality**.

**Formula:** `OEE = Availability × Performance × Quality`

At NAXCON GmbH's F-35 manufacturing facility, OEE is tracked per workstation (drilling, assembly, inspection) to identify bottlenecks and drive continuous improvement.

### Key Components

| Component | Formula | What It Measures | Example (F-35 work cell) |
|-----------|---------|-----------------|--------------------------|
| **Availability** | `Run Time / Planned Production Time` | Uptime — is the machine running when scheduled? | Planned 8h shift, 30min breakdown → Availability = 93.75% |
| **Performance** | `(Ideal Cycle Time × Total Parts) / Run Time` | Speed — is it running at the optimal pace? | Ideal 2 min/part, actual 2.5 min → Performance = 80% |
| **Quality** | `Good Parts / Total Parts Produced` | Yield — how many parts pass inspection? | 100 produced, 3 rejected → Quality = 97% |
| **OEE** | A × P × Q | Overall effectiveness | 93.75% × 80% × 97% = **72.75%** |

**World-class OEE:** 85%+ (Availability 90%, Performance 95%, Quality 99.9%)

### Comparison: Process vs. Discrete Manufacturing KPIs

| Aspect | Process KPI (Your Background — Oil & Gas) | Discrete KPI (NAXCON — Aerospace) |
|--------|-------------------------------------------|------------------------------------|
| **Unit** | Flow rate, pressure, purity (continuous) | Parts count, cycle time (per unit) |
| **Availability** | Upstream/downtime of separation train | Machine uptime per work cell |
| **Quality** | Product spec compliance (API gravity, BS&W) | Dimensional tolerance, surface finish, torque specs |
| **Bottleneck** | Throughput constrained by process limits | Bottleneck station in line (drum-buffer-rope) |
| **Data source** | SCADA log per minute/hour | MES per work order / shift |

### How to Apply It (Step-by-Step)

**Step 1 — Accept your current mental model is transferable**
At Weatherford, you monitored:
- KPI: well-testing throughput (barrels/day per mobile lab)
- Quality: BS&W within spec
- Performance: calibration intervals, repeatability

At NAXCON, the KPI structure is identical — only the unit changes (parts/hour instead of bbl/day).

**Step 2 — Learn to read an OEE dashboard**
During onboarding, ask to see the OEE board for your line:
- Which stations are below 85%?
- What's the biggest loss category (availability, performance, or quality)?
- How is the KPI target set (historical baseline, customer requirement)?

**Step 3 — Use OEE decomposition to find root causes**
When a station has low OEE:
1. Look at the three components separately
2. If **Availability** is low → investigate breakdown patterns (PM schedule, operator training, spare parts)
3. If **Performance** is low → check cycle times (tool wear, material variation, process parameters)
4. If **Quality** is low → inspect defect pattern (tooling, material batch, operator technique)

**Real-world example (F-35 production cell):**
- **Observation:** Station 3 (composite layup) OEE = 52%, well below target
- **Decomposition:** Availability 95% ✓, Performance 85% △, Quality **64%** ❌
- **Root cause:** Layup defects (wrinkling, delamination) in 36% of parts
- **Fix:** Adjust vacuum bagging procedure + add operator retraining
- **Result:** Quality climbs to 92%, OEE rises to 74%

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Looking at OEE in isolation | Decompose into A × P × Q — the component tells you *where* to fix |
| Setting OEE target without baseline | Measure current state for 1 month before setting improvement targets |
| Ignoring small stops (under 2 min) | Micro-stops often add 5-10% performance loss — track with MES |
| OEE as a blame tool | OEE is a *process* metric, not a *person* metric; share with operators, not against them |
| Only reporting good numbers | Escalate bad OEE early — the bottleneck is the most important station |


