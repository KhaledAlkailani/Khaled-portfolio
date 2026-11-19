# HeaderGuard

A lightweight HTTP response-header reviewer. Runs offline on a captured header block or makes one HEAD request to an authorized URL.

```bash
python tools/headerguard.py --headers-file examples/response-headers.txt --https
# Only on authorized endpoints:
python tools/headerguard.py --url https://example.org
```

Reviews CSP presence, nosniff, referrer policy, frame restrictions, and HSTS on HTTPS. The output intentionally says **review** rather than declaring an application vulnerable.

**Limits:** response-header presence does not prove a policy is safe. CSP syntax, actual directives, redirect paths, application behavior, and browser interpretation require deeper investigation. Servers that reject HEAD require an offline header capture.
