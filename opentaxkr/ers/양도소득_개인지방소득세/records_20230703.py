from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import List
from opentaxkr.ers import ERSRecord, ERSReport
from opentaxkr.ers.양도소득_개인지방소득세 import 양도소득_개인지방소득세신고서식
from opentaxkr.ers.양도소득세.records_20230502 import 양도소득세신고
from opentaxkr.models import 세무프로그램코드


@dataclass(kw_only=True)
class LI01_양도소득_과세표준확정신고_HEADER(ERSRecord):
    자료구분: str = field(default='01', metadata={'max_length': 2, '점검': '01', '비고': 'Not null'})
    서식코드: str = field(default='C116300', metadata={'max_length': 7, '점검': 'C116300', '비고': 'Not null'})
    세목구분코드: str = field(default='140002', metadata={'max_length': 6, '점검': '140002', '비고': 'Not null'})
    신고서식코드: str = field(default=None, metadata={'max_length': 5, '점검': 'B4011', '비고': 'Not null'})
    세무프로그램코드: str = field(default=None, metadata={'max_length': 4, '점검': '', '비고': 'Not null'})
    세무대리인_주민_법인등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '', '비고': 'Null 허용'})
    세무대리인_성명_법인명: str = field(default=None, metadata={'max_length': 80, '점검': '', '비고': 'Null 허용'})
    세무대리인_사업자등록번호: str = field(default=None, metadata={'max_length': 10, '점검': '', '비고': 'Null 허용'})
    세무대리인_연락처: str = field(default=None, metadata={'max_length': 16, '점검': '', '비고': 'Null 허용'})
    납부기한: str = field(default=None, metadata={'max_length': 8, '점검': '', '비고': 'Null 허용'})
    적용서식: str = field(default=None, metadata={'max_length': 10, '점검': 'V2020.1.01.', '비고': 'Not null'})


@dataclass(kw_only=True)
class LI02_양도소득_과세표준확정신고_기본정보(ERSRecord):
    자료구분: str = field(default='02', metadata={'max_length': 2, '점검': '02', '비고': 'Not null'})
    서식코드: str = field(default='C116300', metadata={'max_length': 7, '점검': 'C116300', '비고': 'Not null'})
    납세자_주민등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '', '비고': 'Not null (1)'})
    납세자_성명: str = field(default=None, metadata={'max_length': 80, '점검': '', '비고': 'Not null (1)'})
    납세자_우편번호_현재주소: str = field(default=None, metadata={'max_length': 6, '점검': '', '비고': 'Null 허용 (1)'})
    납세자_주소_현재주소: str = field(default=None, metadata={'max_length': 200, '점검': '', '비고': 'Null 허용 (1)'})
    납세지_우편번호: str = field(default=None, metadata={'max_length': 6, '점검': '', '비고': 'Null 허용 (1)'})
    납세지_주소: str = field(default=None, metadata={'max_length': 200, '점검': '', '비고': 'Not null (1)'})
    납세지_시도코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Not null (1)'})
    납세지_시군구코드: str = field(default=None, metadata={'max_length': 3, '점검': '', '비고': 'Not null (1)'})
    납세지_법정동코드: str = field(default=None, metadata={'max_length': 5, '점검': '', '비고': 'Not null (1)'})
    납세자_구분: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Not null'})
    신고구분: str = field(default=None, metadata={'max_length': 2, '점검': '11,13', '비고': 'Not null'})
    신고유형: str = field(default=None, metadata={'max_length': 1, '점검': '', '비고': 'Not null (2)'})
    귀속년도: str = field(default=None, metadata={'max_length': 4, '점검': '', '비고': 'Not null'})
    양도소득년월: str = field(default=None, metadata={'max_length': 6, '점검': '', '비고': 'Not null'})
    전화번호: str = field(default=None, metadata={'max_length': 16, '점검': '', '비고': 'Null 허용 (1)'})
    휴대전화: str = field(default=None, metadata={'max_length': 16, '점검': '', '비고': 'Null 허용 (1)'})
    전자우편번호: str = field(default=None, metadata={'max_length': 100, '점검': '', '비고': 'Null 허용 (1)'})
    거주구분: str = field(default=None, metadata={'max_length': 1, '점검': '', '비고': 'Not null (1)'})
    거주지국코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Not null (1)'})
    양수인_주민등록번호: str = field(default=None, metadata={'max_length': 13, '점검': '', '비고': 'Null 허용 (3)'})
    양수인_성명: str = field(default=None, metadata={'max_length': 80, '점검': '', '비고': 'Null 허용 (3)'})
    양수인_분자지분율: Decimal = field(default='0', metadata={'max_length': 11, '점검': '', '비고': 'Not Null default 0 (3)', 'decimal_places': 3})
    양수인_분모지분율: Decimal = field(default='0', metadata={'max_length': 11, '점검': '', '비고': 'Not Null default 0 (3)', 'decimal_places': 3})
    양도인과의_관계코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Null 허용 (3)'})
    양도자산종류_코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Null 허용'})
    양도일자: date = field(default=None, metadata={'max_length': 8, '점검': '', '비고': 'Not null (2)'})
    양도물건지_대표_우편번호: str = field(default=None, metadata={'max_length': 6, '점검': '', '비고': 'Null 허용 (3)'})
    양도물건지_대표_주소: str = field(default=None, metadata={'max_length': 130, '점검': '', '비고': 'Null 허용 (3) 신고유형이 (1,3,5,9,B)인 경우 필수'})
    은행코드_지방세_환급금: str = field(default=None, metadata={'max_length': 3, '점검': '', '비고': 'Null 허용(15)'})
    계좌번호_지방세_환급금: str = field(default=None, metadata={'max_length': 20, '점검': '', '비고': 'Null 허용(15)'})
    국적코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Null 허용 (1)'})


