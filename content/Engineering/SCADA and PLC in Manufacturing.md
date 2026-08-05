---
title: "SCADA & PLC in Aerospace Manufacturing"
date: 2026-08-05
publish: true
description: "SCADA and PLC fundamentals for aerospace manufacturing — the automation pyramid, PLC vs SCADA differences, and real-world F-35 work cell applications at NAXCON."
tags:
  - SCADA
  - PLC
  - manufacturing
  - automation
  - aerospace
reading_time: "3 min"
type: concept-guide
lang: en
---




## SCADA & PLC in Aerospace Manufacturing

### What They Are

**PLC** (Programmable Logic Controller) is an industrial computer that controls machines and processes in real time — it reads sensors (temperature, position, pressure) and actuates outputs (motors, valves, solenoids). **SCADA** (Supervisory Control and Data Acquisition) is the system that monitors and controls multiple PLCs from a central computer.

In the NAXCON F-35 context:
- **PLC** controls each work cell (CNC machine, drilling station, robotic arm)
- **SCADA** (or the HMI interface) shows operators what the PLC is doing — speed, cycle count, alarms
- **MES** reads data from PLC via SCADA to track production KPIs

### The Automation Pyramid

```
Level 4 — ERP (Business Planning)
    ↑
Level 3 — MES (Production Management)
    ↑
Level 2 — SCADA / HMI (Supervision)
    ↑
Level 1 — PLC (Control)
    ↑
Level 0 — Sensors & Actuators (Machines)
```

### Key Differences: PLC vs SCADA

| Aspect | PLC | SCADA |
|--------|-----|-------|
| **Function** | Executes control logic (open valve, start motor) | Visualizes, monitors, and logs PLC data |
| **Response time** | Milliseconds (real-time control loop) | Seconds (data refresh cycle) |
| **Input** | Sensors (limit switch, thermocouple, encoder) | PLC registers, tags, alarms |
| **Output** | Actuators (motor start, valve open, alarm light) | Trends, dashboards, reports, alarm logs |
| **User** | Controls engineer, maintenance technician | Operator, process engineer, production manager |
| **Programming** | Ladder logic, Structured Text, Function Block | Tag configuration, HMI screens, historian setup |

### How You Already Know This (Weatherford → NAXCON)

| Your Experience (Weatherford) | Aerospace Equivalent (NAXCON) |
|------------------------------|-------------------------------|
| Red Eye water-cut meter → PLC → SCADA | CNC machine → PLC → MES integration |
| Pressure transmitter calibration | Temperature sensor I/O check |
| SCADA trends (oil/water ratio over shift) | OEE dashboard (cycle time, quality over shift) |
| Alarm management (high pressure, low flow) | Alarm management (tool wear, temperature out of spec) |
| Data historian for reporting | MES data collection for traceability |

### How to Apply It (Step-by-Step)

**Step 1 — Recognize your SCADA experience is directly transferable**
At Weatherford you worked with:
- Sensors (pressure, temperature, flow) → same as aerospace (position, force, torque)
- PLC control logic → same pattern (if sensor > threshold → actuate alarm)
- SCADA visualization → same concept, different HMI software
- Data logging → same requirement for traceability

**Step 2 — Learn the specific PLC platform at NAXCON**
Common in German aerospace manufacturing:
- **[[Siemens S7]] / [[TIA Portal]]** — most common in German industry
- **Rockwell / Allen-Bradley** — US equipment (common with F-35/US supply chain)
- **Beckhoff** — PC-based control for specialized work cells

**Step 3 — Understand the PLC → MES data link**
This is the critical interface for your role:
- PLC counts: parts produced, cycle time per part
- PLC quality: torque values, dimensional measurements, pass/fail signals
- PLC alarms: machine fault codes, maintenance triggers
- MES reads this data to calculate OEE and track production

**Real-world example (CNC drilling cell at NAXCON):**
- **PLC:** Controls spindle speed, feed rate, coolant flow
- **Sensors:** Position encoder (drill depth), torque sensor, temperature
- **SCADA/HMI:** Shows operator: current part N/200, cycle time, alarm status
- **MES integration:** PLC sends → part count ✓, cycle time ✓, reject signal ✓
- **Your role:** If OEE is low on this station → check PLC data via SCADA → identify if the issue is speed (performance), downtime (availability), or rejects (quality)

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Thinking SCADA = MES | SCADA monitors *machine* data; MES manages *production* data — different layers |
| Ignoring the PLC-MES link during commissioning | If PLC data doesn't reach MES correctly, OEE tracking is broken from day 1 |
| Assuming all PLCs speak the same protocol | Siemens, Rockwell, Beckhoff use different protocols — verify MES compatibility |
| Over-relying on SCADA trends without shop-floor validation | A sensor can drift; validate with manual measurement periodically |


