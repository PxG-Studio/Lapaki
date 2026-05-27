# Architecture Documentation Overview

> **Purpose:** This directory contains all architectural diagrams and compliance annotations for the Health Data Architecture Framework.  
> **COBIT alignment:** APO03 (Managed Enterprise Architecture), MEA01 (Managed Performance and Conformance Monitoring)

---

## Documents

| File | Diagrams | Type | Description |
|------|----------|------|-------------|
| [`01-swimlanes.md`](./01-swimlanes.md) | 4 | `sequenceDiagram` | Role-based swimlane diagrams for 4 key workflows |
| [`02-flowcharts.md`](./02-flowcharts.md) | 5 | `flowchart TD/LR` | Process flowcharts for pipeline, access control, CDM, de-ID, research |
| [`03-mindmap.md`](./03-mindmap.md) | 1 | `mindmap` | Full framework architecture mindmap (5 branches, 90+ nodes) |
| [`04-mindmap-notes.md`](./04-mindmap-notes.md) | — | Table | Annotated compliance reference: Node × Standard × COBIT × Risk × Evidence |

**Total diagrams: 10 Mermaid diagrams across 4 files**

---

## How to Render Mermaid Diagrams

All diagrams use standard [Mermaid](https://mermaid.js.org) syntax and render natively in:

1. **GitHub.com** — Auto-renders in any `.md` file view ✅
2. **VS Code** — Install the [Mermaid Preview](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) extension
3. **Mermaid Live Editor** — Paste diagram code at [mermaid.live](https://mermaid.live)
4. **Obsidian** — Enable the Mermaid plugin in Community Plugins

---

## Node Color Semantics

The color system is consistent across all diagrams:

| Color | Hex | Phase / Role |
|-------|-----|-------------|
| 🟣 Indigo | `#6366f1` | Operational / Source Systems (Phase 1) |
| 🔵 Sky Blue | `#0ea5e9` | Internal Research Environment (Phase 2) |
| 🟣 Violet | `#8b5cf6` | External Collaborative Research (Phase 3) |
| 🟡 Amber | `#f59e0b` | De-Identified / PHI-Free data |
| 🟢 Teal | `#14b8a6` | Self-Service Analytics |
| 🔴 Red | `#dc2626` | PHI / High-risk identified data |
| 🟢 Green | `#059669` | Approved / compliant outcomes |
| 🟠 Orange | `#d97706` | Decision / assessment points |

---

## HIPAA Phase Mapping

Each diagram maps to a specific HIPAA compliance domain:

| Diagram | HIPAA Domain | Key Safeguard |
|---------|-------------|--------------|
| Swimlane 1 — Ingestion | §164.308(a)(1) Risk Management | Administrative |
| Swimlane 2 — De-ID Workflow | §164.514(b) De-Identification | Privacy Rule |
| Swimlane 3 — External Collab | §164.308(b) BAA + §164.504(e) | Administrative |
| Swimlane 4 — Incident Response | §164.308(a)(6) + §164.400–414 | Breach Notification |
| Flowchart 1 — Full Pipeline | All safeguards | Overview |
| Flowchart 2 — PHI Classification | §164.514(b)/(e) | Privacy Rule |
| Flowchart 3 — Access Control | §164.312(a)(1) | Technical |
| Flowchart 4 — CDM Mapping | §164.312(b) Audit | Technical |
| Flowchart 5 — Research Lifecycle | §164.508 Authorization | Privacy Rule |
| Mindmap | All | Framework overview |

---

## COBIT Governance Cross-Reference

| Pipeline Phase | COBIT Domain | Primary Objectives |
|---------------|-------------|-------------------|
| Source Systems (EHR, Operational DW) | APO, BAI | APO03, APO14, BAI03, BAI06 |
| Internal Research (CDM, De-ID) | APO, DSS | APO11, APO12, APO13, DSS05, DSS06 |
| External Collaboration | EDM, APO | EDM03, EDM05, APO08, APO10 |
| Incident Response | DSS, MEA | DSS02, DSS04, MEA01, MEA03 |
| Audit & Compliance | MEA | MEA01, MEA02, MEA03, MEA04 |

---

## Quick Navigation

- 🏊 [Swimlane Diagrams →](./01-swimlanes.md) — Workflow-level view with role swim lanes
- 🔀 [Flowcharts →](./02-flowcharts.md) — Process-level decision trees and pipeline flows
- 🧠 [Mindmap →](./03-mindmap.md) — Bird's-eye architecture overview
- 📋 [Compliance Notes →](./04-mindmap-notes.md) — Per-node standard citations, COBIT mapping, risk, and audit evidence
