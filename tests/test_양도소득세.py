from dataclasses import asdict
from datetime import date
from decimal import Decimal
from unittest import TestCase

from opentaxkr.ers import detect_report_type
from opentaxkr.ers.util import ZERO
from opentaxkr.ers.양도소득_개인지방소득세.records_20230703 import 양도소득_개인지방소득세신고
from opentaxkr.ers.양도소득세 import 양도소득_과세구분, 자산의종류, 주식종류코드, 취득유형
from opentaxkr.ers.양도소득세.records_20230502 import TI06_주식양도소득금액_계산명세, 양도소득세신고
from opentaxkr.models import 세무대리인, 납세자


class Test주식양도소득세신고(TestCase):
    maxDiff = None

    def test_주식양도소득세신고(self):
        report = 양도소득세신고(
            납세자(
                납세자ID='123412-1234123',
                납세자명='강감찬',
                홈택스ID='ganggamchan',
                휴대전화번호='01051223344',
                주소='서울시 강남구 선릉로 522, 2001',
                국적코드='KR',
                거주지국가코드='KR'
            ),
            과세기간=date(2023, 1, 1),
            세무대리인_obj=세무대리인(
                대표자주민등록번호='',
                법인등록번호='1101710104593',
                대표자성명='',
                전화번호='021234567',
                사업자등록번호='5158612345',
                관리번호='W98765',
                성명='김은부',
                생년월일='19800101',
                홈택스ID='kimunbu',
            ),
            작성일자=date(2024, 4, 5),
            제출일자=date(2024, 4, 4),
        )

        report.TI06_주식양도소득금액_계산명세.append(TI06_주식양도소득금액_계산명세(
            과세구분=양도소득_과세구분.과세.value,  # TODO
            주식종목명='해외주식',
            사업자등록번호='',  # TODO 국내주식은 입력 필요
            자산의종류=자산의종류.비상장주식_중소기업외_2018귀속_이후_대주주제외_국외주식_기타_.value,  # TODO
            주식종류코드=주식종류코드.국외주식등_중소기업외법인.value,  # TODO
            취득유형=취득유형.매매.value,  # TODO
            취득유형별양도주식수=Decimal(0),  # TODO
            양도일자='20231231',
            주당양도가액=0,  # TODO
            양도가액=10_000_000,
            취득일자='20220101',
            주당취득가액=0,  # TODO
            취득가액=5_000_000,
            필요경비=1_000_000,
            과세대상양도소득금액=4_000_000,
            감면소득금액=0,  # TODO
            감면종류='ZZZ',  # TODO
            감면율=ZERO,  # TODO
            자동계산불러오기구분값='1',
            국내외구분='1',
            소재지국='US',
            소재지국명='미국',
            ISIN코드='',  # 국외 필수 입력
            ISIN코드구분='C',  # 국외는 C
            필요경비신고자료일련번호=0,  # 필요경비가 0인 경우. 필요경비가 존재하는 경우 취득가액및필요경비계산상세명세서의 3번항목
            과세이연_여부='ZZ',
            전체양도소득금액=1000,
            비과세양도소득금액=0,
        ))
        report.TI06_주식양도소득금액_계산명세.append(TI06_주식양도소득금액_계산명세(
            과세구분=양도소득_과세구분.과세.value,
            주식종목명='해외주식',
            사업자등록번호='',  # TODO 국내주식은 입력 필요
            자산의종류=자산의종류.비상장주식_중소기업외_2018귀속_이후_대주주제외_국외주식_기타_.value,
            주식종류코드=주식종류코드.국외주식등_중소기업외법인.value,
            취득유형=취득유형.매매.value,
            취득유형별양도주식수=Decimal(0),
            양도일자='2023-12-31',
            주당양도가액=0,
            양도가액=10_000_000,
            취득일자='20220101',
            주당취득가액=0,  # TODO
            취득가액=6_000_000,
            필요경비=5_000_000,
            과세대상양도소득금액=-1_000_000,
            감면소득금액=0,  # TODO
            감면종류='ZZZ',  # TODO
            감면율=ZERO,  # TODO
            자동계산불러오기구분값='1',
            국내외구분='1',
            소재지국='US',
            소재지국명='미국',
            ISIN코드='',  # 국외 필수 입력
            ISIN코드구분='C',  # 국외는 C
            필요경비신고자료일련번호=0,  # 필요경비가 0인 경우. 필요경비가 존재하는 경우 취득가액및필요경비계산상세명세서의 3번항목
            과세이연_여부='ZZ',
            전체양도소득금액=1000,
            비과세양도소득금액=0,
        ))

        report.calculate()

        with open('samples/양도소득세_C116300.01', 'rb') as f:
            data = f.read()
            # 샘플 파일에 빠진 정보를 채워서 테스트 통과시키기
            expected = detect_report_type(data).parse(data.splitlines())
            expected[1]['도로명_도로명코드'] = '116803122006'
            expected[1]['도로명_읍면동일련번호'] = '04'
            expected[1]['도로명_지하만있는건물구분'] = '0'
            self.assertEqual(expected, report.serialize())

        with open('samples/양도소득세_지방소득세_C116300.Y11', 'rb') as f:
            data = f.read()
            expected = detect_report_type(data).parse(data.splitlines())

            self.assertEqual(expected, 양도소득_개인지방소득세신고(report).serialize())