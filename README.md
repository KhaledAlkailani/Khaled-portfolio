<div align="center">

<img src="assets/portfolio-banner.svg" alt="Khaled AlKailani cybersecurity portfolio" width="100%">

</div>

---

## Start with the work

This portfolio is built around **inspectable security work**.

Not a long list of tools.  
Not self-rated skill bars.  
Not claims that cannot be checked.

The projects below show how I approach security problems: reconstruct the technical story, separate evidence from assumption, identify the root cause, and verify whether the fix actually changed the outcome.

<div align="center">

<img src="assets/proof-of-work.svg" alt="Evidence at a glance" width="100%">

</div>

---

# Featured Case Study

## [Attack to Validation](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation)

**Offensive Security · DFIR · Linux · Application Security · Remediation Validation**

> **2 servers · 8 findings · 2 connected attack paths · 8 validated remediations**

A two-server security assessment that continued beyond vulnerability discovery.

The offensive phase established how the weaknesses could be reached and chained. The defensive phase then reconstructed the same activity using **service logs, Apache logs, packet evidence, filesystem artifacts, application source, and container metadata**.

Each finding was traced to a root cause, remediated, and retested against the original behavior.

<div align="center">

<img src="assets/WhatsApp%20Image%20main.jpeg" alt="Khaled AlKailani presenting the Attack to Validation cybersecurity capstone" width="92%">

<br>

<sub>During the capstone discussion, presenting the two-server assessment and explaining the attack paths before the National Cyber Security Center panel.</sub>

</div>

### What can be inspected

| Evidence | What it demonstrates |
|---|---|
| [Attack paths](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation/blob/main/docs/attack-paths.md) | How separate weaknesses connected into larger compromise paths |
| [Timeline](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation/blob/main/docs/timeline.md) | Reconstruction from timestamps and multiple evidence sources |
| [Root-cause analysis](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation/blob/main/docs/root-cause-analysis.md) | Why the findings existed, not only what was vulnerable |
| [Remediation & validation](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation/blob/main/docs/remediation-and-validation.md) | Whether the original impact still worked after the fix |
| [Scope & limitations](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation/blob/main/docs/scope-and-limitations.md) | Where the evidence stops and where claims should stop too |

**Project:** [Open the repository →](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation)

---

# Additional Case Studies

<table>
<tr>
<td width="50%" valign="top">

## [TwoMillion Security Assessment](https://github.com/KhaledAlkailani/TwoMillion-Security-Assessment)

**Web / API Security · Authorization · Command Injection · Linux**

An authorized Hack The Box assessment documenting how multiple weaknesses combined into a larger attack path.

The write-up focuses on the sequence between findings, the security control that failed, and practical remediation rather than treating each vulnerability as an isolated screenshot.

**Signals in the work**
- Web and API testing
- Authorization analysis
- Attack-path reasoning
- Technical finding documentation
- Remediation thinking

</td>
<td width="50%" valign="top">

## [JobApplicant — Windows Forensic Investigation](https://github.com/KhaledAlkailani/J0bApplic-nt)

**DFIR · IIS / Windows Logs · NTFS · Filesystem Analysis · Python**

A forensic investigation into suspicious activity in a Windows environment.

The analysis correlates web, host, and filesystem evidence, then goes deeper into NTFS structures when the relevant evidence is no longer available as a normal file.

**Signals in the work**
- Evidence correlation
- Windows forensic reasoning
- IIS and host-log analysis
- NTFS / MFT investigation
- Working from incomplete evidence

</td>
</tr>
</table>

---

## [Vulnerability Management Procedure](https://github.com/KhaledAlkailani/vulnerability-management-procedure)

**GRC · Vulnerability Management · Risk Treatment · ISO/IEC 27001:2022**

A practical governance procedure for managing technical vulnerabilities from identification through verified closure.

The project defines scanning cadence, remediation ownership, severity-based deadlines, risk exceptions, technical verification, and management reporting. It also includes operational templates for a vulnerability register and risk-exception requests.

**Signals in the work**
- Vulnerability-management lifecycle design
- Remediation SLAs and escalation logic
- RACI-style ownership model
- Risk-exception governance
- Verification-before-closure principle
- ISO/IEC 27001:2022 Annex A 8.8 mapping

