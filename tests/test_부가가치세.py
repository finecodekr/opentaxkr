import unittest

from opentaxkr.ers.부가가치세 import 부가가치세신고


class Test부가가치세(unittest.TestCase):
    def test_과세기간(self):
        부가가치세신고()