@dataclass(kw_only=True)
class LI03_양도소득_과세표준확정신고_세율별내역(ERSRecord):
    자료구분: str = field(default='03', metadata={'max_length': 2, '점검': '03', '비고': 'Not null'})
    서식코드: str = field(default='C116300', metadata={'max_length': 7, '점검': 'C116300', '비고': 'Not null'})
    자료구분2: str = field(default=None, metadata={'max_length': 1, '점검': '1,2', '비고': 'Not null'})
    국내외구분코드: str = field(default=None, metadata={'max_length': 1, '점검': '1,2', '비고': 'Not null'})
    세율구분코드: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Not null'})
    지방소득세_양도소득과세표준: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (5)'})
    세율: Decimal = field(default='0', metadata={'max_length': 4, '점검': '', '비고': 'Not Null default 0 (6)', 'decimal_places': 3})
    산출세액: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (7)'})
    감면세액: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (8)'})
    외국납부세액공제: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (9)'})
    예정신고납부세액공제: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0'})
    특별징수세액공제: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (11)(10)'})
    신고불성실가산구분: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Null 허용'})
    부정신고사유: str = field(default=None, metadata={'max_length': 2, '점검': '', '비고': 'Null 허용'})
    신고불성실가산적용세율: Decimal = field(default='0', metadata={'max_length': 5, '점검': '', '비고': 'Not Null default 0', 'decimal_places': 4})
    부정신고적용과표: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0'})
    무_과소신고_가산세_신고불성실: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (12)'})
    기타_가산세_기장불성실: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (12)'})
    납부불성실_가산세납부지연_가산세: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (12)'})
    납부지연일수: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0'})
    가산세_합계: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (12)'})
    기신고_결정_경정세액_조정공제: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (13)'})
    납부_환급할_총세액: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (14)'})
    전자신고_세액공제: int = field(default=0, metadata={'max_length': 14, '점검': '', '비고': 'Not Null default 0 (11)'})


