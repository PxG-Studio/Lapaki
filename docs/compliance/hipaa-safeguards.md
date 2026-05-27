# HIPAA Safeguards — Administrative, Physical & Technical

> **Regulatory basis:** 45 CFR Part 164, Subparts A, C, and E  
> **Applicable entities:** Covered entities and their business associates  
> **COBIT alignment:** APO13 (Managed Security), DSS05 (Managed Security Services), MEA03 (Managed Compliance)

---

## Overview

The Health Insurance Portability and Accountability Act (HIPAA) Security Rule (45 CFR §164.302–318) requires covered entities and business associates to implement administrative, physical, and technical safeguards to protect the confidentiality, integrity, and availability of electronic protected health information (ePHI).

This document maps each required and addressable safeguard specification to its application within the health data architecture framework described in this repository.

---

## 1. Administrative Safeguards (45 CFR §164.308)

Administrative safeguards are the policies, procedures, and processes that manage the selection, development, implementation, and maintenance of security measures.

### 1.1 Security Management Process (§164.308(a)(1)) — Required

| Specification | Implementation in Framework |
|--------------|----------------------------|
| Risk Analysis | Conduct annual risk assessment covering all pipeline nodes (EHR → Operational DW → CDM → External Hub). Document likelihood and impact for each threat scenario. |
| Risk Management | Implement risk treatment plan per EDM03 (Ensured Risk Optimization). Maintain risk register with residual risk acceptance thresholds. |
| Sanction Policy | Written sanctions for workforce members who fail to comply with security policies. Escalation from warning → termination → regulatory reporting. |
| Information System Activity Review | Automated log review via SIEM. Monthly audit of privileged account activity. Real-time alerting for anomalous query patterns on PHI-containing systems. |

### 1.2 Assigned Security Responsibility (§164.308(a)(2)) — Required

Designate a Privacy Officer and a Security Officer with distinct, documented responsibilities. The Security Officer owns the security program; the Privacy Officer owns the privacy program. Neither role can be held by the same individual in organizations with >50 workforce members.

### 1.3 Workforce Security (§164.308(a)(3)) — Required

| Specification | Implementation |
|--------------|---------------|
| Authorization and/or Supervision | Role-based access control (RBAC) matrix defines access tiers. See `governance/access-control-matrix.md`. |
| Workforce Clearance Procedure | Background screening before access to CDM or identified data systems. |
| Termination Procedures | Automated account deprovisioning within 4 hours of termination. Revoke all tokens, VPN certificates, and data access agreements. |

### 1.4 Information Access Management (§164.308(a)(4)) — Required

Access to PHI-containing systems requires:
1. Unique user identification
2. Documented business justification
3. Supervisor approval
4. IRB authorization (for research access)
5. Data Use Agreement execution (for external access)
6. Minimum necessary principle enforcement

### 1.5 Security Awareness and Training (§164.308(a)(5)) — Required

Annual HIPAA security training is mandatory for all workforce members with access to any PHI-containing system. Training covers:
- PHI identification and classification
- Incident recognition and reporting
- Phishing awareness
- Password hygiene and MFA usage
- Proper use of de-identified data

### 1.6 Security Incident Procedures (§164.308(a)(6)) — Required

Documented incident response plan per `governance/incident-response-plan.md`. Includes:
- Detection → Containment → Assessment → Notification → Recovery → Post-Incident Review
- 60-day HHS notification deadline for breaches affecting ≥500 individuals (45 CFR §164.410)
- Media notification for breaches in state of residence

### 1.7 Contingency Plan (§164.308(a)(7)) — Required

| Specification | Implementation |
|--------------|---------------|
| Data Backup Plan | Encrypted daily backups of all CDM data. Off-site backup retention ≥7 years. |
| Disaster Recovery Plan | RTO ≤4 hours for critical research systems. RPO ≤1 hour for CDM. |
| Emergency Mode Operation Plan | Read-only access to critical clinical data during emergency. Research access suspended. |
| Testing and Revision Procedure | Annual disaster recovery tabletop exercise. Quarterly backup restoration test. |
| Applications and Data Criticality Analysis | Tiered system criticality: Clinical (Tier 1), Research Identified (Tier 2), Research De-ID (Tier 3). |

### 1.8 Evaluation (§164.308(a)(8)) — Required

Annual technical and non-technical evaluation of security program effectiveness. Results reported to executive leadership and data governance committee (COBIT EDM01).

### 1.9 Business Associate Contracts (§164.308(b)(1)) — Required

All vendors, partners, and contractors with access to PHI must execute a Business Associate Agreement (BAA) prior to access. BAAs must include:
- Permitted uses and disclosures
- Safeguards requirements
- Breach reporting obligations (to covered entity within 60 days of discovery)
- Data return or destruction upon contract termination

---

## 2. Physical Safeguards (45 CFR §164.310)

Physical safeguards protect electronic information systems and related equipment from natural and environmental hazards, and unauthorized intrusion.

### 2.1 Facility Access Controls (§164.310(a)(1)) — Required

| Specification | Implementation |
|--------------|---------------|
| Contingency Operations | Documented procedures for physical access during disaster. |
| Facility Security Plan | Badge access control for all data center and server room facilities. |
| Access Control and Validation Procedures | Two-factor physical access (badge + PIN) for data center. |
| Maintenance Records | Log all facility maintenance. Escort required for non-badged personnel in secure areas. |

### 2.2 Workstation Use (§164.310(b)) — Required

Workstations accessing ePHI must use encrypted storage, screen lock after ≤5 minutes of inactivity, and position monitors to prevent visual observation by unauthorized individuals.

### 2.3 Workstation Security (§164.310(c)) — Required

