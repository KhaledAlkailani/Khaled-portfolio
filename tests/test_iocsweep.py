import unittest
from tools.iocsweep import load_indicators, matches, scan

class IOCSweepTests(unittest.TestCase):
    def test_exact_ip(self):
        self.assertFalse(matches({"src_ip":"203.0.113.100"},{"type":"ip","value":"203.0.113.10"}))
    def test_cidr(self):
        self.assertTrue(matches({"dst_ip":"198.51.100.20"},{"type":"cidr","value":"198.51.100.0/24"}))
    def test_domain_boundary(self):
        i = {"type":"domain","value":"bad.example"}
        self.assertTrue(matches({"domain":"api.bad.example"}, i))
        self.assertFalse(matches({"domain":"notbad.example"}, i))
    def test_invalid(self):
        with self.assertRaises(ValueError):
            load_indicators("ip:bad-ip")
