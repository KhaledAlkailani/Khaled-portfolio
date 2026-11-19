import unittest
from tools.headerguard import parse, audit

class HeaderGuardTests(unittest.TestCase):
    def test_normalization(self):
        self.assertEqual(parse("HTTP/1.1 200 OK\nX-Content-Type-Options: nosniff\n")["x-content-type-options"], "nosniff")
    def test_missing(self):
        self.assertEqual(audit({}, https=True)["review_needed"], 5)
    def test_http_excludes_hsts(self):
        self.assertEqual(len(audit({}, https=False)["results"]), 4)
    def test_present(self):
        h = {"Content-Security-Policy":"frame-ancestors 'none'", "X-Content-Type-Options":"nosniff",
             "Referrer-Policy":"no-referrer","Strict-Transport-Security":"max-age=123"}
        self.assertEqual(audit(h)["review_needed"], 0)
