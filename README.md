# Lapaki — Health Data Architecture Framework

<div align="center">

![Framework Version](https://img.shields.io/badge/framework-v1.0.0-6366f1?style=for-the-badge&logo=databricks&logoColor=white)
![HIPAA Compliant](https://img.shields.io/badge/HIPAA-Compliant-00b894?style=for-the-badge&logo=shield&logoColor=white)
![COBIT 2019](https://img.shields.io/badge/COBIT-2019-0ea5e9?style=for-the-badge&logo=checkmarx&logoColor=white)
![OMOP CDM](https://img.shields.io/badge/OMOP-CDM%20v5.4-f59e0b?style=for-the-badge&logo=databricks&logoColor=white)
![License](https://img.shields.io/badge/license-Apache%202.0-8b5cf6?style=for-the-badge&logo=apache&logoColor=white)
![No PHI](https://img.shields.io/badge/PHI--Free-Shareable-14b8a6?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

**A generalizable, audit-ready framework for clinical and research data architecture in healthcare systems.**

*From EHR source systems → Internal research environments → External collaborative networks*

[📐 Architecture Diagrams](./docs/architecture/) · [🏛️ COBIT Framework](./docs/cobit/) · [🔒 Compliance](./docs/compliance/) · [🎯 Interactive Visualization](./visualizations/) · [📚 References](./docs/references/)

</div>

---

## Overview

**Lapaki** is an open-source, industry-standard framework that maps the complete clinical and research data pipeline in healthcare organizations using only generic, broadly applicable classifications. No institution-specific names, proprietary system configurations, or identifiable patient health information (PHI) are referenced anywhere in this repository.

The framework is designed to be:
- **Shareable** — safe to present to external partners, regulators, and academic collaborators
- **Auditable** — every design decision is traceable to a published standard
- **Reproducible** — fully generic architecture replicable at any health system
- **Governance-ready** — aligned to COBIT 2019, HIPAA, NIST, and ISO 27001

---

## The Three-Phase Pipeline

```
┌────────────────────────────────────────────────────────────────────┐
│  PHASE 1: OPERATIONAL & SOURCE           │  PHASE 2: INTERNAL      │  PHASE 3: EXTERNAL   │
│                                          │  RESEARCH              │  COLLABORATIVE       │
│  EHR System ──► Operational DW           │  Integrated DW ──► CDM │  Regional Hub ──►    │
│  Research Data Capture ────────────────►│  De-ID Dataset          │  Academic Consortia  │
│  Claims & Payer Data ──────────────────►│  Priority Cohorts       │  Industry Partners   │
│  Operational Self-Service ◄─────────────│                         │  Multi-Site Queries  │
└────────────────────────────────────────────────────────────────────┘
```

---

## Repository Structure

```
Lapaki/
├── README.md                              ← You are here
├── LICENSE                               Apache 2.0
├── SECURITY.md                           Security disclosure policy
├── CONTRIBUTING.md                       Contribution guidelines + DCO
├── CODE_OF_CONDUCT.md                    Contributor Covenant v2.1
├── CHANGELOG.md                          Semantic versioning history
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   └── compliance_issue.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── ci.yml                        Lint + diagram validation
│       ├── compliance-audit.yml          Automated compliance checks
│       └── branch-protection.yml        Branch rule enforcement
│
├── docs/
│   ├── architecture/
│   │   ├── 01-swimlanes.md              Mermaid swimlane diagrams (×4)
│   │   ├── 02-flowcharts.md             Mermaid flowcharts (×5)
│   │   ├── 03-mindmap.md               Full architecture mindmap
│   │   └── 04-mindmap-notes.md         Annotated compliance notes table
│   ├── cobit/
│   │   ├── README.md                    COBIT 2019 overview
│   │   ├── 01-governance-system.md     EDM01–EDM06
│   │   ├── 02-align-plan-organize.md   APO01–APO14
│   │   ├── 03-build-acquire.md         BAI01–BAI11
│   │   ├── 04-deliver-service.md       DSS01–DSS06
│   │   ├── 05-monitor-evaluate.md      MEA01–MEA04
│   │   ├── 06-maturity-model.md        5-level maturity model (8 dimensions)
│   │   └── 07-cobit-mermaid.md         All COBIT Mermaid diagrams
│   ├── compliance/
│   │   ├── README.md                    Compliance overview
│   │   ├── hipaa-safeguards.md          Administrative/Physical/Technical
│   │   ├── hitech-requirements.md       HITECH breach notification
│   │   ├── nist-800-53.md              NIST controls mapped to pipeline
│   │   ├── iso-27001.md               ISO 27001:2022 control mapping
│   │   └── audit-checklist.md          10/10 audit-ready checklist
│   └── references/
│       └── bibliography.md             Full bibliography with 3 cited papers
│
├── visualizations/
│   ├── README.md                        Visualization guide
│   └── health-data-architecture-framework.html  ← Interactive D3.js visualization
│
└── governance/
    ├── data-governance-policy.md        Enterprise data governance policy
    ├── access-control-matrix.md         RBAC matrix for data access tiers
    ├── data-classification-scheme.md   PHI → De-ID → Public classification
    └── incident-response-plan.md        HIPAA breach response SOP
```

---

## Compliance Standards Matrix

| Standard | Version | Coverage | Status |
|----------|---------|---------|--------|
| HIPAA Privacy Rule | 45 CFR §164.500–534 | PHI handling, minimum necessary, patient rights | ✅ Addressed |
| HIPAA Security Rule | 45 CFR §164.302–318 | Administrative, physical, technical safeguards | ✅ Addressed |
| HIPAA Breach Notification | 45 CFR §164.400–414 | Incident response, HHS reporting timelines | ✅ Addressed |
| HITECH Act | Pub.L. 111-5 | Enhanced enforcement, EHR incentives | ✅ Addressed |
| NIST SP 800-53 Rev. 5 | 2020 | 20 control families mapped to pipeline | ✅ Addressed |
| NIST SP 800-188 | 2023 | De-identification of healthcare data | ✅ Addressed |
| ISO/IEC 27001:2022 | 2022 | 93 Annex A controls mapped | ✅ Addressed |
| COBIT 2019 | 2018 | All 40 governance/management objectives | ✅ Addressed |
| OMOP CDM | v5.4 | Common data model for research | ✅ Referenced |
| PCORNet CDM | v6.1 | Patient-centered outcomes research network | ✅ Referenced |
| HL7 FHIR | R4 (4.0.1) | Clinical interoperability standard | ✅ Referenced |
| CDISC SDTM | v1.8 | Clinical trial data standard | ✅ Referenced |
| FAIR Principles | 2016 | Findable/Accessible/Interoperable/Reusable | ✅ Addressed |
| NIH Inclusion Policy | Rev. 2023 | Equitable research participation | ✅ Referenced |

---

## Branch Strategy

| Branch | Purpose | Protection Rules |
|--------|---------|-----------------|
| `main` | Production-ready documentation | Require 1 reviewer, CI must pass, no force push |
| `develop` | Integration branch for completed features | CI must pass |
| `staging` | Pre-production validation environment | Mirrors main protection |
| `baseline` | Locked compliance audit baseline (v1.0.0) | No direct pushes after tag |
| `prototype` | Experimental features and drafts | No protection |

---

## Key Framework Nodes

### Phase 1 — Operational & Source Systems

| Node | Classification | Primary Standard |
|------|--------------|-----------------|
| EHR System | Source System | HL7 FHIR R4, HL7 v2, C-CDA |
| Operational Data Warehouse | Analytics Store | SQL Relational, Kimball Star Schema |
| Research Data Capture | External Input | CDISC ODM, HL7 FHIR Questionnaire |
| Claims & Payer Data | Administrative | X12 EDI 837/835, CMS CCLF |
| Operational Self-Service | Analytics Tool | SMART on FHIR, RBAC |

### Phase 2 — Internal Research Environment

| Node | Classification | Primary Standard |
|------|--------------|-----------------|
| Integrated Research Warehouse | Centralized DW | FAIR Principles, ISO 25012 |
| Common Data Model | Research Schema | OMOP CDM v5.4, PCORNet v6.1, i2b2 |
| De-Identified Research Dataset | PHI-Free | HIPAA 45 CFR §164.514(b), NIST SP 800-188 |
| Priority Population Cohorts | Limited Dataset | 45 CFR §164.514(e), NIH DUA |

### Phase 3 — External Collaborative Research

| Node | Classification | Primary Standard |
|------|--------------|-----------------|
| Regional/National Data Hub | Multi-Site Hub | PCORNet, OHDSI, NIH N3C |
| Multi-Site De-Identified Pool | PHI-Free Federated | NIH Certificate of Confidentiality |
| Academic Research Consortia | Academic Partner | NIH Grant Policy, IRB Auth Agreement |
| Clinical Trial & Industry Partners | Industry | ICH E6 GCP, FDA 21 CFR Part 11 |
| Multi-Site Query Platform | Self-Service | TriNetX, OHDSI Atlas, PopMedNet |

---

## Academic References

This framework is grounded in peer-reviewed literature:

1. **Ohno-Machado, L. et al. (2014).** pSCANNER: patient-centered Scalable National Network for Effectiveness Research. *JAMIA*, 21(4), 621–626. https://doi.org/10.1136/amiajnl-2014-002751 — *Foundational OMOP multi-site integration and SOPs for secure enclave operations.*

2. **Toward integrated sleep health: multimodal AI governance (2026).** PMC13000207. — *Enterprise pipeline governance with dynamic-consent logging and automated privacy audits.*

3. **Chawla, M. et al. (2024).** Toward Trustworthy AI Systems: A Converged Architecture for Governance, Reliability, and Automated Testing. *IJETCSIT*, 5(3). https://ijetcsit.org/index.php/ijetcsit/article/view/684 — *Bridges technical pipelines with CMMI-level enterprise governance.*

> See [`docs/references/bibliography.md`](./docs/references/bibliography.md) for the full annotated bibliography.

---

## Interactive Visualization

The repository includes a fully interactive D3.js visualization of the complete data architecture:

**File:** [`visualizations/health-data-architecture-framework.html`](./visualizations/health-data-architecture-framework.html)

Open the file directly in any modern browser — no server required.

**Features:**
- 14 nodes across all pipeline phases with phase-coded color system
- 15 directional edges with animated data-flow particles
- Click any node to highlight connected subgraph + view full compliance metadata
- Phase filter pills (Operational / Internal Research / External Collab)
- Node drag, zoom/pan, node search, label toggle
- Edge type legend (Primary Flow / De-Identification / Federation / etc.)
- Bottom standards watermark: `OMOP · PCORNet · i2b2 · HL7 FHIR · HIPAA Safe Harbor`

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/PxG-Studio/Lapaki.git
cd Lapaki

# View the interactive visualization
open visualizations/health-data-architecture-framework.html

# Browse COBIT framework documentation
open docs/cobit/README.md

# Review compliance audit checklist
open docs/compliance/audit-checklist.md
```

---

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). All contributions require a Developer Certificate of Origin (DCO) sign-off. Security vulnerabilities should be reported per [`SECURITY.md`](./SECURITY.md).

---

## License

Apache License 2.0 — See [`LICENSE`](./LICENSE).

This framework contains no patient data, no PHI, and no institution-specific configurations. It is a generic reference architecture suitable for public sharing.

---

<div align="center">
<sub>Built with COBIT 2019 · HIPAA · NIST SP 800-53 · ISO 27001 · OMOP · HL7 FHIR · FAIR Principles</sub>
</div>
