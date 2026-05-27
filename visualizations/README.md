# Interactive Visualizations

This directory contains the interactive D3.js visualization of the Health Data Architecture Framework.

## Files

### `health-data-architecture-framework.html`

A fully self-contained, single-file interactive visualization built with D3.js v7.

**Open directly in any modern browser — no server, no build step required.**

```bash
open visualizations/health-data-architecture-framework.html
```

#### Features

| Feature | Description |
|---------|-------------|
| **14 nodes** | All pipeline nodes across Operational, Internal Research, External Collaborative, De-Identified, and Self-Service phases |
| **15 edges** | Directional connections with type-coded colors and dashes |
| **Animated flow** | Data-flow particles travel along edges in real time |
| **Node detail panel** | Click any node to see its Industry Standard box, description, and connection list |
| **Phase filtering** | Isolate Operational / Internal Research / External Collaborative phases |
| **Node drag** | Freely reposition any node |
| **Search** | Fuzzy search by label, tags, or standards text |
| **Zoom/pan** | Mouse wheel zoom, drag to pan, ⊡ to fit-to-view |
| **Keyboard shortcuts** | `+`/`-` zoom, `0` fit, `Esc` deselect |

#### Node Color System

| Color | Hex | Phase |
|-------|-----|-------|
| Indigo | `#6366f1` | Operational / Source Systems |
| Sky Blue | `#0ea5e9` | Internal Research Environment |
| Violet | `#8b5cf6` | External Collaborative Research |
| Amber | `#f59e0b` | De-Identified (PHI-Free) |
| Teal | `#14b8a6` | Self-Service Analytics |

#### Edge Type Legend

| Color | Style | Meaning |
|-------|-------|---------|
| `#818cf8` Indigo | Solid | Primary data flow |
| `#6b7a99` Grey | Dashed `5,4` | Secondary input |
| `#f59e0b` Amber | Solid | De-identification transform |
| `#14b8a6` Teal | Dashed `7,4` | Self-service access |
| `#34d399` Green | Dashed `3,5` | Cohort extract |
| `#a78bfa` Violet | Solid | Federation / collaboration |

#### Standards Watermark

The visualization includes a footer watermark:
```
OMOP · PCORNet · i2b2 · HL7 FHIR · HIPAA Safe Harbor · Expert Determination
```

#### No PHI Declaration

This visualization contains:
- ❌ No patient data
- ❌ No PHI
- ❌ No institution-specific configurations
- ✅ Only generic, industry-standard classification labels

---

## Adding Visualizations

To add new visualizations to this directory:
1. Use only generic, non-PHI labels
2. Reference industry standards in node metadata
3. Include the standards watermark
4. Test in Chrome, Firefox, and Safari
5. Open a PR with `diagram` type in the commit message