**Project:** [Open the repository →](https://github.com/KhaledAlkailani/vulnerability-management-procedure)

---

## [OverTheWire Bandit — Linux Security Journey](https://github.com/KhaledAlkailani/bandit-linux-security-journey)

**Linux · Networking · Privilege · Automation · Git Security**

A spoiler-safe documentation project built from completing the OverTheWire Bandit progression through Level 33.

Instead of publishing passwords or challenge answers, the repository reorganizes the work into practical security capabilities: Linux fundamentals, data analysis, networking, privilege boundaries, cron and automation, restricted environments, and Git history.

**Signals in the work**
- Practical Linux command-line fluency
- SSH, local services, TLS, and service discovery
- SUID and execution-context reasoning
- Cron and scheduled-task analysis
- Restricted-shell and forced-program behavior
- Git history, branches, tags, and hooks
- Learning documentation that separates concepts from answers

**Project:** [Open the repository →](https://github.com/KhaledAlkailani/bandit-linux-security-journey)

---

## [MD5 Collision Lab](https://github.com/KhaledAlkailani/md5-collision-lab)

**Cryptography Fundamentals · Linux · C++ Build Troubleshooting · Binary Analysis**

A hands-on FastColl experiment that turns the abstract concept of an MD5 collision into an independently verified result.

The lab documents the full path from source compilation and dependency troubleshooting to collision generation and binary-level verification.

**Signals in the work**
- Diagnosing missing Boost dependencies and compatibility issues
- Compiling a C++ security tool on Kali Linux
- Generating two distinct files with the same MD5 digest
- Verifying the result independently with `md5sum`, `cmp` / `diff`, `strings`, and `xxd`
- Distinguishing collision resistance from unrelated concepts such as encryption or preimage recovery

**Project:** [Open the repository →](https://github.com/KhaledAlkailani/md5-collision-lab)

---

## [Security+ SY0-701 — Learning Journey](https://github.com/KhaledAlkailani/security-plus-sy0-701-journey)

**Security Fundamentals · Architecture · Operations · GRC · Scenario Reasoning**

A structured study repository that turns Security+ preparation into inspectable cybersecurity learning rather than a collection of memorized definitions.

The repository organizes the five SY0-701 domains into concept notes, technical comparisons, scenario-based reasoning, progress tracking, and a mistakes-review loop.

**Signals in the work**
- Structured coverage across all five Security+ domains
- Comparisons such as IAM vs PAM, IDS vs IPS, and authentication vs authorization
- Scenario reasoning for incident investigation, firewall troubleshooting, access control, and vulnerability management
- Objective and learning-state tracking
- Exam-integrity approach with no dumps or proprietary live-exam content

**Project:** [Open the repository →](https://github.com/KhaledAlkailani/security-plus-sy0-701-journey)

---

# Working Method

<div align="center">

<img src="assets/how-i-work.svg" alt="Security investigation workflow" width="100%">

</div>

The sequence matters.

A finding is useful.  
A defensible explanation of **what happened, why it happened, and whether the remediation held up** is more useful.

---

# Security Principles I Keep Coming Back To

```text
Open port ≠ vulnerability.

Finding ≠ evidence.

Authentication ≠ authorization.

HTTP 200 ≠ exploit success.

Container root ≠ host root.

Deleting an exposed credential ≠ rotating it.

Patch installed ≠ fix proven.
```

These distinctions look small, but they are where weak technical conclusions often begin.

---

# Areas Represented in the Portfolio

| Area | Evidence in the projects |
|---|---|
| **Security Operations** | Log review, correlation, timelines, investigation reasoning |
| **DFIR** | Host artifacts, filesystem evidence, Windows forensics, packet evidence |
| **Security Engineering** | Hardening, access control, credential handling, remediation validation |
| **Offensive Security** | Enumeration, web/API testing, attack-path development, controlled exploitation |
| **Application Security** | XSS, authorization failures, unsafe input handling, exposed configuration and credentials |
| **Technical Communication** | Findings, root causes, limitations, remediation steps, evidence-backed conclusions |

---

# Training & Practical Experience

## Nashama Cyber 12 — Cybersecurity Practical Training

**440 hours · National Cyber Security Center (NCSC) · Amman**

An intensive hands-on cybersecurity program built around realistic security scenarios, technical labs, and investigation-driven work.

<div align="center">

<p>
  <img src="assets/WhatsApp%20Image%202026-11-19%20at%208.40.42%20PM%20%281%29.jpeg" alt="Nashama Cyber 12 practical training" width="48%">
  <img src="assets/WhatsApp%20Image%202026-11-19%20at%208.40.42%20PM.jpeg" alt="Nashama Cyber 12 practical training" width="48%">
</p>

<p>
  <img src="assets/WhatsApp%20Image%202026-11-19%20at%208.40.43%20PM%20%281%29.jpeg" alt="Nashama Cyber 12 practical training" width="48%">
  <img src="assets/WhatsApp%20Image%202026-11-19%20at%208.40.43%20PM.jpeg" alt="Nashama Cyber 12 practical training" width="48%">
</p>

<sub>Snapshots from the hands-on training environment during Nashama Cyber 12.</sub>

</div>

### Security Operations & Incident Investigation

- Investigated security events, system activity, logs, and network traffic to identify suspicious behavior and reconstruct attack activity.
- Practiced SOC-style monitoring and log analysis using **Splunk** and SIEM concepts.
- Worked through scenarios covering **detection, investigation, containment, remediation, and validation**.
- Applied **MITRE ATT&CK** and **NIST** guidance to structure investigations and document attacker behavior.

### Network, Systems & Security Testing

- Worked across **Windows and Linux** environments at the network, host, and application levels.
- Performed reconnaissance, enumeration, network analysis, and controlled security testing using **Nmap, Wireshark, Burp Suite, and Splunk**.
- Practiced troubleshooting and analysis across **TCP/IP, DNS, HTTP, LAN/WAN, access management, system monitoring, and security controls**.
- Built practical experience in vulnerability assessment, web application security, network security, and remediation verification.

### Documentation & Security Frameworks

- Produced technical reports covering observed activity, supporting evidence, findings, impact, and recommended remediation.
- Used frameworks and methodologies including **MITRE ATT&CK, NIST, and ISO 27001** during practical exercises.
- Developed the habit of separating **finding, evidence, root cause, remediation, and validation** rather than treating them as the same thing.

---

## CyberX — Cybersecurity Internship

**Jun 2025 – Aug 2025 · King Hussein Business Park, Amman**

Worked across cybersecurity research, governance, awareness, and practical security analysis.

### Governance & Regulatory Work

- Researched cybersecurity controls, policies, and regulatory requirements, including Saudi cybersecurity control frameworks and **NCA ECC-related material**.
- Worked with security frameworks and standards including **ISO 27001, NIST CSF, CIS Controls, and NCA ECC**.
- Contributed to policy, procedure, compliance, and security-documentation activities.

### Security Awareness & Training Content

Created and organized cybersecurity awareness and learning material covering topics such as:

`Cybersecurity Risk Management` ·
`Data & Information Protection` ·
`Identity & Access Management` ·
`Information Systems & Processing Facilities` ·
`Mobile Device Security` ·
`Third-Party Cybersecurity`

The work involved translating technical and regulatory security concepts into structured material that could be understood by employees and non-specialist audiences.

### Technical & Investigation Exposure

- Researched digital forensics, cybercrime investigations, digital-evidence handling, preservation, and investigation procedures.
- Used **Wireshark and Nmap** in practical network and security analysis exercises.
- Organized technical findings and converted security concepts into clear documentation and learning material.

---

# Practice Platforms

**TryHackMe:** [VAnTAB](https://tryhackme.com/p/VAnTAB)

**Hack The Box:**  
[TwoMillion Security Assessment](https://github.com/KhaledAlkailani/TwoMillion-Security-Assessment) ·
[JobApplicant Investigation](https://github.com/KhaledAlkailani/J0bApplic-nt)

---

<div align="center">

### Khaled AlKailani

**Cybersecurity · Security Operations · DFIR · Security Engineering**

[GitHub](https://github.com/KhaledAlkailani) · [TryHackMe](https://tryhackme.com/p/VAnTAB)

<br>

<sub>All security assessments referenced here were performed in authorized environments.</sub>

</div>
