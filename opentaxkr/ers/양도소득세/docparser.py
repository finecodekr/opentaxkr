from datetime import date
from pathlib import Path

from opentaxkr.ers.docparser import parse_to_classes


parse_to_classes('양도소득세 전자신고 파일설명서_V5.8_(20200224).htm', Path(__file__).parent, 'TI', date(2020, 2, 24))
parse_to_classes('양도소득세 전자신고 파일설명서_V5.13_(20230502).htm', Path(__file__).parent, 'TI', date(2023, 5, 2))
