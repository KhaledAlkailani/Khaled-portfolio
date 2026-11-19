# Scope and limitations

All bundled logs and indicators are synthetic; example IPs are taken from documentation ranges.

- **AuthTrail:** offline and heuristic; OpenSSH/syslog formats and timestamps vary. No account reputation, baselining, or production alert suppression.
- **HeaderGuard:** checks basic response-header presence and one exact `nosniff` value, not overall web-app security. Live mode sends one HEAD request; redirects may be followed by the HTTP library.
- **IOCSweep:** local CSV and local IOC file only; no enrichment, indicator freshness scoring, or SIEM integration.

Run the remote-header option only for endpoints you own or have permission to assess. Do not add credentials, real customer data, tokens or raw production logs to this public repository.

Automated unit tests cover representative cases, not every input or deployment scenario.
