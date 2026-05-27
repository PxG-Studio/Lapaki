# Build, Acquire & Implement (BAI) Domain — BAI01–BAI11

> **COBIT 2019 Reference:** Build, Acquire & Implement (BAI) is the management objective domain in COBIT 2019 that governs how solutions are identified, built, acquired, deployed, and maintained to enable the organization's strategy. In a healthcare research data environment, BAI objectives govern the full lifecycle of CDM infrastructure development: from requirements definition through solution build, testing, deployment, transition, and ongoing knowledge and asset management. Failure to govern these objectives rigorously results in CDM implementations that are insecure, non-conformant, or unable to meet research and regulatory requirements.

---

## Table of Contents

- [BAI01 — Managed Programs](#bai01--managed-programs)
- [BAI02 — Managed Requirements Definition](#bai02--managed-requirements-definition)
- [BAI03 — Managed Solutions Identification and Build](#bai03--managed-solutions-identification-and-build)
- [BAI04 — Managed Availability and Capacity](#bai04--managed-availability-and-capacity)
- [BAI05 — Managed Organizational Change Enablement](#bai05--managed-organizational-change-enablement)
- [BAI06 — Managed IT Changes](#bai06--managed-it-changes)
- [BAI07 — Managed IT Change Acceptance and Transitioning](#bai07--managed-it-change-acceptance-and-transitioning)
- [BAI08 — Managed Knowledge](#bai08--managed-knowledge)
- [BAI09 — Managed Assets](#bai09--managed-assets)
- [BAI10 — Managed Configuration](#bai10--managed-configuration)
- [BAI11 — Managed Projects](#bai11--managed-projects)

---

## BAI01 — Managed Programs

### Healthcare Context

BAI01 requires the organization to manage collections of related projects and activities as coordinated programs with shared governance, resources, and accountability. In a healthcare research data environment, the most consequential programs are: **CDM migration programs** (transitioning from one CDM version to another, e.g., OMOP CDW v5.3 to v5.4, or from a legacy data warehouse to OMOP CDW); **FHIR R4 adoption programs** (implementing HL7 FHIR R4 APIs as the primary data exchange mechanism for both EHR data ingestion and researcher data access); and **EHR-to-CDM ETL programs** (the ongoing development and maintenance of the full ETL pipeline from source EHR systems through staging to the CDM).

These programs are distinct from ordinary projects because they span multiple years, involve multiple interdependent project workstreams, require sustained executive sponsorship, and produce benefits only when all components are successfully delivered. A CDM migration program, for example, requires coordinated delivery of: updated ETL code, vocabulary updates, data quality validation, researcher communication and re-training, analytics tool reconfiguration, and regulatory documentation updates — all of which must be sequenced carefully to avoid disrupting ongoing research studies that depend on the current CDM version.

Program governance must establish a Program Management Office (PMO) function, a Program Steering Committee with appropriate clinical, research, IT, and compliance representation, formal stage gates with exit criteria, and a benefits realization framework. Program-level risks (schedule risk, data quality risk, research disruption risk) must be actively managed across the full program lifecycle.

### Key Activities

- **Establish a CDM Migration Program Governance Structure:** Define Program Steering Committee membership, roles, decision rights, and meeting cadence; establish program-level PMO function; document governance structure in the program charter.
- **Define Program Stage Gates with Healthcare-Specific Exit Criteria:** Require formal stage gate reviews at program initiation, design completion, build completion, testing completion, and go-live; define exit criteria for each gate including CDM conformance test pass rates, IRB notification completion, and researcher communication milestones.
- **Manage Cross-Project Dependencies:** Maintain a program-level dependency register identifying all inter-project dependencies (e.g., vocabulary update must precede ETL regression test; EHR upgrade must precede FHIR API testing); monitor dependency status weekly.
- **Track Program-Level Benefits Realization:** Define measurable program benefits (improved CDM conformance score, reduced query response time, new FHIR API capability); baseline current state before program initiation; measure achievement at 6 and 12 months post-completion.
- **Manage Stakeholder Communication at Program Level:** Develop and execute a program-level communication plan targeting researchers, clinical informaticists, IRB, compliance, and executive leadership; provide monthly program status reports; conduct formal stakeholder briefings at each stage gate.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Program Stage Gate Pass Rate (First Attempt) | ≥ 85% of stage gates passed without remediation cycle | Per gate |
| Program Schedule Variance (SV) | SV ≤ ± 15% of planned program timeline | Monthly |
| Post-Program Benefit Realization Rate | ≥ 80% of defined program benefits achieved at 12-month assessment | 12 months post-completion |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.308(a)(8) | Evaluation — requirement to assess effect of program changes on security |
| NIST SP 800-53 Rev. 5 | SA-3 (System Development Life Cycle) | SDLC governance for program deliverables |

---

## BAI02 — Managed Requirements Definition

### Healthcare Context

BAI02 governs the elicitation, analysis, validation, and management of requirements for IT solutions and services. In a healthcare research data environment, **requirements definition is driven by three primary sources**: IRB-approved research protocols (which specify what data elements are required, what time periods are relevant, and what de-identification or consent conditions apply); clinical informatics specifications (which define how clinical concepts map to CDM domains and standard vocabularies); and regulatory requirements (HIPAA minimum necessary standard, NIH data sharing requirements, FDA data standards for RWE).

Requirements in a CDM context are inherently complex because they involve multiple layers: the **phenotype definition** (the clinical algorithm used to identify a cohort or outcome), the **CDM mapping specification** (how source EHR codes map to OMOP standard concepts), the **data quality requirement** (what quality thresholds must be met for the data to be research-grade), and the **access control requirement** (who can access what data under what conditions). All four layers must be explicitly documented and validated before any build activity begins.

The IRB plays a unique role in requirements definition for healthcare research data — the IRB-approved protocol is effectively the authoritative requirements document for data use, and any deviation from the protocol's data specifications requires IRB amendment. The requirements management process must include a formal mechanism for linking CDM data access requests to specific IRB-approved protocols and tracking any protocol amendments that affect data requirements.

### Key Activities

- **Develop IRB-Linked Data Requirements Specifications:** For each research project, develop a formal Data Requirements Specification document that includes: IRB protocol number, approved data elements, time period, required CDM domains, applicable de-identification or Limited Dataset parameters, and data quality thresholds; obtain PI and IRB liaison sign-off.
- **Formalize Phenotype Definition Management:** Maintain a Phenotype Library (aligned with OHDSI PhenotypeLibrary or PCORNet Phenotype Catalog) documenting all implemented phenotype algorithms with: clinical rationale, OMOP concept set definitions, validation results, applicable studies, and version history.
- **Elicit Requirements Using Structured Techniques:** Use structured requirement elicitation techniques (joint application design sessions with researchers, CDM data profiling sessions, OMOP ATLAS cohort definition workshops) to ensure requirements are complete, unambiguous, and testable.
- **Validate Requirements Against CDM Feasibility:** Conduct formal feasibility analysis for each data requirement against the current CDM data holdings (availability, completeness, plausibility of required data elements); document feasibility findings and communicate limitations to researchers before build commitment.
- **Maintain a Requirements Traceability Matrix:** Link each approved requirement to the IRB protocol citation, the CDM implementation artifact (ETL rule, ATLAS concept set, SQL query), the test case, and the data quality check; update throughout the project lifecycle.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Requirements Traceability Coverage | 100% of implemented CDM data elements traceable to approved IRB requirement | Per project |
| Requirements Change Rate Post-Approval | ≤ 15% requirements change rate after formal sign-off | Per project |
| Phenotype Library Coverage (Active Studies) | 100% of active research cohort definitions documented in Phenotype Library | Quarterly |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Privacy Rule | 45 CFR § 164.502(b) | Minimum necessary — requirements must specify minimum data needed |
| HIPAA Privacy Rule | 45 CFR § 164.512(i) | Research exception requirements (IRB waiver or authorization) |
| NIST SP 800-53 Rev. 5 | SA-15 (Development Process, Standards, and Tools) | Requirements management standards |

---

## BAI03 — Managed Solutions Identification and Build

### Healthcare Context

BAI03 requires the organization to design, build, and configure solutions in a structured, quality-assured manner aligned with approved requirements. In a healthcare research data environment, the primary build activities are: **CDM ETL development** (writing, testing, and maintaining the transformation code that converts EHR source data to OMOP or PCORNet CDM format); **de-identification pipeline development** (building the automated processes that produce Safe Harbor or Expert Determination de-identified datasets); **FHIR API build and configuration** (implementing SMART on FHIR-compliant APIs for data exchange); and **data quality validation tool configuration** (deploying and customizing OHDSI ACHILLES, DQD, and PCORNet DQR tools).

The CDM ETL development process must follow a formal **software development lifecycle (SDLC)** with requirements traceability, peer code review, automated unit testing, integration testing, and production deployment approval. ETL code must be version-controlled (Git) with branching strategy aligned to CDM version lifecycle. All ETL code that processes PHI must be treated as a **high-assurance software component** requiring security code review and compliance validation before deployment.

De-identification pipeline development requires particular rigor because errors in de-identification are PHI breaches — there is no acceptable defect rate. The pipeline must implement Safe Harbor de-identification per 45 CFR § 164.514(b)(2) or Expert Determination per § 164.514(b)(1), and must be validated against an independent PHI detection benchmark (i2b2/VA de-identification challenge, 2014 i2b2 NLP De-identification Challenge datasets) before any production deployment.

### Key Activities

- **Establish a CDM ETL SDLC:** Define and enforce a formal SDLC for all CDM ETL development including: requirements traceability, design documentation, peer code review (mandatory), automated unit test coverage ≥ 80%, integration testing in staging environment, and documented deployment approval process.
- **Implement ETL Version Control with CDM Lifecycle Alignment:** Maintain all ETL code in a Git repository with branching strategy aligned to CDM version branches (e.g., `omop-v5.3`, `omop-v5.4`); require pull request review and CI/CD pipeline pass before merge to main.
- **Build and Validate De-identification Pipeline:** Design de-identification pipeline components for each HIPAA Safe Harbor identifier category (18 identifiers per 45 CFR § 164.514(b)(2)(i)); validate pipeline against PHI detection benchmarks; document validation results and obtain Privacy Officer sign-off before production use.
- **Configure and Validate FHIR APIs:** Implement HL7 FHIR R4 APIs conformant to US Core Implementation Guide (v6.1) and SMART on FHIR (v2.0); conduct FHIR conformance testing using Inferno test kit; document API conformance statement.
- **Deploy Automated Build and Test Infrastructure:** Implement CI/CD pipeline (GitHub Actions, GitLab CI, or equivalent) for all CDM ETL and de-identification code; require automated unit test, linting, and security scan pass before any code is promoted to staging or production.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| ETL Unit Test Coverage | ≥ 80% line coverage for all production ETL modules | Per build |
| De-identification Validation F1 Score (PHI Detection) | ≥ 0.98 recall on benchmark PHI entity set | Per pipeline deployment |
| FHIR Conformance Test Pass Rate (Inferno) | ≥ 95% of required test cases passing | Per API release |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Privacy Rule | 45 CFR § 164.514(b) | De-identification methods — Safe Harbor, Expert Determination |
| NIST SP 800-53 Rev. 5 | SA-11 (Developer Testing and Evaluation) | Security testing during development |
| HL7 FHIR US Core | v6.1.0 | API conformance standard |

---

## BAI04 — Managed Availability and Capacity

### Healthcare Context

BAI04 requires the organization to ensure that IT services have sufficient availability and capacity to meet current and future demands. In a healthcare research data environment, CDM availability is a critical research enabler — researchers depend on uninterrupted CDM access to execute ongoing study queries, track cohort accrual, and meet grant-mandated analysis milestones. Unplanned CDM downtime can delay NIH-funded research with real consequences for grant renewal.

Capacity management is increasingly critical as CDM data volumes grow. A health system adding new EHR source sites, integrating genomic data, or adopting real-time FHIR feeds can experience order-of-magnitude growth in CDM storage and compute requirements within a single grant cycle. Without proactive capacity planning, the organization faces emergency infrastructure scaling events that introduce security and stability risks.

Availability planning must address **planned maintenance windows** (CDM unavailability during ETL batch loads, CDM version upgrades, system patching) as well as unplanned outages. Maintenance windows must be communicated to researchers in advance, scheduled during low-demand periods (nights and weekends), and minimized in duration through automation and parallel processing techniques.

### Key Activities

- **Develop an Annual Capacity Plan:** Project CDM storage, compute, and network capacity requirements for the next 12–24 months based on the research portfolio pipeline, planned EHR integrations, and data volume growth trends; align capacity investments with the APO06 budget process.
- **Implement CDM Availability Monitoring:** Deploy uptime monitoring for all CDM-facing services (query portal, FHIR API, data export pipeline); alert on-call engineer within 5 minutes of any service degradation; publish availability metrics to stakeholders monthly.
- **Define and Enforce Maintenance Windows:** Establish and publish standard CDM maintenance windows (e.g., Saturday 02:00–06:00 local time); notify researchers ≥ 5 business days before any scheduled maintenance exceeding 2 hours; document all maintenance events in an incident log.
- **Implement Auto-Scaling for Cloud CDM Workloads:** For cloud-hosted CDM infrastructure, configure auto-scaling policies for compute resources during peak query demand periods; set capacity thresholds to prevent performance degradation; test auto-scaling behavior quarterly.
- **Conduct Quarterly Capacity Reviews:** Review actual resource utilization (CPU, memory, storage, network I/O) against capacity plan projections quarterly; adjust capacity plan based on observed growth trends and upcoming portfolio changes; escalate capacity shortfalls to APO06 for budget action.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| CDM Query Portal Availability | ≥ 99.5% monthly uptime during research hours (06:00–22:00) | Monthly |
| CDM Storage Utilization Rate | ≤ 75% of provisioned storage capacity at all times | Monthly |
| Capacity Plan Forecast Accuracy | Actual resource consumption within ± 20% of annual capacity plan projection | Annual |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.308(a)(7)(ii)(A) | Data backup plan — capacity to restore backups |
| HIPAA Security Rule | 45 CFR § 164.308(a)(7)(ii)(C) | Disaster recovery plan — capacity and recovery targets |
| NIST SP 800-53 Rev. 5 | CP-2 (Contingency Plan) | Availability and capacity contingency planning |

---

## BAI05 — Managed Organizational Change Enablement

### Healthcare Context

BAI05 requires the organization to manage the organizational change aspects of any IT solution implementation to ensure that stakeholders are prepared, willing, and able to use new or changed solutions effectively. In a healthcare research data environment, **organizational change management is among the most underinvested and highest-failure-risk activities** in CDM program delivery. A technically perfect CDM migration will fail to deliver research value if researchers do not adopt the new system, if clinical informaticists resist new ETL workflows, or if clinical departments do not trust the data quality.

The change management challenge in healthcare is compounded by the **clinical informatics culture gap** — clinical researchers are trained in biomedical science, not data engineering, and may have strong resistance to changes in the data environment they have been using for years. A move from ICD-9 to ICD-10 codes, or from a legacy data warehouse to OMOP CDW, fundamentally changes the analytics tools and code that researchers rely on. Without structured change enablement, these transitions generate significant researcher frustration, shadow data systems, and risk of non-compliant workarounds.

Change enablement must be tailored to the specific stakeholder group: researchers need updated cohort definition training and analytics tool walkthroughs; clinical department data stewards need ETL mapping documentation and data quality dashboard training; IT and data engineering staff need technical training on new CDM schema, ETL tooling, and CI/CD processes; compliance and privacy staff need updates on any changes to PHI handling in the new system.

### Key Activities

- **Conduct Stakeholder Change Impact Assessment:** Before any major CDM change, assess the impact on each stakeholder group (researchers, clinical informaticists, IT, compliance, IRB); document impact ratings and develop targeted change enablement plans for each high-impact group.
- **Develop and Deliver Role-Specific Training Programs:** Design and deliver training programs for each affected stakeholder group before go-live; include OHDSI ATLAS cohort definition workshops for researchers, ETL documentation walkthroughs for data engineers, and data quality dashboard training for data stewards.
- **Establish Researcher Support Help Desk:** During CDM migration periods, establish a dedicated researcher support function (email, ticketing system, or office hours) to address CDM change questions; set response time SLA of ≤ 1 business day; track and report support request volume and resolution rate.
- **Communicate Change Timeline and Impact Proactively:** Develop and execute a structured communication plan covering all major CDM changes; communicate ≥ 30 days in advance of go-live for any change affecting researcher analytics; provide clear documentation of what is changing, why, and what researchers need to do differently.
- **Monitor Post-Change Adoption Metrics:** Track CDM adoption indicators post-go-live (active user sessions, query volume, researcher satisfaction survey scores, support ticket volume); use adoption data to identify and address barriers to effective use.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Researcher Training Completion Rate (Pre-Go-Live) | ≥ 90% of active CDM users trained before major CDM go-live | Per major change |
| Post-Change Researcher Satisfaction Score | ≥ 3.8 / 5.0 on post-change satisfaction survey | Per major change |
| Support Help Desk Response SLA Adherence | ≥ 95% of researcher support tickets responded to within 1 business day | During transition period |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.308(a)(5) | Security awareness and training — change-driven training requirements |
| NIST SP 800-53 Rev. 5 | AT-3 (Role-Based Training) | Role-based training for system changes |

---

## BAI06 — Managed IT Changes

### Healthcare Context

BAI06 requires the organization to manage all IT changes in a controlled, authorized, and documented manner to minimize the risk of service disruption and unauthorized modification. In a healthcare research data environment, **IT change management is particularly high-stakes** because unauthorized or poorly managed changes to CDM schema, ETL logic, or vocabulary tables can introduce systematic data quality errors that silently corrupt ongoing research studies without any immediate indication of failure.

The most consequential change categories in a CDM environment include: **CDM schema version upgrades** (e.g., OMOP CDW v5.3 → v5.4, which involves new table definitions, new vocabulary columns, and revised ETL specification requirements); **EHR interface changes** (modifications to the HL7 or FHIR feeds from the source EHR that can alter the availability or format of specific clinical data elements); **vocabulary table updates** (monthly RxNorm releases, biannual LOINC releases, annual SNOMED CT releases — each of which can affect concept mappings and therefore query results); **ETL code changes** (modifications to transformation logic that can alter how specific clinical events are mapped to CDM domains); and **security configuration changes** (firewall rules, access control changes, encryption key rotations).

All changes must pass through a formal **Change Advisory Board (CAB)** review before implementation in production. Emergency changes (required to remediate an active security incident or critical data quality failure) may follow an expedited approval process but must be retrospectively reviewed by the CAB within 5 business days.

### Key Activities

- **Implement a Formal Change Management Process:** Establish a documented change management process covering: change request submission, change classification (standard/normal/emergency), impact assessment, change advisory board review, approval, scheduled implementation, post-implementation review, and documentation.
- **Operate a CDM Change Advisory Board (CAB):** Convene a CDM-specific CAB meeting at least bi-weekly; include representation from data engineering, clinical informatics, research operations, compliance, and IT security; require CAB approval for all Normal and Emergency CDM changes.
- **Enforce Change Freeze Periods for Active Research Studies:** Implement CDM change freeze periods aligned with critical research milestones (primary analysis periods, regulatory submission windows, IRB protocol expiration dates); require CDM Change Director approval to break freeze.
- **Manage Vocabulary Update Change Process:** Treat all OMOP vocabulary table updates as Normal Changes requiring CAB review; validate vocabulary updates in staging environment (test impact on existing ATLAS concept sets, assess query result changes); document validation results before production deployment.
- **Document All Changes in Change Log:** Maintain a comprehensive CDM Change Log recording all implemented changes with: change ID, type, date, description, implementer, CAB approval reference, and post-implementation review outcome; retain for ≥ 6 years per HIPAA documentation requirements.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Change Success Rate (No Post-Implementation Issues) | ≥ 95% of implemented changes with no unplanned rollback or incident | Monthly |
| Unauthorized Change Rate | Zero unauthorized CDM changes detected | Monthly |
| Emergency Change CAB Retrospective Review Completion | 100% of emergency changes retrospectively reviewed within 5 business days | Per emergency change |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.308(a)(8) | Periodic technical and non-technical evaluation of changes |
| NIST SP 800-53 Rev. 5 | CM-3 (Configuration Change Control) | Change control for configuration-managed systems |
| NIST SP 800-53 Rev. 5 | SA-10 (Developer Configuration Management) | Change management during development |

---

## BAI07 — Managed IT Change Acceptance and Transitioning

### Healthcare Context

BAI07 requires the organization to formally accept and transition new or significantly changed IT solutions into production in a controlled manner with defined acceptance criteria, rollback plans, and stakeholder communication. In a healthcare research data environment, **production CDM cutover is the highest-risk event in the CDM program lifecycle**. A failed or poorly managed cutover can make research data inaccessible to ongoing studies, corrupt the CDM with partially transformed data, or introduce security vulnerabilities if go-live checklists are not fully executed.

The CDM cutover plan must be exhaustively documented, rehearsed (dry run in staging), and approved by all stakeholder groups before go-live. The plan must define: the specific cutover window; the sequence of steps with assigned owners and estimated durations; go/no-go decision criteria at each checkpoint; a rollback trigger point and rollback procedure (including estimated rollback duration and data restoration steps); researcher communication before, during, and after cutover; and post-go-live validation steps (automated data quality checks, manual spot-check validation, researcher acceptance testing).

Researchers with active IRB-approved studies that depend on CDM data must be individually notified of the cutover timeline and the expected impact on their specific data access. Where a CDM version change affects the definition or completeness of existing phenotypes, the researcher must be informed and, where required by the IRB protocol, a protocol amendment may be needed before the researcher can use data from the new CDM version.

### Key Activities

- **Develop and Rehearse a Detailed CDM Cutover Plan:** Create a step-by-step cutover runbook with owner, duration, and verification criteria for each step; conduct a full dry-run cutover in the staging environment at least 14 days before production go-live; document and address all issues found during dry run.
- **Define and Test Rollback Procedures:** Define the rollback trigger (specific data quality failure threshold or system failure criterion); document the full rollback procedure including data restoration steps, timeline, and post-rollback verification; test rollback in staging environment before production go-live.
- **Obtain Formal Go-Live Acceptance Sign-Off:** Require written go-live acceptance from: Data Engineering Lead (ETL and quality validation), Clinical Informatics Lead (CDM conformance), IRB Liaison (research study impact notification), CISO (security checklist completion), and CDM Program Sponsor (executive acceptance).
- **Communicate Cutover to All Affected Researchers:** Send targeted communications to all active CDM users ≥ 10 business days before cutover; include impact description, cutover window, expected downtime duration, rollback scenario communication, and post-go-live support contact.
- **Conduct Structured Post-Go-Live Review:** Within 5 business days of production go-live, conduct a formal post-implementation review covering: cutover plan adherence, actual vs. planned downtime, data quality validation results, researcher support ticket volume, and outstanding issues; document and track all action items.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Cutover Runbook Step Completion Rate | 100% of runbook steps completed during production cutover | Per cutover event |
| Post-Cutover Unplanned Rollback Rate | Zero unplanned rollbacks post-production go-live | Per cutover event |
| Researcher Cutover Notification Lead Time | 100% of active researchers notified ≥ 10 business days before cutover | Per cutover event |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.308(a)(8) | Evaluation of security after significant operational changes |
| NIST SP 800-53 Rev. 5 | SA-10 (Developer Configuration Management) | Production transition controls |
| NIST SP 800-53 Rev. 5 | CP-10 (System Recovery and Reconstitution) | Recovery procedures for failed transitions |

---

## BAI08 — Managed Knowledge

### Healthcare Context

BAI08 requires the organization to manage knowledge assets — information, expertise, and know-how — in a way that ensures critical knowledge is captured, maintained, accessible, and protected from loss due to staff turnover. In a healthcare research data environment, knowledge management is a **persistent organizational vulnerability** because CDM implementation knowledge (ETL logic, concept mapping rationale, data quality exception history, phenotype validation results) is highly specialized, difficult to document comprehensively, and often concentrated in a very small number of individuals.

The primary knowledge assets in a clinical data program include: the **CDM Data Dictionary** (the authoritative reference for every CDM table, column, data type, vocabulary, and constraint); the **Phenotype Library** (documented clinical algorithms for cohort identification and outcome definition, with validation evidence); the **ETL Documentation** (functional specification of each ETL transformation, including source-to-target mapping, business rules, exception handling, and version history); the **Data Quality Exception Log** (historical record of known data quality issues, their root causes, and remediation status, essential for accurate interpretation of research findings); and the **Wiki or Knowledge Base** (operational documentation for common CDM tasks, query templates, researcher FAQs, and system administration procedures).

Knowledge management must address the critical risk of **key person dependency** — the scenario where the departure of a single data engineer or clinical informaticist takes institutional CDM knowledge with them. All knowledge assets must be documented, maintained in a version-controlled repository, and accessible to at least two staff members at all times.

### Key Activities

- **Maintain the CDM Data Dictionary:** Develop and maintain an authoritative, machine-readable CDM data dictionary covering all CDM tables, columns, allowed values, vocabulary mappings, and relationships; publish in the data catalog; update within 5 business days of any CDM schema change.
- **Operate and Grow the Phenotype Library:** Maintain a formal Phenotype Library (aligned with OHDSI PhenotypeLibrary or PCORNet Phenotype Catalog) with all implemented phenotype algorithms documented including: clinical definition, ATLAS/SQL implementation, validation study references, applicable CDM version, and version history; add new phenotypes within 30 days of research project completion.
- **Version-Control All ETL Documentation:** Store all ETL functional specifications in a version-controlled document repository (Git or Confluence with version history); require ETL documentation updates as a prerequisite for merge to main branch; include source-to-target mapping, business rules, exception handling, and vocabulary mapping rationale.
- **Implement a Researcher-Facing Knowledge Base:** Maintain a searchable knowledge base (Confluence, SharePoint, or equivalent) for researcher-facing CDM documentation: query templates, cohort definition walkthroughs, data quality caveats, vocabulary reference guides, and researcher FAQs; review and update quarterly.
- **Conduct Knowledge Transfer and Cross-Training:** Require explicit knowledge transfer sessions when key CDM personnel transition (offboarding checklist); mandate cross-training so each critical CDM function is performed independently by at least two staff members; document cross-training completion in the workforce competency matrix.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| ETL Documentation Currency | 100% of production ETL modules with documentation updated within 5 business days of change | Continuous |
| Phenotype Library Coverage (Active Studies) | 100% of phenotypes used in active studies documented in library | Quarterly |
| Knowledge Base Researcher Satisfaction Score | ≥ 4.0 / 5.0 on annual researcher knowledge base usability survey | Annual |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.316(b) | Documentation — retention of policies and procedures for 6 years |
| NIST SP 800-53 Rev. 5 | AT-4 (Training Records) | Knowledge and training documentation |
| NIST SP 800-53 Rev. 5 | CM-9 (Configuration Management Plan) | Documentation of system configuration knowledge |

---

## BAI09 — Managed Assets

### Healthcare Context

BAI09 requires the organization to manage its IT assets — hardware, software, data, and licenses — throughout their full lifecycle, from acquisition through disposal. In a healthcare research data environment, **asset management is a direct HIPAA compliance requirement** because PHI is stored on physical and virtual assets that must be tracked, controlled, and properly disposed of. Failure to track and manage assets containing PHI can result in breaches through loss of unencrypted devices, unauthorized software installation, or inadequate disposal of storage media.

The asset inventory for a clinical data program includes: **data warehouse servers** (physical or virtual machines hosting the CDM database, ETL engine, FHIR server, and analytics tools); **CDM software licenses** (OMOP community tools are open-source, but commercial CDM platforms, analytics tools such as SAS or MATLAB, and ETL tools may carry significant licensing costs and compliance obligations); **ETL tool licenses** (commercial ETL platforms such as Informatica, Talend, or Microsoft SSIS); **encryption key management assets** (HSMs or cloud KMS keys used to protect CDM data at rest and in transit); and **endpoint devices** (workstations and laptops used by data engineers and researchers to access CDM data, each a potential PHI breach vector if not properly controlled).

Software license compliance is a specific risk in academic healthcare settings where grant-funded software licenses may expire, be incorrectly scoped (e.g., a research license inadvertently used for clinical operations), or be non-transferable between grant periods. The asset register must track license expiration dates and scope restrictions for all licensed CDM tools.

### Key Activities

- **Maintain a Comprehensive CDM Asset Inventory:** Develop and maintain a complete inventory of all hardware, software, and data assets involved in CDM operations; include asset type, owner, location (physical or cloud), HIPAA PHI classification, license status, support contract expiration, and disposition status; update within 10 business days of any asset change.
- **Implement Software License Compliance Program:** Track all CDM software licenses (commercial and open-source with license restrictions) in the asset inventory; calendar renewal dates with 90-day advance alerts; conduct annual software license reconciliation comparing installed software against licensed entitlements.
- **Manage Encryption Key Lifecycle:** Implement a formal encryption key lifecycle management process (generation, distribution, storage in HSM or cloud KMS, rotation schedule, revocation, and destruction); document key custodians; test key restoration procedures quarterly.
- **Enforce HIPAA-Compliant Device Management:** Enforce full-disk encryption on all endpoints with CDM or PHI access (BitLocker, FileVault, or equivalent); enforce mobile device management (MDM) enrollment; require remote wipe capability for all mobile endpoints; conduct quarterly device inventory audit.
- **Implement Secure Asset Disposal Process:** Require NIST 800-88-compliant media sanitization (Clear, Purge, or Destroy) for all storage media being decommissioned; obtain and retain written certification of sanitization; include in BAA terms with hosting vendors.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Asset Inventory Completeness | ≥ 98% of CDM-related assets documented in inventory | Quarterly audit |
| Software License Compliance Rate | 100% of deployed software within licensed scope | Annual reconciliation |
| Endpoint Encryption Compliance Rate | 100% of endpoints with CDM/PHI access encrypted and MDM-enrolled | Monthly |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.310(d) | Device and media controls — disposal, re-use, accountability |
| NIST SP 800-88 Rev. 1 | Full guide | Media sanitization guidelines |
| NIST SP 800-53 Rev. 5 | CM-8 (System Component Inventory) | Hardware and software inventory |

---

## BAI10 — Managed Configuration

### Healthcare Context

BAI10 requires the organization to establish and maintain accurate configuration baselines for IT systems and to control changes to those configurations. In a healthcare research data environment, **configuration management is a foundational security and data quality control** because unauthorized or undocumented configuration changes can introduce PHI exposure, degrade CDM data quality, or cause compliance gaps. HIPAA's requirement for a documented sanction policy and information system activity review (45 CFR § 164.308(a)(1)(ii)(C) and (D)) depends on having a reliable configuration baseline to detect anomalous system behavior.

Configuration baselines must be defined and maintained for: **CDM database configuration** (OMOP CDM schema version, database engine settings, tablespace definitions, index configurations); **EHR interface configurations** (HL7 connection parameters, FHIR endpoint URLs, authentication credentials, data scope definitions); **security settings** (firewall rules, security group configurations, MFA enforcement policies, audit logging settings, encryption algorithm selections); **ETL tool configurations** (connection strings, scheduling parameters, error handling settings); and **FHIR server configurations** (endpoint definitions, supported US Core profiles, authentication/authorization settings).

Configuration drift — the gradual deviation of actual system configuration from the approved baseline — is a persistent risk in complex CDM environments. Configuration drift detection must be automated, with alerts generated whenever a detected configuration state differs from the approved baseline. All configuration changes must flow through the BAI06 change management process.

### Key Activities

- **Define and Document CDM Configuration Baselines:** Develop and approve formal configuration baselines for all CDM infrastructure components; document baselines in the configuration management database (CMDB); obtain CISO sign-off; update baselines through the BAI06 change management process.
- **Implement Automated Configuration Drift Detection:** Deploy configuration compliance scanning tools (AWS Config, Azure Policy, Ansible playbooks, Chef InSpec, or equivalent) to continuously monitor CDM infrastructure configuration against approved baselines; alert on any detected drift within 4 hours.
- **Manage CDM Schema Version Configuration:** Treat the CDM schema version as a configuration item; document the installed CDM version, vocabulary version, and any local extensions in the CMDB; require formal change approval before schema version changes; maintain schema history with effective dates.
- **Control EHR Interface Configurations:** Treat all EHR interface connection parameters (HL7 endpoints, FHIR URLs, authentication credentials, data scope) as configuration items; store in encrypted credential vault; require change approval for any modification; conduct quarterly review of all active interface configurations.
- **Conduct Quarterly Configuration Audit:** Perform quarterly automated configuration compliance audit comparing actual system state against approved baselines for all CDM components; generate compliance report; remediate all detected deviations within 30 days; report results to CISO.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Configuration Compliance Rate | ≥ 99% of CDM components in compliance with approved baseline | Monthly automated scan |
| Configuration Drift Detection Time | ≤ 4 hours from drift occurrence to alert generation | Continuous |
| Configuration Deviation Remediation Time | 100% of detected deviations remediated within 30 days | Per deviation |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Security Rule | 45 CFR § 164.308(a)(1)(ii)(D) | Information system activity review — requires stable, known configuration |
| NIST SP 800-53 Rev. 5 | CM-2 (Baseline Configuration) | Configuration baseline requirement |
| NIST SP 800-53 Rev. 5 | CM-6 (Configuration Settings) | Security configuration settings |
| NIST SP 800-53 Rev. 5 | CM-7 (Least Functionality) | Restrict system functionality to minimum required |

---

## BAI11 — Managed Projects

### Healthcare Context

BAI11 requires the organization to manage individual IT projects using defined project management practices that ensure projects are delivered on time, within budget, within scope, and at acceptable risk levels. In a healthcare research data environment, **project management carries distinctive constraints** that do not apply in other industries: IRB protocol timelines (which create hard deadlines for data availability), grant reporting periods (which create hard deadlines for research deliverables), and grant budget periods (which may not accommodate project cost overruns). A data infrastructure project that runs over budget may literally defund a research study.

The project management framework must accommodate the **IRB lifecycle** as a formal external dependency. Before any research data project begins, the IRB approval must be in place, and the project plan must account for IRB review timelines, potential protocol amendments, and annual protocol renewal requirements. Project managers must maintain awareness of IRB-imposed conditions that affect the data project scope (e.g., data destruction requirements at study close, consent limitations on data reuse).

Research data projects also require careful **deliverable definition** that goes beyond typical IT deliverables. A CDM data delivery project must define: the specific CDM domains to be populated, the date range of the data, the de-identification method applied, the data quality validation approach, the transfer mechanism, and the acceptance criteria (data quality thresholds that the researcher must confirm before accepting the deliverable).

### Key Activities

- **Implement a Standardized Research Data Project Lifecycle:** Define and enforce a standard project lifecycle for all research data delivery projects: Initiation (IRB confirmation, data requirements specification), Planning (project plan, resource assignment, risk register), Execution (ETL development, quality validation), Delivery (researcher acceptance testing), and Closure (lessons learned, archive); require formal phase-gate documentation at each transition.
- **Maintain IRB Timeline Integration in Project Planning:** Include IRB approval date, protocol expiration date, and renewal schedule as explicit milestones in all research data project plans; monitor IRB timeline dependencies actively; alert PI ≥ 60 days before protocol expiration.
- **Apply Earned Value Management for Grant-Funded Projects:** Use Earned Value Management (EVM) for all data projects with grant budgets ≥ $100K; track Planned Value (PV), Earned Value (EV), and Actual Cost (AC) monthly; report Schedule Performance Index (SPI) and Cost Performance Index (CPI) to project sponsor.
- **Maintain Project Risk Registers:** Maintain an active risk register for each research data project; identify risks specific to healthcare data projects (IRB delays, EHR interface instability, CDM vocabulary gaps, re-identification risk in small cohorts); review and update bi-weekly during execution.
- **Conduct Formal Project Closure with Lessons Learned:** At project completion, conduct a structured lessons learned session; document findings in the organizational knowledge base (BAI08); confirm data disposition per IRB protocol and DUA; obtain PI acceptance sign-off; archive all project documentation per HIPAA retention requirements.

### Metrics

| Metric | Target | Measurement Frequency |
|---|---|---|
| Project Schedule Performance Index (SPI) | SPI ≥ 0.90 (≤ 10% schedule variance) | Monthly |
| IRB Timeline Compliance Rate | 100% of projects with IRB protocol current (not expired) throughout project lifecycle | Continuous |
| Project Closure Documentation Completion Rate | 100% of completed projects with lessons learned documented and data disposition confirmed | Per project closure |

### HIPAA / NIST Alignment

| Standard | Citation | Alignment |
|---|---|---|
| HIPAA Privacy Rule | 45 CFR § 164.512(i) | Research exception requirements (project must have active IRB approval) |
| 2 CFR Part 200 | §§ 200.302–200.309 | Financial management and reporting for grant-funded projects |
| NIST SP 800-53 Rev. 5 | PM-13 (Security and Privacy Workforce) | Project workforce competency requirements |

---

*Document Version: 1.0 | Effective Date: 2026-05-26 | Owner: Data Governance Committee | Review Cycle: Annual*
*Standards References: COBIT 2019 (ISACA, 2018); HIPAA Security Rule 45 CFR Part 164 Subpart C; HIPAA Privacy Rule 45 CFR Part 164 Subpart E; NIST SP 800-53 Rev. 5; 2 CFR Part 200 (Uniform Guidance); HL7 FHIR R4 Specification; OMOP CDM v5.4 Specification*
