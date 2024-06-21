from datetime import date
from pathlib import Path

from opentaxkr.ers.docparser import parse_to_classes


parse_to_classes('개인지방소득세(양도소득)_파일레이아웃_v1.2.3_20230703.html',
                 Path(__file__).parent, 'LI', date(2023, 7, 3))