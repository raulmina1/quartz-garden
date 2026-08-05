---
title: "Discrete vs Process Manufacturing"
date: 2026-08-05
publish: true
description: "Discrete manufacturing fundamentals — serialized units, BOMs, routing, and work orders vs continuous process manufacturing. How F-35 aerospace parts flow through NAXCON's production line."
tags:
  - discrete-manufacturing
  - manufacturing
  - aerospace
  - production
  - process-engineering
reading_time: "4 min"
type: concept-guide
lang: en
---




## Discrete Manufacturing

### What It Is

**Discrete Manufacturing** is the production of **distinct, countable units** — individual parts or assemblies that can be physically separated, counted, and tracked. Each unit has its own identity (serial number), BOM (Bill of Materials), and production routing. Contrast this with **process manufacturing** (oil refining, chemical blending) where the output is a continuous flow or a batch of inseparable material.

In the F-35 aerospace context at NAXCON GmbH, discrete manufacturing means producing individual components (wing ribs, fuselage brackets, landing gear parts) with strict traceability per serial number, governed by AS9100 aerospace quality standards.

### Key Principles

| Principle | Discrete Manufacturing | Your Experience (Process) |
|-----------|----------------------|---------------------------|
| **Unit identity** | Every part = unique serial number, full genealogy | You tracked batch lots (e.g., a tank of crude), not individual units |
| **Routing** | Part moves through stations (cut → drill → inspect → assemble) | Your process was a continuous flow (well → separator → tank) |
| **BOM (Bill of Materials)** | Recipe for each part: materials, components, sub-assemblies | Your "recipe" was the P&ID (piping & instrumentation, not bill per unit) |
| **Work order** | Specific order for N units of part #XYZ | Your "work order" was a well-testing campaign (volume, not unit count) |
| **Routing flexibility** | Parts can skip stations, take different paths | Process flow is fixed by pipe layout |
| **Inventory** | WIP at each station = parts waiting | WIP in process = fluid in pipes or tanks |

### Comparison: Discrete vs. Process Manufacturing

| Dimension | Discrete Manufacturing (NAXCON) | Your Background (Process) |
|-----------|---------------------------------|---------------------------|
| **Output** | Countable units (pieces, assemblies) | Continuous flow (liters, barrels, kg) |
| **Product ID** | Serial number per unit | Batch/lot number per volume |
| **Flow** | Discontinuous — moves station to station by work order | Continuous — flows through pipes |
| **Bottleneck** | Station with longest cycle time | Pipe diameter, pressure drop, or separator capacity |
| **Quality** | Dimensional check per unit (pass/fail) | Specification per batch (composition, purity) |
| **MES role** | Track each unit's location & status | Monitor flow rate, temp, pressure |
| **Changeover** | Tooling change per part type (minutes/hours) | Changeover = cleaning between campaigns (hours/days) |
| **Traceability** | Serial # → each operation timestamped | Batch # → temperature & pressure profile |

### How to Apply It (Step-by-Step)

**Step 1 — Recognize you already have transferable experience**
From your cover letter: each pressure vessel, heat exchanger, and flare system you designed **carried its own BOM, routing, and fabrication QC protocol** — this IS discrete manufacturing logic applied to equipment design, just not on the production floor.

**Step 2 — Adapt your mental model**
When you hear "work order for 50 bracket assemblies":
- Think: like designing 50 identical pressure vessels, each with its own serial number
- The QC protocol (material cert → weld inspection → hydrotest) is the same pattern as inspection at each station

**Step 3 — Learn the key differences**
- **Cycle time:** instead of "how fast does the fluid flow?" → "how long from start to finish per unit?"
- **WIP:** instead of "volume in the pipe" → "how many units are waiting at each station?"
- **Changeover:** a new F-35 variant = new tooling, new routing, new program → plan ahead

**Real-world example (F-35 wing rib production at NAXCON):**
- **Work order:** 200 wing ribs, type A-12, due 15 Aug
- **Routing:** Saw cut (St.1) → CNC milling (St.2) → Heat treat (St.3) → Dimensional inspection (St.4)
- **Way you think now:** "1 piece enters St.1 every 8 min, 10 pieces per batch, 20 batches total"
- **Challenge at St.2:** 6 min per piece vs. target 5 min → **over-run by 20%**
- **Solution:** Add parallel operation at St.2 (two CNCs running) or adjust cycle time target
- **Your advantage:** You already structured projects with equipment lists, timelines, and QC — same logic, different scale

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Treating the line as continuous flow | Each unit is an individual — track serialized work orders, not volume |
| Ignoring WIP (thinking "it's fine") | WIP between stations = cash tied up = bottleneck indicator |
| Using process-manufacturing vocabulary (flow, rate, throughput) without understanding discrete meaning | Learn the language: cycle time, takt time, changeover, WIP, routing, BOM |
| Not checking work order status per station | In MES, check how many parts are at each station vs. time schedule |
| Underestimating changeover time | A new part type costs setup time — plan changeovers as part of the schedule |


