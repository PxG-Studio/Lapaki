# Changelog

All notable changes to the Lapaki Health Data Architecture Framework are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- GDPR / EU data protection compliance mapping
- HITRUST CSF v11 control mapping
- State-level privacy law matrix (CCPA, CPRA, NY SHIELD Act)
- Python data quality validation scripts
- FHIR R4 to OMOP ETL reference implementation

---

## [1.0.0] — 2024-05-27

### Added

#### Architecture Documentation
- Four Mermaid swimlane diagrams covering end-to-end pipeline, de-identification workflow, external collaboration request, and incident response
- Five Mermaid flowcharts covering complete data pipeline, PHI classification decision tree, access control authorization, CDM mapping, and research request lifecycle
- Full architecture mindmap with all 14 framework nodes
- Annotated compliance notes table (Node × Standard × COBIT × Risk × Audit Evidence)

#### COBIT 2019 Framework
- Comprehensive coverage of all 40 governance and management objectives
- EDM01–EDM06 governance domain (6 objectives)
- APO01–APO14 Align, Plan, Organize domain (14 objectives)
- BAI01–BAI11 Build, Acquire, Implement domain (11 objectives)
- DSS01–DSS06 Deliver, Service, Support domain (6 objectives)
- MEA01–MEA04 Monitor, Evaluate, Assess domain (4 objectives)
- 5-level maturity model across 8 dimensions
- COBIT ↔ HIPAA control mapping diagrams

#### Compliance Documentation
- HIPAA Administrative, Physical, and Technical Safeguards mapping
- HITECH Act breach notification requirements and timelines
- NIST SP 800-53 Rev. 5 control family mappings
- ISO/IEC 27001:2022 Annex A control mappings
- 10/10 audit-ready checklist with 50+ checkpoints

#### Interactive Visualization
- D3.js force-directed graph with 14 nodes and 15 connections
- Phase filtering, animated data-flow particles, node search
- Glassmorphic detail panel with standards metadata per node
- Edge type legend and bottom standards watermark

#### Governance Templates
- Enterprise data governance policy
- Role-based access control (RBAC) matrix
- Data classification scheme (Identified → Limited Dataset → De-Identified → Public)
- Incident response plan (HIPAA breach notification SOP)

#### Repository Infrastructure
- Apache 2.0 license
- Security disclosure policy
- Contributing guide with DCO requirement
- Contributor Covenant v2.1 Code of Conduct
- GitHub Actions CI/CD workflows
- Issue templates (bug, feature, compliance)
- Pull request template

#### Academic References
- Ohno-Machado et al. (2014) pSCANNER — OMOP multi-site integration
- Trustworthy AI health pipeline governance (2026) — PMC13000207
- Chawla et al. (2024) — CMMI-level AI compliance governance

### Branch Strategy Established
- `main` — production-ready, protected
- `develop` — active development integration
- `staging` — pre-production validation
- `baseline` — compliance audit snapshot (v1.0.0 tag)
- `prototype` — experimental features

---

[Unreleased]: https://github.com/PxG-Studio/Lapaki/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/PxG-Studio/Lapaki/releases/tag/v1.0.0
