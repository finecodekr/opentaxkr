import unittest
from datetime import date

from opentaxkr.ers import 양도소득세
from opentaxkr.ers.양도소득세 import records_20200224, records_20230502, 양도소득세신고


class TestERSReport(unittest.TestCase):
    maxDiff = None

    def test_find_class(self):
        self.assertEqual(records_20200224.양도소득세신고, 양도소득세신고.as_of(date(2022, 1, 1)))
        self.assertEqual(records_20230502.양도소득세신고, 양도소득세신고.as_of(date(2024, 1, 1)))
        self.assertRaises(ValueError, 양도소득세신고.as_of, date(2019, 1, 1))


class TestParsingERS(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        with open('samples/양도소득세_C116300.01', 'rb') as f:
            cls.lines = f.readlines()

    def test_match_record_class(self):
        self.assertTrue(양도소득세.TI01_양도소득세과세표준신고서_HEADER.match(self.lines[0]))
        self.assertFalse(양도소득세.TI02_양도소득세과세표준신고서_기본사항.match(self.lines[0]))
        self.assertTrue(양도소득세.TI03_양도소득과세표준신고서_세율별내역.match(self.lines[2]))

    def test_find_matching_record(self):
        self.assertEqual(양도소득세.TI01_양도소득세과세표준신고서_HEADER, 양도소득세신고.find_record_class(self.lines[0]))
        self.assertEqual(양도소득세.TI02_양도소득세과세표준신고서_기본사항, 양도소득세신고.find_record_class(self.lines[1]))

    def test_parse_record(self):
        self.assertEqual('강감찬', 양도소득세신고.parse_record(self.lines[0]).성명)

    def test_parse_ers_file_and_serialize_back(self):
        with open('samples/양도소득세_C116300.01', 'rb') as f:
            report = 양도소득세신고.parse(f)
            self.assertEqual('강감찬', report.TI01_양도소득세과세표준신고서_HEADER[0].성명)

            f.seek(0)
            self.assertListEqual(f.read().splitlines(), report.serialize().splitlines())