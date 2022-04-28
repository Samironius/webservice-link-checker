
import unittest
from main import geturls


class UnitTests(unittest.TestCase):
    def test_google_unblock(self):
        self.assertEqual(geturls("google.com"), 'unblocked')

    def test_google_block(self):
        self.assertEqual(geturls("googlle.com"), 'blocked')

    def test_google_block2(self):
        self.assertEqual(geturls("google.com:443/search"), 'blocked')

if __name__ == '__main__':
    unittest.main()