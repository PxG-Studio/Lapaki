# Data Governance Policy

> **Authority:** Data Governance Committee, reporting to Executive Leadership  
> **COBIT alignment:** EDM01 (Ensured Governance Framework Setting), APO01 (Managed IT Management Framework)  
> **Standard basis:** FAIR Data Principles (Wilkinson et al., 2016); ISO/IEC 25012 Data Quality  
> **Review cycle:** Annual, approved by Data Governance Committee

---

## 1. Purpose

This policy establishes the enterprise data governance framework for clinical and research data managed within the health data architecture. It defines the principles, roles, responsibilities, and processes that govern how data is acquired, maintained, used, and retired throughout its lifecycle.

---

## 2. Governing Principles

### 2.1 FAIR Data Principles

All research data managed within this framework shall adhere to the FAIR Principles (Wilkinson et al., 2016, *Scientific Data*):

| Principle | Requirement |
|-----------|------------|
| **Findable** | Data assets are registered in the institutional data catalog with unique persistent identifiers (e.g., DOI for datasets) and rich metadata |
| **Accessible** | Data is retrievable via standardized protocols. Access restrictions are explicitly documented with clear governance processes for requesting access |
| **Interoperable** | Data uses standardized clinical terminologies (LOINC, SNOMED CT, RxNorm, ICD-10) and is structured per recognized common data models (OMOP, PCORNet, i2b2, HL7 FHIR) |
| **Reusable** | Data is richly described with data dictionaries, provenance records, and usage licenses. De-identified data is published under open-access terms where appropriate |

### 2.2 Minimum Necessary

Access to PHI and limited datasets shall be restricted to the minimum necessary to accomplish the stated purpose (45 CFR §164.502(b)).

### 2.3 Data Stewardship

Every data asset has a designated Data Steward accountable for its quality, documentation, appropriate use, and compliance.

### 2.4 Privacy by Design

Privacy protections are built into the architecture of each pipeline stage, not added as an afterthought. De-identification is the default; access to identified data requires explicit justification.

---

## 3. Roles and Responsibilities

### 3.1 Data Governance Committee (DGC)

- **Composition:** Chief Data Officer (chair), Privacy Officer, Security Officer, Research Informatics Director, Legal Counsel, representative researcher
- **Meeting frequency:** Monthly (minimum); ad-hoc for urgent matters
- **Responsibilities:** Approve data governance policies, resolve disputes, set data access standards, review audit reports, approve new data use agreements

### 3.2 Chief Data Officer / Data Governance Lead

- Chairs the DGC
- Accountable for overall data governance program
- Reports to executive leadership per COBIT EDM01

### 3.3 Privacy Officer

- Accountable for HIPAA compliance
- Approves PHI access requests (T4)
- Reviews and approves de-identification certifications
- Manages breach response per `governance/incident-response-plan.md`

### 3.4 Security Officer

- Accountable for technical security of all data systems
- Manages access provisioning and deprovisioning
- Maintains security audit logs

### 3.5 Data Stewards

- Subject-matter experts for specific data domains (clinical, claims, research)
- Maintain data dictionaries and metadata
- Approve data quality standards for their domain
- Review and resolve data quality issues

### 3.6 Data Custodians

- IT and data engineering staff responsible for the technical implementation
- Execute data movement, transformation, and storage per Steward direction
- Do not make governance decisions

---

## 4. Data Lifecycle Management

### 4.1 Acquisition

All new data sources entering the pipeline must:
1. Have a documented data inventory entry (source, format, refresh frequency, sensitivity tier)
2. Have a signed Data Use Agreement (if external source)
3. Have a Business Associate Agreement (if containing PHI)
4. Undergo data quality profiling before integration

### 4.2 Processing & Transformation

ETL processes must:
1. Be version-controlled and peer-reviewed
2. Preserve lineage (source → transform → target)
3. Apply terminology normalization (LOINC, SNOMED, RxNorm, ICD-10) consistently
4. Log all transformations for audit purposes

### 4.3 Use & Access

Research access is governed by the RBAC matrix in `governance/access-control-matrix.md`. All access requests are logged. Access is reviewed at defined intervals per the RBAC schedule.

### 4.4 Retention

| Data Type | Minimum Retention | Regulatory Basis |
|-----------|-----------------|-----------------|
| PHI (all forms) | 6 years from creation OR last effective date | 45 CFR §164.530(j) |
| Research data | Per IRB protocol or funder requirement (typically 7–10 years) | NIH grants policy |
| De-identification certifications | 6 years | 45 CFR §164.514 |
| Audit logs | 6 years | 45 CFR §164.312(b) |
| Incident response records | 6 years | 45 CFR §164.530(j) |

### 4.5 Destruction

PHI and limited dataset destruction must follow NIST SP 800-88 media sanitization guidelines:
- **Electronic media:** Cryptographic erasure (preferred) or physical destruction
- **Paper:** Cross-cut shredding (minimum DIN 66399 security level P-4)
- **Certificate of destruction:** Required; retain for 6 years

---

## 5. Data Quality Standards

Data quality is measured across five dimensions per ISO/IEC 25012:

| Dimension | Definition | Minimum Threshold |
|-----------|-----------|------------------|
| **Completeness** | Percentage of required fields populated | ≥95% for critical fields |
| **Accuracy** | Conformance to source-of-truth values | ≥98% for coded fields |
| **Consistency** | Cross-system agreement | ≥97% across EHR and claims |
| **Timeliness** | Data freshness relative to source | ≤30 days for research DW |
| **Validity** | Conformance to defined value sets | ≥99% (SNOMED, LOINC, ICD-10) |

Data quality metrics are reported to the DGC monthly and published in the institutional data catalog.

---

## 6. Policy Enforcement

Violations of this policy may result in:
1. Revocation of data access privileges
2. Mandatory retraining
3. HR disciplinary action up to and including termination
4. Referral to legal and compliance for regulatory reporting if applicable

---

*Approved by Data Governance Committee. Effective: 2024-05-27. Next review: 2025-05-27.*
