---
title: "Automation Commissioning in Aerospace"
date: 2026-08-05
publish: true
description: "Step-by-step automation commissioning lifecycle — FAT, SAT, I/O checks, dry/wet runs, PPAP, and Run-at-Rate validation for CNC work cells."
tags:
  - engineering
  - commissioning
  - automation
  - manufacturing
  - aerospace
  - PLC
reading_time: "4 min"
type: concept-guide
lang: en
semantic_class: concept-guide
---




## Automation Commissioning

### What It Is

**Automation Commissioning** is the systematic process of testing, verifying, and bringing an automated system or production line from installation to fully operational status. It ensures that machines, PLCs, sensors, robotics, and MES integration work together correctly before serial production begins.

In the F-35 context at NAXCON GmbH, commissioning means: a new work cell (e.g., a CNC drilling station) arrives, gets installed, connected to the plant network and MES, tested against AS9100 aerospace standards, and handed over to production — all with documented protocols.

### Key Components

| Component | What It Involves | Your Transferable Experience |
|-----------|-----------------|------------------------------|
| **FAT (Factory Acceptance Test)** | Test at the equipment supplier's site before shipment | Like factory hydrotest of a pressure vessel before delivery |
| **SAT (Site Acceptance Test)** | Test at NAXCON after installation, under real conditions | Like commissioning a well-testing Red Eye measurement system on-site |
| **I/O Check** | Verify every sensor/actuator responds correctly | Like checking pressure transmitter calibration at Weatherford |
| **Dry Run** | Run empty cycle without raw material | Like a water test on a separation train before introducing crude |
| **Wet Run** | Run with actual material, first articles | Like first barrel through a newly commissioned separator |
| **PPAP (Production Part Approval Process)** | Customer (Lockheed Martin) approves first article | Like client sign-off on new well-testing protocol |
| **Run at Rate (R@R)** | Run at full production speed for X hours without failure | Like 24h endurance test of a mobile lab at rated capacity |

### Comparison: Commissioning in Your Background vs. Aerospace

| Aspect | Process Commissioning (Your Experience) | Aerospace/Automation Commissioning (NAXCON) |
|--------|----------------------------------------|----------------------------------------------|
| **System** | Separation train, flare system, well test equipment | CNC machine, automated assembly cell, robotic work station |
| **Test medium** | Water → crude → product | Dry run → first article → serial production |
| **Specs** | API, ASME, ASTM | AS9100, customer (Lockheed) specs, FAA/EASA |
| **Documentation** | P&ID redlining, pressure test reports | FAT/SAT protocol, MES integration test, PPAP |
| **Acceptance** | Client engineer signs off (test metrics) | Customer quality engineer + NAXCON QA sign off |
| **Automation level** | Manual operation with SCADA monitoring | PLC/HMI + MES integration + possibly robotics |
| **Ramp-up** | Gradually increase flow/capacity | Ramp up part count per shift while maintaining quality |

### How to Apply It (Step-by-Step)

**Step 1 — Recognize you've already done commissioning**
At Weatherford, you:
1. Installed Red Eye water-cut meters on-site (installation)
2. Connected to SCADA system (integration)
3. Calibrated against reference samples (verification)
4. Compared readings with lab results (validation)
5. Trained operators (handover)

This is the **exact same lifecycle** as commissioning an automated work cell — just different equipment.

**Step 2 — Learn the commissioning vocabulary for NAXCON**
During onboarding, understand:
- Which equipment is being commissioned (new or retrofitted?)
- Who is the supplier (internal NAXCON team or external vendor?)
- What are the acceptance criteria (cycle time, tolerance, OEE contribution?)
- Which quality standard applies (AS9100 Rev D?)

**Step 3 — For automation-commissioning, focus on the PLC-to-MES link**
The critical difference from your past experience:
- Weatherford: SCADA read values and operator acted
- NAXCON: MES reads cycle counts + quality data from PLC automatically
- **Your commission task:** verify that the PLC sends correct data to MES (correct part count, cycle time, alarm codes)

**Real-world example (commissioning a 5-axis CNC drilling cell):**
1. **FAT** (at supplier's facility): Machine drills 10 test coupons within ±0.05mm tolerance → PASS
2. **Installation:** Machine arrives at Weeze, bolted to floor, power + network connected
3. **I/O Check:** All 48 sensors (tool changer, spindle speed, coolant flow, door interlocks) respond correctly on HMI
4. **SAT:** Dry run (no material) — cycle time 14.2 min vs. target 14.0 → close, acceptable
5. **MES Integration:** MES reads part count ✓, cycle time ✓, alarm codes ✓ — data link verified
6. **Wet Run (First Article):** 5 wing ribs produced, all pass dimensional inspection (±0.03mm)
7. **PPAP:** Lockheed Martin QA approves first-article report
8. **R@R:** Run at full speed (50 parts/shift) for 5 consecutive shifts — 0 rejects, OEE 89%
9. **Handover:** SOP written, operators trained, spare parts in stock → **production ready**

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Treating the MES connection as secondary | Commission the data link *as part of* the equipment — without MES, OEE tracking is manual |
| Rushing dry runs to get to serial production | A thorough dry run catches 80% of issues; wet runs are expensive per part |
| Skipping operator training before handover | Train operators *during* commissioning (they spot usability issues engineers miss) |
| Not documenting deviations | Every deviation (tight tolerance, unexpected cycle time) goes into commission report — it's evidence for the customer |
| Assuming FAT = SAT | Site conditions (power stability, temperature, network latency) can differ; SAT is a separate test |

¿Preguntas sobre commissioning o automatización industrial? Escríbeme → [raul.mina1@outlook.com](mailto:raul.mina1@outlook.com)


