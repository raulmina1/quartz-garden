---
title: "⚙️ Gas Retention Calculator — A Python Tool for Separator Design"
date: 2026-08-09
tags:
  - engineering
  - python
  - well-testing
  - process-engineering
  - showcase
description: "A Python calculator for horizontal three-phase separator design — gas critical velocity (Souders-Brown), Stokes liquid–liquid separation, and retention times. Built for well-testing service."
reading_time: "5 min"
lang: en
publish: true
type: showcase
---

# ⚙️ Gas Retention Calculator — A Python Tool for Separator Design

> Every separator design question comes down to three numbers: **how fast can gas flow without re-entraining liquid, how long do the liquid phases need to separate, and does the vessel actually deliver that retention time?** This calculator answers all three in one script.

---

## The Problem

In well-testing and oilfield services, horizontal three-phase separators (LLV type) must be checked against process conditions before every job. The engineering hand-calculations — critical gas velocity, liquid–liquid settling, retention times — are repetitive, error-prone, and take hours when done by hand per equipment serial number.

The tool I built automates the full check from a single set of inputs.

---

## What It Calculates

| Output | Method | Why it matters |
|---|---|---|
| **Gas critical velocity** | Souders–Brown (`K` factor) | Prevents liquid re-entrainment in the gas outlet |
| **Liquid–liquid settling** | Stokes' law (with Ks coefficient by SG) | Ensures oil/water separation within the vessel |
| **Gas mixture properties** | Kay's rule — MW, pseudocritical T/P, Z | Real-gas density from field chromatography |
| **Retention times** | Vessel geometry + level control heights | Validates HH/LL/N levels against minimum requirements |
| **Nozzle & demister checks** | API 12J ρV² limit, demister sizing | Verifies the datasheet internals |

---

## Design Decisions Worth Stealing

### 1. Data-driven gas composition
Instead of hard-coding a single gas density, the script takes a **full chromatographic composition** (N₂, CO₂, C1–C6+) and computes MW, pseudocritical properties, and Z with Kay's rule. Change the composition, and every downstream number updates.

### 2. Geometry from the datasheet
Vessel diameter, seam-to-seam length, weir height fraction, and **incremental level-control heights** (LLLL → HH) come straight from the equipment datasheet — so the retention-time check reflects the *actual* vessel, not an idealized one.

### 3. API 12J limits built in
The gas outlet check compares ρV² against the API 12J limit (1,500 lb/(ft·s²) with a deflector plate) — the standard that field separators are actually designed to.

---

## The Output

The script prints a structured report:

```
SEPARADOR TRIFÁSICO HORIZONTAL (LLV)
  Cálculo de Velocidad Crítica del Gas y Tiempo de Retención

PROPIEDADES CALCULADAS
  MW mezcla gaseosa          = 19.86 lb/lbmol
  ...
```

Every section is labeled, every intermediate value shown — so a process engineer can trace the numbers back to the datasheet in minutes.

---

## Why This Matters Beyond the Field

This is the pattern behind any useful engineering tool: **take a standard you already trust (Souders–Brown, Stokes, API 12J), encode the datasheet geometry, and make the composition an input.** The same skeleton ports directly to:

- Two-phase vertical separators (different K, different geometry)
- Scrubbers and knockout drums
- Any equipment check that today lives in a spreadsheet

---

> [!note] RA
> A calculator without a buyer is homework. A calculator with a network is a product waiting for a price tag.
