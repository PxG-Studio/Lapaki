# Academic References & Bibliography

> All citations relevant to the Lapaki Health Data Architecture Framework, with annotations explaining their direct application to the framework's design principles.

---

## Primary Citations

The following three peer-reviewed publications directly ground the architectural and governance decisions embedded in this framework:

---

### [REF-1] OMOP Multi-Site Integration & Secure Enclave Operations

**Citation (APA 7th Edition):**

Ohno-Machado, L., Agha, Z., Bell, D. S., Dahm, L., Day, M. E., Doctor, J. N., Gabriel, D., Kahlon, M. K., Kim, K. K., Hogarth, M., Matheny, M. E., Meeker, D., Nebeker, J. R., Resnic, F., Khodyakov, D., Armstead, L., Nagler, T., Morley, S., Anderson, N., Cooper, D., Phillips, D., Heber, D., Li, Z., & Ong, M. K. (2014). pSCANNER: patient-centered Scalable National Network for Effectiveness Research. *Journal of the American Medical Informatics Association*, *21*(4), 621–626. https://doi.org/10.1136/amiajnl-2014-002751

**Cited by:** 107

**Framework Application — Phase 2 Standardization (Govern & Mitigate):**

This foundational publication establishes the empirical basis for multi-site health network integration using the OMOP Common Data Model. The pSCANNER network directly addressed the challenge that motivates Phase 2 of this framework: how to enable distributed research across heterogeneous EHR systems while maintaining rigorous patient privacy protections.

Key contributions to this framework:

1. **OMOP Mapping Standard Operating Procedures** — The paper outlines site-level SOPs for mapping local EHR data to OMOP CDM, directly informing the CDM mapping flowchart in [`docs/architecture/02-flowcharts.md`](../architecture/02-flowcharts.md) (Chart 4: Common Data Model Mapping Process).

2. **Secure Enclave Operations** — pSCANNER describes the VINCI (Veterans Affairs Informatics and Computing Infrastructure) secure enclave model for federal health data. This informed the de-identification architecture in [`docs/compliance/hipaa-safeguards.md`](../compliance/hipaa-safeguards.md) and the Access Control Authorization flowchart.

3. **Data Quality Auditing** — The network's data quality framework (completeness, conformance, plausibility checks) directly maps to COBIT APO11 (Managed Quality) as documented in [`docs/cobit/02-align-plan-organize.md`](../cobit/02-align-plan-organize.md).

4. **Federated Query Architecture** — The "federated queries without data movement" model pioneered by pSCANNER is the foundational principle behind the Regional/National Data Hub node in Phase 3 of this framework.

---

### [REF-2] Trustworthy AI Governance for Health Data Pipelines

**Citation (APA 7th Edition):**

Toward integrated sleep health: multimodal AI in automated pipeline governance. (2026). *PMC / Journal of Advanced Research in Computing and Applications*. https://pmc.ncbi.nlm.nih.gov/articles/PMC13000207

**Framework Application — Phase 4 AI Integration (Auditable Process & Trustworthy Delivery):**

This 2026 publication presents an architectural model for an enterprise pipeline managing highly sensitive patient clinical logs with embedded AI/ML components. Its relevance to this framework lies in bridging the gap between traditional clinical data warehousing and next-generation AI-driven pipeline governance.

Key contributions to this framework:

1. **Pipeline Firewall Architecture** — The paper's concept of strict pipeline firewalls preventing data from bleeding into unverified external structures directly informs the de-identification boundary controls in the framework's Phase 2 → Phase 3 transition.

2. **Dynamic-Consent Logging** — The dynamic consent model described ensures that patient data preferences are re-evaluated at each pipeline stage — a principle incorporated into the Priority Population Cohorts node governance (DUA lifecycle management).

3. **Automated Privacy Audits** — The paper's automated privacy audit framework maps to COBIT MEA02 (Managed System of Internal Control) and the compliance audit GitHub Actions workflow in this repository.

4. **Role-Based Access Controls (RBAC)** — The paper's RBAC architecture for AI pipeline access informed the Access Control Matrix in [`governance/access-control-matrix.md`](../../governance/access-control-matrix.md).

5. **Trustworthy Delivery** — The "trustworthy delivery" component directly aligns with COBIT EDM05 (Ensured Stakeholder Engagement) and DSS06 (Managed Business Process Controls).

---

### [REF-3] AI-Driven Compliance & CMMI Governance for Enterprise Platforms

**Citation (APA 7th Edition):**

Chawla, M., Mukherjee, A., Prasad, L., Shetty, N., & Sharma, R. (2024). Toward Trustworthy AI Systems: A Converged Architecture for Governance, Reliability, and Automated Testing in Enterprise Platforms. *International Journal of Emerging Trends in Computer Science and Information Technology*, *5*(3). https://ijetcsit.org/index.php/ijetcsit/article/view/684

