# Incident Response Plan — HIPAA Breach Notification SOP

> **Regulatory basis:** 45 CFR §§164.308(a)(6), 164.400–414  
> **COBIT alignment:** DSS02 (Managed Service Requests and Incidents), DSS04 (Managed Continuity)  
> **Review cycle:** Annual, or after any breach or near-miss event

---

## 1. Purpose and Scope

This Incident Response Plan establishes the Standard Operating Procedure (SOP) for detecting, containing, assessing, and reporting security incidents and HIPAA breaches involving electronic protected health information (ePHI).

**Scope:** Applies to all workforce members, contractors, and business associates with access to any system containing or transmitting ePHI.

---

## 2. Incident Response Team

| Role | Responsibility |
|------|--------------|
| **Incident Commander** | Security Officer — Leads response, declares severity level |
| **Privacy Officer** | Determines breach vs. non-breach; leads notification |
| **Legal Counsel** | Reviews notifications; advises on regulatory obligations |
| **IT Security** | Technical containment, forensic evidence preservation |
| **Communications Lead** | Internal and external communications |
| **Executive Sponsor** | C-suite escalation for Severity 1 incidents |

---

## 3. Incident Severity Classification

| Severity | Criteria | Response Time |
|----------|---------|--------------|
| **SEV-1 (Critical)** | Confirmed breach of ≥500 PHI records; ransomware; nation-state attack | Immediate — 1 hour |
| **SEV-2 (High)** | Confirmed breach of <500 PHI records; insider threat confirmed | 4 hours |
| **SEV-3 (Medium)** | Suspected breach; unauthorized access detected; phishing with credential exposure | 24 hours |
| **SEV-4 (Low)** | Policy violation without PHI exposure; near-miss; suspicious activity | 72 hours |

---

## 4. Response Phases

### Phase 1 — Detection & Reporting (Hour 0–24)

**Triggers:** SIEM alert, user report, external notification, audit log anomaly, ransomware indicator

**Actions:**
1. Any workforce member who suspects an incident **must** report immediately to the Security Officer
2. Security Officer documents: discovery date/time, reporter, initial description, systems potentially affected
3. Incident ticket created; evidence preservation initiated (do NOT power off compromised systems)
4. Severity level assigned within 4 hours
5. Incident Response Team assembled

### Phase 2 — Containment (Hour 1–48)

**Actions:**
1. Isolate affected systems from network (without destroying evidence)
2. Revoke compromised credentials
3. Preserve logs: authentication, access, system events (minimum 90-day retention)
4. Forensic image of affected systems before remediation
5. Document all containment actions with timestamps

### Phase 3 — Risk Assessment (Day 2–15)

Conduct the **4-Factor HIPAA Risk Assessment** (45 CFR §164.402):

| Factor | Questions to Answer |
|--------|-------------------|
| **1. Nature and extent** | What PHI types were involved? How many individuals? What identifiers? |
| **2. Unauthorized recipient** | Who received the data? Are they obligated to protect it? |
| **3. Acquisition/viewing** | Was the PHI actually accessed or just potentially exposed? |
| **4. Mitigation** | Was the data retrieved? Was recipient trustworthy? |

**Determination:**
- If all 4 factors support low probability of compromise → **Not a breach** (document rationale; retain 6 years)
- Otherwise → **Breach confirmed** → proceed to Phase 4

### Phase 4 — Notification (Day 15–60)

**Milestone tracking:**

```
Day 0  ──── Incident Discovery
Day 15 ──── Breach determination complete
Day 30 ──── Affected individuals identified
Day 45 ──── Notifications drafted and approved by Legal
Day 60 ──── All notifications sent (HARD DEADLINE)
```

**Notification actions:**
1. **Individuals** — Written notification per 45 CFR §164.404
2. **HHS** — Online portal submission per 45 CFR §164.408
3. **Media** (if ≥500 in jurisdiction) — Press release per 45 CFR §164.406
4. **Business Associates** — If BA caused breach, they notify CE; CE notifies individuals

### Phase 5 — Recovery & Remediation (Day 30–90)

1. Patch or replace compromised systems
2. Reset all potentially compromised credentials
3. Restore from verified clean backups
4. Enhanced monitoring for 90 days post-incident
5. Verify no persistence mechanisms remain

### Phase 6 — Post-Incident Review (Day 60–90)

1. Root cause analysis (5-Whys or Fishbone)
2. Update policies and procedures based on lessons learned
3. Update risk register
4. Retrain affected workforce members
5. Brief executive leadership and data governance committee
6. Retain all incident documentation ≥6 years (45 CFR §164.530(j))

---

## 5. Evidence Preservation

All the following must be preserved and protected from modification:
- System and application logs (authentication, access, error)
- Network flow logs
- Email headers and message metadata
- Physical access logs
- Any external communications related to the incident

Logs must be cryptographically signed or stored in write-once storage to ensure chain of custody.

---

## 6. Testing

This incident response plan must be tested:
- **Annual tabletop exercise** — Simulate a breach scenario with full IR team
- **Quarterly communication test** — Verify all team contact information is current
- **After any actual incident** — Update plan based on gaps identified

---

## 7. Contact Directory

*(To be populated by implementing organization)*

| Role | Name | Primary Contact | Backup Contact |
|------|------|----------------|---------------|
| Security Officer | [TBD] | [TBD] | [TBD] |
| Privacy Officer | [TBD] | [TBD] | [TBD] |
| Legal Counsel | [TBD] | [TBD] | [TBD] |
| HHS OCR Hotline | N/A | 1-800-368-1019 | ocrportal.hhs.gov |
| FBI Cyber Division | N/A | 1-855-292-3937 | ic3.gov |
