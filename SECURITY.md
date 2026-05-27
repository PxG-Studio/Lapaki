# Security Policy

## Reporting a Vulnerability

The Lapaki project takes security seriously. Since this repository contains healthcare data architecture documentation, we apply the same rigor to our open-source security posture as we expect from the systems this framework describes.

**Do NOT open a public GitHub Issue for security vulnerabilities.**

### Reporting Process

1. Email **security@studiopxg.com** with the subject line: `[LAPAKI-SECURITY] <brief description>`
2. Include:
   - A description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact assessment
   - Your suggested fix (if any)
3. You will receive an acknowledgment within **48 hours**
4. We target a fix or mitigation within **7 business days** for critical issues

### Scope

This repository contains:
- Documentation (Markdown)
- Interactive HTML/JavaScript visualizations
- GitHub Actions workflow definitions
- Configuration files

**In scope:**
- Malicious scripts embedded in HTML visualizations
- GitHub Actions workflow injection vulnerabilities
- Supply chain issues in CDN-loaded dependencies (D3.js, Google Fonts)
- Exposed credentials or tokens in any committed file

**Out of scope:**
- Theoretical privacy concerns about the generic framework (no PHI is present)
- GitHub platform vulnerabilities (report to GitHub Security)

### Dependency Security

The interactive visualization (`visualizations/health-data-architecture-framework.html`) loads the following external resources:
- `https://d3js.org/d3.v7.min.js` — D3.js data visualization library
- `https://fonts.googleapis.com` — Google Fonts (Inter, JetBrains Mono)

If you identify a compromised version of any dependency, please report immediately using the process above.

### Supported Versions

| Version | Supported |
|---------|-----------|
| `main` branch | ✅ Active support |
| `v1.x.x` releases | ✅ Security patches |
| `prototype` branch | ❌ Not supported |

---

*This security policy is compliant with responsible disclosure principles and the coordinated vulnerability disclosure (CVD) model.*
