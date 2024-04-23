from itertools import groupby
from typing import List
from decimal import Decimal
from dataclasses import dataclass, field
from opentaxkr.ers import ERSRecord
from opentaxkr.ers import 양도소득세
from opentaxkr.ers.address import 도로명주소
from opentaxkr.ers.util import yn, country_name, deduct
from opentaxkr.ers.양도소득세 import 주식종류코드
from opentaxkr.models import 세무프로그램코드


@dataclass(kw_only=True)
class TI01_양도소득세과세표준신고서_HEADER(ERSRecord):
    자료구분: str = field(default='01', metadata={'max_length': 2, '점검': '01', '비고': 'Not Null'})
    서식코드: str = field(default='C116300', metadata={'max_length': 7, '점검': 'C116300', '비고': 'Not Null'})
    납세자ID: str = field(metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not Null'})
    납세자구분: str = field(metadata={'max_length': 2, '점검': '00, 01, 02~06, 07, 08, 09,', '비고': 'Not Null'})
    세목코드: str = field(metadata={'max_length': 2, '점검': '22', '비고': 'Not Null'})
    신고구분코드: str = field(metadata={'max_length': 2, '점검': '01,03', '비고': 'Not Null'})
    신고유형: str = field(metadata={'max_length': 1, '점검': '1,2,3,4,5,6,7,9', '비고': 'Not Null'})
    과세기간_년월: str = field(metadata={'max_length': 6, '점검': '년월형식점검', '비고': 'Not Null'})
    신고구분상세코드: str = field(metadata={'max_length': 2, '점검': '35', '비고': 'Not Null'})
    신고서종류코드: str = field(metadata={'max_length': 3, '점검': '', '비고': 'Not Null'})
    민원종류코드: str = field(default=None, metadata={'max_length': 5, '점검': 'FD001', '비고': 'Not null'})
    사용자ID: str = field(metadata={'max_length': 20, '점검': '길이점검', '비고': 'Not Null'})
    제출년월: str = field(metadata={'max_length': 6, '점검': '길이점검', '비고': 'Not Null'})
    성명: str = field(metadata={'max_length': 30, '점검': '길이점검', '비고': 'Not Null'})
    은행코드_국세환급금: str = field(default=None, metadata={'max_length': 3, '점검': '은행코드CHECK', '비고': 'Null허용'})
    계좌번호_국세환급금: str = field(default=None, metadata={'max_length': 20, '점검': '길이점검(16자리초과여부)', '비고': 'Null허용'})
    예금종류: str = field(default=None, metadata={'max_length': 20, '점검': '길이점검', '비고': 'Null허용'})
    세무대리대표자주민등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '주민등록번호CHECK', '비고': 'Null허용'})
    세무대리대표자성명: str = field(default=None, metadata={'max_length': 30, '점검': '길이점검', '비고': 'Null허용'})
    세무대리인전화번호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    세무대리사업자등록번호: str = field(default=None, metadata={'max_length': 10, '점검': '사업자번호CHECK+무세적', '비고': 'Null허용'})
    세무대리인관리번호: str = field(default=None, metadata={'max_length': 6, '점검': '길이점검', '비고': 'Null허용'})
    세무프로그램코드: str = field(metadata={'max_length': 4, '점검': '세무프로그램코드점검', '비고': 'Not Null'})
    작성일자: str = field(metadata={'max_length': 8, '점검': '길이점검', '비고': 'Not Null'})
    양도일자: str = field(metadata={'max_length': 8, '점검': '길이점검', '비고': 'Not Null'})
    세무대리인성명: str = field(default=None, metadata={'max_length': 60, '점검': '길이점검', '비고': 'Null 허용'})
    세무대리인생년월일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    공란: str = field(default=None, metadata={'max_length': 47, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI02_양도소득세과세표준신고서_기본사항(ERSRecord):
    자료구분: str = field(default='02', metadata={'max_length': 2, '점검': '02', '비고': 'Not Null'})
    서식코드: str = field(default='C116300', metadata={'max_length': 7, '점검': 'C116300', '비고': 'Not Null'})
    주소_법정동코드: str = field(metadata={'max_length': 10, '점검': '법정동코드점검', '비고': 'Not Null'})
    주소_특수지코드: str = field(default=None, metadata={'max_length': 1, '점검': '0~9', '비고': 'Null 허용'})
    주소_번지: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    주소_호: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    주소_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    주소_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    주소_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    주소_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    주소_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    전화번호: str = field(metadata={'max_length': 12, '점검': '길이점검', '비고': 'Not Null'})
    전자메일주소: str = field(default=None, metadata={'max_length': 50, '점검': '길이점검', '비고': 'Null허용'})
    내외국인여부: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    거주구분: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    거주지국코드: str = field(metadata={'max_length': 3, '점검': '길이점검', '비고': 'Not Null'})
    거주지국명: str = field(metadata={'max_length': 40, '점검': '길이점검', '비고': 'Not Null'})
    도로명_도로명코드: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null 허용'})
    도로명_도로명: str = field(default=None, metadata={'max_length': 80, '점검': '길이점검', '비고': 'Null 허용'})
    도로명_지하만있는건물구분: str = field(default=None, metadata={'max_length': 1, '점검': '0,1', '비고': 'Null 허용'})
    도로명_건물번호_본번: int = field(default=None, metadata={'max_length': 5, '점검': '숫자,길이점검', '비고': 'Null 허용'})
    도로명_건물번호_부번: int = field(default=None, metadata={'max_length': 5, '점검': '숫자,길이점검', '비고': 'Null 허용'})
    도로명_아파트동_도로명: str = field(default=None, metadata={'max_length': 22, '점검': '길이점검', '비고': 'Null 허용'})
    도로명_아파트호_도로명: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null 허용'})
    도로명_읍면동일련번호: str = field(default=None, metadata={'max_length': 2, '점검': '길이점검', '비고': 'Null 허용'})
    국적코드: str = field(metadata={'max_length': 3, '점검': '길이점검', '비고': 'Not Null'})
    공란: str = field(default=None, metadata={'max_length': 51, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI03_양도소득과세표준신고서_세율별내역(ERSRecord):
    자료구분: str = field(default='03', metadata={'max_length': 2, '점검': '03', '비고': 'Not Null'})
    서식코드: str = field(default='C116300', metadata={'max_length': 7, '점검': 'C116300', '비고': 'Not Null'})
    국내외분: str = field(metadata={'max_length': 1, '점검': '1,9,Z', '비고': 'Not Null'})
    세율구분: str = field(metadata={'max_length': 2, '점검': '10,15,20…', '비고': 'Not Null'})
    양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    기신고_결정_경정된양도소득금액_합계: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    양도소득기본공제: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    과세표준: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    세율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 2})
    산출세액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    감면세액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    외국납부세액공제: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    예정신고납부세액공제: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    원천징수세액공제: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    가산세_신고불성실: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    가산세_납부불성실: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    가산세_계: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    기신고_결정_경정세액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    자진납부할_세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    분납할_세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    자진납부세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    농어촌특별세_소득세감면세액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    농어촌특별세_세율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '', '비고': 'Not Null default 0', 'decimal_places': 2})
    농어촌특별세_산출세액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    농어촌특별세_수정신고가산세등: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    농어촌특별세_기신고_결정_경정세액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    농어촌특별세_자진납부할_세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    농어촌특별세_분납할세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    농어촌특별세_자진납부_세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    주민세_소득세자진납부할_세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    주민세_세율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '01000', '비고': 'Not Null default 0', 'decimal_places': 2})
    주민세_산출세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    주민세_자진납부세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    소득감면대상_소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    가산세_기장불성실등: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0 (14)'})
    전자신고세액공제: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 46, '점검': '길이점검', '비고': 'SPACE'})

    def __post_init__(self):
        self.과세표준 = self.양도소득금액 - self.양도소득기본공제
        if self.세율구분 != '00':
            self.산출세액 = self.과세표준 * Decimal(self.세율) / Decimal(100)
        self.자진납부할_세액 = self.산출세액
        self.주민세_세율 = Decimal(10)