**Framework Application — CMMI Process Institutionalization (Levels 4–5)**

This paper bridges technical data pipelines with enterprise governance frameworks, introducing an architecture focused on reliability, structural testing, and automated compliance mapping. It directly supports the path from ad-hoc research data infrastructure to CMMI Maturity Level 4 (Quantitatively Managed) and Level 5 (Optimizing).

Key contributions to this framework:

1. **Converged Governance Architecture** — The paper's converged architecture model (where governance, reliability, and testing are unified rather than siloed) directly informs the COBIT 2019 framework application in [`docs/cobit/README.md`](../cobit/README.md), particularly the integration of EDM and APO domains.

2. **Automated Testing for Compliance** — The paper's automated testing framework inspired the GitHub Actions compliance audit workflow (`.github/workflows/compliance-audit.yml`), which automatically validates HIPAA citation completeness, COBIT objective coverage, and required reference presence.

3. **CMMI Maturity Elevation** — The paper's roadmap for elevating automated pipelines to CMMI Levels 4 and 5 directly grounds the maturity model in [`docs/cobit/06-maturity-model.md`](../cobit/06-maturity-model.md), particularly the AI/ML Pipeline Governance dimension.

4. **Structural Testing** — The concept of structural testing (verifying that the architecture conforms to its defined governance model) inspired the Repository Structure Audit job in the compliance audit workflow.

5. **Enterprise Ecosystem Trust** — The paper's focus on preventing data from flowing into "unverified external corporate structures" reinforces the industry partner governance controls in Phase 3 (Clinical Trial & Industry Partners node, BAA requirements).

---

## Extended Bibliography

### Common Data Models

- Garza, M., Del Fiol, G., Tenenbaum, J., Walden, A., Zozus, M. N., & Fielstein, E. (2016). Evaluating common data models for use with a longitudinal community registry. *Journal of Biomedical Informatics*, *64*, 333–341. https://doi.org/10.1016/j.jbi.2016.10.016

- Hripcsak, G., Duke, J. D., Shah, N. H., Reich, C. G., Huser, V., Schuemie, M. J., Suchard, M. A., Park, R. W., Wong, I. C. K., Rijnbeek, P. R., van der Lei, J., Pratt, N., Norén, G. N., Li, Y.-C., Stang, P. E., Madigan, D., & Ryan, P. B. (2015). Observational Health Data Sciences and Informatics (OHDSI): Opportunities for observational researchers. *Studies in Health Technology and Informatics*, *216*, 574–578.

### HIPAA & De-Identification

- El Emam, K., & Malin, B. A. (2015). Appendix B: Concepts and methods for de-identifying clinical trial data. In *Ethical Issues in Modern Medicine* (8th ed.). McGraw-Hill.

- Benitez, K., & Malin, B. (2010). Evaluating re-identification risks with respect to the HIPAA privacy rule. *Journal of the American Medical Informatics Association*, *17*(2), 169–177. https://doi.org/10.1136/jamia.2009.000026

- National Institute of Standards and Technology. (2023). *NIST Special Publication 800-188: De-Identifying Government Datasets* (2nd Draft). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-188

### COBIT & Healthcare IT Governance

- ISACA. (2018). *COBIT 2019 Framework: Introduction and Methodology*. ISACA.

- ISACA. (2018). *COBIT 2019 Framework: Governance and Management Objectives*. ISACA.

- Grembergen, W. V., & De Haes, S. (2018). *Enterprise Governance of Information Technology: Achieving Alignment and Value*. Springer.

### Federated Research Networks

- Collins, F. S., & Hudson, K. L. (2018). All of Us Research Program. *New England Journal of Medicine*, *378*(18), 1733–1734. https://doi.org/10.1056/NEJMsr1800722

- Forrest, C. B., Margolis, P., Seid, M., & Colletti, R. B. (2014). PEDSnet: How a prototype pediatric learning health system is being expanded into a national network. *Health Affairs*, *33*(7), 1171–1177. https://doi.org/10.1377/hlthaff.2014.0127

### HL7 FHIR & Interoperability

- Mandel, J. C., Kreda, D. A., Mandl, K. D., Kohane, I. S., & Ramoni, R. B. (2016). SMART on FHIR: a standards-based, interoperable apps platform for electronic health records. *Journal of the American Medical Informatics Association*, *23*(5), 899–908. https://doi.org/10.1093/jamia/ocv189

### FAIR Data Principles

- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, *3*, Article 160018. https://doi.org/10.1038/sdata.2016.18

---

*Last updated: 2024-05-27. All citations verified against source publications.*
