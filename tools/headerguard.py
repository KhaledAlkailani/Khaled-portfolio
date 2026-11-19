"""Review security-related HTTP response headers (offline by default)."""
import argparse
import json
from email.parser import Parser
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def parse(text):
    lines = text.splitlines()
    if lines and lines[0].startswith("HTTP/"):
        lines.pop(0)
    return {k.lower(): v.strip() for k,v in Parser().parsestr("\n".join(lines), headersonly=True).items()}

def audit(headers, https=True):
    h = {k.lower(): v.strip() for k,v in headers.items()}
    csp = h.get("content-security-policy", "")
    checks = {
        "Content-Security-Policy": bool(csp),
        "X-Content-Type-Options: nosniff": h.get("x-content-type-options", "").lower() == "nosniff",
        "Referrer-Policy": bool(h.get("referrer-policy")),
        "Frame restrictions": bool(h.get("x-frame-options")) or "frame-ancestors" in csp.lower(),
    }
    if https:
        checks["Strict-Transport-Security"] = bool(h.get("strict-transport-security"))
    return {"results": [{"control": k, "status": "present" if v else "review"} for k,v in checks.items()],
            "review_needed": sum(not value for value in checks.values()),
            "note": "Presence does not establish effectiveness. Review header values and application context."}

def remote(url):
    target = urlparse(url)
    if target.scheme not in ("http", "https") or not target.hostname:
        raise ValueError("Expected an http:// or https:// URL")
    request = Request(url, method="HEAD", headers={"User-Agent": "HeaderGuard/1.0"})
    try:
        with urlopen(request, timeout=5) as response:
            return dict(response.headers.items()), urlparse(response.geturl()).scheme == "https"
    except HTTPError as exc:
        if exc.code == 405:
            raise ValueError("HEAD unsupported; use --headers-file") from exc
        return dict(exc.headers.items()), target.scheme == "https"
    except URLError as exc:
        raise ValueError(str(exc.reason)) from exc

def main():
    p = argparse.ArgumentParser(description=__doc__)
    inputs = p.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--headers-file", type=Path)
    inputs.add_argument("--url", help="Only inspect sites you own or are authorized to assess")
    p.add_argument("--https", action="store_true", help="Treat offline headers as HTTPS")
    args = p.parse_args()
    try:
        if args.headers_file:
            headers, https = parse(args.headers_file.read_text(encoding="utf-8")), args.https
        else:
            headers, https = remote(args.url)
        result = audit(headers, https)
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
