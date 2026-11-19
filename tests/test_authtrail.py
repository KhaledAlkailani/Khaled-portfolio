import unittest
from datetime import datetime, timedelta
from tools.authtrail import parse, analyze

class AuthTrailTests(unittest.TestCase):
    def test_parse(self):
        row = "Nov 19 09:00:10 host sshd[1]: Failed password for admin from 203.0.113.20 port 53001 ssh2"
        events = parse(row, 2026)
        self.assertEqual(events[0]["ip"], "203.0.113.20")
    def test_burst(self):
        t = datetime(2026, 11, 19)
        rows = [dict(time=t + timedelta(seconds=i), action="failed", user="admin", ip="203.0.113.20", line=i+1) for i in range(5)]
        self.assertEqual(analyze(rows)["alerts"][0]["type"], "possible_bruteforce")
    def test_success_correlation(self):
        t = datetime(2026, 11, 19)
        rows = [dict(time=t, action="failed", user="admin", ip="203.0.113.20", line=1),
                dict(time=t + timedelta(seconds=5), action="accepted", user="admin", ip="203.0.113.20", line=2)]
        self.assertEqual(analyze(rows)["alerts"][0]["type"], "success_after_failures")
    def test_window_expiration(self):
        t = datetime(2026, 11, 19)
        rows = [dict(time=t + timedelta(minutes=i*30), action="failed", user="admin", ip="203.0.113.20", line=i+1) for i in range(5)]
        self.assertFalse(analyze(rows)["alerts"])
