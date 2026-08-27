---
title: "MES — Manufacturing Execution Systems"
date: 2026-08-05
publish: true
description: "Manufacturing Execution Systems (MES) explained — work order management, traceability, OEE data collection, and the MES-to-ERP integration layer."
tags:
  - MES
  - manufacturing
  - OEE
  - industry-4.0
  - aerospace
reading_time: "3 min"
type: concept-guide
lang: en
---




## MES — Manufacturing Execution Systems

### What It Is

**MES** (Manufacturing Execution System) is a digital system that tracks, monitors, and documents the transformation of raw materials into finished goods in real time on the factory floor. It sits **between** the ERP (Enterprise Resource Planning — business/orders level) and the actual production machinery (PLC/SCADA — control level). MES answers the question: *"What is happening on the shop floor right now, and how efficiently is it running?"*

In the context of NAXCON GmbH and F-35 aerospace manufacturing, MES handles component traceability, work order routing, quality checks, and production-status visibility across the Weeze facility.

### Key Components

| Component | Function | NAXCON Relevance |
|-----------|----------|------------------|
| **Work Order Management** | Routes jobs through production steps (BOM → fabrication → inspection → assembly) | F-35 components require strict routing per AS9100 aerospace standards |
| **Data Collection & Acquisition** | Captures real-time data from machines, sensors, operators (cycle times, temperatures, pressures) | Similar to SCADA data acquisition at Weatherford (Red Eye systems) |
| **Quality Management (QMS)** | Tracks inspections, defects, non-conformances per part | Aerospace AS9100 requires lot/batch traceability per serial number |
| **Performance Analysis (OEE)** | Calculates OEE from availability, performance, and quality data | Directly feeds KPI/OEE reporting for process optimization |
| **Traceability & Genealogy** | Records every operation per serial number — full history of each part | F-35 supply chain demands full part genealogy (birth-to-death) |
| **Inventory Tracking** | WIP (Work-in-Progress) visibility at each production stage | Avoids bottlenecks in F-35 component flow |

### Comparison: MES vs. What You Already Know

| Aspect | SCADA (Weatherford) | MES (NAXCON) |
|--------|--------------------|--------------|
| **Scope** | Local — monitors specific equipment/sensors | Plant-wide — coordinates all production steps |
| **Granularity** | Milliseconds (real-time control loop) | Seconds/minutes (production tracking loop) |
| **Data** | Raw values: pressure, temperature, flow | Aggregated: cycle counts, OEE, yield, downtime |
| **Decision support** | Alarms & thresholds | Trends, KPIs, bottlenecks (longer time horizon) |
| **Connection** | Connected to PLCs/sensors directly | Connected to ERP (orders) + SCADA (machine data) |
| **User** | Operator (process stability) | Production manager (efficiency & quality) |

### How to Apply It (Step-by-Step)

**Step 1 — Understand MES data flow into your role**
You won't configure MES directly, but you'll use its outputs. At NAXCON, you'll read MES dashboards for:
- Work order status per station
- OEE trends per shift
- Quality alerts (defects exceeding threshold)

**Step 2 — Map your SCADA experience to MES vocabulary**
At Weatherford you monitored Red Eye water-cut data via SCADA. In MES terms:
- Data collection → you already did this
- Performance tracking → same logic, different time scale ([[OEE]] is the manufacturing KPI)
- Exception handling → alarms you already responded to

**Step 3 — Learn the MES platform at NAXCON**
Ask during onboarding: which MES system? (common: Siemens Opcenter, SAP ME, DELMIA Apriso). Each has similar functions but different UI.

**Step 4 — Use MES data for process optimization**
Your daily work as Junior Process Engineer:
- Pull MES reports → identify bottleneck station
- Analyse OEE → find root cause (low availability? slow cycle time? quality rejects?)
- Propose improvement → adjust process parameters or workflow
- Verify improvement → compare OEE before/after in MES

**Real-world example (F-35 aerospace):**
- **Problem:** OEE at Station 5 (wing rib drilling) is 62% vs. target 85%
- **MES data:** Shows availability loss (30% of shift = machine idle waiting for material)
- **Root cause:** Material from Station 4 arrives late due to suboptimal routing
- **Solution:** Reroute work order trigger in MES so Station 5 starts 10 min earlier
- **Result:** OEE improves to 78%, quality unaffected

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Treating MES = SCADA | Understand MES is a *production management* layer, not a *control* layer |
| Ignoring MES data (sticking to manual logs) | Pull OEE daily — data reveals patterns your eyes miss |
| Assuming MES replaces ERP | MES complements ERP: ERP = what to make; MES = how to make it |
| Over-reliance on MES reports without ground-truth walking | Validate MES data with actual shop floor observation (Gemba walk) |

¿Quieres entender cómo MES transforma la producción? Escríbeme → [raul.mina1@outlook.com](mailto:raul.mina1@outlook.com)


