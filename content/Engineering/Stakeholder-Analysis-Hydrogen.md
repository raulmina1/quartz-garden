---
title: "🤝 Stakeholder Analysis in Hydrogen Projects"
date: 2026-08-07
tags:
  - engineering
  - hydrogen
  - stakeholder-management
  - project-management
  - energy
description: "How stakeholder theory maps Power/Legitimacy/Urgency in hydrogen projects — full analysis of grey, blue, and green hydrogen alternatives in Germany."
reading_time: "5 min"
lang: en
publish: true
type: concept-guide
semantic_class: concept-guide
see_also:
  - "[[Engineering/Hydrogen-Pathways]]"
  - "[[Engineering/SMR]]"
  - "[[Wirtschaft/CO2-Kosten]]"
---

# 🤝 Stakeholder Analysis in Hydrogen Projects

> Hydrogen projects fail on stakeholder alignment more often than on technology. Mapping who holds power, legitimacy, and urgency — and how each alternative pathway shifts those balances — is the difference between a project that gets built and one that dies in permitting.

---

## Why Stakeholder Theory Matters for Energy Projects

Stakeholder theory treats an organization not as a single entity but as a collection of groups, each with different, often narrow interests (Parmar et al., 2010). The goal of project decision-making is to reconcile those interests — to find a cooperation method that lets the collective group move forward, even when the agreement isn't always on equal terms.

For an industrial energy project (a hydrogen plant, a CCS chain, a pipeline), this isn't academic. Every stakeholder group has the power to accelerate, delay, or kill the project:

| Group | What they control |
|---|---|
| Project owners | Final investment approval |
| Investors & lenders | Capital, financing terms, hurdle rates |
| Customers | Revenue, off-take volumes |
| Regulators | Permits, timelines, conditions |
| NGOs & public opinion | Litigation, reputation, political pressure |

---

## The Power–Legitimacy–Urgency Framework

The classic framework (Mitchell et al.) classifies stakeholders along three dimensions:

- **Power** — the ability to influence the project (H/M/L)
- **Legitimacy** — the perceived validity of their claims (H/M/L)
- **Urgency** — the time-sensitivity of their demands (H/M/L)

High-power + high-legitimacy + high-urgency stakeholders are *definitive* — the project must satisfy them or it stops. The interesting work is in the middle: groups with high legitimacy but low power (workforce, NGOs) that can still stall a project through reputation or resistance.

---

## Case Study: German Hydrogen Project Stakeholder Map

The table below maps **13 stakeholder groups** for a hydrogen production project in Germany, evaluated across three alternative pathways:

- **Alt 0 — Grey SMR:** steam methane reforming without carbon capture
- **Alt 1 — Blue Hydrogen:** SMR + CCS
- **Alt 2 — Green Hydrogen:** electrolysis with renewable electricity

| Stakeholder group | Power | Legitimacy | Urgency | Why they matter | Main risks | Alt 0 Grey SMR | Alt 1 Blue H₂ | Alt 2 Green H₂ |
|---|---|---|---|---|---|---|---|---|
| Project owners | H | H | H | Final investment approval | Financing rejection, schedule delays, scope cuts | Lose | Lose | Win |
| Equity investors | H | M | H | Can stop project via capital withdrawal | Financing gap, higher hurdle rate | Win | Lose | Win |
| Debt providers & risk transfer | H | M | H | Dictate financing terms | Refusal, higher WACC, insurance exclusions | Win | Lose | Win |
| Hydrogen customers | H | H | H | Payment / off-take | Revenue risk, price renegotiation, volume | Win | Lose | Win |
| Hydrogen market traders | M | M | M | Shape marketability & premiums | Market access risk, weak premium realization | Win | Lose | Win |
| CO₂ value chain (transport & storage) | H | M | H | Define storage access | No storage access, tariff shock, schedule slips | Lose | Win | Lose |
| Regulation & permitting authorities | H | H | H | Approve timelines | Permitting delays, additional conditions, redesign | Lose | Win | Win |
| NGOs & environmental groups | M | H | H | High legitimacy & urgency | Litigation, injunctions, reputational damage | Lose | Mixed | Win |
| Grid operators & electricity actors | M | H | H | Set cost difference of pathway | Connection delays, curtailment, high power prices | Neutral | Neutral | Mixed |
| EPC contractors & vendors | H | M | L | High influence during delivery | Cost overruns, delays, performance shortfalls | Lose | Win | Win |
| Workforce | M | H | L | Legitimate & operationally critical | Resistance, delays, incidents, productivity loss | Win | Win | Lose |
| Certification bodies | M | H | H | Enable premiums / compliance value | Greenwashing claims, disputes | Lose | Win | Win |
| Media & public opinion | M | M | H | Urgency amplifier | Reputational damage, political pressure | Lose | Win | Win |

---

## Reading the Map: What It Tells Us

**Grey SMR wins with the market, loses with everyone else.**
Equity investors, debt providers, customers, and traders all prefer grey hydrogen because it's cheapest — €1.5–2.5/kg with no capture penalty. But it loses with the CO₂ value chain (no CCS means no storage contracts), regulators, NGOs, and certification bodies. In a country with carbon pricing and climate law, that's a structural mismatch: the people who finance the project love it, the people who permit it don't.

**Blue hydrogen splits the room — and that's the point.**
The CO₂ value chain, regulators, EPC contractors, certification bodies, and media all favor blue over grey. Investors and traders prefer it over green because the economics are more mature (€2–3/kg vs €3–7/kg for green). The losers are the hydrogen customers and traders who face the carbon cost pass-through. Blue hydrogen's fate depends on one infrastructure question: **is there CO₂ transport and storage access?** Without it, the pathway collapses regardless of policy support.

**Green hydrogen is the only pathway with no definitive losers.**
Every high-legitimacy group (owners, investors, customers, regulators, NGOs, certification bodies) is either neutral or wins. The main risk is economic: grid operators get "mixed" because curtailment risk and high power prices can erode the business case, and the workforce loses because electrolysis is less labor-intensive than reforming plants.

---

## The Practical Takeaway

For any hydrogen project, the stakeholder map tells you where to spend your alignment effort:

1. **Definitive stakeholders (H/H/H):** owners, customers, regulators — must be actively managed from day one
2. **Dormant power (H power, L urgency):** EPC contractors — engage early in delivery planning, not at contract signature
3. **High legitimacy, low power:** workforce and NGOs — don't ignore; a permitting challenge or labor dispute can kill a project that "had all the right approvals"

The alternative that maximizes the *set* of satisfied stakeholders — not the one that maximizes return on paper — is usually the one that gets built.

---

## Related

- [[Engineering/Hydrogen-Pathways|🧪 Hydrogen Production Pathways]]
- [[Engineering/SMR|🏭 Steam Methane Reforming (SMR)]]
- [[Wirtschaft/CO2-Kosten|🌍 CO₂ Costs and Their Impact on German Electricity Prices]]

---

*Which stakeholder do you think kills more hydrogen projects — investors or NGOs? In my experience, the answer is usually the one you least expected.*

> [!note] RA
> Built from my MSc research on hydrogen project viability in Germany — stakeholder mapping was the part that changed how I look at every project since.
