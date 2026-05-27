# COBIT 2019 Framework — Healthcare Data Architecture Application

> **Classification:** Internal Governance Documentation — Lapaki Health Data Architecture Project  
> **Standard:** COBIT 2019 (ISACA)  
> **Version:** 1.0  
> **Effective Date:** 2026-05-26  
> **Review Cycle:** Annual  
> **Owner:** Data Governance Committee  

---

## 1. Introduction to COBIT 2019

**COBIT 2019** (Control Objectives for Information and Related Technologies, 2019 Edition) is the globally authoritative framework for **IT governance and management**, published by ISACA. It provides a comprehensive set of universally applicable principles, practices, analytical tools, and models that define and deliver a reference architecture for the governance of enterprise IT. First published in 1996 as an audit-focused control framework, COBIT has evolved through five major versions; the 2019 edition represents the most significant redesign, shifting from a fixed-process architecture to a **flexible, design-factor-driven governance system** that adapts to enterprise context, scale, and risk profile.

COBIT 2019 distinguishes sharply between **governance** (the "Evaluate, Direct, and Monitor" tier) and **management** (the operational tier that "Plans, Builds, Runs, and Monitors"). This separation mirrors the classic Carver/Jensen board governance model and is particularly significant in healthcare, where regulatory bodies expect demonstrable board-level accountability for information assets containing Protected Health Information (PHI).

The COBIT 2019 framework is maintained through a suite of core publications:
- **COBIT 2019 Framework: Introduction and Methodology** — foundational principles, design factors, and system overview
- **COBIT 2019 Framework: Governance and Management Objectives** — the 40 objectives with detailed guidance
- **COBIT 2019 Design Guide** — governance system design using design factors and focus areas
- **COBIT 2019 Implementation Guide** — change management and roadmap guidance

---

## 2. The Six Governance Principles of COBIT 2019

COBIT 2019 is built upon **six overarching governance principles** that collectively describe what a well-governed enterprise information system looks like. These principles replace the five principles of COBIT 5 and are expressly designed to be independent of organizational size, sector, or regulatory environment — making them portable to the highly regulated healthcare domain.

| # | Principle | Healthcare Application |
|---|-----------|----------------------|
| 1 | **Provides Stakeholder Value** | Every investment in health data infrastructure must trace to measurable clinical or research value — patient safety improvements, research output, or operational efficiency. |
| 2 | **Holistic Approach** | Data governance cannot be siloed; it must encompass people (clinical staff, researchers, data stewards), processes (ETL pipelines, de-identification workflows), and technology (CDM platforms, federated query engines). |
| 3 | **Dynamic Governance System** | As regulatory requirements evolve (e.g., HIPAA updates, 21st Century Cures Act mandates), the governance system must adapt without requiring wholesale redesign. |
| 4 | **Governance Distinct from Management** | The Data Governance Committee (board-delegated) sets policy and direction; the Research Informatics team executes. These roles must never be conflated in healthcare data governance. |
| 5 | **Tailored to Enterprise Needs** | The 15 design factors (enterprise strategy, risk profile, compliance requirements, IT-sourcing model, etc.) allow COBIT to be right-sized to a healthcare research network's specific context. |
| 6 | **End-to-End Governance System** | PHI governance spans from point-of-care EHR capture through CDM transformation, de-identification, federated query, and research publication — all touchpoints are in scope. |

---

## 3. The Five Management Domains and Objective Architecture

COBIT 2019 organizes its **40 governance and management objectives** across one governance domain and four management domains. Each objective defines a purpose statement, key activities, related guidance, and process capability indicators.

### 3.1 Governance Domain

| Domain | Code | Full Name | Objectives | Focus |
|--------|------|-----------|------------|-------|
| Governance | **EDM** | Evaluate, Direct, and Monitor | **6** | Board and executive-level governance: strategy, risk appetite, stakeholder expectations |

The six EDM objectives (EDM01–EDM06) are the accountability layer. In healthcare, these map to board resolutions, data governance charters, and IRB oversight structures.

### 3.2 Management Domains

| Domain | Code | Full Name | Objectives | Focus |
|--------|------|-----------|------------|-------|
| Align, Plan, Organize | **APO** | Align, Plan, Organize | **14** | Strategy alignment, risk management, portfolio management, HR, quality, security architecture |
| Build, Acquire, Implement | **BAI** | Build, Acquire, Implement | **11** | Solution delivery, change management, knowledge management, asset management |
| Deliver, Service, Support | **DSS** | Deliver, Service, Support | **6** | Service delivery, IT operations, incident management, business continuity, security operations |
| Monitor, Evaluate, Assess | **MEA** | Monitor, Evaluate, Assess | **4** | Performance monitoring, compliance, audit assurance, external assurance |

