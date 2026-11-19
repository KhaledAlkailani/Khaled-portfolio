"""Offline SSH log triage. Accepts common OpenSSH auth.log records."""
import argparse
import json
import re
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path

LOG = re.compile(r"^(?P<date>[A-Z][a-z]{2}\s+\d{1,2}\s+\d\d:\d\d:\d\d)\s+\S+\s+sshd(?:\[\d+\])?: (?P<msg>.*)$")
FAIL = re.compile(r"^Failed \S+ for (?:invalid user )?(?P<user>\S+) from (?P<ip>[\da-fA-F:.]+) port \d+")
OK = re.compile(r"^Accepted \S+ for (?P<user>\S+) from (?P<ip>[\da-fA-F:.]+) port \d+")

def parse(text, year):
    events = []
    for number, line in enumerate(text.splitlines(), 1):
        record = LOG.match(line)
        if not record:
            continue
        fail = FAIL.match(record["msg"])
        success = OK.match(record["msg"]) if not fail else None
        if not (fail or success):
            continue
        try:
            stamp = datetime.strptime(f"{year} {record['date']}", "%Y %b %d %H:%M:%S")
        except ValueError:
            continue
        match = fail or success
        events.append(dict(time=stamp, action="failed" if fail else "accepted",
                           user=match["user"], ip=match["ip"], line=number))
    return sorted(events, key=lambda e: (e["time"], e["line"]))

def analyze(events, threshold=5, minutes=10):
    if threshold <= 0 or minutes <= 0:
        raise ValueError("threshold and minutes must be positive")
    windows = defaultdict(deque)
    active = set()
    alerts = []
    for event in events:
        ip = event["ip"]
        window = windows[ip]
        while window and event["time"] - window[0]["time"] > timedelta(minutes=minutes):
            window.popleft()
        if event["action"] == "failed":
            window.append(event)
            if len(window) >= threshold and ip not in active:
                alerts.append(dict(type="possible_bruteforce", ip=ip,
                                   timestamp=event["time"].isoformat(),
                                   failed_attempts=len(window),
                                   source_lines=[x["line"] for x in window]))
                active.add(ip)
            elif len(window) < threshold:
                active.discard(ip)
        else:
            related = [x for x in window if x["user"] == event["user"]]
            if related:
                alerts.append(dict(type="success_after_failures", ip=ip,
                                   user=event["user"], timestamp=event["time"].isoformat(),
                                   preceding_failures=len(related),
                                   source_lines=[x["line"] for x in related] + [event["line"]]))
    return dict(summary=dict(parsed_events=len(events),
                             failed_logins=sum(e["action"] == "failed" for e in events),
                             successful_logins=sum(e["action"] == "accepted" for e in events),
                             alerts=len(alerts)),
                alerts=alerts,
                note="Heuristic for triage; investigate context before drawing conclusions.")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("logfile", type=Path)
    p.add_argument("--year", type=int, default=datetime.now().year)
    p.add_argument("--threshold", type=int, default=5)
    p.add_argument("--window", type=int, default=10)
    args = p.parse_args()
    try:
        output = analyze(parse(args.logfile.read_text(encoding="utf-8"), args.year),
                         args.threshold, args.window)
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
