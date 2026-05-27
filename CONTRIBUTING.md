# Contributing to Lapaki

Thank you for your interest in contributing to the Lapaki Health Data Architecture Framework. This document outlines the standards and processes for all contributions.

---

## Developer Certificate of Origin (DCO)

All contributions to this repository require a **Developer Certificate of Origin** sign-off. By signing off your commits, you certify that you have the right to submit the contribution under the Apache 2.0 license.

```bash
git commit -s -m "Your commit message"
```

This adds `Signed-off-by: Your Name <your.email@example.com>` to your commit message.

The full DCO text is available at: https://developercertificate.org/

---

## Branch Strategy

| Branch | Purpose | Who can push |
|--------|---------|-------------|
| `main` | Production-ready documentation | Via PR only (1 required reviewer) |
| `develop` | Active development | Via PR with CI passing |
| `staging` | Pre-production validation | Via PR from `develop` |
| `baseline` | Compliance audit snapshot | Read-only after v1.0.0 tag |
| `prototype` | Experimental work | Direct push allowed |

**Workflow:**
1. Branch from `develop` (e.g., `feat/hipaa-safeguards-update`)
2. Make changes and commit with DCO sign-off
3. Open PR against `develop`
4. CI checks must pass
5. One reviewer approval required
6. Merge via squash commit

---

## What We Welcome

- **Corrections** to standard citations (cite section numbers precisely)
- **Additional Mermaid diagrams** expanding the architecture coverage
- **New compliance mappings** (GDPR, CCPA, state privacy laws, HITRUST CSF)
- **Translations** of framework documentation to other languages
- **Improvements** to the interactive D3.js visualization
- **COBIT objective expansions** for additional management domains
- **Governance templates** (DUA templates, IRB checklists, data request forms)

---

## What We Do Not Accept

- Any content containing real PHI, patient data, or identifiable information
- Institution-specific configurations that could reveal proprietary details
- Vendor-specific lock-in recommendations without generic alternatives
- Unverified compliance claims without traceable standard citations

---

## Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
Signed-off-by: Name <email>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `compliance`, `diagram`

**Examples:**
```
docs(cobit): add APO13 managed security objective detail

compliance(hipaa): update breach notification timeline per HHS guidance

diagram(swimlane): add external collaboration request swimlane
```

---

## Mermaid Diagram Standards

All Mermaid diagrams must:
1. Use valid Mermaid syntax (validated by CI)
2. Include a prose description above the diagram (≥100 words)
3. Reference the relevant compliance standard in diagram labels or prose
4. Use consistent color semantics:
   - Indigo/`#6366f1` → Operational systems
   - Sky/`#0ea5e9` → Internal research
   - Violet/`#8b5cf6` → External collaborative
   - Amber/`#f59e0b` → De-identified data
   - Teal/`#14b8a6` → Self-service tools

---

## Citation Standards

When citing standards or academic papers:
- Use full citation with DOI where available
- Include section numbers for regulatory citations (e.g., 45 CFR §164.514(b))
- For academic papers, use APA 7th edition format
- Add new citations to `docs/references/bibliography.md`

---

## Code of Conduct

All contributors must adhere to our [Code of Conduct](./CODE_OF_CONDUCT.md). We are committed to providing a welcoming and inclusive environment for everyone.

---

## Questions

Open a [GitHub Discussion](https://github.com/PxG-Studio/Lapaki/discussions) for questions, ideas, or general feedback.