**Total: 40 objectives across 5 domains.**

The APO domain is particularly dense because it encompasses the full "plan before you build" philosophy — including APO13 (Information Security Management) and APO14 (Data Management), both of which are tier-one priorities for healthcare data architecture.

---

## 4. Application to Healthcare Data Architecture

### 4.1 Why Healthcare Data Governance Is Uniquely Complex

Healthcare data governance presents a confluence of pressures absent in most other regulated industries:

1. **Dual regulatory regimes**: HIPAA imposes federal baseline requirements; state laws (e.g., California CMIA, New York SHIELD Act) may be stricter. COBIT's dynamic governance principle accommodates this layering.
2. **Research vs. clinical tension**: Data collected for clinical care is frequently re-purposed for research under IRB waiver. COBIT's benefits delivery (EDM02) and risk optimization (EDM03) objectives formalize the deliberate balancing act this requires.
3. **Multi-site federated architectures**: Ohno-Machado et al. (2014) described the **pSCANNER** network, a multi-site OMOP CDM federation supporting privacy-preserving distributed queries across PCORnet sites (*JAMIA* 21(4):621–626). COBIT's management domains provide the control scaffolding that makes such architectures governable — specifically APO14 (Data Management), BAI08 (Knowledge Management), and DSS05 (Managed Security Services).
4. **AI/ML pipeline governance**: As large language models and predictive algorithms enter clinical decision support, governance of training data, model provenance, and algorithmic bias becomes a regulatory imperative. The 2026 PMC13000207 study on trustworthy AI pipeline governance demonstrates that COBIT-aligned data stewardship frameworks reduce model validation failure rates and improve audit trail completeness in multi-site AI deployments.
5. **FAIR data principles**: The research community's adoption of Findable, Accessible, Interoperable, Reusable (FAIR) principles creates governance obligations for metadata curation, persistent identifiers, and controlled-access data sharing that COBIT's transparency (EDM06) and data management (APO14) objectives directly address.

### 4.2 The Lapaki Health Data Architecture Context

This documentation governs the **Lapaki Health Data Architecture**, a federated research data platform implementing:
- OMOP CDM v5.4 as the canonical data model
- Safe Harbor and Expert Determination de-identification pathways (45 CFR §164.514)
- Distributed query infrastructure (analogous to the pSCANNER architecture)
- AI/ML pipeline components subject to the governance provisions of Chawla et al. (2024), which establishes that trustworthy AI systems in healthcare require explicit COBIT-aligned compliance governance, including documented risk appetite, control testing evidence, and continuous monitoring (*IJETCSIT* 5(3))

---

## 5. Framework Cross-Mapping: COBIT 2019 ↔ HIPAA / HITRUST / NIST / ISO 27001

COBIT 2019 is not a standalone compliance framework; it operates as a **governance meta-framework** that unifies control requirements from domain-specific standards. The following mapping reflects the Lapaki project's multi-framework alignment strategy.

| COBIT 2019 Objective | HIPAA Reference | HITRUST CSF | NIST SP 800-53 | ISO 27001:2022 |
|----------------------|-----------------|-------------|----------------|----------------|
| EDM01 — Governance Framework | Privacy Rule §164.530 | Control Category 01 | PL-1, PL-2 | A.5.1, A.5.2 |
| EDM03 — Risk Optimization | Security Rule §164.308(a)(1) | Control Category 06 | RA-1 through RA-9 | A.8.2, Clause 6.1.2 |
| APO12 — Risk Management | Security Rule §164.308(a)(1)(ii)(A) | Control Category 06 | RA-3, PM-9 | A.5.3, A.6.1 |
| APO13 — Security Management | Security Rule §164.308–§164.312 | Control Categories 07–10 | PL-8, SA-2 | Annex A Controls |
| APO14 — Data Management | Privacy Rule §164.502–§164.514 | Control Category 07 | AC-1, SI-12 | A.8.1, A.8.2 |
| BAI06 — Change Management | Security Rule §164.308(a)(5) | Control Category 10 | CM-3, CM-5 | A.8.32 |
| DSS05 — Security Services | Security Rule §164.312 | Control Categories 01–10 | AC-2, AC-17, AU-2 | A.8.3, A.8.6 |
| DSS06 — Business Process Controls | Breach Notification §164.400–§164.414 | Control Category 09 | IR-4, SI-3 | A.5.26 |
| MEA01 — Performance Monitoring | Security Rule §164.308(a)(8) | Control Category 09 | AU-6, CA-7 | A.8.15, A.8.16 |
| MEA02 — Internal Assurance | Security Rule §164.308(a)(8) | Control Category 09 | CA-2, AU-12 | A.5.35 |
| MEA03 — External Compliance | All HIPAA Rules | All HITRUST Categories | PM-1, CA-5 | Clause 9.3 |
| MEA04 — External Assurance | HIPAA BAA §164.308(b) | Control Category 09 | CA-2, CA-3 | A.5.36 |

