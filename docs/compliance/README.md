# Compliance Documentation Overview

> **Regulatory scope:** HIPAA, HITECH, NIST SP 800-53, ISO/IEC 27001:2022  
> **COBIT alignment:** MEA03 (Managed Compliance with External Requirements)  
> **Last review:** 2024-05-27

---

This directory contains the full compliance documentation for the Health Data Architecture Framework. Each document maps framework design decisions to specific regulatory requirements, enabling an auditor to trace every architectural choice to its governing standard.

## Documents in This Directory

| Document | Standard(s) | Coverage |
|----------|------------|---------|
| [`hipaa-safeguards.md`](./hipaa-safeguards.md) | 45 CFR §164 | All 3 safeguard categories + de-identification standards |
| [`hitech-requirements.md`](./hitech-requirements.md) | Pub.L. 111-5 | Breach notification, enhanced enforcement, EHR incentives |
| [`nist-800-53.md`](./nist-800-53.md) | NIST SP 800-53 Rev. 5 | 20 control families mapped to pipeline |
| [`iso-27001.md`](./iso-27001.md) | ISO/IEC 27001:2022 | Annex A controls mapped to framework |
| [`audit-checklist.md`](./audit-checklist.md) | All | 50+ checkpoint audit-ready checklist |

## Compliance Standards Summary

### HIPAA (Health Insurance Portability and Accountability Act)
- **Privacy Rule** (45 CFR §164.500–534): PHI handling, minimum necessary, patient rights, authorized disclosures
- **Security Rule** (45 CFR §164.302–318): Administrative, physical, technical safeguards for ePHI
- **Breach Notification Rule** (45 CFR §164.400–414): Notification timelines, HHS reporting, media notification
- **De-Identification** (45 CFR §164.514): Safe Harbor (18 identifiers) and Expert Determination methods

### HITECH Act (Health Information Technology for Economic and Clinical Health)
- Enhanced HIPAA enforcement with increased civil monetary penalties (up to $1.9M per violation category/year)
- Extended breach notification requirements to business associates
- Required notification to individuals whose PHI was breached

### NIST SP 800-53 Rev. 5
- 20 control families, 1,000+ individual controls
- Framework uses: Access Control (AC), Audit (AU), Identification/Authentication (IA), Incident Response (IR), Risk Assessment (RA), System and Communications Protection (SC)

### ISO/IEC 27001:2022
- Information Security Management System (ISMS) requirements
- 93 Annex A controls across 4 themes: Organizational, People, Physical, Technological
- Requires documented ISMS scope, risk treatment plan, and annual management review

## Compliance Posture Statement

> This framework is designed from the ground up to support HIPAA compliance, COBIT governance, and industry-standard security practices. **No PHI is stored, processed, or transmitted within this repository.** All architectural recommendations reference published regulatory standards with exact citation numbers. Organizations implementing this framework must conduct their own HIPAA risk analysis per 45 CFR §164.308(a)(1) and engage qualified legal and compliance counsel.
