---
title: "ERP & MES Integration in Manufacturing"
date: 2026-08-05
publish: true
description: "How ERP and MES systems integrate in smart factories — from SAP production orders to real-time shop-floor execution with MES for component manufacturing."
tags:
  - ERP
  - MES
  - manufacturing
  - integration
  - aerospace
reading_time: "3 min"
type: concept-guide
lang: en
---




## ERP / MES Integration

### What It Is

**ERP** (Enterprise Resource Planning) is the business-level system that manages orders, inventory, purchasing, finance, and HR. **MES** (Manufacturing Execution System) manages the actual production on the shop floor. The integration between ERP and MES is what makes a factory "smart" — orders flow from ERP → MES → machines, and production data flows back from machines → MES → ERP.

At NAXCON, the ERP→MES pipeline handles the F-35 production lifecycle:
1. **ERP** receives a sales order from Lockheed Martin for 500 wing ribs
2. **ERP** creates a production order in MES with BOM, routing, due date
3. **MES** tracks each rib through the workstations (cut → drill → inspect)
4. **MES** reports back to ERP: completion status, material consumed, labor hours

### Key Differences

| Aspect | ERP | MES |
|--------|-----|-----|
| **Scope** | Entire company (finance, sales, purchasing, HR, production) | Shop floor only (production execution) |
| **Time horizon** | Weeks/months (planning, ordering) | Minutes/shifts (real-time execution) |
| **Unit of work** | Sales order, purchase order, work order | Work order, operation, serial number |
| **Data granularity** | Aggregated (daily output, monthly cost) | Detailed (cycle time per part, OEE per shift) |
| **User** | Management, planning, purchasing | Production manager, process engineer, operator |
| **Typical systems** | SAP, Microsoft Dynamics, Oracle | Siemens Opcenter, DELMIA Apriso, Rockwell |

### The Integration Pipeline

```
ERP (Business Layer)
    │
    ├─ Sales Order (Lockheed Martin order for 500 ribs)
    ├─ Material Requirements (raw aluminum ordered)
    ├─ Production Order created in MES
    └─ Inventory Updates (material issued to production)
           ↓
MES (Production Layer)
    │
    ├─ Work Order per station (routing)
    ├─ Real-time tracking (which part is at which station)
    ├─ Quality checks (dimensions, torque, surface)
    └─ Performance data (cycle time, OEE)
           ↓
PLC / SCADA (Machine Layer)
    ├─ Machine control (speed, feed rate)
    ├─ Sensor data (temperature, vibration)
    └─ Part identification (barcode scan per operation)
```

### How to Apply It (Step-by-Step)

**Step 1 — Learn the ERP system at NAXCON**
During onboarding, ask:
- Which ERP system? (Common in German aerospace: SAP, proALPHA, Microsoft Dynamics 365)
- How are production orders created? (Manual by planning? Auto from sales order?)
- How does MES report completion to ERP? (Job closing transaction? Barcode scan?)

**Step 2 — Understand the data flow for your role**
As Junior Process Engineer, you'll mainly work in MES, but you need to understand ERP:
- Production order priorities come from ERP (customer due dates)
- Raw material availability is managed by ERP (can't start without material)
- Cost data flows to ERP (labor hours, material consumption from MES)

**Step 3 — Identify integration gaps**
Common issues:
- MES reports part completion but ERP still shows "in production"
- Material issued in MES doesn't match inventory in ERP (scrap not recorded)
- Cycle times in MES differ from planning times in ERP

**Real-world example (F-35 bracket shortage):**
- **Problem:** Station 5 (drilling) is idle — no material
- **MES data:** Shows 50 parts waiting at Station 3 (inspection)
- **ERP data:** Raw aluminum is in inventory (100 sheets available)
- **Root cause:** ERP → MES material transfer hasn't been triggered for the work order
- **Your action:** Escalate to planning — ERP release flag missing for this order
- **Result:** Material released, production resumes in 2 hours

### Common Mistakes vs. Best Practices

| ❌ Mistake | ✅ Best Practice |
|-----------|------------------|
| Thinking ERP and MES are the same system | They serve different purposes and users — understand the boundary |
| Ignoring ERP (focusing only on MES shop floor data) | Production order delays often originate in ERP (material release, planning) |
| Manually fixing MES data without updating ERP | A fix in MES that doesn't sync to ERP creates inventory/reporting discrepancies |
| Expecting real-time data from ERP | ERP is usually batch-updated (hourly/daily); MES is real-time |

¿Te interesa la integración ERP/MES en tu planta? Escríbeme → [raul.mina1@outlook.com](mailto:raul.mina1@outlook.com)