@dataclass(kw_only=True)
class TI04_양도소득과세표준신고서_양수인내역(ERSRecord):
    자료구분: str = field(default='04', metadata={'max_length': 2, '점검': '04', '비고': 'Not Null'})
    서식코드: str = field(default='C116300', metadata={'max_length': 7, '점검': 'C116300', '비고': 'Not Null'})
    일련번호: str = field(metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null'})
    양수인_주민사업자구분: str = field(metadata={'max_length': 1, '점검': '1,2', '비고': 'Not Null'})
    양수인_내외국인_구분코드: str = field(metadata={'max_length': 1, '점검': '1,9', '비고': 'Not Null'})
    양수인_주민등록번호: str = field(metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not Null'})
    양수인_성명: str = field(metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not Null'})
    양수인_전화번호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': ''})
    양수인_지분_분자: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    양수인_지분_분모: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    양수인_양도자와의관계: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    공란: str = field(default=None, metadata={'max_length': 24, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI05_양도소득금액_계산명세(ERSRecord):
    자료구분: str = field(default='05', metadata={'max_length': 2, '점검': '05', '비고': 'Not Null'})
    서식코드: str = field(default='C116400', metadata={'max_length': 7, '점검': 'C116400', '비고': 'Not Null'})
    일련번호: str = field(default='1', metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null default 1'})
    과세구분: str = field(metadata={'max_length': 2, '점검': '', '비고': 'Not Null'})
    국내외분_소재지: str = field(metadata={'max_length': 1, '점검': '1', '비고': 'Not Null'})
    세율구분: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    자산의종류: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    소재지_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    거래일자_양도일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    거래일자_양도등기목적: str = field(metadata={'max_length': 6, '점검': '', '비고': 'Not Null'})
    거래일자_양도등기원인: str = field(default=None, metadata={'max_length': 4, '점검': '', '비고': 'Null허용'})
    거래일자_취득일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    거래일자_취득등기목적: str = field(metadata={'max_length': 6, '점검': '', '비고': 'Not Null'})
    거래일자_취득등기원인: str = field(default=None, metadata={'max_length': 4, '점검': '', '비고': 'Null허용'})
    거래자산면적_총면적_토지_면적: Decimal = field(default='0',
                                      metadata={
                                          'max_length': 11,
                                          '점검': '양의실수형식점검',
                                          '비고': 'Not Null default 0',
                                          'decimal_places': 3
                                      })
    거래자산면적_총면적_토지_지분_분자: Decimal = field(default='0',
                                         metadata={
                                             'max_length': 11,
                                             '점검': '양의실수형식점검',
                                             '비고': 'Not Null default 0',
                                             'decimal_places': 3
                                         })
    거래자산면적_총면적_토지_지분_분모: Decimal = field(default='0',
                                         metadata={
                                             'max_length': 11,
                                             '점검': '양의실수형식점검',
                                             '비고': 'Not Null default 0',
                                             'decimal_places': 3
                                         })
    거래자산면적_총면적_건물_면적: Decimal = field(default='0',
                                      metadata={
                                          'max_length': 11,
                                          '점검': '양의실수형식점검',
                                          '비고': 'Not Null default 0',
                                          'decimal_places': 3
                                      })
    거래자산면적_총면적_건물_지분_분자: Decimal = field(default='0',
                                         metadata={
                                             'max_length': 11,
                                             '점검': '양의실수형식점검',
                                             '비고': 'Not Null default 0',
                                             'decimal_places': 3
                                         })
    거래자산면적_총면적_건물_지분_분모: Decimal = field(default='0',
                                         metadata={
                                             'max_length': 11,
                                             '점검': '양의실수형식점검',
                                             '비고': 'Not Null default 0',
                                             'decimal_places': 3
                                         })
    거래자산면적_양도면적_토지_면적: Decimal = field(default='0',
                                       metadata={
                                           'max_length': 11,
                                           '점검': '양의실수형식점검',
                                           '비고': 'Not Null default 0',
                                           'decimal_places': 3
                                       })
    거래자산면적_양도면적_건물_면적: Decimal = field(default='0',
                                       metadata={
                                           'max_length': 11,
                                           '점검': '양의실수형식점검',
                                           '비고': 'Not Null default 0',
                                           'decimal_places': 3
                                       })
    거래자산면적_취득면적_토지_면적: Decimal = field(default='0',
                                       metadata={
                                           'max_length': 11,
                                           '점검': '양의실수형식점검',
                                           '비고': 'Not Null default 0',
                                           'decimal_places': 3
                                       })
    거래자산면적_취득면적_건물_면적: Decimal = field(default='0',
                                       metadata={
                                           'max_length': 11,
                                           '점검': '양의실수형식점검',
                                           '비고': 'Not Null default 0',
                                           'decimal_places': 3
                                       })
    거래금액_양도가액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    거래금액_취득가액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득가액종류: str = field(metadata={'max_length': 2, '점검': '01,02,03,04,05, 11,12,13,14', '비고': 'Not Null'})
    기납부토지초과이득세: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    기타필요경비: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도차익_전체양도차익: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도차익_비과세양도차익: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도차익_과세대상양도차익: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    장기보유특별공제: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감면소득금액_세액감면대상: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감면종류: str = field(default=None, metadata={'max_length': 3, '점검': '', '비고': 'Null허용'})
    감면율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 2})
    양도시기준시가_건물_일반건물: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도시기준시가_건물_오피스텔_상업용: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도시기준시가_건물_개별_공동주택: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도시기준시가_토지: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도시기준시가_합계: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득시기준시가_건물_일반건물: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득시기준시가_건물_오피스텔_상업용: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득시기준시가_건물_개별_공동주택: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득시기준시가_토지: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득시기준시가_합계: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    자동계산불러오기구분값: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    소재지국: str = field(metadata={'max_length': 3, '점검': '길이점검', '비고': 'Not Null'})
    소재지국명: str = field(metadata={'max_length': 40, '점검': '길이점검', '비고': 'Not Null'})
    소재지: str = field(default=None, metadata={'max_length': 60, '점검': '길이점검', '비고': 'Null 허용'})
    감면소득금액_소득금액감면대상: int = field(default=None, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'NotNull default0 (17)'})
    필요경비신고자료일련번호: int = field(default=None, metadata={'max_length': 6, '점검': '양의실수형식점검', '비고': 'NotNull default 0'})
    장기보유특별공제적용구분코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'NotNull default ‘ZZ’'})
    주택거주기간년수: int = field(default=None, metadata={'max_length': 4, '점검': '양의실수형식점검', '비고': 'NotNull default 0'})
    _1세대1주택비과세_보유기간: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'NotNull default ‘ZZ’'})
    _1세대1주택_비과세_거주기간: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'NotNull default ‘ZZ’'})
    공란: str = field(default=None, metadata={'max_length': 38, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI06_주식양도소득금액_계산명세(ERSRecord):
    자료구분: str = field(default='06', metadata={'max_length': 2, '점검': '06', '비고': 'Not Null'})
    서식코드: str = field(default='C116500', metadata={'max_length': 7, '점검': 'C116500', '비고': 'Not Null'})
    일련번호: str = field(default='1', metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null default 1'})
    과세구분: str = field(metadata={'max_length': 2, '점검': '01,05,ZZ', '비고': 'Not Null'})
    주식종목명: str = field(metadata={'max_length': 30, '점검': '길이점검', '비고': 'Not Null'})
    사업자등록번호: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Null허용, 부분 Not Null'})
    자산의종류: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    주식종류코드: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    취득유형: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    취득유형별양도주식수: Decimal = field(default='0',
                                metadata={
                                    'max_length': 23,
                                    '점검': '양의실수형식점검',
                                    '비고': 'Not Null default 0',
                                    'decimal_places': 10
                                })
    양도일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    주당양도가액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    양도가액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    취득일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    주당취득가액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    취득가액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    필요경비: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    과세대상양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감면소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    감면종류: str = field(metadata={'max_length': 3, '점검': '', '비고': 'Not Null'})
    감면율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 2})
    자동계산불러오기구분값: str = field(metadata={'max_length': 1, '점검': '', '비고': 'Not Null'})
    국내외구분: str = field(metadata={'max_length': 1, '점검': '', '비고': 'Not Null'})
    소재지국: str = field(metadata={'max_length': 3, '점검': '', '비고': 'Not Null'})
    소재지국명: str = field(metadata={'max_length': 40, '점검': '', '비고': 'Not Null'})
    ISIN코드: str = field(default=None, metadata={'max_length': 15, '점검': '', '비고': 'Null허용'})
    ISIN코드구분: str = field(default=None, metadata={'max_length': 3, '점검': '', '비고': 'Null허용'})
    필요경비신고자료일련번호: int = field(default=None, metadata={'max_length': 6, '점검': '양의실수형식점검', '비고': 'NotNull default 0'})
    과세이연_여부: str = field(default=None, metadata={'max_length': 2, '점검': '02, ZZ', '비고': 'NULL 허용'})
    전체양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    비과세양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 2, '점검': '길이점검', '비고': 'SPACE'})

    def __post_init__(self):
        self.국내외구분 = '1' if self.소재지국 == 'KR' else '2'
        self.전체양도소득금액 = self.양도가액 - self.취득가액 - self.필요경비