Physical controls on workstations: cable locks, managed device enrollment, remote wipe capability.

### 2.4 Device and Media Controls (§164.310(d)(1)) — Required

| Specification | Implementation |
|--------------|---------------|
| Disposal | NIST SP 800-88 media sanitization for all decommissioned devices. Certificate of destruction required. |
| Media Re-Use | Overwrite/wipe before reassignment of any storage media that held ePHI. |
| Accountability | Asset inventory of all media containing ePHI. Annual reconciliation. |
| Data Backup and Storage | See §164.308(a)(7) contingency plan above. |

---

## 3. Technical Safeguards (45 CFR §164.312)

Technical safeguards are the technology, and the policies and procedures for its use, that protect ePHI and control access.

### 3.1 Access Control (§164.312(a)(1)) — Required

| Specification | Status | Implementation |
|--------------|--------|---------------|
| Unique User Identification | Required | No shared accounts. Every user has a unique identifier tied to their HR record. |
| Emergency Access Procedure | Required | Break-glass accounts with dual authorization, full audit logging, and mandatory post-use review. |
| Automatic Logoff | Addressable | 5-minute session timeout for CDM access portals. 15 minutes for research workstations. |
| Encryption and Decryption | Addressable | AES-256 encryption at rest. TLS 1.3 in transit. HSM for key management. |

### 3.2 Audit Controls (§164.312(b)) — Required

All systems containing ePHI must generate and retain audit logs recording:
- All login/logout events (success and failure)
- All data access events (query, read, export)
- All data modification events (create, update, delete)
- All administrative actions (account creation, permission changes)

Audit logs retained for minimum 6 years (aligned with HIPAA records retention). Logs protected from modification and accessible for OCR audit.

### 3.3 Integrity (§164.312(c)(1)) — Required

| Specification | Implementation |
|--------------|---------------|
| Authentication Mechanism | Hash verification of CDM data exports. Digital signatures on de-identified dataset certifications. Message authentication codes (MACs) for data-in-transit. |

### 3.4 Transmission Security (§164.312(e)(1)) — Required

| Specification | Implementation |
|--------------|---------------|
| Encryption | TLS 1.3 (minimum TLS 1.2) for all ePHI transmission. No unencrypted email for ePHI. Encrypted SFTP for batch data transfers. |
| Integrity Controls | HTTPS with certificate pinning for API connections. Checksum verification on batch transfers. |

---

## 4. De-Identification Standards (45 CFR §164.514)

### 4.1 Safe Harbor Method (§164.514(b))

Removal of all 18 identifier categories:

| # | Identifier Category | Notes |
|---|--------------------|----|
| 1 | Names | First, middle, last, suffix, prefixes |
| 2 | Geographic subdivisions smaller than state | ZIP codes, street addresses, county, city (except first 3 digits of ZIP with population >20,000) |
| 3 | Dates (except year) | Birth date, admission date, discharge date, date of death |
| 4 | Telephone numbers | All phone numbers |
| 5 | Fax numbers | All fax numbers |
| 6 | Email addresses | Personal and work emails |
| 7 | Social Security numbers | Full or partial SSN |
| 8 | Medical record numbers | Any assigned MRN |
| 9 | Health plan beneficiary numbers | Payer ID numbers |
| 10 | Account numbers | Financial account numbers |
| 11 | Certificate/license numbers | Medical, driver's license |
| 12 | Vehicle identifiers | VIN, license plates |
| 13 | Device identifiers | Serial numbers, IMEI |
| 14 | URLs | Personal web addresses |
| 15 | IP addresses | Full or partial IPs |
| 16 | Biometric identifiers | Fingerprints, retina scans, voice prints |
| 17 | Full-face photographs | And comparable images |
| 18 | Any other unique identifier | Codes, characteristics that could identify the individual |

Additionally: "The covered entity does not have actual knowledge that the information could be used alone or in combination with other information to identify an individual."

### 4.2 Expert Determination Method (§164.514(b)(1))

A person with appropriate knowledge of statistical and scientific principles and methods must:
1. Apply generally accepted principles for such statistical and scientific methods
2. Determine that the risk of identifying an individual is very small
3. Document the methods and results justifying the determination

Expert determination certifications must be retained as part of the organization's HIPAA compliance records.

### 4.3 Limited Dataset (§164.514(e))

A Limited Dataset may retain:
- Town or city, state, and ZIP code
- Dates (admission, discharge, service, birth, death)
- Ages
- Geographic subdivisions other than street address

A Limited Dataset requires a Data Use Agreement (DUA) specifying:
- Permitted uses and disclosures
- Prohibition on identifying or contacting individuals
- Requirement to use safeguards

---

## 5. Compliance Cross-Reference

| HIPAA Provision | COBIT Objective | NIST SP 800-53 Control |
|----------------|----------------|----------------------|
| §164.308(a)(1) Risk Analysis | EDM03, APO12 | RA-3, RA-5 |
| §164.308(a)(4) Access Management | APO01, DSS05 | AC-1, AC-2, AC-3 |
| §164.308(a)(5) Training | APO07 | AT-2, AT-3 |
| §164.308(a)(6) Incident Response | DSS02 | IR-1 through IR-8 |
| §164.308(a)(7) Contingency | DSS04 | CP-2, CP-9, CP-10 |
| §164.312(a)(1) Access Control | DSS05 | AC-2, AC-17, IA-2 |
| §164.312(b) Audit Controls | MEA01 | AU-2, AU-3, AU-12 |
| §164.312(e)(1) Transmission Security | DSS05 | SC-8, SC-28 |
| §164.514(b) De-Identification | APO11 | PM-25 |
