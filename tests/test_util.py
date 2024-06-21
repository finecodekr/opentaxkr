import unittest

from opentaxkr.ers.util import deduct


class TestUtil(unittest.TestCase):
    def test_deduct(self):
        self.assertEqual((1_000_000, 1_500_000), deduct(1_000_000, 2_500_000))
        self.assertEqual((0, 2_500_000), deduct(-1_000_000, 2_500_000))