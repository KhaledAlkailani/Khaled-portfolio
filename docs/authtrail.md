# AuthTrail

Small offline SSH authentication log triage tool. It parses common OpenSSH syslog lines, groups failures by source IP, and highlights a successful login after failed attempts for the same user and IP.

```bash
python tools/authtrail.py examples/auth.log --year 2026
python tools/authtrail.py examples/auth.log --year 2026 --threshold 3 --window 5
```

**Evidence:** each alert contains source line references and a timestamp. The bundled example has five failures followed by a successful login.

**Limits:** only common SSHD log patterns are supported; classic syslog lines have no year or timezone, and logs around New Year need special care. A failed-login burst may be normal operational activity. This is triage, not account-compromise confirmation.