This mapping is maintained as a living document and serves as the primary evidence artifact for cross-framework compliance audits.

---

## 6. The COBIT 2019 Performance Management System

COBIT 2019 adopts the **ISO/IEC 33020 process measurement framework** (derived from CMMI) to assess capability at each of the 40 objectives. Six **capability levels** are defined, with each level representing a progressively more mature, repeatable, and measurable state:

| Level | Designation | Definition | Healthcare Data Governance Indicator |
|-------|-------------|------------|--------------------------------------|
| **0** | **Incomplete** | The process is not implemented or does not achieve its purpose | No formal data governance; PHI access is uncontrolled |
| **1** | **Performed** | The process achieves its purpose through ad hoc activities | Data governance exists but is undocumented; de-identification is manual |
| **2** | **Managed** | The process is planned, monitored, and adjusted | Documented policies exist; de-identification workflow is repeatable but not measured |
| **3** | **Established** | The process uses a defined standard process | OMOP CDM adopted; de-identification SOPs approved; audit logs exist |
| **4** | **Predictable** | The process operates within defined limits | Statistical process control applied; breach detection SLAs defined and met |
| **5** | **Optimizing** | The process is continuously improved | Federated learning pipelines with automated drift detection; governance metrics drive investment decisions |

Assessment against these levels requires **objective evidence** — policy documents, process outputs, meeting minutes, audit logs, and test results. The Lapaki project targets **Level 3 (Established)** as the current-state baseline, with a 24-month roadmap toward **Level 4 (Predictable)** in the highest-priority domains (EDM03, APO13, APO14, DSS05, MEA01, MEA03).

---

## 7. Why COBIT 2019 Was Selected for Lapaki Governance

The selection of COBIT 2019 as the governing framework for the Lapaki Health Data Architecture was informed by a structured evaluation against three alternative frameworks (NIST CSF, ISO 27001 alone, and HITRUST CSF alone) across six selection criteria:

1. **Healthcare regulatory alignment**: COBIT's explicit cross-mapping capability allows simultaneous alignment with HIPAA, HITRUST, and NIST without maintaining three separate control inventories.
2. **Research data management specificity**: APO14 (Managed Data) provides explicit guidance on data classification, data quality, metadata management, and data lifecycle — capabilities required by the OMOP CDM implementation.
3. **AI/ML governance coverage**: Chawla et al. (2024) demonstrates that COBIT's management objectives, particularly APO12 (Risk Management) and MEA01 (Monitoring), are extensible to AI system lifecycle governance in ways that narrow security frameworks (ISO 27001 alone) are not.
4. **Federated architecture support**: The trustworthy AI pipeline governance study (PMC13000207, 2026) identifies COBIT's holistic approach as particularly valuable in multi-site healthcare networks where governance authority is distributed across institutional boundaries.
5. **Maturity roadmap support**: The six-level capability model provides a defensible, auditable progression path that satisfies Big Four consulting review standards and HITRUST certification evidence requirements.
6. **ISACA ecosystem**: Availability of certified professionals (CISA, CRISC, CGEIT), tooling, and ISACA-maintained cross-reference mappings reduces implementation cost and accelerates audit preparation.

---

## 8. References

1. **Ohno-Machado, L., et al. (2014).** pSCANNER: Patient-centered scalable national network for effectiveness research. *Journal of the American Medical Informatics Association (JAMIA)*, **21**(4), 621–626. [https://doi.org/10.1136/amiajnl-2014-002751](https://doi.org/10.1136/amiajnl-2014-002751)  
   *Context: Multi-site OMOP CDM integration, federated query architecture, privacy-preserving distributed research network governance.*

2. **[Toward Integrated Sleep Health] (2026).** Trustworthy AI pipeline governance in multi-site health research networks. PMC13000207. *PubMed Central.*  
   *Context: Governance requirements for AI/ML pipelines in federated healthcare data environments; COBIT-aligned data stewardship.*

3. **Chawla, A., et al. (2024).** Trustworthy AI Systems: Governance, Compliance, and Accountability Frameworks. *International Journal of Emerging Technologies in Computer Science and Information Technology (IJETCSIT)*, **5**(3).  
   *Context: COBIT-aligned AI compliance governance; control mapping for machine learning pipeline auditability and regulatory compliance.*

---

*This document is maintained by the Lapaki Data Governance Committee and reviewed annually in accordance with COBIT 2019 EDM01 requirements. Questions should be directed to the designated Data Governance Officer.*
