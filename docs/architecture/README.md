# Architecture Documentation Overview

> **Document Purpose:** This guide serves as the master navigation reference for the Lapaki health data pipeline architecture documentation suite. It provides technical orientation for engineers, clinical informaticists, compliance officers, and governance stakeholders who need to understand how the health data pipeline is architecturally structured, how to interpret the diagrams contained in these documents, how the architecture maps to regulatory phases and COBIT governance domains, and how to navigate to the specific technical documentation most relevant to their role.

---

## Table of Contents

- [Overview of Architecture Documentation Files](#overview-of-architecture-documentation-files)
- [How to Read Mermaid Diagrams](#how-to-read-mermaid-diagrams)
- [Color Semantics Reference](#color-semantics-reference)
- [Architecture-to-HIPAA Phase Mapping](#architecture-to-hipaa-phase-mapping)
- [COBIT Domain Governance Cross-Reference](#cobit-domain-governance-cross-reference)
- [Quick Navigation](#quick-navigation)

---

## Overview of Architecture Documentation Files

The Lapaki architecture documentation suite consists of four files, each providing a distinct visual and conceptual perspective on the health data pipeline. Together, they constitute a complete multi-view architectural model conformant with established enterprise architecture documentation practice (TOGAF 10 Architecture Content Framework, ArchiMate 3.2 viewpoint types). Each file is described below with its diagram inventory, intended audience, and primary use case.

---

### File 1: [01-swimlanes.md](./01-swimlanes.md)

**Title:** Health Data Pipeline — End-to-End Swimlane Architecture

**Diagram Count:** 3 Mermaid diagrams

**Diagram Types:**
- Swimlane process flow (Mermaid `flowchart LR` with subgraph swim lanes)
- Data lifecycle swimlane (actor/process decomposition)
- HIPAA safeguard swimlane (administrative/physical/technical lanes)

**Intended Audience:** Data engineers, clinical informaticists, privacy officers, IRB staff, HIPAA auditors

**Primary Use Case:** Understanding the end-to-end flow of clinical data from EHR source systems through staging, CDM transformation, de-identification, quality validation, and researcher delivery — organized by the organizational actor responsible for each process step. The swimlane format is the most accessible architecture view for non-technical governance stakeholders because it explicitly shows who does what at each stage.

**Key Content:**
- EHR-to-CDM data flow with actor assignments (Data Engineering, Clinical Informatics, Privacy, Research, IT Security)
- De-identification decision points with HIPAA citation markers
- PHI boundary visualization (where data transitions from identifiable to de-identified)
- Researcher access provisioning workflow
- Audit trail generation points

**Regulatory Sensitivity:** HIGH — contains detailed PHI flow documentation. Distribute on need-to-know basis.

---

### File 2: [02-flowcharts.md](./02-flowcharts.md)

**Title:** Health Data Pipeline — Detailed Flowcharts

**Diagram Count:** 5 Mermaid diagrams

**Diagram Types:**
- ETL pipeline flowchart (`flowchart TD` — top-down process detail)
- De-identification decision tree (`flowchart TD` — branching logic)
- Access control and provisioning flow (`flowchart LR`)
- Incident response workflow (`flowchart TD`)
- CDM version change management flow (`flowchart LR`)

**Intended Audience:** Data engineers, ETL developers, security architects, compliance officers, incident response team

**Primary Use Case:** Providing detailed, step-by-step process documentation for the key operational workflows in the health data pipeline. These flowcharts are the primary reference for data engineers implementing ETL logic, security staff executing incident response, and compliance officers documenting process controls for audit. Each flowchart includes decision nodes, error handling paths, and the regulatory control check points that must be satisfied before process advancement.

**Key Content:**
- Complete ETL pipeline with gate controls (record count reconciliation, referential integrity, DQD thresholds)
- De-identification method selection decision tree (Safe Harbor vs. Expert Determination)
- RBAC access provisioning with IRB verification steps
- HIPAA breach risk assessment decision tree (four-factor test)
- CDM change management flow (CAB approval, staging validation, rollback trigger)

**Regulatory Sensitivity:** HIGH — contains system-level process documentation. Suitable for internal distribution.

---

### File 3: [03-mindmap.md](./03-mindmap.md)

**Title:** Health Data Pipeline — Knowledge Architecture Mind Map

**Diagram Count:** 2 Mermaid diagrams

**Diagram Types:**
- Conceptual mind map (`mindmap`) — CDM data domains and relationships
- Governance knowledge map (`mindmap`) — governance structure and accountability

**Intended Audience:** New team members, researchers, clinical department leadership, executive stakeholders seeking conceptual orientation

**Primary Use Case:** Providing a high-level conceptual map of the health data pipeline's knowledge architecture — what data is collected, how it is organized, how governance is structured, and how the pipeline's components relate to each other. Mind maps are the most effective entry point for stakeholders who are new to the CDM environment or who need a conceptual overview before engaging with the more detailed architectural views.

**Key Content:**
- OMOP CDM domain taxonomy (Clinical Events, Health System, Standardized Vocabularies, Health Economics)
- CDM vocabulary hierarchy (SNOMED CT, LOINC, RxNorm, ICD-10, CPT-4)
- Governance structure mind map (DGC, Privacy Officer, CISO, IRB Liaison, Data Stewards)
- Regulatory compliance knowledge map (HIPAA, Common Rule, NIH DMSP, State Law)
- Research use case taxonomy (cohort studies, case-control, RWE, federated analysis)

**Regulatory Sensitivity:** LOW — conceptual, no PHI or system-specific details.

---

### File 4: [04-mindmap-notes.md](./04-mindmap-notes.md)

**Title:** Architecture Decision Records and Technical Notes

**Diagram Count:** 1 Mermaid diagram (Architecture Decision sequence diagram)

**Diagram Types:**
- Architecture Decision Record (ADR) reference diagram (`sequenceDiagram`)
- Annotated architecture notes (extended prose with embedded code blocks)

**Intended Audience:** Data architects, senior data engineers, technology leadership, external assessors

**Primary Use Case:** Documenting the rationale behind key architectural decisions in the health data pipeline. Architecture Decision Records (ADRs) provide the institutional memory of *why* the architecture is designed the way it is — which CDM standard was selected and why, which cloud platform was chosen and why HIPAA BAA considerations factored into that choice, which de-identification method was selected and the expert rationale, and which FHIR profile was implemented. This documentation is particularly valuable for audit defense (demonstrating that architectural choices were deliberate and risk-informed), onboarding new architects, and evaluating future architectural changes.

**Key Content:**
- ADR-001: Selection of OMOP CDW as primary CDM standard (rationale, alternatives considered, OHDSI network alignment)
- ADR-002: Cloud hosting provider selection with HIPAA BAA compliance rationale
- ADR-003: De-identification method selection (Safe Harbor vs. Expert Determination)
- ADR-004: FHIR R4 + US Core IG as the API standard
- ADR-005: Federated query architecture decision (local CDM + distributed network participation)
- Technical implementation notes for CDM ETL, FHIR server, and security configuration

**Regulatory Sensitivity:** MEDIUM — contains architectural rationale but no PHI. Contains system configuration details that should be protected from public disclosure.

---

## How to Read Mermaid Diagrams

Mermaid is an open-source, text-based diagramming language that renders diagrams natively in many modern documentation platforms. All diagrams in this architecture suite are written in Mermaid syntax. No specialized drawing tools are required.

### Rendering Environments

| Environment | Rendering Method | Notes |
|---|---|---|
| **GitHub.com** | Native (automatic) | All `.md` files with Mermaid code blocks render automatically in the GitHub web interface. No configuration required. |
| **VS Code** | Mermaid Preview extension | Install "Mermaid Preview" (bierner.mermaid-markdown-syntax-highlighting) or "Markdown Preview Mermaid Support" (Matt Bierner). Use `Ctrl+Shift+V` (Cmd+Shift+V on Mac) to open preview. |
| **Mermaid Live Editor** | Browser-based (no install) | Navigate to [https://mermaid.live](https://mermaid.live). Paste the Mermaid code block content (without the triple backtick fences) into the editor. Diagrams render in real time. Supports PNG and SVG export. |
| **Obsidian** | Native with "Mermaid" core plugin | Enable the Mermaid plugin in Obsidian settings. All Mermaid code blocks render in Reading View. |
| **Confluence** | Mermaid macro (plugin required) | Install the "Mermaid Diagrams for Confluence" marketplace app. Use the Mermaid macro to embed diagram code. |
| **Notion** | Code block (manual) | Mermaid does not render natively in Notion. Use the Mermaid Live Editor to export PNG/SVG and embed as images. |
| **GitLab** | Native (automatic) | GitLab renders Mermaid in all wiki pages and README files natively. |

### Diagram Type Reference

| Mermaid Directive | Diagram Type | Used For |
|---|---|---|
| `flowchart TD` | Top-down flowchart | Process flows, decision trees, pipeline stages |
| `flowchart LR` | Left-to-right flowchart | System architecture views, data flows, service interactions |
| `flowchart TD` with `subgraph` | Swimlane flowchart | Actor-based process views, HIPAA safeguard categorization |
| `mindmap` | Mind map | Conceptual knowledge maps, domain taxonomy |
| `sequenceDiagram` | Sequence diagram | Protocol interactions, API call sequences, decision processes |
| `gantt` | Gantt chart | Project timelines, compliance calendar visualization |
| `erDiagram` | Entity-relationship diagram | CDM data model, database schema documentation |

### Reading Conventions

- **Arrows** (`-->`, `---`, `==>`) indicate data flow, process transitions, or relationships. Arrow direction indicates flow direction.
- **Diamond nodes** (`{Decision?}`) indicate decision points where the process branches based on a condition.
- **Subgraph blocks** (`subgraph Name`) group related nodes into a labeled container — used to represent organizational layers (swimlanes), system tiers, or thematic groupings.
- **Node shapes**: `[Rectangular]` = process or system; `(Rounded)` = start/end; `{Diamond}` = decision; `[(Database)]` = data store; `((Circle))` = connector or event.
- **Colors**: See the Color Semantics Reference section below.

---

## Color Semantics Reference

The following color conventions are used consistently across all architecture diagrams in this suite. Colors are applied using Mermaid `style` declarations or `classDef`/`class` assignments.

| Color | Hex | Semantic Meaning | Applied To |
|---|---|---|---|
| 🔴 Red / Crimson | `#C0392B` | PHI-bearing, highest sensitivity | Nodes/systems containing identifiable PHI; PHI breach risk paths |
| 🟠 Orange | `#E67E22` | Limited Dataset or partially de-identified | Nodes/data containing HIPAA Limited Dataset (dates, geographic data retained) |
| 🟡 Yellow / Amber | `#F39C12` | Research-accessible, de-identified | CDM data released for research access post de-identification |
| 🟢 Green | `#27AE60` | Fully de-identified / public | Data meeting HIPAA Safe Harbor or Expert Determination standards |
| 🔵 Blue / Steel | `#2980B9` | Governance / administrative | Governance processes, policy controls, administrative safeguards |
| 🟣 Purple / Violet | `#8E44AD` | Security controls / technical safeguards | Security systems (SIEM, MFA, encryption, DLP, access control) |
| ⚫ Dark Gray | `#2C3E50` | External actors / regulators | External entities (HHS OCR, NIH, IRB, OIG, EHR vendor) |
| ⬜ Light Gray | `#ECF0F1` | Infrastructure / support systems | Supporting infrastructure (databases, servers, network) |
| 🩵 Teal / Cyan | `#16A085` | Data quality | DQD checks, quality gates, ACHILLES validation |
| 🟤 Brown / Tan | `#795548` | Archived / historical | Archived data, backup storage, historical records |

### HIPAA PHI Boundary Line

In all flowcharts depicting data flow, the **PHI Boundary** — the point at which data transitions from PHI-bearing to de-identified status — is marked with a dashed double line (`===` in Mermaid) and labeled explicitly. This boundary is the most compliance-critical visual element in any data flow diagram and must be clearly readable by any reviewer.

---

## Architecture-to-HIPAA Phase Mapping

The following table maps each major architectural component and pipeline phase to the applicable HIPAA regulatory phase and the specific HIPAA implementation specification that governs it. This mapping is essential for Privacy Officers, Security Officers, and auditors who need to trace specific HIPAA compliance obligations to the architectural components that implement them.

| Architecture Phase / Component | Pipeline Stage | HIPAA Rule | Specific Section | Safeguard Type | Compliance Obligation |
|---|---|---|---|---|---|
| EHR Data Source Integration | Extraction | Security Rule | 45 CFR § 164.312(e) | Technical | Transmission Security — TLS 1.3 required for all HL7/FHIR feeds |
| Staging Database | Ingestion | Security Rule | 45 CFR § 164.312(a)(1) | Technical | Access Control — unique user identification, automatic logoff |
| ETL Transformation Engine | Transformation | Security Rule | 45 CFR § 164.308(a)(1) | Administrative | Security Management — risk analysis covers ETL as PHI system |
| CDM Database (OMOP CDW) | Storage | Security Rule | 45 CFR § 164.312(a)(2)(iv) | Technical | Encryption at rest — AES-256 required |
| De-identification Pipeline | De-identification | Privacy Rule | 45 CFR § 164.514(b) | Administrative | De-identification — Safe Harbor or Expert Determination required |
| DQD / ACHILLES Validation | Quality Assurance | Security Rule | 45 CFR § 164.308(a)(8) | Administrative | Evaluation — assessing effectiveness of security measures |
| Research Access Portal (ATLAS/i2b2) | Researcher Access | Security Rule | 45 CFR § 164.312(b) | Technical | Audit Controls — complete access log required |
| FHIR R4 API | Data Exchange | Security Rule | 45 CFR § 164.312(e)(2)(ii) | Technical | Encryption in transit — required for PHI transmission |
| Data Export / Transfer | Data Delivery | Privacy Rule | 45 CFR § 164.502(b) | Administrative | Minimum Necessary Standard — scope data to IRB-approved purpose |
| Backup / Recovery | Business Continuity | Security Rule | 45 CFR § 164.308(a)(7) | Administrative | Contingency Plan — data backup, DR, emergency mode |
| Audit Log Infrastructure | Monitoring | Security Rule | 45 CFR § 164.312(b) | Technical | Audit Controls — hardware, software, procedural mechanisms |
| Access Provisioning Workflow | Identity Management | Security Rule | 45 CFR § 164.308(a)(3) | Administrative | Workforce Security — authorization and supervision |
| Incident Response System | Breach Management | Breach Notification | 45 CFR §§ 164.400–414 | Administrative | Breach notification procedures and timelines |
| BAA Documentation | Vendor Management | Privacy Rule | 45 CFR § 164.502(e) | Administrative | Business Associate Agreement required before PHI sharing |
| Data Retention / Disposition | End-of-Lifecycle | Privacy Rule | 45 CFR § 164.530(j) | Administrative | Documentation retention ≥ 6 years from creation or last effective date |

---

## COBIT Domain Governance Cross-Reference

The following table maps each major pipeline phase and architectural component to the COBIT 2019 governance/management objective domain(s) primarily responsible for governing that phase. This cross-reference enables COBIT governance assessors and DGC members to identify which COBIT objectives are most directly relevant to a given architectural component, and which architectural components provide implementation evidence for a given COBIT objective assessment.

| Pipeline Phase / Component | Primary COBIT Domain | Primary COBIT Objective(s) | Secondary COBIT Objective(s) |
|---|---|---|---|
| Data Governance Charter and Framework | APO — Align, Plan & Organize | APO01 (Managed IT Management Framework) | APO08 (Managed Relationships) |
| Data Strategy and Roadmap | APO — Align, Plan & Organize | APO02 (Managed Strategy) | APO05 (Managed Portfolio) |
| CDM Enterprise Architecture | APO — Align, Plan & Organize | APO03 (Managed Enterprise Architecture) | BAI03 (Managed Solutions Identification and Build) |
| AI/ML Innovation Governance | APO — Align, Plan & Organize | APO04 (Managed Innovation) | APO12 (Managed Risk) |
| Data Infrastructure Portfolio | APO — Align, Plan & Organize | APO05 (Managed Portfolio) | BAI11 (Managed Projects) |
| Data Infrastructure Budget | APO — Align, Plan & Organize | APO06 (Managed Budget and Costs) | BAI11 (Managed Projects) |
| Workforce and Training | APO — Align, Plan & Organize | APO07 (Managed Human Resources) | DSS05 (Managed Security Services) |
| Stakeholder and Consortium Relationships | APO — Align, Plan & Organize | APO08 (Managed Relationships) | MEA03 (Managed Compliance) |
| SLAs for CDM Services | APO — Align, Plan & Organize | APO09 (Managed Service Agreements) | DSS01 (Managed Operations) |
| Vendor and BAA Management | APO — Align, Plan & Organize | APO10 (Managed Vendors) | APO12 (Managed Risk) |
| CDM Data Quality Management | APO — Align, Plan & Organize | APO11 (Managed Quality) | MEA01 (Managed Performance) |
| Information Risk Management | APO — Align, Plan & Organize | APO12 (Managed Risk) | DSS05 (Managed Security Services) |
| HIPAA Security Program | APO — Align, Plan & Organize | APO13 (Managed Security) | DSS05 (Managed Security Services) |
| Data Catalog and FAIR Principles | APO — Align, Plan & Organize | APO14 (Managed Data) | BAI08 (Managed Knowledge) |
| CDM Migration Programs | BAI — Build, Acquire & Implement | BAI01 (Managed Programs) | BAI07 (Managed IT Change Acceptance) |
| Research Data Requirements | BAI — Build, Acquire & Implement | BAI02 (Managed Requirements Definition) | BAI11 (Managed Projects) |
| ETL Development and FHIR API Build | BAI — Build, Acquire & Implement | BAI03 (Managed Solutions Identification and Build) | BAI06 (Managed IT Changes) |
| CDM Capacity and Availability Planning | BAI — Build, Acquire & Implement | BAI04 (Managed Availability and Capacity) | DSS04 (Managed Continuity) |
| Researcher Change Adoption | BAI — Build, Acquire & Implement | BAI05 (Managed Organizational Change Enablement) | APO07 (Managed Human Resources) |
| CDM Schema Version Changes | BAI — Build, Acquire & Implement | BAI06 (Managed IT Changes) | BAI07 (Managed IT Change Acceptance) |
| Production CDM Cutover | BAI — Build, Acquire & Implement | BAI07 (Managed IT Change Acceptance and Transitioning) | BAI06 (Managed IT Changes) |
| Data Dictionary and Phenotype Library | BAI — Build, Acquire & Implement | BAI08 (Managed Knowledge) | APO14 (Managed Data) |
| CDM Asset and License Management | BAI — Build, Acquire & Implement | BAI09 (Managed Assets) | DSS05 (Managed Security Services) |
| CDM Configuration Baselines | BAI — Build, Acquire & Implement | BAI10 (Managed Configuration) | APO13 (Managed Security) |
| Research Data Project Governance | BAI — Build, Acquire & Implement | BAI11 (Managed Projects) | MEA01 (Managed Performance) |
| CDM Pipeline Operations | DSS — Deliver, Service & Support | DSS01 (Managed Operations) | MEA01 (Managed Performance) |
| Data Access Requests and Incident Response | DSS — Deliver, Service & Support | DSS02 (Managed Service Requests and Incidents) | APO12 (Managed Risk) |
| CDM Data Quality Problem Management | DSS — Deliver, Service & Support | DSS03 (Managed Problems) | APO11 (Managed Quality) |
| Disaster Recovery and CDM Backup | DSS — Deliver, Service & Support | DSS04 (Managed Continuity) | BAI04 (Managed Availability) |
| HIPAA Technical Safeguards | DSS — Deliver, Service & Support | DSS05 (Managed Security Services) | APO13 (Managed Security) |
| De-identification and ETL Controls | DSS — Deliver, Service & Support | DSS06 (Managed Business Process Controls) | APO11 (Managed Quality) |
| CDM KPI Dashboard Monitoring | MEA — Monitor, Evaluate & Assess | MEA01 (Managed Performance and Conformance Monitoring) | DSS01 (Managed Operations) |
| Internal Control Assessment | MEA — Monitor, Evaluate & Assess | MEA02 (Managed System of Internal Control) | APO12 (Managed Risk) |
| HIPAA and Regulatory Compliance | MEA — Monitor, Evaluate & Assess | MEA03 (Managed Compliance with External Requirements) | APO13 (Managed Security) |
| External Audit and Penetration Testing | MEA — Monitor, Evaluate & Assess | MEA04 (Managed Assurance) | MEA02 (Managed System of Internal Control) |

---

## Quick Navigation

### By Role

| Your Role | Start Here | Then Read |
|---|---|---|
| **Data Engineer / ETL Developer** | [02-flowcharts.md](./02-flowcharts.md) — ETL pipeline flowchart | [04-mindmap-notes.md](./04-mindmap-notes.md) — ADR-001 (CDM selection), ADR-004 (FHIR) |
| **Clinical Informaticist** | [03-mindmap.md](./03-mindmap.md) — CDM domain mind map | [01-swimlanes.md](./01-swimlanes.md) — PHI boundary swimlane |
| **Privacy Officer / HIPAA Compliance** | [01-swimlanes.md](./01-swimlanes.md) — HIPAA safeguard swimlane | [02-flowcharts.md](./02-flowcharts.md) — De-identification decision tree |
| **Information Security Officer** | [02-flowcharts.md](./02-flowcharts.md) — Incident response workflow | [04-mindmap-notes.md](./04-mindmap-notes.md) — ADR-002 (cloud BAA), ADR-003 (de-ID) |
| **Research Program Director / PI** | [03-mindmap.md](./03-mindmap.md) — Research use case taxonomy | [01-swimlanes.md](./01-swimlanes.md) — Researcher access provisioning |
| **IRB Staff** | [01-swimlanes.md](./01-swimlanes.md) — IRB authorization swimlane | [02-flowcharts.md](./02-flowcharts.md) — Access provisioning flow |
| **Executive / Governance** | [03-mindmap.md](./03-mindmap.md) — Governance mind map | [01-swimlanes.md](./01-swimlanes.md) — End-to-end overview |
| **External Auditor / Assessor** | [01-swimlanes.md](./01-swimlanes.md) — PHI data flow | [02-flowcharts.md](./02-flowcharts.md) — All control flows |

### By COBIT Governance Domain

| COBIT Domain | Architecture File(s) Most Relevant |
|---|---|
| APO (Align, Plan & Organize) | [03-mindmap.md](./03-mindmap.md) — Governance structure; [04-mindmap-notes.md](./04-mindmap-notes.md) — ADRs |
| BAI (Build, Acquire & Implement) | [02-flowcharts.md](./02-flowcharts.md) — ETL and change flows; [04-mindmap-notes.md](./04-mindmap-notes.md) — ADRs |
| DSS (Deliver, Service & Support) | [01-swimlanes.md](./01-swimlanes.md) — Operations swimlane; [02-flowcharts.md](./02-flowcharts.md) — Incident response |
| MEA (Monitor, Evaluate & Assess) | [02-flowcharts.md](./02-flowcharts.md) — Monitoring flows; [01-swimlanes.md](./01-swimlanes.md) — Audit trail points |

### By File

| File | Direct Link | Description |
|---|---|---|
| `01-swimlanes.md` | [Open →](./01-swimlanes.md) | End-to-end swimlane architecture with actor assignments |
| `02-flowcharts.md` | [Open →](./02-flowcharts.md) | Detailed operational flowcharts for ETL, de-ID, access, incident response |
| `03-mindmap.md` | [Open →](./03-mindmap.md) | Conceptual mind maps for CDM domains and governance |
| `04-mindmap-notes.md` | [Open →](./04-mindmap-notes.md) | Architecture Decision Records and technical notes |

---

## Document Maintenance

This README should be reviewed and updated:
- Within 30 days of any new architecture file being added to the `/docs/architecture/` directory
- Within 30 days of any significant modification to the described architecture files
- At least annually as part of the COBIT APO03 architecture review cycle

**Document Owner:** Data Architecture Lead  
**Review Authority:** Data Governance Committee  
**Version:** 1.0  
**Effective Date:** 2026-05-26  
**Next Review Date:** 2027-05-26

---

*Standards References: TOGAF 10 Architecture Content Framework; ArchiMate 3.2; COBIT 2019 (ISACA, 2018); HIPAA Security Rule 45 CFR Part 164 Subpart C; HIPAA Privacy Rule 45 CFR Part 164 Subpart E; Mermaid.js v10 Specification; HL7 FHIR R4 Specification; OMOP CDM v5.4 Specification*
