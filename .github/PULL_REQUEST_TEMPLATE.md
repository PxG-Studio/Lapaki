## Pull Request Checklist

**Branch:** `$SOURCE_BRANCH` → `$TARGET_BRANCH`

### Description
<!-- Describe what this PR changes and why -->

### Type of Change
- [ ] 📐 Architecture diagram addition/update
- [ ] 🏛️ COBIT framework documentation
- [ ] 🔒 Compliance documentation
- [ ] 🎨 Interactive visualization update
- [ ] 📚 Reference/bibliography update
- [ ] 🏗️ Governance template
- [ ] ⚙️ CI/CD workflow update
- [ ] 📄 General documentation

### Compliance Checklist
- [ ] **No PHI** — This PR contains no patient health information, real clinical data, or identifiable configurations
- [ ] **Standard citations** — All regulatory references include exact CFR sections or standard version numbers
- [ ] **Mermaid syntax** — All new Mermaid diagrams have been validated locally with `mmdc`
- [ ] **COBIT alignment** — New content references at least one COBIT 2019 objective
- [ ] **Bibliography** — New academic references added to `docs/references/bibliography.md`

### Testing
- [ ] CI passes locally (run `npm run lint` if applicable)
- [ ] Mermaid diagrams render correctly in GitHub preview
- [ ] Interactive visualization tested in Chrome/Firefox/Safari

### DCO Sign-off
- [ ] All commits include `Signed-off-by:` line per DCO requirements

### Related Issues
Closes #

---
> ⚠️ **Reviewer reminder:** Verify no PHI or institution-specific data before approving.
