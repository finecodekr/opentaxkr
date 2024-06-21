from datetime import datetime
from typing import BinaryIO

from .records_20230703 import *


def detect_report_date(data: BinaryIO):
    return datetime.strptime(
        LI01_양도소득_과세표준확정신고_HEADER.extract_field(LI01_양도소득_과세표준확정신고_HEADER.fields()['적용서식'], data), 
        '%Y%m%d').date()