class 양도소득_개인지방소득세신고(ERSReport):
    LI01_양도소득_과세표준확정신고_HEADER: List[LI01_양도소득_과세표준확정신고_HEADER]
    LI02_양도소득_과세표준확정신고_기본정보: List[LI02_양도소득_과세표준확정신고_기본정보]
    LI03_양도소득_과세표준확정신고_세율별내역: List[LI03_양도소득_과세표준확정신고_세율별내역]
    format_class = 양도소득_개인지방소득세신고서식

    def __init__(self, 국세신고: 양도소득세신고):
        super().__init__()
        self.LI01_양도소득_과세표준확정신고_HEADER = [
            LI01_양도소득_과세표준확정신고_HEADER(세무대리인_사업자등록번호=국세신고.세무대리인.사업자등록번호,
                                      세무대리인_성명_법인명=국세신고.세무대리인.성명,
                                      세무대리인_연락처=국세신고.세무대리인.전화번호,
                                      세무대리인_주민_법인등록번호=국세신고.세무대리인.법인등록번호 or 국세신고.세무대리인.대표자주민등록번호,
                                      적용서식='V2020.1.01.',
                                      세무프로그램코드=세무프로그램코드,
                                      신고서식코드='B4011')
        ]
        self.LI02_양도소득_과세표준확정신고_기본정보 = [
            LI02_양도소득_과세표준확정신고_기본정보(납세자_주민등록번호=국세신고.납세자.납세자ID,
                                    납세자_성명=국세신고.납세자.납세자명,
                                    납세자_우편번호_현재주소=국세신고.납세자.도로명주소.우편번호,
                                    납세자_주소_현재주소=국세신고.납세자.주소,
                                    납세지_우편번호=국세신고.납세자.도로명주소.우편번호,
                                    납세지_시도코드=국세신고.납세자.도로명주소.도로명코드[:2],
                                    납세지_시군구코드=국세신고.납세자.도로명주소.도로명코드[2:5],
                                    납세지_법정동코드=국세신고.납세자.도로명주소.법정동코드[5:],
                                    납세자_구분='01' if 국세신고.납세자.국적코드 == 'KR' else '02',
                                    납세지_주소=국세신고.납세자.주소,
                                    신고구분='11',
                                    신고유형='7',
                                    귀속년도=str(국세신고.과세기간.year),
                                    양도소득년월=f'{국세신고.과세기간.year}12',
                                    전화번호=국세신고.납세자.휴대전화번호,
                                    전자우편번호=국세신고.납세자.전자메일주소,
                                    거주구분='1' if 국세신고.납세자.국적코드 == 국세신고.납세자.거주지국가코드 else '2',
                                    거주지국코드=국세신고.납세자.거주지국가코드,
                                    양도일자=max((record.양도일자 for record in 국세신고.TI06_주식양도소득금액_계산명세)),
                                    양도자산종류_코드='ZZ',
                                    양도물건지_대표_주소='해외주식')
        ]
        self.LI03_양도소득_과세표준확정신고_세율별내역 = [
            LI03_양도소득_과세표준확정신고_세율별내역(자료구분2='1' if record.세율구분 == '00' else '2',
                                     국내외구분코드='1' if record.국내외분 == '1' else '2',
                                     세율구분코드=record.세율구분,
                                     지방소득세_양도소득과세표준=record.과세표준,
                                     세율=record.세율 // 10,
                                     산출세액=record.산출세액 // 10,
                                     감면세액=0,
                                     외국납부세액공제=0,
                                     예정신고납부세액공제=0,
                                     특별징수세액공제=0,
                                     신고불성실가산구분='',
                                     부정신고사유='',
                                     신고불성실가산적용세율=Decimal('0'),
                                     부정신고적용과표=0,
                                     무_과소신고_가산세_신고불성실=0,
                                     기신고_결정_경정세액_조정공제=0,
                                     납부_환급할_총세액=record.자진납부할_세액 // 10,
                                     전자신고_세액공제=0) for record in sorted(국세신고.TI03_양도소득과세표준신고서_세율별내역, key=lambda r: r.세율구분)
            if record.국내외분 != 'Z'
        ]
