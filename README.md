# Khaled AlKailani

**Cybersecurity · Security operations, engineering & testing**  
Based in Jordan

I'm a cybersecurity graduate with 440 hours of practical training through **Nashama Cyber 12**, delivered through Jordan's National Cyber Security Center.

The work I enjoy most is connecting the technical details: how an attack path developed, what the logs and system artifacts can actually prove, and whether a defensive change held up when tested again.

This repository is an index of my security investigations and a home for a few small Python tools. The projects are intentionally documented with their evidence, limitations, and reproducible steps.

## Selected work

### [Two-server assessment — from attack path to validated remediation](https://github.com/KhaledAlkailani/cybersecurity-capstone-attack-to-validation)
**Security assessment · incident reconstruction · Linux · remediation**

Assessed two servers running web applications and file-sharing services. Documented eight findings across two attack paths, reconstructed activity using logs and packet evidence, and recorded the remediation and retesting process.

**What to look at:** attack paths, root-cause analysis, and the before/after validation results.

### [TwoMillion — security assessment](https://github.com/KhaledAlkailani/TwoMillion-Security-Assessment)
**Web/API testing · broken access control · command injection · Linux**

An authorized Hack The Box assessment showing how individual weaknesses combined into a full compromise. The write-up focuses on the authorization failure, command-execution root cause, impact, and practical remediation.

**What to look at:** the sequence of findings and why each weakness mattered to the next step.

### [JobApplicant — Windows forensic investigation](https://github.com/KhaledAlkailani/J0bApplic-nt)
**DFIR · IIS/Windows logs · NTFS · Python**

An investigation into suspicious activity in a Windows environment. Correlated web, event-log, and filesystem artifacts; explored NTFS MFT record fixup and attribute parsing to work with evidence that was no longer available as a normal file.

**What to look at:** evidence correlation and the filesystem analysis approach. The public write-up does not publish challenge answers.

## Small tools

These are deliberately narrow utilities rather than attempts to recreate a SIEM or vulnerability scanner. Each accepts local sample data, produces structured output, and has unit tests.

| Tool | What it does | Read more |
| --- | --- | --- |
| **AuthTrail** | Flags bursts of failed SSH logins and correlates a later success from the same IP and username. | [Notes](docs/authtrail.md) · [Code](tools/authtrail.py) |
| **HeaderGuard** | Reviews common HTTP response security headers, with an offline mode and an optional single HEAD request. | [Notes](docs/headerguard.md) · [Code](tools/headerguard.py) |
| **IOCSweep** | Matches IP addresses, CIDR ranges and domains against a local CSV event export, retaining source row references. | [Notes](docs/iocsweep.md) · [Code](tools/iocsweep.py) |

### Try them

Python 3.10+; no external packages required.

```bash
git clone https://github.com/KhaledAlkailani/Khaled-portfolio.git
cd Khaled-portfolio

python tools/authtrail.py examples/auth.log --year 2026
python tools/headerguard.py --headers-file examples/response-headers.txt --https
python tools/iocsweep.py examples/events.csv examples/indicators.txt

python -m unittest discover -s tests -v
```

For example, AuthTrail's synthetic SSH log produces **two leads**: a burst of five failed logins and a successful login afterward. The JSON output includes the source line numbers so each observation can be checked against the input.

See the [technical limitations](docs/limitations.md) before using results for any real-world security decision.

## Practice platforms

- [TryHackMe — VAnTAB](https://tryhackme.com/p/VAnTAB)
- **Hack The Box:** [TwoMillion assessment](https://github.com/KhaledAlkailani/TwoMillion-Security-Assessment) · [JobApplicant investigation](https://github.com/KhaledAlkailani/J0bApplic-nt)

## Scope

The assessments above were conducted in authorized environments. The bundled inputs are synthetic and use documentation IP ranges. Tool findings are **investigative leads**, not proof of compromise or a production security assessment.

The code, tests, sample inputs, and notes are public so the claims here can be checked rather than taken on trust.
