from datetime import datetime, date
from typing import BinaryIO

from opentaxkr.ers.report import 전자신고서식


class 양도소득_개인지방소득세신고서식(전자신고서식):
    module = '양도소득세'
    report_date_field = '작성일자'

    def extract_기준일자(self, data: BinaryIO):
        return datetime.strptime(self.extract_field(
            self.find_field('TI01_양도소득세과세표준신고서_HEADER', self.report_date_field), data
        ),'%Y%m%d').date()

    @staticmethod
    def 주택임대사업자_업종코드():
        return [701101, 701102, 701103, 701104, 701301]

    def filename(self, first_record):
        return f"{date.today().strftime('%Y%m%d')}{first_record['서식코드']}.{first_record.get('세목구분코드')}"


양도소득_개인지방소득세신고서식.load_histories()
