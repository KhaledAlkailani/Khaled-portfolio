# IOCSweep

Matches a local list of IP, CIDR, and domain indicators against CSV events. Reports the indicator and original CSV row for follow-up.

```bash
python tools/iocsweep.py examples/events.csv examples/indicators.txt
```

Indicator file syntax: `ip:203.0.113.50`, `cidr:198.51.100.0/24`, or `domain:bad.example`. Domain indicators match the exact domain or a subdomain (not arbitrary substrings). IP and CIDR indicators match `src_ip` and `dst_ip`.

**Limits:** this is exact and domain-suffix correlation, not threat intelligence enrichment. It assumes a specific CSV schema and does not normalize every possible telemetry format. Matches can be benign and must be validated.
