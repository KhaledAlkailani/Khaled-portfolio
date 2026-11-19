"""Offline IOC matcher for IP, CIDR, and domain values in CSV events."""
import argparse
import csv
import ipaddress
import json
from pathlib import Path

COLUMNS = ("timestamp", "src_ip", "dst_ip", "domain", "event")

def load_indicators(text):
    indicators = []
    for number, raw in enumerate(text.splitlines(), 1):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        kind, sep, value = raw.partition(":")
        kind, value = kind.lower().strip(), value.lower().strip()
        try:
            if not sep or kind not in ("ip", "cidr", "domain"):
                raise ValueError("expected ip:, cidr: or domain:")
            if kind == "ip":
                value = str(ipaddress.ip_address(value))
            elif kind == "cidr":
                value = str(ipaddress.ip_network(value, strict=False))
            elif not value or value.startswith(".") or value.endswith(".") or any(
                not label or len(label) > 63 or label.startswith("-") or label.endswith("-") or
                not all(c.isalnum() or c == "-" for c in label)
                for label in value.split(".")
            ):
                raise ValueError("invalid domain")
        except ValueError as exc:
            raise ValueError(f"Invalid indicator on line {number}: {exc}") from exc
        indicators.append(dict(type=kind, value=value))
    return indicators

def matches(row, indicator):
    kind, value = indicator["type"], indicator["value"]
    if kind == "domain":
        domain = (row.get("domain") or "").strip().lower().rstrip(".")
        return domain == value or domain.endswith("." + value)
    for key in ("src_ip", "dst_ip"):
        try:
            ip = ipaddress.ip_address((row.get(key) or "").strip())
            if kind == "ip" and str(ip) == value:
                return True
            if kind == "cidr" and ip in ipaddress.ip_network(value):
                return True
        except ValueError:
            continue
    return False

def scan(rows, indicators):
    findings = []
    for line, row in enumerate(rows, 2):
        for indicator in indicators:
            if matches(row, indicator):
                findings.append({"row": line, "indicator": indicator,
                                 "event": {name: row.get(name, "") for name in COLUMNS}})
    return {"summary": {"events_scanned": len(rows), "indicators_loaded": len(indicators),
                         "matches": len(findings)}, "matches": findings,
            "note": "Indicator overlap is not proof of malicious activity."}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("events", type=Path)
    p.add_argument("indicators", type=Path)
    args = p.parse_args()
    try:
        indicators = load_indicators(args.indicators.read_text(encoding="utf-8"))
        with args.events.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or any(col not in reader.fieldnames for col in COLUMNS):
                raise ValueError("CSV requires: " + ", ".join(COLUMNS))
            rows = list(reader)
        result = scan(rows, indicators)
    except (OSError, ValueError, csv.Error) as exc:
        p.error(str(exc))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
