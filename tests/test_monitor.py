import unittest
from monitoramento import check_site

class TestMonitor(unittest.TestCase):
    def test_site_online(self):
        self.assertTrue(check_site("https://example.com"))

    def test_site_offline(self):
        self.assertFalse(check_site("https://invalid-site-xyz123.com"))

if __name__ == "__main__":
    unittest.main()