@dataclass(kw_only=True)
class TI07_취득가액및필요경비계산상세명세(ERSRecord):
    자료구분: str = field(default='07', metadata={'max_length': 2, '점검': '07', '비고': 'Not Null'})
    서식코드: str = field(default='C116600', metadata={'max_length': 7, '점검': 'C116600', '비고': 'Not Null'})
    필요경비신고자료일련번호: str = field(default='1', metadata={'max_length': 6, '점검': '', '비고': 'Not Null default 1'})
    구분코드: str = field(metadata={'max_length': 5, '점검': '숫자,길이점검', '비고': 'Not Null'})
    상세일련번호: str = field(metadata={'max_length': 6, '점검': '', '비고': 'Not Null'})
    상호: str = field(metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not Null'})
    사업자등록번호: str = field(default=None, metadata={'max_length': 10, '점검': '길이점검', '비고': '항목설명 참조'})
    지급일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': '항목설명 참조'})
    지급금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    증빙종류코드: str = field(default='ZZ', metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null default ZZ'})
    공란: str = field(default=None, metadata={'max_length': 81, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI08_매매계약서(ERSRecord):
    자료구분: str = field(default='08', metadata={'max_length': 2, '점검': '08', '비고': 'Not Null'})
    서식코드: str = field(default='YA00100', metadata={'max_length': 7, '점검': 'YA00100', '비고': 'Not Null'})
    일련번호: str = field(default='1', metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null default 1'})
    구분: str = field(metadata={'max_length': 1, '점검': '1,2', '비고': 'Not Null'})
    계약서종류: str = field(metadata={'max_length': 1, '점검': '1,2,3', '비고': 'Not Null'})
    국내외구분: str = field(metadata={'max_length': 1, '점검': '1,9', '비고': 'Not Null'})
    공란: str = field(default=None, metadata={'max_length': 82, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI09_매매계약서_채무인수_추가(ERSRecord):
    자료구분: str = field(default='09', metadata={'max_length': 2, '점검': '09', '비고': 'Not Null'})
    서식코드: str = field(default='YA00100', metadata={'max_length': 7, '점검': 'YA00100', '비고': 'Not Null'})
    일련번호: str = field(default='1', metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null default 1'})
    채무구분: str = field(default=None, metadata={'max_length': 1, '점검': '', '비고': ''})
    일련번호_상세: str = field(default='1', metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null default 1'})
    금액: int = field(default=None, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Null허용'})
    채권자명: str = field(default=None, metadata={'max_length': 50, '점검': '길이점검', '비고': 'Null허용'})
    공제방법: str = field(default=None, metadata={'max_length': 1, '점검': '1,2', '비고': 'Null허용'})
    공란: str = field(default=None, metadata={'max_length': 14, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI10_매매계약서_물건(ERSRecord):
    자료구분: str = field(default='10', metadata={'max_length': 2, '점검': '10', '비고': 'Not Null'})
    서식코드: str = field(default='YA00100', metadata={'max_length': 7, '점검': 'YA00100', '비고': 'Not Null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    소재지_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자, 길이점검', '비고': 'Not Null default 0'})
    소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자, 길이점검', '비고': 'Not Null default 0'})
    소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null 허용'})
    소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null 허용'})
    소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null 허용'})
    소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null 허용'})
    소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null 허용'})
    지목: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Null 허용'})
    면적: Decimal = field(default=None, metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Null 허용', 'decimal_places': 3})
    지분_분자: Decimal = field(default=None, metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Null 허용', 'decimal_places': 3})
    지분_분모: Decimal = field(default=None, metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Null 허용', 'decimal_places': 3})
    소재지국: str = field(default=None, metadata={'max_length': 3, '점검': '', '비고': 'Not null default KR'})
    소재지국명: str = field(default=None, metadata={'max_length': 40, '점검': '', '비고': 'Null 허용'})
    소재지: str = field(default=None, metadata={'max_length': 60, '점검': '', '비고': 'Null 허용'})
    공란: str = field(default=None, metadata={'max_length': 50, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI11_20_소재지_물건의_소재지_주소를_기입함_매매계약서_거래상대방(ERSRecord):
    자료구분: str = field(default='11', metadata={'max_length': 2, '점검': '11', '비고': 'Not Null'})
    서식코드: str = field(default='YA00100', metadata={'max_length': 7, '점검': 'YA00100', '비고': 'Not Null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    거래상대방_주민사업자구분: str = field(metadata={'max_length': 1, '점검': '1,2', '비고': 'Not Null'})
    거래상대방_내외국인_구분코드: str = field(metadata={'max_length': 1, '점검': '1,9', '비고': 'Not Null'})
    거래상대방_주민등록번호: str = field(metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not Null'})
    거래상대방_성명: str = field(metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not Null'})
    거래상대방_주소: str = field(metadata={'max_length': 100, '점검': '길이점검', '비고': 'Not Null'})
    거래상대방_지분_분자: Decimal = field(metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null', 'decimal_places': 3})
    거래상대방_지분_분모: Decimal = field(metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null', 'decimal_places': 3})
    공란: str = field(default=None, metadata={'max_length': 32, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI12_매매계약서_거래내역(ERSRecord):
    자료구분: str = field(default='12', metadata={'max_length': 2, '점검': '12', '비고': 'Not Null'})
    서식코드: str = field(default='YA00100', metadata={'max_length': 7, '점검': 'YA00100', '비고': 'Not Null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    거래내역_일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    거래금액구분코드: str = field(default=None, metadata={'max_length': 1, '점검': '1,2,3,9', '비고': 'Not null'})
    거래내역_금액: int = field(default=None, metadata={'max_length': 13, '점검': '양의실수형식점검', '비고': 'Not null'})
    거래내역_증빙: str = field(default=None, metadata={'max_length': 1, '점검': '1,2', '비고': 'Not null'})
    공란: str = field(default=None, metadata={'max_length': 56, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI13_매매계약서_공인중개사인적사항(ERSRecord):
    자료구분: str = field(default='13', metadata={'max_length': 2, '점검': '13', '비고': 'Not Null'})
    서식코드: str = field(default='YA00100', metadata={'max_length': 7, '점검': 'YA00100', '비고': 'Not Null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    공인중개사_상호: str = field(default=None, metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not null'})
    공인중개사_전화번호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    공인중개사_구분: str = field(default=None, metadata={'max_length': 1, '점검': '1, 2', '비고': 'Not null default 1'})
    공인중개사_사업자_등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '길이점검', '비고': 'Null허용'})
    공인중개사_대표자: str = field(default=None, metadata={'max_length': 30, '점검': '길이점검', '비고': 'Not null'})
    공인중개사_소재지: str = field(default=None, metadata={'max_length': 100, '점검': '길이점검', '비고': 'Not null'})
    공란: str = field(default=None, metadata={'max_length': 63, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI14_농어촌주택_등_취득자에_대한_과세특례신고서(ERSRecord):
    자료구분: str = field(default='14', metadata={'max_length': 2, '점검': '14', '비고': 'Not Null'})
    서식코드: str = field(default='M111700', metadata={'max_length': 7, '점검': 'M111700', '비고': 'Not Null'})
    주택구분: str = field(metadata={'max_length': 2, '점검': '01,02', '비고': 'Not Null'})
    소재지_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '(6)', '비고': 'Null허용'})
    소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    주택의종류: str = field(metadata={'max_length': 1, '점검': '1,2', '비고': 'Not Null'})
    면적_토지: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    면적_건물: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    기준시가_취득당시: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    기준시가_일반주택양도당시: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    계약금납부일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    농어촌주택등의보유기간_시작일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null허용'})
    농어촌주택등의보유기간_종료일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null허용'})
    공란: str = field(default=None, metadata={'max_length': 9, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI15_1세대1주택_특례적용신고서(ERSRecord):
    자료구분: str = field(default='15', metadata={'max_length': 2, '점검': '15', '비고': 'Not Null'})
    서식코드: str = field(default='C115800', metadata={'max_length': 7, '점검': 'C115800', '비고': 'Not Null'})
    주택구분: str = field(metadata={'max_length': 2, '점검': '01,03,04,05', '비고': 'Not Null'})
    소재지_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    면적_토지: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    면적_토지: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    소유자_성명: str = field(metadata={'max_length': 30, '점검': '길이점검', '비고': 'Not Null'})
    소유자_주민등록번호: str = field(metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not Null'})
    소유자_소득자와관계: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    취득일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    거주기간_시작일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    거주기간_종료일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    공란: str = field(default=None, metadata={'max_length': 49, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI16_1세대3주택이상자의_장기임대주택_등_일반세율적용신청서(ERSRecord):
    자료구분: str = field(default='16', metadata={'max_length': 2, '점검': '16', '비고': 'Not null'})
    서식코드: str = field(default='C116200', metadata={'max_length': 7, '점검': 'C116200', '비고': 'Not null'})
    일련번호: str = field(default='1', metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null default 1'})
    양도주택_구분: str = field(metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not Null'})
    양도주택_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    양도주택_소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    양도주택_소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    양도주택_소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    양도주택_소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_주택면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    양도주택_토지면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    양도주택_취득당시기준시가합계액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도주택_국민주택여부: str = field(metadata={'max_length': 1, '점검': 'Y,N', '비고': 'Not Null'})
    양도주택_취득일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도주택_양도일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도주택임대내용_사업자등록등이후기준호수임대기간_시작일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    양도주택임대내용_사업자등록등이후기준호수임대기간_종료일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    양도주택임대내용_공제기간_시작일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    양도주택임대내용_공제기간_종료일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    양도주택임대내용_주택임대기간: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    양도주택임대내용_세법상사업자등록_등록일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    양도주택임대내용_세법상사업자등록_등록호수: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    양도주택임대내용_임대주택법에의한임대사업자등록_등록일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null 허용'})
    양도주택임대내용_임대주택법에의한임대사업자등록_등록호수: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    임차인: str = field(default=None, metadata={'max_length': 30, '점검': '길이점검', '비고': 'Null 허용'})
    공란: str = field(default=None, metadata={'max_length': 28, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI17_1세대3주택이상자의_장기임대주택_등_일반세율적용신청서_상세(ERSRecord):
    자료구분: str = field(default='17', metadata={'max_length': 2, '점검': '17', '비고': 'Not null'})
    서식코드: str = field(default='C116200', metadata={'max_length': 7, '점검': 'C116200', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    소재지_법정동코드: str = field(default=None, metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not null'})
    소재지_특수지코드: str = field(default=None, metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not null'})
    소재지_번지: str = field(default=None, metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not null default 0'})
    소재지_호: str = field(default=None, metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not null default 0'})
    소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    개시일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    종료일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    임대기간등: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    공란: str = field(default=None, metadata={'max_length': 64, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI18_공익사업용토지_등에_대한_세액감면신청서(ERSRecord):
    자료구분: str = field(default='18', metadata={'max_length': 2, '점검': '18', '비고': 'Not null'})
    서식코드: str = field(default='M109000', metadata={'max_length': 7, '점검': 'M109000', '비고': 'Not null'})
    일련번호: str = field(default='1', metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not Null default 1'})
    신청인_상호또는법인명: str = field(metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not Null'})
    신청인_사업자등록번호: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    신청인_대표자성명: str = field(metadata={'max_length': 30, '점검': '길이점검', '비고': 'Not Null'})
    신청인_주민등록번호: str = field(metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not Null'})
    신청인_주소또는본점소재지: str = field(metadata={'max_length': 100, '점검': '길이점검', '비고': 'Not Null'})
    신청인_전화번호: str = field(metadata={'max_length': 12, '점검': '길이점검', '비고': 'Not Null'})
    매입토지_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    매입토지_소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    매입토지_소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    매입토지_소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    매입토지_소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    매입토지_소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    매입토지_소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    매입토지_소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    매입토지_소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    매입토지_면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    매입토지_매입가격: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식검사', '비고': 'Not Null default 0'})
    매입토지_매입일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    매입토지_계약일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    매입토지_감면받을세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식검사', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 16, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI19_장기임대주택_또는_신축임대주택_양도소득세액감면_면제_신청서(ERSRecord):
    자료구분: str = field(default='19', metadata={'max_length': 2, '점검': '19', '비고': 'Not null'})
    서식코드: str = field(default='M111300', metadata={'max_length': 7, '점검': 'M111300', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    양도물건_양도일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도물건_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    양도물건_소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    양도물건_소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    양도물건_소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    양도물건_소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    양도물건_소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    양도물건_소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    양도물건_소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    양도물건_소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    양도물건_물건표시: str = field(metadata={'max_length': 70, '점검': '길이점검', '비고': 'Not Null'})
    양도물건_대지면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    양도물건_건물면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    주택임대기간_개시일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    주택임대기간_종료일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    주택임대기간_공제기간_시작일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    주택임대기간_공제기간_종료일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    주택임대기간_세액감면대상기간: str = field(metadata={'max_length': 4, '점검': '길이점검', '비고': 'Not Null'})
    주택임대기간_세액감면비율: Decimal = field(default='0',
                                   metadata={
                                       'max_length': 5,
                                       '점검': '양의실수형식점검',
                                       '비고': 'Not Null default 0',
                                       'decimal_places': 2
                                   })
    감면대상소득: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감면받고자하는세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 27, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI20_미분양주택과세특례적용신고서(ERSRecord):
    자료구분: str = field(default='20', metadata={'max_length': 2, '점검': '20', '비고': 'Not null'})
    서식코드: str = field(default='M1114000', metadata={'max_length': 7, '점검': 'M1114000', '비고': 'Not null'})
    양도소득세_과세표준: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식검사', '비고': 'Not Null default 0'})
    양도소득세_특례세율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '02000', '비고': 'Not Null default 0', 'decimal_places': 2})
    양도소득세_산출세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식검사', '비고': 'Not Null default 0'})
    종합소득세_총수입금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식검사', '비고': 'Not Null default 0'})
    종합소득세_필요경비: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식검사', '비고': 'Not Null default 0'})
    종합소득세_차감소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식검사', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 21, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI21_미분양주택과세특례적용신고서_미분양주택양도명세(ERSRecord):
    자료구분: str = field(default='21', metadata={'max_length': 2, '점검': '21', '비고': 'Not null'})
    서식코드: str = field(default='M1114000', metadata={'max_length': 7, '점검': 'M1114000', '비고': 'Not null'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    소재지_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    토지면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    건물면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    취득_계약일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    공란: str = field(default=None, metadata={'max_length': 56, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI22_구조조정대상부동산_등_세액감면신청서(ERSRecord):
    자료구분: str = field(default='22', metadata={'max_length': 2, '점검': '22', '비고': 'Not null'})
    서식코드: str = field(default='M106000', metadata={'max_length': 7, '점검': 'M106000', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    과세연도_시작일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    과세연도_종료일: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도당시의기준시가: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득당시의기준시가: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득일부터5년이되는날의기준시가: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    _5년이내발생한양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감면비율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 2})
    감면대상양도소득금액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감면받을세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    조세특례제한법시행령조항: str = field(metadata={'max_length': 1, '점검': '1,2', '비고': 'Not Null'})
    공란: str = field(default=None, metadata={'max_length': 22, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI23_양도소득세특례세율적용신청서(ERSRecord):
    자료구분: str = field(default='23', metadata={'max_length': 2, '점검': '23', '비고': 'Not null'})
    서식코드: str = field(default='M111500', metadata={'max_length': 7, '점검': 'M111500', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    양도주택_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    양도주택_소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    양도주택_소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    양도주택_소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    양도주택_소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    양도주택_토지면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    양도주택_건물면적: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    양도주택_취득일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    양도주택_양도일자: str = field(metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not Null'})
    특례세율_과세표준: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    특례세율_특례세율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '01000', '비고': 'Not Null default 0', 'decimal_places': 2})
    특례세율_산출세액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    신축주택취득_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    신축주택취득_소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    신축주택취득_소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    신축주택취득_소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    신축주택취득_소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    신축주택취득_소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    신축주택취득_소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    신축주택취득_소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    신축주택취득_소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    신축주택취득_토지면적: Decimal = field(default='0',
                                 metadata={
                                     'max_length': 11,
                                     '점검': '양의실수형식점검',
                                     '비고': 'Not Null default 0',
                                     'decimal_places': 3
                                 })
    신축주택취득_건물면적: Decimal = field(default='0',
                                 metadata={
                                     'max_length': 11,
                                     '점검': '양의실수형식점검',
                                     '비고': 'Not Null default 0',
                                     'decimal_places': 3
                                 })
    신축주택취득_취득일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Null허용'})
    신축주택취득_취득예정시기: str = field(default=None, metadata={'max_length': 50, '점검': '길이점검', '비고': 'Null허용'})
    공란: str = field(default=None, metadata={'max_length': 54, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI24_조합원입주권_소유자_1세대1주택_특례적용신고서(ERSRecord):
    자료구분: str = field(default='24', metadata={'max_length': 2, '점검': '24', '비고': 'Not null'})
    서식코드: str = field(default='C116100', metadata={'max_length': 7, '점검': 'C116100', '비고': 'Not null'})
    주택구분: str = field(default=None, metadata={'max_length': 2, '점검': '06,07', '비고': 'Not null'})
    소재지_법정동코드: str = field(metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not Null'})
    소재지_특수지코드: str = field(metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not Null'})
    소재지_번지: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_호: str = field(default='0', metadata={'max_length': 4, '점검': '숫자,길이점검', '비고': 'Not Null default 0'})
    소재지_아파트명: str = field(default=None, metadata={'max_length': 40, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트동: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_아파트호: str = field(default=None, metadata={'max_length': 12, '점검': '길이점검', '비고': 'Null허용'})
    소재지_통: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    소재지_반: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Null허용'})
    면적_토지: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    면적_건물: Decimal = field(default='0', metadata={'max_length': 11, '점검': '양의실수형식점검', '비고': 'Not Null default 0', 'decimal_places': 3})
    소유자_성명: str = field(default=None, metadata={'max_length': 30, '점검': '길이점검', '비고': 'Not null'})
    소유자_주민등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not null'})
    소유자_소득자와관계: str = field(default=None, metadata={'max_length': 2, '점검': '길이점검', '비고': 'Not null'})
    취득일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    양도일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    거주기간_시작일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    거주기간_종료일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    사업시행인가일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    관리처분계획인가일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    완성일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    양도가액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 62, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI25_현물출자등에_대한_세액감면_면제신청서(ERSRecord):
    자료구분: str = field(default='25', metadata={'max_length': 2, '점검': '25', '비고': 'Not null'})
    서식코드: str = field(default='M103100', metadata={'max_length': 7, '점검': 'M103100', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    구분: str = field(default=None, metadata={'max_length': 1, '점검': '1~8', '비고': 'Not null'})
    과세연도_시작일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    과세연도_종료일: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    감면받으려는_법인세: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감면받으려는_양도세: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    조세특례제한법시행령조항: str = field(default=None, metadata={'max_length': 1, '점검': '', '비고': 'Not null'})
    양수인: str = field(default=None, metadata={'max_length': 30, '점검': '', '비고': ''})
    공란: str = field(default=None, metadata={'max_length': 11, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI26_주식거래명세서(ERSRecord):
    자료구분: str = field(default='26', metadata={'max_length': 2, '점검': '26', '비고': 'Not null'})
    서식코드: str = field(default='C116700', metadata={'max_length': 7, '점검': 'C116700', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    주식_출자증권발행법인_법인명: str = field(default=None, metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_사업자등록번호: str = field(default=None, metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_사업연도: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_소재지: str = field(metadata={'max_length': 100, '점검': '길이점검', '비고': 'Not Null'})
    주식_출자증권발행법인_법인구분: str = field(default=None, metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_법인규모: str = field(default=None, metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_발행주식총수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    주식_출자증권발행법인_자본금: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 33, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI27_주식거래명세서_상세(ERSRecord):
    자료구분: str = field(default='27', metadata={'max_length': 2, '점검': '27', '비고': 'Not null'})
    서식코드: str = field(default='C116700', metadata={'max_length': 7, '점검': 'C116700', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    양수자_성명_법인명: str = field(default=None, metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not null'})
    양수자_주민_법인등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not null'})
    양수자_사업자등록번호: str = field(default=None, metadata={'max_length': 10, '점검': '길이점검', '비고': 'null허용'})
    양수자_주소: str = field(metadata={'max_length': 100, '점검': '길이점검', '비고': 'Not Null'})
    양도내용_종목명: str = field(default=None, metadata={'max_length': 50, '점검': '길이점검', '비고': 'Not null'})
    양도내용_양도일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    양도내용_주식_출자지분수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도내용_단가: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도내용_양도가액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도내용_수수료: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도내용_증권거래세: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도내용_농특세: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득내용_취득일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    취득내용_주식_출자지분수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득내용_단가: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득내용_취득가액: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    취득내용_수수료: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    양도차익: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 37, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI28_대주주등신고서(ERSRecord):
    자료구분: str = field(default='28', metadata={'max_length': 2, '점검': '28', '비고': 'Not null'})
    서식코드: str = field(default='C116800', metadata={'max_length': 7, '점검': 'C116800', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    주식_출자증권발행법인_법인명: str = field(default=None, metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_사업자등록번호: str = field(default=None, metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_사업연도: str = field(default=None, metadata={'max_length': 4, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_소재지: str = field(metadata={'max_length': 100, '점검': '길이점검', '비고': 'Not Null'})
    주식_출자증권발행법인_법인구분: str = field(default=None, metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_법인규모: str = field(default=None, metadata={'max_length': 1, '점검': '길이점검', '비고': 'Not null'})
    주식_출자증권발행법인_발행주식총수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    주식_출자증권발행법인_자본금: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 33, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI29_대주주등신고서_상세(ERSRecord):
    자료구분: str = field(default='29', metadata={'max_length': 2, '점검': '29', '비고': 'Not null'})
    서식코드: str = field(default='C116800', metadata={'max_length': 7, '점검': 'C116800', '비고': 'Not null'})
    일련번호: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    일련번호_상세: str = field(default=None, metadata={'max_length': 6, '점검': '숫자,길이점검', '비고': 'Not null default 1'})
    주주1인및기타주주_구분: str = field(default=None, metadata={'max_length': 2, '점검': '01,02', '비고': 'Not null'})
    주주1인및기타주주_성명_법인명: str = field(default=None, metadata={'max_length': 60, '점검': '길이점검', '비고': 'Not null'})
    주주1인및기타주주_주민등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '길이점검', '비고': 'Not null'})
    직전사업연도말_주식수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    직전사업연도말_지분율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '', '비고': 'Not Null default 0', 'decimal_places': 2})
    증가_일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    증가_원인코드: str = field(default=None, metadata={'max_length': 2, '점검': '01,02,03,04,05,06', '비고': 'Not null'})
    증가_주식수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    감소_일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    감소_원인코드: str = field(default=None, metadata={'max_length': 2, '점검': '01,02,03,04,05,06', '비고': 'Not null'})
    감소_주식수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    대주주된날현재_일자: str = field(default=None, metadata={'max_length': 8, '점검': '일자형식점검', '비고': 'Not null'})
    대주주된날현재_주식수: int = field(default=0, metadata={'max_length': 13, '점검': '정수형식점검', '비고': 'Not Null default 0'})
    대주주된날현재_지분율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '', '비고': 'Not Null default 0', 'decimal_places': 2})
    주주1인과의관계_관계: str = field(default=None, metadata={'max_length': 10, '점검': '길이점검', '비고': 'Not null'})
    주주1인과의관계_코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Not null'})
    공란: str = field(default=None, metadata={'max_length': 102, '점검': '길이점검', '비고': 'SPACE'})


@dataclass(kw_only=True)
class TI30_국외자산양도소득세액공제_필요경비산입신청서(ERSRecord):
    자료구분: str = field(default='30', metadata={'max_length': 2, '점검': '30', '비고': 'Not null'})
    서식코드: str = field(default='C117300', metadata={'max_length': 7, '점검': 'C117300', '비고': 'Not null'})
    국내_국외분: str = field(default=None, metadata={'max_length': 1, '점검': '9', '비고': 'Not null'})
    세율구분코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Not null'})
    순번: str = field(default=None, metadata={'max_length': 6, '점검': '', '비고': 'Not null'})
    소재지국코드: str = field(default=None, metadata={'max_length': 3, '점검': '', '비고': 'Null 허용'})
    소재지국명: str = field(default=None, metadata={'max_length': 40, '점검': '', '비고': 'Null 허용'})
    소재지: str = field(default=None, metadata={'max_length': 60, '점검': '', '비고': 'Null 허용'})
    국외자산양도소득세액: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    동부가세액: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    합계: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    양도소득산출세액: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    양도소득금액_당해과세기간: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    양도소득금액_국외자산: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    공제한도: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    공제액: int = field(default=0, metadata={'max_length': 13, '점검': '', '비고': 'Not Null default 0'})
    공란: str = field(default=None, metadata={'max_length': 25, '점검': '', '비고': 'SPACE'})


class 양도소득세신고(양도소득세.양도소득세신고):
    TI01_양도소득세과세표준신고서_HEADER: List[TI01_양도소득세과세표준신고서_HEADER] = field(default_factory=list)
    TI02_양도소득세과세표준신고서_기본사항: List[TI02_양도소득세과세표준신고서_기본사항] = field(default_factory=list)
    TI03_양도소득과세표준신고서_세율별내역: List[TI03_양도소득과세표준신고서_세율별내역] = field(default_factory=list)
    TI04_양도소득과세표준신고서_양수인내역: List[TI04_양도소득과세표준신고서_양수인내역] = field(default_factory=list)
    TI05_양도소득금액_계산명세: List[TI05_양도소득금액_계산명세] = field(default_factory=list)
    TI06_주식양도소득금액_계산명세: List[TI06_주식양도소득금액_계산명세] = field(default_factory=list)
    TI07_취득가액및필요경비계산상세명세: List[TI07_취득가액및필요경비계산상세명세] = field(default_factory=list)
    TI08_매매계약서: List[TI08_매매계약서] = field(default_factory=list)
    TI09_매매계약서_채무인수_추가: List[TI09_매매계약서_채무인수_추가] = field(default_factory=list)
    TI10_매매계약서_물건: List[TI10_매매계약서_물건] = field(default_factory=list)
    TI11_20_소재지_물건의_소재지_주소를_기입함_매매계약서_거래상대방: List[TI11_20_소재지_물건의_소재지_주소를_기입함_매매계약서_거래상대방] = field(default_factory=list)
    TI12_매매계약서_거래내역: List[TI12_매매계약서_거래내역] = field(default_factory=list)
    TI13_매매계약서_공인중개사인적사항: List[TI13_매매계약서_공인중개사인적사항] = field(default_factory=list)
    TI14_농어촌주택_등_취득자에_대한_과세특례신고서: List[TI14_농어촌주택_등_취득자에_대한_과세특례신고서] = field(default_factory=list)
    TI15_1세대1주택_특례적용신고서: List[TI15_1세대1주택_특례적용신고서] = field(default_factory=list)
    TI16_1세대3주택이상자의_장기임대주택_등_일반세율적용신청서: List[TI16_1세대3주택이상자의_장기임대주택_등_일반세율적용신청서] = field(default_factory=list)
    TI17_1세대3주택이상자의_장기임대주택_등_일반세율적용신청서_상세: List[TI17_1세대3주택이상자의_장기임대주택_등_일반세율적용신청서_상세] = field(default_factory=list)
    TI18_공익사업용토지_등에_대한_세액감면신청서: List[TI18_공익사업용토지_등에_대한_세액감면신청서] = field(default_factory=list)
    TI19_장기임대주택_또는_신축임대주택_양도소득세액감면_면제_신청서: List[TI19_장기임대주택_또는_신축임대주택_양도소득세액감면_면제_신청서] = field(default_factory=list)
    TI20_미분양주택과세특례적용신고서: List[TI20_미분양주택과세특례적용신고서] = field(default_factory=list)
    TI21_미분양주택과세특례적용신고서_미분양주택양도명세: List[TI21_미분양주택과세특례적용신고서_미분양주택양도명세] = field(default_factory=list)
    TI22_구조조정대상부동산_등_세액감면신청서: List[TI22_구조조정대상부동산_등_세액감면신청서] = field(default_factory=list)
    TI23_양도소득세특례세율적용신청서: List[TI23_양도소득세특례세율적용신청서] = field(default_factory=list)
    TI24_조합원입주권_소유자_1세대1주택_특례적용신고서: List[TI24_조합원입주권_소유자_1세대1주택_특례적용신고서] = field(default_factory=list)
    TI25_현물출자등에_대한_세액감면_면제신청서: List[TI25_현물출자등에_대한_세액감면_면제신청서] = field(default_factory=list)
    TI26_주식거래명세서: List[TI26_주식거래명세서] = field(default_factory=list)
    TI27_주식거래명세서_상세: List[TI27_주식거래명세서_상세] = field(default_factory=list)
    TI28_대주주등신고서: List[TI28_대주주등신고서] = field(default_factory=list)
    TI29_대주주등신고서_상세: List[TI29_대주주등신고서_상세] = field(default_factory=list)
    TI30_국외자산양도소득세액공제_필요경비산입신청서: List[TI30_국외자산양도소득세액공제_필요경비산입신청서] = field(default_factory=list)

    def calculate(self):
        for record in self.TI06_주식양도소득금액_계산명세:
            record.calculate()
        self.TI03_양도소득과세표준신고서_세율별내역.clear()
        for index, record in enumerate(self.TI06_주식양도소득금액_계산명세):
            record.일련번호 = str(index + 1).zfill(6)
        양도소득기본공제_한도 = 2500000
        for v_국내외구분, group in groupby(self.TI06_주식양도소득금액_계산명세, lambda x: x.국내외구분):
            국내외분 = '1' if v_국내외구분 == '1' else '9'
            for v_주식종류코드, records in groupby(group, lambda x: x.주식종류코드):
                양도소득금액 = sum((record.전체양도소득금액 for record in records))
                양도소득기본공제, 양도소득기본공제_한도 = deduct(양도소득금액, 양도소득기본공제_한도)
                self.TI03_양도소득과세표준신고서_세율별내역.append(
                    TI03_양도소득과세표준신고서_세율별내역(국내외분=국내외분,
                                           세율구분=주식종류코드(v_주식종류코드).세율구분.value[0],
                                           세율=주식종류코드(v_주식종류코드).세율구분.세율,
                                           양도소득금액=양도소득금액,
                                           양도소득기본공제=양도소득기본공제,
                                           과세표준=양도소득금액 - 양도소득기본공제,
                                           농어촌특별세_세율=Decimal(20)))
            세율별내역 = [r for r in self.TI03_양도소득과세표준신고서_세율별내역 if r.국내외분 == 국내외분 and r.세율구분 != '00']
            self.TI03_양도소득과세표준신고서_세율별내역.append(
                TI03_양도소득과세표준신고서_세율별내역(국내외분='1' if v_국내외구분 == '1' else '9',
                                       세율구분='00',
                                       세율=Decimal('0'),
                                       양도소득금액=sum((r.양도소득금액 for r in 세율별내역)),
                                       양도소득기본공제=sum((r.양도소득기본공제 for r in 세율별내역)),
                                       과세표준=sum((r.과세표준 for r in 세율별내역)),
                                       산출세액=sum((r.산출세액 for r in 세율별내역)),
                                       자진납부할_세액=sum((r.자진납부할_세액 for r in 세율별내역))))
        합계내역 = [r for r in self.TI03_양도소득과세표준신고서_세율별내역 if r.세율구분 == '00' and r.국내외분 != 'Z']
        self.TI03_양도소득과세표준신고서_세율별내역.append(
            TI03_양도소득과세표준신고서_세율별내역(국내외분='Z',
                                   세율구분='00',
                                   양도소득금액=sum((record.양도소득금액 for record in 합계내역)),
                                   양도소득기본공제=sum((record.양도소득기본공제 for record in 합계내역)),
                                   과세표준=sum((record.과세표준 for record in 합계내역)),
                                   산출세액=sum((r.산출세액 for r in 합계내역)),
                                   자진납부세액=sum((r.자진납부할_세액 for r in 합계내역)),
                                   주민세_소득세자진납부할_세액=sum((r.자진납부할_세액 for r in 합계내역)),
                                   주민세_산출세액=int(sum((r.산출세액 for r in 합계내역)) * Decimal('0.1')),
                                   주민세_자진납부세액=int(sum((r.산출세액 for r in 합계내역)) * Decimal('0.1'))))
        self.TI03_양도소득과세표준신고서_세율별내역.append(
            TI03_양도소득과세표준신고서_세율별내역(국내외분='Z', 세율구분='98', 과세표준=self.TI03_양도소득과세표준신고서_세율별내역[-1].과세표준 * Decimal(0.1)))
        address = 도로명주소.parse(self.납세자.주소)
        self.TI02_양도소득세과세표준신고서_기본사항 = [
            TI02_양도소득세과세표준신고서_기본사항(전화번호=self.납세자.휴대전화번호,
                                   주소_법정동코드=address.법정동코드,
                                   내외국인여부=yn(self.납세자.국적코드 == 'KR'),
                                   거주구분=yn(self.납세자.국적코드 != self.납세자.거주지국가코드),
                                   거주지국코드=self.납세자.거주지국가코드,
                                   거주지국명=country_name(self.납세자.거주지국가코드),
                                   국적코드=self.납세자.국적코드,
                                   도로명_도로명코드=address.도로명코드,
                                   도로명_도로명=address.도로명,
                                   도로명_지하만있는건물구분=address.지하여부,
                                   도로명_건물번호_본번=address.건물본번,
                                   도로명_건물번호_부번=address.건물부번,
                                   도로명_아파트동_도로명='',
                                   도로명_아파트호_도로명='',
                                   도로명_읍면동일련번호=address.읍면동일련번호,
                                   주소_번지=address.지번본번_번지,
                                   주소_호=address.지번부번_호,
                                   주소_아파트명=address.건물명,
                                   주소_아파트호=address.상세주소,
                                   주소_특수지코드=address.특수지코드)
        ]
        self.TI01_양도소득세과세표준신고서_HEADER = [
            TI01_양도소득세과세표준신고서_HEADER(성명=self.납세자.납세자명,
                                     납세자ID=self.납세자.납세자ID,
                                     납세자구분='01',
                                     세목코드='22',
                                     신고구분코드='01',
                                     신고유형='7',
                                     과세기간_년월=self.과세기간.strftime('%Y%m'),
                                     신고구분상세코드='01',
                                     신고서종류코드='D01',
                                     민원종류코드='FD001',
                                     사용자ID=self.세무대리인.홈택스ID,
                                     제출년월=self.제출일자.strftime('%Y%m'),
                                     세무프로그램코드=세무프로그램코드,
                                     작성일자=self.작성일자.strftime('%Y%m%d'),
                                     양도일자=max((record.양도일자 for record in self.TI06_주식양도소득금액_계산명세)),
                                     세무대리대표자주민등록번호=self.세무대리인.대표자주민등록번호,
                                     세무대리대표자성명=self.세무대리인.대표자성명,
                                     세무대리인성명=self.세무대리인.성명,
                                     세무대리인생년월일=self.세무대리인.생년월일,
                                     세무대리인전화번호=self.세무대리인.전화번호,
                                     세무대리사업자등록번호=self.세무대리인.사업자등록번호,
                                     세무대리인관리번호=self.세무대리인.관리번호)
        ]
