from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import List, ClassVar
from opentaxkr.ers import ERSRecord, ERSField, ERSReport


@dataclass(kw_only=True)
class v1_1_신고서_Head_레코드(ERSRecord):
    자료구분: str = ERSField(default='11,12', 길이=2, 누적=2, 점검='11,12', 비고='Not null')
    서식코드: str = ERSField(default='I103200, I106000', 길이=7, 누적=9, 점검='I103200, I106000', 비고='Not null')
    납세자ID: str = ERSField(default=None, 길이=13, 누적=22, 점검='사업자번호 CHECK+무세적', 비고='Not null')
    세목코드: str = ERSField(default=None, 길이=2, 누적=24, 점검='41', 비고='Not null')
    신고구분코드: str = ERSField(default=None, 길이=2, 누적=26, 점검='01,03', 비고='Not null')
    신고구분상세코드: str = ERSField(default=None, 길이=2, 누적=28, 점검='', 비고='Not null')
    과세기간_년기_월: str = ERSField(default=None, 길이=6, 누적=34, 점검='년월형식점검', 비고='Not null')
    신고서종류코드: str = ERSField(default=None, 길이=3, 누적=37, 점검='', 비고='Not null')
    사용자ID: str = ERSField(default=None, 길이=20, 누적=57, 점검='길이점검 →USERID', 비고='Not null')
    납세자번호: str = ERSField(default=None, 길이=13, 누적=70, 점검='숫자,길이점검', 비고='Null 허용')
    세무대리인성명: str = ERSField(default=None, 길이=30, 누적=100, 점검='', 비고='Null 허용')
    세무대리인전화번호1_지역번호: str = ERSField(default=None, 길이=4, 누적=104, 점검='', 비고='Null 허용')
    세무대리인전화번호2_국번: str = ERSField(default=None, 길이=5, 누적=109, 점검='', 비고='Null 허용')
    세무대리인전화번호3_지역번호_국번을제외한번호: str = ERSField(default=None, 길이=5, 누적=114, 점검='', 비고='Null 허용')
    상호_법인명: str = ERSField(default=None, 길이=30, 누적=144, 점검='', 비고='Not null')
    성명_대표자명: str = ERSField(default=None, 길이=30, 누적=174, 점검='', 비고='Not null')
    사업장소재지: str = ERSField(default=None, 길이=70, 누적=244, 점검='', 비고='Null 허용')
    사업장전화번호: str = ERSField(default=None, 길이=14, 누적=258, 점검='', 비고='Null 허용')
    사업자주소: str = ERSField(default=None, 길이=70, 누적=328, 점검='', 비고='Null 허용')
    사업자전화번호: str = ERSField(default=None, 길이=14, 누적=342, 점검='', 비고='Null 허용')
    업태명: str = ERSField(default=None, 길이=30, 누적=372, 점검='', 비고='Not null')
    종목명: str = ERSField(default=None, 길이=50, 누적=422, 점검='', 비고='Not null')
    업종코드: str = ERSField(default=None, 길이=7, 누적=429, 점검='업종코드CHECK', 비고='Not null')
    과세기간시작일자: date = ERSField(default=None, 길이=8, 누적=437, 점검='일자형식점검', 비고='Not null')
    과세기간종료일자: date = ERSField(default=None, 길이=8, 누적=445, 점검='일자형식점검', 비고='Not null')
    작성일자: date = ERSField(default=None, 길이=8, 누적=453, 점검='일자형식점검', 비고='Not null')
    보정신고구분: str = ERSField(default=None, 길이=1, 누적=454, 점검='N', 비고='Not null default ‘N’')
    사업자휴대전화: str = ERSField(default=None, 길이=14, 누적=468, 점검='', 비고='Null 허용')
    세무프로그램코드: str = ERSField(default=None, 길이=4, 누적=472, 점검='길이점검', 비고='Not null')
    세무대리인사업자번호: str = ERSField(default=None, 길이=13, 누적=485, 점검='사업자번호 CHECK+무세적', 비고='Null 허용')
    전자메일주소: str = ERSField(default=None, 길이=50, 누적=535, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=65, 누적=600, 점검='길이점검', 비고='space')


@dataclass(kw_only=True)
class v1_2_일반과세자_신고서_레코드(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103200', 길이=7, 누적=9, 점검='I103200', 비고='Not Null')
    매출과세세금계산서발급금액: int = ERSField(default=0, 길이=15, 누적=24, 점검='정수점검', 비고='Not Null default 0')
    매출과세세금계산서발급세액: int = ERSField(default=0, 길이=13, 누적=37, 점검='정수점검', 비고='Not Null default 0')
    매출과세매입자발행세금계산서금액: int = ERSField(default=0, 길이=13, 누적=50, 점검='정수점검', 비고='Not Null default 0')
    매출과세매입자발행세금계산서세액: int = ERSField(default=0, 길이=13, 누적=63, 점검='정수점검', 비고='Not Null default 0')
    매출과세카드현금발행금액: int = ERSField(default=0, 길이=15, 누적=78, 점검='정수점검', 비고='Not Null default 0')
    매출과세카드현금발행세액: int = ERSField(default=0, 길이=15, 누적=93, 점검='정수점검', 비고='Not Null default 0')
    매출과세기타금액: int = ERSField(default=0, 길이=13, 누적=106, 점검='정수점검', 비고='Not Null default 0')
    매출과세기타세액: int = ERSField(default=0, 길이=13, 누적=119, 점검='정수점검', 비고='Not Null default 0')
    매출영세율세금계산서발급금액: int = ERSField(default=0, 길이=13, 누적=132, 점검='정수점검', 비고='Not Null default 0')
    매출영세율기타금액: int = ERSField(default=0, 길이=15, 누적=147, 점검='정수점검', 비고='Not Null default 0')
    매출예정누락합계금액: int = ERSField(default=0, 길이=13, 누적=160, 점검='정수점검', 비고='Not Null default 0')
    매출예정누락합계세액: int = ERSField(default=0, 길이=13, 누적=173, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출세금계산서금액: int = ERSField(default=0, 길이=13, 누적=186, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출세금계산서세액: int = ERSField(default=0, 길이=13, 누적=199, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출과세기타금액: int = ERSField(default=0, 길이=13, 누적=212, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출과세기타세액: int = ERSField(default=0, 길이=13, 누적=225, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출영세율세금계산서금액: int = ERSField(default=0, 길이=13, 누적=238, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출영세율기타금액: int = ERSField(default=0, 길이=13, 누적=251, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출명세합계금액: int = ERSField(default=0, 길이=13, 누적=264, 점검='정수점검', 비고='Not Null default 0')
    예정누락매출명세합계세액: int = ERSField(default=0, 길이=13, 누적=277, 점검='정수점검', 비고='Not Null default 0')
    매출대손세액가감세액: int = ERSField(default=0, 길이=13, 누적=290, 점검='정수점검', 비고='Not Null default 0')
    과세표준금액: int = ERSField(default=0, 길이=15, 누적=305, 점검='정수점검', 비고='Not Null default 0')
    산출세액: int = ERSField(default=0, 길이=15, 누적=320, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서수취일반금액: int = ERSField(default=0, 길이=15, 누적=335, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서수취일반세액: int = ERSField(default=0, 길이=13, 누적=348, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서수취고정자산금액: int = ERSField(default=0, 길이=13, 누적=361, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서수취고정자산세액: int = ERSField(default=0, 길이=13, 누적=374, 점검='정수점검', 비고='Not Null default 0')
    매입예정누락합계금액: int = ERSField(default=0, 길이=13, 누적=387, 점검='정수점검', 비고='Not Null default 0')
    매입예정누락합계세액: int = ERSField(default=0, 길이=13, 누적=400, 점검='정수점검', 비고='Not Null default 0')
    예정누락매입신고세금계산서금액: int = ERSField(default=0, 길이=13, 누적=413, 점검='정수점검', 비고='Not Null default 0')
    예정누락매입신고세금계산서세액: int = ERSField(default=0, 길이=13, 누적=426, 점검='정수점검', 비고='Not Null default 0')
    예정누락매입기타공제금액: int = ERSField(default=0, 길이=13, 누적=439, 점검='정수점검', 비고='Not Null default 0')
    예정누락매입기타공제세액: int = ERSField(default=0, 길이=13, 누적=452, 점검='정수점검', 비고='Not Null default 0')
    예정누락매입명세합계금액: int = ERSField(default=0, 길이=13, 누적=465, 점검='정수점검', 비고='Not Null default 0')
    예정누락매입명세합계세액: int = ERSField(default=0, 길이=13, 누적=478, 점검='정수점검', 비고='Not Null default 0')
    매입자발행세금계산서매입금액: int = ERSField(default=0, 길이=13, 누적=491, 점검='정수점검', 비고='Not Null default 0')
    매입자발행세금계산서매입세액: int = ERSField(default=0, 길이=13, 누적=504, 점검='정수점검', 비고='Not Null default 0')
    매입기타공제매입금액: int = ERSField(default=0, 길이=13, 누적=517, 점검='정수점검', 비고='Not Null default 0')
    매입기타공제매입세액: int = ERSField(default=0, 길이=13, 누적=530, 점검='정수점검', 비고='Not Null default 0')
    그밖의공제매입명세합계금액: int = ERSField(default=0, 길이=13, 누적=543, 점검='정수점검', 비고='Not Null default 0')
    그밖의공제매입명세합계세액: int = ERSField(default=0, 길이=13, 누적=556, 점검='정수점검', 비고='Not Null default 0')
    매입세액합계금액: int = ERSField(default=0, 길이=15, 누적=571, 점검='정수점검', 비고='Not Null default 0')
    매입세액합계세액: int = ERSField(default=0, 길이=13, 누적=584, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할매입합계금액: int = ERSField(default=0, 길이=13, 누적=597, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할매입합계세액: int = ERSField(default=0, 길이=13, 누적=610, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할매입금액: int = ERSField(default=0, 길이=13, 누적=623, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할매입세액: int = ERSField(default=0, 길이=13, 누적=636, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할공통매입면세사업금액: int = ERSField(default=0, 길이=13, 누적=649, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할공통매입면세사업세액: int = ERSField(default=0, 길이=13, 누적=662, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할대손처분금액: int = ERSField(default=0, 길이=13, 누적=675, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할대손처분세액: int = ERSField(default=0, 길이=13, 누적=688, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할매입명세합계금액: int = ERSField(default=0, 길이=13, 누적=701, 점검='정수점검', 비고='Not Null default 0')
    공제받지못할매입명세합계세액: int = ERSField(default=0, 길이=13, 누적=714, 점검='정수점검', 비고='Not Null default 0')
    차감합계금액: int = ERSField(default=0, 길이=15, 누적=729, 점검='정수점검', 비고='Not Null default 0')
    차감합계세액: int = ERSField(default=0, 길이=13, 누적=742, 점검='정수점검', 비고='Not Null default 0')
    납부_환급세액: int = ERSField(default=0, 길이=13, 누적=755, 점검='정수점검', 비고='Not Null default 0')
    그밖의경감공제세액: int = ERSField(default=0, 길이=15, 누적=770, 점검='정수점검', 비고='Not Null default 0')
    그밖의경감공제명세합계세액: int = ERSField(default=0, 길이=15, 누적=785, 점검='정수점검', 비고='Not Null default 0')
    경감공제합계세액: int = ERSField(default=0, 길이=13, 누적=798, 점검='정수점검', 비고='Not Null default 0')
    예정신고미환급세액: int = ERSField(default=0, 길이=13, 누적=811, 점검='정수점검', 비고='Not Null default 0')
    예정고지세액: int = ERSField(default=0, 길이=13, 누적=824, 점검='정수점검', 비고='Not Null default 0')
    사업양수자의대리납부기납부세액: int = ERSField(default=0, 길이=13, 누적=837, 점검='정수점검', 비고='Not Null default 0')
    매입자납부특례기납부세액: int = ERSField(default=0, 길이=13, 누적=850, 점검='정수점검', 비고='Not Null default 0')
    가산세액계: int = ERSField(default=0, 길이=13, 누적=863, 점검='정수점검', 비고='Not Null default 0')
    차감납부할세액: int = ERSField(default=0, 길이=15, 누적=878, 점검='정수점검', 비고='Not Null default 0')
    과세표준명세수입금액제외금액: int = ERSField(default=0, 길이=13, 누적=891, 점검='정수점검', 비고='Not Null default 0')
    과세표준명세합계수입금액: int = ERSField(default=0, 길이=15, 누적=906, 점검='정수점검', 비고='Not Null default 0')
    면세사업수입금액제외금액: int = ERSField(default=0, 길이=13, 누적=919, 점검='정수점검', 비고='Not Null default 0')
    면세사업합계수입금액: int = ERSField(default=0, 길이=15, 누적=934, 점검='정수점검', 비고='Not Null default 0')
    계산서교부금액: int = ERSField(default=0, 길이=15, 누적=949, 점검='정수점검', 비고='Not Null default 0')
    계산서수취금액: int = ERSField(default=0, 길이=15, 누적=964, 점검='정수점검', 비고='Not Null default 0')
    환급구분코드: str = ERSField(default='‘ZZ’', 길이=2, 누적=966, 점검='‘10’,’20’, ’30’,’40’, ’41’,’42’, ‘43’,’ZZ’', 비고='Not Null default ‘ZZ’')
    은행코드_국세환급금: str = ERSField(default=None, 길이=3, 누적=969, 점검='', 비고='Null 허용')
    계좌번호_국세환급금: str = ERSField(default=None, 길이=20, 누적=989, 점검='', 비고='Null 허용')
    총괄납부승인번호: str = ERSField(default=None, 길이=9, 누적=998, 점검='', 비고='Null 허용')
    은행지점명: str = ERSField(default=None, 길이=30, 누적=1028, 점검='', 비고='Null 허용')
    폐업일자: date = ERSField(default=None, 길이=8, 누적=1036, 점검='공란점검', 비고='Null 허용')
    폐업사유: str = ERSField(default=None, 길이=3, 누적=1039, 점검='공란점검', 비고='Null 허용')
    기한후_과세표준여부: str = ERSField(길이=1, 누적=1040, 점검='Y,N', 비고='Not Null')
    실차감납부할세액: int = ERSField(default=0, 길이=15, 누적=1055, 점검='정수점검', 비고='Not Null default 0')
    일반과세자구분: str = ERSField(default='0', 길이=1, 누적=1056, 점검='0, 2,3,5', 비고='Not Null default 0')
    조기환급취소구분: str = ERSField(default='0', 길이=1, 누적=1057, 점검='1:조기환급취소', 비고='Not Null default 0')
    수출기업_수입_납부유예: int = ERSField(default=0, 길이=15, 누적=1072, 점검='정수점검', 비고='Not Null default 0')
    신용카드업자의_대리납부_기납부세액: int = ERSField(default=0, 길이=13, 누적=1085, 점검='정수점검', 비고='Not Null default 0')
    소규모_개인사업자_부가가치세_감면세액: int = ERSField(default=0, 길이=13, 누적=1098, 점검='정수점검', 비고='Not Null default 0')
    영세율상호주의여부: str = ERSField(default=None, 길이=1, 누적=1099, 점검='‘Y’,’N’', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=1, 누적=1100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v1_3_간이과세자_신고서_레코드(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I106000', 길이=7, 누적=9, 점검='I106000', 비고='Not Null')
    과표과세부가가치율코드_1: str = ERSField(default=None, 길이=2, 누적=11, 점검='금액이 0이 아니면 35', 비고='Null 허용')
    과표과세금액_1: int = ERSField(default=0, 길이=13, 누적=24, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_1: Decimal = ERSField(default='0', 길이=5, 누적=29, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_1: int = ERSField(default=0, 길이=13, 누적=42, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율코드_2: str = ERSField(default=None, 길이=2, 누적=44, 점검='금액이 0이 아니면 36', 비고='Null 허용')
    과표과세금액_2: int = ERSField(default=0, 길이=13, 누적=57, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_2: Decimal = ERSField(default='0', 길이=5, 누적=62, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_2: int = ERSField(default=0, 길이=13, 누적=75, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율코드_3: str = ERSField(default=None, 길이=2, 누적=77, 점검='금액이 0이 아니면 37', 비고='Null 허용')
    과표과세금액_3: int = ERSField(default=0, 길이=13, 누적=90, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_3: Decimal = ERSField(default='0', 길이=5, 누적=95, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_3: int = ERSField(default=0, 길이=13, 누적=108, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율코드_4: str = ERSField(default=None, 길이=2, 누적=110, 점검='금액이 0이 아니면 38', 비고='Null 허용')
    과표과세금액_4: int = ERSField(default=0, 길이=13, 누적=123, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_4: Decimal = ERSField(default='0', 길이=5, 누적=128, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_4: int = ERSField(default=0, 길이=13, 누적=141, 점검='정수점검', 비고='Not Null default 0')
    과표영세율코드: str = ERSField(default=None, 길이=2, 누적=143, 점검='금액이 0이 아니면 24', 비고='Null 허용')
    과표영세율금액: int = ERSField(default=0, 길이=13, 누적=156, 점검='정수점검', 비고='Not Null default 0')
    과표영세율부가가치율: Decimal = ERSField(default='0', 길이=5, 누적=161, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표재고납부세액: int = ERSField(default=0, 길이=13, 누적=174, 점검='정수점검', 비고='Not Null default 0')
    과세표준금액: int = ERSField(default=0, 길이=15, 누적=189, 점검='정수점검', 비고='Not Null default 0')
    산출세액: int = ERSField(default=0, 길이=15, 누적=204, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서공제금액: int = ERSField(default=0, 길이=13, 누적=217, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서공제세액: int = ERSField(default=0, 길이=13, 누적=230, 점검='정수점검', 비고='Not Null default 0')
    매입매입자발행금액: int = ERSField(default=0, 길이=13, 누적=243, 점검='정수점검', 비고='Not Null default 0')
    매입매입자발행세액: int = ERSField(default=0, 길이=13, 누적=256, 점검='정수점검', 비고='Not Null default 0')
    공제세액: int = ERSField(default=0, 길이=15, 누적=271, 점검='정수점검', 비고='Not Null default 0')
    매입자납부특례기납부금액: int = ERSField(default=0, 길이=13, 누적=284, 점검='0', 비고='Not Null default 0')
    매입자납부특례기납부세액: int = ERSField(default=0, 길이=13, 누적=297, 점검='0', 비고='Not Null default 0')
    예정고지_신고세액: int = ERSField(default=0, 길이=15, 누적=312, 점검='정수점검', 비고='Not Null default 0')
    가산세액세액합계: int = ERSField(default=0, 길이=13, 누적=325, 점검='정수점검', 비고='Not Null default 0')
    차감납부할세액_환급받을세액: int = ERSField(default=0, 길이=15, 누적=340, 점검='정수점검', 비고='Not Null default 0')
    과세수입금액합계: int = ERSField(default=0, 길이=13, 누적=353, 점검='정수점검', 비고='Not Null default 0')
    기타수입금액합계: int = ERSField(default=0, 길이=13, 누적=366, 점검='정수점검', 비고='Not Null default 0')
    면세수입금액합계: int = ERSField(default=0, 길이=13, 누적=379, 점검='정수점검', 비고='Not Null default 0')
    면세기타수입금액합계: int = ERSField(default=0, 길이=13, 누적=392, 점검='정수점검', 비고='Not Null default 0')
    폐업일자: date = ERSField(default=None, 길이=8, 누적=400, 점검='공란점검', 비고='Null 허용')
    폐업사유: str = ERSField(default=None, 길이=3, 누적=403, 점검='공란점검', 비고='Null 허용')
    기한후_과세표준여부: str = ERSField(길이=1, 누적=404, 점검='Y,N', 비고='Not Null')
    은행코드_국세환급금: str = ERSField(default=None, 길이=3, 누적=407, 점검='숫자점검', 비고='Null 허용')
    계좌번호_국세환급금: str = ERSField(default=None, 길이=20, 누적=427, 점검='', 비고='Null 허용')
    은행지점명: str = ERSField(default=None, 길이=30, 누적=457, 점검='', 비고='Null 허용')
    실차감납부할세액: int = ERSField(default=0, 길이=15, 누적=472, 점검='정수점검', 비고='Not Null default 0')
    납부면제구분: str = ERSField(길이=1, 누적=473, 점검='0', 비고='Not Null')
    과세유형전환일: str = ERSField(default=None, 길이=8, 누적=481, 점검='공란점검', 비고='Null 허용')
    과표과세부가가치율코드_5: str = ERSField(default=None, 길이=2, 누적=483, 점검='금액이 0이 아니면 39', 비고='Null 허용')
    과표과세금액_5: int = ERSField(default=0, 길이=13, 누적=496, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_5: Decimal = ERSField(default='0', 길이=5, 누적=501, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_5: int = ERSField(default=0, 길이=13, 누적=514, 점검='정수점검', 비고='Not Null default 0')
    세금계산서발급금액_5: int = ERSField(default=0, 길이=13, 누적=527, 점검='정수점검', 비고='Not Null default 0')
    매입자발행세금계산서금액_5: int = ERSField(default=0, 길이=13, 누적=540, 점검='정수점검', 비고='Not Null default 0')
    신용카드_현금영수증금액_5: int = ERSField(default=0, 길이=13, 누적=553, 점검='정수점검', 비고='Not Null default 0')
    기타매출금액_5: int = ERSField(default=0, 길이=13, 누적=566, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율코드_6: str = ERSField(default=None, 길이=2, 누적=568, 점검='금액이 0이 아니면 40', 비고='Null 허용')
    과표과세금액_6: int = ERSField(default=0, 길이=13, 누적=581, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_6: Decimal = ERSField(default='0', 길이=5, 누적=586, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_6: int = ERSField(default=0, 길이=13, 누적=599, 점검='정수점검', 비고='Not Null default 0')
    세금계산서발급금액_6: int = ERSField(default=0, 길이=13, 누적=612, 점검='정수점검', 비고='Not Null default 0')
    매입자발행세금계산서금액_6: int = ERSField(default=0, 길이=13, 누적=625, 점검='정수점검', 비고='Not Null default 0')
    신용카드_현금영수증금액_6: int = ERSField(default=0, 길이=13, 누적=638, 점검='정수점검', 비고='Not Null default 0')
    기타매출금액_6: int = ERSField(default=0, 길이=13, 누적=651, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율코드_7: str = ERSField(default=None, 길이=2, 누적=653, 점검='금액이 0이 아니면 41', 비고='Null 허용')
    과표과세금액_7: int = ERSField(default=0, 길이=13, 누적=666, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_7: Decimal = ERSField(default='0', 길이=5, 누적=671, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_7: int = ERSField(default=0, 길이=13, 누적=684, 점검='정수점검', 비고='Not Null default 0')
    세금계산서발급금액_7: int = ERSField(default=0, 길이=13, 누적=697, 점검='정수점검', 비고='Not Null default 0')
    매입자발행세금계산서금액_7: int = ERSField(default=0, 길이=13, 누적=710, 점검='정수점검', 비고='Not Null default 0')
    신용카드_현금영수증금액_7: int = ERSField(default=0, 길이=13, 누적=723, 점검='정수점검', 비고='Not Null default 0')
    기타매출금액_7: int = ERSField(default=0, 길이=13, 누적=736, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율코드_8: str = ERSField(default=None, 길이=2, 누적=738, 점검='금액이 0이 아니면 42', 비고='Null 허용')
    과표과세금액_8: int = ERSField(default=0, 길이=13, 누적=751, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_8: Decimal = ERSField(default='0', 길이=5, 누적=756, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_8: int = ERSField(default=0, 길이=13, 누적=769, 점검='정수점검', 비고='Not Null default 0')
    세금계산서발급금액_8: int = ERSField(default=0, 길이=13, 누적=782, 점검='정수점검', 비고='Not Null default 0')
    매입자발행세금계산서금액_8: int = ERSField(default=0, 길이=13, 누적=795, 점검='정수점검', 비고='Not Null default 0')
    신용카드_현금영수증금액_8: int = ERSField(default=0, 길이=13, 누적=808, 점검='정수점검', 비고='Not Null default 0')
    기타매출금액_8: int = ERSField(default=0, 길이=13, 누적=821, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율코드_9: str = ERSField(default=None, 길이=2, 누적=823, 점검='금액이 0이 아니면 43', 비고='Null 허용')
    과표과세금액_9: int = ERSField(default=0, 길이=13, 누적=836, 점검='정수점검', 비고='Not Null default 0')
    과표과세부가가치율_9: Decimal = ERSField(default='0', 길이=5, 누적=841, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    과표과세세액_9: int = ERSField(default=0, 길이=13, 누적=854, 점검='정수점검', 비고='Not Null default 0')
    세금계산서발급금액_9: int = ERSField(default=0, 길이=13, 누적=867, 점검='정수점검', 비고='Not Null default 0')
    매입자발행세금계산서금액_9: int = ERSField(default=0, 길이=13, 누적=880, 점검='정수점검', 비고='Not Null default 0')
    신용카드_현금영수증금액_9: int = ERSField(default=0, 길이=13, 누적=893, 점검='정수점검', 비고='Not Null default 0')
    기타매출금액_9: int = ERSField(default=0, 길이=13, 누적=906, 점검='정수점검', 비고='Not Null default 0')
    과표영세율금액_세금계산서발급분: int = ERSField(default=0, 길이=13, 누적=919, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서공제금액_21_7_1_이후: int = ERSField(default=0, 길이=13, 누적=932, 점검='정수점검', 비고='Not Null default 0')
    매입세금계산서공제세액_21_7_1_이후: int = ERSField(default=0, 길이=13, 누적=945, 점검='정수점검', 비고='Not Null default 0')
    매입매입자발행금액_21_7_1_이후: int = ERSField(default=0, 길이=13, 누적=958, 점검='정수점검', 비고='Not Null default 0')
    매입매입자발행세액_21_7_1_이후: int = ERSField(default=0, 길이=13, 누적=971, 점검='정수점검', 비고='Not Null default 0')
    영세율상호주의여부: str = ERSField(default=None, 길이=1, 누적=972, 점검='‘Y’,’N’', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=28, 누적=1000, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_3_간이과세자_신고서_레코드_사업장현황명세서(ERSRecord):
    자료구분: str = ERSField(default='14', 길이=2, 누적=2, 점검='14', 비고='Not Null')
    서식코드: str = ERSField(default='I104400', 길이=7, 누적=9, 점검='I104400', 비고='Not Null')
    자가타가구분: str = ERSField(길이=2, 누적=11, 점검='01,02', 비고='Not Null')
    사업장대지: int = ERSField(default=0, 길이=7, 누적=18, 점검='숫자점검', 비고='Not Null default 0')
    사업장건물_지하: int = ERSField(default=0, 길이=3, 누적=21, 점검='숫자점검', 비고='Not Null default 0')
    사업장건물_지상: int = ERSField(default=0, 길이=3, 누적=24, 점검='숫자점검', 비고='Not Null default 0')
    사업장건물_바닥면적: int = ERSField(default=0, 길이=7, 누적=31, 점검='숫자점검', 비고='Not Null default 0')
    사업장건물_연면적: int = ERSField(default=0, 길이=7, 누적=38, 점검='숫자점검', 비고='Not Null default 0')
    객실수: int = ERSField(default=0, 길이=7, 누적=45, 점검='양수점검', 비고='Not Null default 0')
    탁자수: int = ERSField(default=0, 길이=7, 누적=52, 점검='양수점검', 비고='Not Null default 0')
    의자수: int = ERSField(default=0, 길이=7, 누적=59, 점검='양수점검', 비고='Not Null default 0')
    주차장_유_무: str = ERSField(default=None, 길이=1, 누적=60, 점검='Y,N', 비고='Null 허용')
    종업원수: int = ERSField(default=0, 길이=7, 누적=67, 점검='양수점검', 비고='Not Null default 0')
    차량수_승용차: int = ERSField(default=0, 길이=7, 누적=74, 점검='양수점검', 비고='Not Null default 0')
    차량수_화물차: int = ERSField(default=0, 길이=7, 누적=81, 점검='양수점검', 비고='Not Null default 0')
    월기준: str = ERSField(길이=2, 누적=83, 점검='06,12', 비고='Not Null')
    보증금: int = ERSField(default=0, 길이=9, 누적=92, 점검='양수점검', 비고='Not Null default 0')
    월세: int = ERSField(default=0, 길이=11, 누적=103, 점검='양수점검', 비고='Not Null default 0')
    전기_가스료: int = ERSField(default=0, 길이=9, 누적=112, 점검='양수점검', 비고='Not Null default 0')
    수도료: int = ERSField(default=0, 길이=9, 누적=121, 점검='양수점검', 비고='Not Null default 0')
    인건비: int = ERSField(default=0, 길이=9, 누적=130, 점검='양수점검', 비고='Not Null default 0')
    기타경비: int = ERSField(default=0, 길이=9, 누적=139, 점검='양수점검', 비고='Not Null default 0')
    월기본경비계: int = ERSField(default=0, 길이=9, 누적=148, 점검='양수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=52, 누적=200, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_3_간이과세자_신고서_레코드_신용카드매출전표_등_발행금액집계표(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103400', 길이=7, 누적=9, 점검='I103400', 비고='Not Null')
    전체발행금액_합계: int = ERSField(default=0, 길이=15, 누적=24, 점검='정수점검', 비고='Not Null default 0')
    신용카드등발행금액_합계: int = ERSField(default=0, 길이=13, 누적=37, 점검='정수점검', 비고='Not Null default 0')
    현금영수증발행금액_합계: int = ERSField(default=0, 길이=13, 누적=50, 점검='정수점검', 비고='Not Null default 0')
    발행금액합계_과세매출분: int = ERSField(default=0, 길이=13, 누적=63, 점검='정수점검', 비고='Not Null default 0')
    신용카드등발행금액_과세매출분: int = ERSField(default=0, 길이=13, 누적=76, 점검='정수점검', 비고='Not Null default 0')
    현금영수증발행금액_과세매출분: int = ERSField(default=0, 길이=13, 누적=89, 점검='정수점검', 비고='Not Null default 0')
    발행금액합계_면세매출분: int = ERSField(default=0, 길이=13, 누적=102, 점검='정수점검', 비고='Not Null default 0')
    신용카드등발행금액_면세매출분: int = ERSField(default=0, 길이=13, 누적=115, 점검='정수점검', 비고='Not Null default 0')
    현금영수증발행금액_면세매출분: int = ERSField(default=0, 길이=13, 누적=128, 점검='정수점검', 비고='Not Null default 0')
    발행금액합계_봉사료: int = ERSField(default=0, 길이=13, 누적=141, 점검='정수점검', 비고='Not Null default 0')
    신용카드등발행금액_봉사료: int = ERSField(default=0, 길이=13, 누적=154, 점검='정수점검', 비고='Not Null default 0')
    현금영수증발행금액_봉사료: int = ERSField(default=0, 길이=13, 누적=167, 점검='정수점검', 비고='Not Null default 0')
    세금계산서교부금액_집계표: int = ERSField(default=0, 길이=13, 누적=180, 점검='정수점검', 비고='Not Null default 0')
    계산서교부금액_집계표: int = ERSField(default=0, 길이=13, 누적=193, 점검='정수점검', 비고='Not Null default 0')
    직불_기명식_선불전자지급수단_합계: int = ERSField(default=0, 길이=13, 누적=206, 점검='정수점검', 비고='Not Null default 0')
    직불_기명식_선불전자지급수단_과세매출분: int = ERSField(default=0, 길이=13, 누적=219, 점검='정수점검', 비고='Not Null default 0')
    직불_기명식_선불전자지급수단_면세매출분: int = ERSField(default=0, 길이=13, 누적=232, 점검='정수점검', 비고='Not Null default 0')
    직불_기명식_선불전자지급수단_봉사료: int = ERSField(default=0, 길이=13, 누적=245, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=5, 누적=250, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_3_간이과세자_신고서_레코드_영세율첨부서류제출명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I105800', 길이=7, 누적=9, 점검='I105800', 비고='Not Null')
    제출사유코드: str = ERSField(길이=2, 누적=11, 점검='01,02', 비고='Not Null')
    제출사유: str = ERSField(길이=60, 누적=71, 점검='', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=77, 점검='숫자,길이점검', 비고='Not Null')
    서류명: str = ERSField(길이=40, 누적=117, 점검='', 비고='Not Null')
    발급자: str = ERSField(길이=20, 누적=137, 점검='', 비고='Not Null')
    발급일자: date = ERSField(길이=8, 누적=145, 점검='일자점검', 비고='Not Null')
    선적일자: date = ERSField(길이=8, 누적=153, 점검='일자점검', 비고='Not Null')
    수출통화코드: str = ERSField(길이=3, 누적=156, 점검='영문자, 길이점검', 비고='Not Null')
    환율: Decimal = ERSField(default='0', 길이=9, 누적=165, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=4)
    당기제출금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=180, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    당기제출금액_원화: int = ERSField(default=0, 길이=15, 누적=195, 점검='정수점검', 비고='Not Null default 0')
    당기신고해당분_외화: Decimal = ERSField(default='0', 길이=15, 누적=210, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    당기신고해당분_원화: int = ERSField(default=0, 길이=15, 누적=225, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=25, 누적=250, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_3_간이과세자_신고서_레코드_의제매입세액공제신고서합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I102300', 길이=7, 누적=9, 점검='I102300', 비고='Not Null')
    거래처수_합계: int = ERSField(default=0, 길이=7, 누적=16, 점검='정수점검', 비고='Not Null default 0')
    매입건수_합계: int = ERSField(default=0, 길이=11, 누적=27, 점검='정수점검', 비고='Not Null default 0')
    매입금액_합계: int = ERSField(default=0, 길이=15, 누적=42, 점검='정수점검', 비고='Not Null default 0')
    공제율구분_합계: str = ERSField(default=None, 길이=1, 누적=43, 점검='0,2,4,6,8,9,A,B,C,D,E, F,G,H,I', 비고='Null 허용')
    매입의제매입세액_합계: int = ERSField(default=0, 길이=13, 누적=56, 점검='정수점검', 비고='Not Null default 0')
    거래처수_계산서: int = ERSField(default=0, 길이=6, 누적=62, 점검='정수점검', 비고='Not Null default 0')
    매입건수_계산서: int = ERSField(default=0, 길이=11, 누적=73, 점검='정수점검', 비고='Not Null default 0')
    매입금액_계산서: int = ERSField(default=0, 길이=15, 누적=88, 점검='정수점검', 비고='Not Null default 0')
    공제율구분_계산서: str = ERSField(default=None, 길이=1, 누적=89, 점검='0,2,4,6,8,9,A,B,C,D,E, F,G,H,I', 비고='Null 허용')
    매입의제매입세액_계산서: int = ERSField(default=0, 길이=13, 누적=102, 점검='정수점검', 비고='Not Null default 0')
    거래처수_신용카드: int = ERSField(default=0, 길이=6, 누적=108, 점검='정수점검', 비고='Not Null default 0')
    매입건수_신용카드: int = ERSField(default=0, 길이=11, 누적=119, 점검='정수점검', 비고='Not Null default 0')
    매입금액_신용카드: int = ERSField(default=0, 길이=15, 누적=134, 점검='정수점검', 비고='Not Null default 0')
    공제율구분_신용카드: str = ERSField(default=None, 길이=1, 누적=135, 점검='0,2,4,6,8,9,A,B,C,D,E, F,G,H,I', 비고='Null 허용')
    매입의제매입세액_신용카드: int = ERSField(default=0, 길이=13, 누적=148, 점검='정수점검', 비고='Not Null default 0')
    거래처수_농어민: int = ERSField(default=0, 길이=6, 누적=154, 점검='정수점검', 비고='Not Null default 0')
    매입건수_농어민: int = ERSField(default=0, 길이=11, 누적=165, 점검='정수점검', 비고='Not Null default 0')
    매입금액_농어민: int = ERSField(default=0, 길이=15, 누적=180, 점검='정수점검', 비고='Not Null default 0')
    공제율구분_농어민: str = ERSField(default=None, 길이=1, 누적=181, 점검='0,2,4,6,8,9,A,B,C,D,E, F,G,H,I', 비고='Null 허용')
    매입의제매입세액_농어민: int = ERSField(default=0, 길이=13, 누적=194, 점검='정수점검', 비고='Not Null default 0')
    과세표준_예정분: int = ERSField(default=0, 길이=15, 누적=209, 점검='정수점검', 비고='Not Null default 0')
    과세표준_확정분: int = ERSField(default=0, 길이=15, 누적=224, 점검='정수점검', 비고='Not Null default 0')
    과세표준_합계: int = ERSField(default=0, 길이=15, 누적=239, 점검='정수점검', 비고='Not Null default 0')
    대상액한도계산_한도율: str = ERSField(default=None, 길이=1, 누적=240, 점검='3,4,5,6', 비고='Null 허용')
    대상액한도계산_한도액: int = ERSField(default=0, 길이=15, 누적=255, 점검='정수점검', 비고='Not Null default 0')
    당기매입액: int = ERSField(default=0, 길이=15, 누적=270, 점검='정수점검', 비고='Not Null default 0')
    공제대상금액: int = ERSField(default=0, 길이=15, 누적=285, 점검='정수점검', 비고='Not Null default 0')
    공제대상세액_공제율: str = ERSField(default=None, 길이=1, 누적=286, 점검='0,2,4,6,8,9,A,B,C,D,E, F,G,H,I', 비고='Null 허용')
    공제대상세액_공제대상세액: int = ERSField(default=0, 길이=13, 누적=299, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_예정신고분: int = ERSField(default=0, 길이=13, 누적=312, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_월별조기분: int = ERSField(default=0, 길이=13, 누적=325, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_합계: int = ERSField(default=0, 길이=13, 누적=338, 점검='정수점검', 비고='Not Null default 0')
    공제_납부할세액: int = ERSField(default=0, 길이=13, 누적=351, 점검='정수점검', 비고='Not Null default 0')
    제1기_과세표준_제조업: int = ERSField(default=0, 길이=15, 누적=366, 점검='정수점검', 비고='Not Null default 0')
    제2기_과세표준_제조업: int = ERSField(default=0, 길이=15, 누적=381, 점검='정수점검', 비고='Not Null default 0')
    _1역년과세표준합계_제조업: int = ERSField(default=0, 길이=15, 누적=396, 점검='정수점검', 비고='Not Null default 0')
    대상액한도계산_한도율_제조업: str = ERSField(default=None, 길이=1, 누적=397, 점검='3,4,5', 비고='Null 허용')
    대상액한도계산_한도액_제조업: int = ERSField(default=0, 길이=15, 누적=412, 점검='정수점검', 비고='Not Null default 0')
    제1기_매입액_제조업: int = ERSField(default=0, 길이=15, 누적=427, 점검='정수점검', 비고='Not Null default 0')
    제2기_매입액_제조업: int = ERSField(default=0, 길이=15, 누적=442, 점검='정수점검', 비고='Not Null default 0')
    _1역년매입액합계_제조업: int = ERSField(default=0, 길이=15, 누적=457, 점검='정수점검', 비고='Not Null default 0')
    공제대상금액_제조업: int = ERSField(default=0, 길이=15, 누적=472, 점검='정수점검', 비고='Not Null default 0')
    공제대상세액_공제율_제조업: str = ERSField(default=None, 길이=1, 누적=473, 점검='2,4,6', 비고='Null 허용')
    공제대상세액_제조업: int = ERSField(default=0, 길이=13, 누적=486, 점검='정수점검', 비고='Not Null default 0')
    제1기_이미공제받은세액_제조업: int = ERSField(default=0, 길이=13, 누적=499, 점검='정수점검', 비고='Not Null default 0')
    제2기_이미공제받은세액_예정분_제조업: int = ERSField(default=0, 길이=13, 누적=512, 점검='정수점검', 비고='Not Null default 0')
    제2기_이미공제받은세액_월별조기분_제조업: int = ERSField(default=0, 길이=13, 누적=525, 점검='정수점검', 비고='Not Null default 0')
    제2기_이미공제받은세액_합계_제조업: int = ERSField(default=0, 길이=13, 누적=538, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_총합계_제조업: int = ERSField(default=0, 길이=13, 누적=551, 점검='정수점검', 비고='Not Null default 0')
    공제_납부할세액_제조업: int = ERSField(default=0, 길이=13, 누적=564, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=36, 누적=600, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_3_간이과세자_신고서_레코드_의제매입세액공제신고서명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I102300', 길이=7, 누적=9, 점검='I102300', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    주민등록번호: str = ERSField(길이=13, 누적=28, 점검='숫자,길이점검', 비고='Not Null')
    성명: str = ERSField(길이=30, 누적=58, 점검='', 비고='Not Null')
    매입건수: int = ERSField(default=0, 길이=11, 누적=69, 점검='정수점검', 비고='Not Null default 0')
    품명: str = ERSField(길이=30, 누적=99, 점검='', 비고='Not Null')
    매입수량: str = ERSField(길이=20, 누적=119, 점검='양수점검', 비고='Not Null')
    매입금액: int = ERSField(default=0, 길이=13, 누적=132, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=68, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_5_재활용폐자원_및_중고자동차매입세액공제신고서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M116300', 길이=7, 누적=9, 점검='M116300', 비고='Not Null')
    매입처수_합계: int = ERSField(default=0, 길이=7, 누적=16, 점검='양수점검', 비고='Not Null default 0')
    건수_합계: int = ERSField(default=0, 길이=11, 누적=27, 점검='양수점검', 비고='Not Null default 0')
    취득금액_합계: int = ERSField(default=0, 길이=15, 누적=42, 점검='정수점검', 비고='Not Null default 0')
    매입세액공제액_합계: int = ERSField(default=0, 길이=15, 누적=57, 점검='정수점검', 비고='Not Null default 0')
    매입처수_영수증: int = ERSField(default=0, 길이=6, 누적=63, 점검='양수점검', 비고='Not Null default 0')
    건수_영수증: int = ERSField(default=0, 길이=11, 누적=74, 점검='양수점검', 비고='Not Null default 0')
    취득금액_영수증: int = ERSField(default=0, 길이=15, 누적=89, 점검='정수점검', 비고='Not Null default 0')
    매입세액공제액_영수증: int = ERSField(default=0, 길이=15, 누적=104, 점검='정수점검', 비고='Not Null default 0')
    매입처수_계산서: int = ERSField(default=0, 길이=6, 누적=110, 점검='양수점검', 비고='Not Null default 0')
    건수_계산서: int = ERSField(default=0, 길이=11, 누적=121, 점검='양수점검', 비고='Not Null default 0')
    취득금액_계산서: int = ERSField(default=0, 길이=15, 누적=136, 점검='정수점검', 비고='Not Null default 0')
    매입세액공제액_계산서: int = ERSField(default=0, 길이=15, 누적=151, 점검='정수점검', 비고='Not Null default 0')
    합계_매출액: int = ERSField(default=0, 길이=15, 누적=166, 점검='정수점검', 비고='Not Null default 0')
    예정분_매출액: int = ERSField(default=0, 길이=15, 누적=181, 점검='정수점검', 비고='Not Null default 0')
    확정분_매출액: int = ERSField(default=0, 길이=15, 누적=196, 점검='정수점검', 비고='Not Null default 0')
    한도율: Decimal = ERSField(default='0', 길이=5, 누적=201, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=2)
    한도액: int = ERSField(default=0, 길이=15, 누적=216, 점검='정수점검', 비고='Not Null default 0')
    합계_당기매입액: int = ERSField(default=0, 길이=15, 누적=231, 점검='정수점검', 비고='Not Null default 0')
    세금계산서_당기매입액: int = ERSField(default=0, 길이=15, 누적=246, 점검='정수점검', 비고='Not Null default 0')
    영수증등_당기매입액: int = ERSField(default=0, 길이=15, 누적=261, 점검='정수점검', 비고='Not Null default 0')
    공제가능한금액: int = ERSField(default=0, 길이=15, 누적=276, 점검='정수점검', 비고='Not Null default 0')
    공제율_분자: int = ERSField(default=0, 길이=5, 누적=281, 점검='3', 비고='Not Null default 0')
    공제율_분모: int = ERSField(default=0, 길이=5, 누적=286, 점검='103', 비고='Not Null default 0')
    공제대상금액: int = ERSField(default=0, 길이=15, 누적=301, 점검='정수점검', 비고='Not Null default 0')
    공제대상세액: int = ERSField(default=0, 길이=13, 누적=314, 점검='정수점검', 비고='Not Null default 0')
    합계_공제받은세액: int = ERSField(default=0, 길이=13, 누적=327, 점검='정수점검', 비고='Not Null default 0')
    예정신고분_공제받은세액: int = ERSField(default=0, 길이=13, 누적=340, 점검='정수점검', 비고='Not Null default 0')
    월별조기분_공제받은세액: int = ERSField(default=0, 길이=13, 누적=353, 점검='정수점검', 비고='Not Null default 0')
    공제_납부할세액: int = ERSField(default=0, 길이=13, 누적=366, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=34, 누적=400, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_5_재활용폐자원_및_중고자동차매입세액공제신고서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M116300', 길이=7, 누적=9, 점검='M116300', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급자성명_상호: str = ERSField(default=None, 길이=60, 누적=75, 점검='', 비고='')
    공급자주민_사업자번호: str = ERSField(길이=13, 누적=88, 점검='', 비고='Not Null')
    건수: int = ERSField(default=0, 길이=11, 누적=99, 점검='양수점검', 비고='Not Null default 0')
    품명: str = ERSField(default=None, 길이=30, 누적=129, 점검='', 비고='')
    수량: int = ERSField(default=0, 길이=11, 누적=140, 점검='정수점검', 비고='Not Null default 0')
    취득금액: int = ERSField(default=0, 길이=13, 누적=153, 점검='정수점검', 비고='Not Null default 0')
    차량번호: str = ERSField(default=None, 길이=20, 누적=173, 점검='', 비고='')
    차대번호: str = ERSField(default=None, 길이=17, 누적=190, 점검='', 비고='')
    재활용폐자원공제유형구분코드: str = ERSField(길이=1, 누적=191, 점검='1,2 점검', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=9, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_6_일반과세전환시재고품및감가상각자산신고서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='V123', 길이=4, 누적=6, 점검='V123', 비고='Not Null')
    일반과세적용시기: date = ERSField(길이=8, 누적=14, 점검='일자형식점검', 비고='Not Null')
    일반과세전환통지: date = ERSField(default=None, 길이=8, 누적=22, 점검='일자형식점검', 비고='Null 허용')
    간이과세포기신고: date = ERSField(default=None, 길이=8, 누적=30, 점검='일자형식점검', 비고='Null 허용')
    기타내용: str = ERSField(default=None, 길이=30, 누적=60, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=40, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_6_일반과세전환시재고품및감가상각자산신고서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='V123', 길이=4, 누적=6, 점검='V123', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=12, 점검='숫자,길이점검', 비고='Not Null')
    품명: str = ERSField(길이=30, 누적=42, 점검='', 비고='Not Null')
    규격: str = ERSField(default=None, 길이=30, 누적=72, 점검='', 비고='Null 허용')
    수량: int = ERSField(default=0, 길이=11, 누적=83, 점검='정수점검', 비고='Not Null default 0')
    단가: int = ERSField(default=0, 길이=13, 누적=96, 점검='정수점검', 비고='Not Null default 0')
    금액_부가세포함: int = ERSField(default=0, 길이=13, 누적=109, 점검='정수점검', 비고='Not Null default 0')
    재고매입_납부세액: int = ERSField(default=0, 길이=13, 누적=122, 점검='정수점검', 비고='Not Null default 0')
    보관장소: str = ERSField(default=None, 길이=70, 누적=192, 점검='', 비고='Null 허용')
    취득일: date = ERSField(default=None, 길이=8, 누적=200, 점검='일자형식점검', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=50, 누적=250, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_7_부동산임대공급가액명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103600', 길이=7, 누적=9, 점검='I103600', 비고='Not Null')
    일련번호구분: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    부동산소재지: str = ERSField(default=None, 길이=70, 누적=85, 점검='', 비고='Null 허용')
    임대계약내용보증금합계: int = ERSField(default=0, 길이=15, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    임대계약내용월세등합계: int = ERSField(default=0, 길이=15, 누적=115, 점검='정수점검', 비고='Not Null default 0')
    임대료수입금액합계: int = ERSField(default=0, 길이=15, 누적=130, 점검='정수점검', 비고='Not Null default 0')
    임대료수입보증금이자합계: int = ERSField(default=0, 길이=15, 누적=145, 점검='정수점검', 비고='Not Null default 0')
    임대료수입월세등합계: int = ERSField(default=0, 길이=15, 누적=160, 점검='정수점검', 비고='Not Null default 0')
    임대인사업자등록번호: str = ERSField(길이=10, 누적=170, 점검='사업자번호CHECK+무세적, 길이점검', 비고='Not Null')
    임대건수: int = ERSField(default=0, 길이=6, 누적=176, 점검='정수점검', 비고='Not Null default 0')
    종사업자일련번호: str = ERSField(길이=4, 누적=180, 점검='종사업자일련번호 숫자,길이점검', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=70, 누적=250, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_7_부동산임대공급가액명세서_세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I103600', 길이=7, 누적=9, 점검='I103600', 비고='Not Null')
    일련번호구분: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=21, 점검='숫자,길이점검', 비고='Not Null')
    층주소: str = ERSField(길이=10, 누적=31, 점검='숫자점검', 비고='Not Null')
    동주소: str = ERSField(default=None, 길이=30, 누적=61, 점검='SPACE', 비고='Null 허용')
    호주소: str = ERSField(default=None, 길이=10, 누적=71, 점검='SPACE', 비고='Null 허용')
    건축물면적: str = ERSField(길이=10, 누적=81, 점검='실수점검', 비고='Not Null')
    임차인상호_성명: str = ERSField(길이=30, 누적=111, 점검='', 비고='Not Null')
    임차인사업자등록번호: str = ERSField(길이=13, 누적=124, 점검='사업자번호CHECK+무세적, 길이점검', 비고='Not Null')
    임대계약입주일자: date = ERSField(default=None, 길이=8, 누적=132, 점검='일자형식점검', 비고='Null 허용')
    임대계약퇴거일자: date = ERSField(default=None, 길이=8, 누적=140, 점검='일자형식점검', 비고='Null 허용')
    임대계약보증금: int = ERSField(default=0, 길이=13, 누적=153, 점검='정수점검', 비고='Not Null default 0')
    임대계약월세금액: int = ERSField(default=0, 길이=13, 누적=166, 점검='정수점검', 비고='Not Null default 0')
    임대료수입합계금액_과세표준: int = ERSField(default=0, 길이=13, 누적=179, 점검='정수점검', 비고='Not Null default 0')
    임대료보증금이자금액: int = ERSField(default=0, 길이=13, 누적=192, 점검='정수점검', 비고='Not Null default 0')
    임대료수입월세금액: int = ERSField(default=0, 길이=13, 누적=205, 점검='정수점검', 비고='Not Null default 0')
    종사업자일련번호: str = ERSField(길이=4, 누적=209, 점검='숫자(정수)점검', 비고='Not Null')
    임대차내역변경일자: date = ERSField(default=None, 길이=8, 누적=217, 점검='일자형식점검', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=33, 누적=250, 점검='', 비고='')


@dataclass(kw_only=True)
class v2_8_간이과세전환시재고품_및_감가상각자산신고서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='V130', 길이=4, 누적=6, 점검='V130', 비고='Not Null')
    과세유형: str = ERSField(길이=1, 누적=7, 점검='2', 비고='Not Null')
    적용기간시작일: date = ERSField(길이=8, 누적=15, 점검='일자형식점검', 비고='Not Null')
    적용기간종료일: date = ERSField(default=None, 길이=8, 누적=23, 점검='일자형식점검', 비고='Null 허용')
    통지일자: date = ERSField(default=None, 길이=8, 누적=31, 점검='일자형식점검', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=19, 누적=50, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_10_사업장별부가가치세과세표준_및_납부세액_환급세액신고명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I104500', 길이=7, 누적=9, 점검='I104500', 비고='Not Null')
    매출과세금액합계: int = ERSField(default=0, 길이=15, 누적=24, 점검='정수점검', 비고='Not Null default 0')
    매출과세세액합계: int = ERSField(default=0, 길이=15, 누적=39, 점검='정수점검', 비고='Not Null default 0')
    매출영세금액합계: int = ERSField(default=0, 길이=15, 누적=54, 점검='정수점검', 비고='Not Null default 0')
    매출영세세액합계: int = ERSField(default=0, 길이=15, 누적=69, 점검='정수점검', 비고='Not Null default 0')
    매입과세금액합계: int = ERSField(default=0, 길이=15, 누적=84, 점검='정수점검', 비고='Not Null default 0')
    매입과세세액합계: int = ERSField(default=0, 길이=15, 누적=99, 점검='정수점검', 비고='Not Null default 0')
    매입의제금액합계: int = ERSField(default=0, 길이=15, 누적=114, 점검='정수점검', 비고='Not Null default 0')
    매입의제세액합계: int = ERSField(default=0, 길이=15, 누적=129, 점검='정수점검', 비고='Not Null default 0')
    가산세합계: int = ERSField(default=0, 길이=15, 누적=144, 점검='정수점검', 비고='Not Null default 0')
    공제세액합계: int = ERSField(default=0, 길이=15, 누적=159, 점검='정수점검', 비고='Not Null default 0')
    납부_환급세액합계: int = ERSField(default=0, 길이=15, 누적=174, 점검='정수점검', 비고='Not Null default 0')
    내부거래_판매목적반출액합계: int = ERSField(default=0, 길이=15, 누적=189, 점검='정수점검', 비고='Not Null default 0')
    내부거래_판매목적반입액합계: int = ERSField(default=0, 길이=15, 누적=204, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=96, 누적=300, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_10_사업장별부가가치세과세표준_및_납부세액_환급세액신고명세서_세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I104500', 길이=7, 누적=9, 점검='I104500', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=19, 점검='사업자번호CHECK DIGIT +무세적', 비고='Not Null')
    사업장소재지: str = ERSField(default=None, 길이=70, 누적=89, 점검='', 비고='Null 허용')
    매출과세금액: int = ERSField(default=0, 길이=15, 누적=104, 점검='정수점검', 비고='Not Null default 0')
    매출과세세액: int = ERSField(default=0, 길이=13, 누적=117, 점검='정수점검', 비고='Not Null default 0')
    매출영세금액: int = ERSField(default=0, 길이=15, 누적=132, 점검='정수점검', 비고='Not Null default 0')
    매출영세세액: int = ERSField(default=0, 길이=13, 누적=145, 점검='정수점검', 비고='Not Null default 0')
    매입과세금액: int = ERSField(default=0, 길이=15, 누적=160, 점검='정수점검', 비고='Not Null default 0')
    매입과세세액: int = ERSField(default=0, 길이=13, 누적=173, 점검='정수점검', 비고='Not Null default 0')
    매입의제금액: int = ERSField(default=0, 길이=15, 누적=188, 점검='정수점검', 비고='Not Null default 0')
    매입의제세액: int = ERSField(default=0, 길이=13, 누적=201, 점검='정수점검', 비고='Not Null default 0')
    가산세: int = ERSField(default=0, 길이=13, 누적=214, 점검='정수점검', 비고='Not Null default 0')
    공제세액: int = ERSField(default=0, 길이=15, 누적=229, 점검='정수점검', 비고='Not Null default 0')
    납부_환급세액: int = ERSField(default=0, 길이=15, 누적=244, 점검='정수점검', 비고='Not Null default 0')
    내부거래_판매목적반출액: int = ERSField(default=0, 길이=15, 누적=259, 점검='정수점검', 비고='Not Null default 0')
    내부거래_판매목적반입액: int = ERSField(default=0, 길이=15, 누적=274, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=26, 누적=300, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_11_건물등_감가상각자산_취득명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103800', 길이=7, 누적=9, 점검='I103800', 비고='Not Null')
    건수_합계_고정자산: int = ERSField(default=0, 길이=11, 누적=20, 점검='양수점검', 비고='Not Null default 0')
    공급가액_합계_고정자산: int = ERSField(default=0, 길이=13, 누적=33, 점검='정수점검', 비고='Not Null default 0')
    세액_합계_고정자산: int = ERSField(default=0, 길이=13, 누적=46, 점검='정수점검', 비고='Not Null default 0')
    건수_건물_구축물: int = ERSField(default=0, 길이=11, 누적=57, 점검='양수점검', 비고='Not Null default 0')
    공급가액_건물_구축물: int = ERSField(default=0, 길이=13, 누적=70, 점검='정수점검', 비고='Not Null default 0')
    세액_건물_구축물: int = ERSField(default=0, 길이=13, 누적=83, 점검='정수점검', 비고='Not Null default 0')
    건수_기계장치: int = ERSField(default=0, 길이=11, 누적=94, 점검='양수점검', 비고='Not Null default 0')
    공급가액_기계장치: int = ERSField(default=0, 길이=13, 누적=107, 점검='정수점검', 비고='Not Null default 0')
    세액_기계장치: int = ERSField(default=0, 길이=13, 누적=120, 점검='정수점검', 비고='Not Null default 0')
    건수_차량운반구: int = ERSField(default=0, 길이=11, 누적=131, 점검='양수점검', 비고='Not Null default 0')
    공급가액_차량운반구: int = ERSField(default=0, 길이=13, 누적=144, 점검='정수점검', 비고='Not Null default 0')
    세액_차량운반구: int = ERSField(default=0, 길이=13, 누적=157, 점검='정수점검', 비고='Not Null default 0')
    건수_기타감가상각: int = ERSField(default=0, 길이=11, 누적=168, 점검='양수점검', 비고='Not Null default 0')
    공급가액_기타감가상각: int = ERSField(default=0, 길이=13, 누적=181, 점검='정수점검', 비고='Not Null default 0')
    세액_기타감가상각: int = ERSField(default=0, 길이=13, 누적=194, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=6, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_12_공제받지못할매입세액명세서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103300', 길이=7, 누적=9, 점검='I103300', 비고='Not Null')
    매수합계_세금계산서: int = ERSField(default=0, 길이=11, 누적=20, 점검='양수점검', 비고='Not Null default 0')
    공급가액합계_세금계산서: int = ERSField(default=0, 길이=15, 누적=35, 점검='정수점검', 비고='Not Null default 0')
    매입세액합계_세금계산서: int = ERSField(default=0, 길이=15, 누적=50, 점검='정수점검', 비고='Not Null default 0')
    공통매입공급가액합계_안분계산: int = ERSField(default=0, 길이=15, 누적=65, 점검='정수점검', 비고='Not Null default 0')
    공통매입세액합계_안분계산: int = ERSField(default=0, 길이=15, 누적=80, 점검='정수점검', 비고='Not Null default 0')
    불공제매입세액합계_안분계산: int = ERSField(default=0, 길이=15, 누적=95, 점검='정수점검', 비고='Not Null default 0')
    불공제매입세액총액합계_정산내역: int = ERSField(default=0, 길이=15, 누적=110, 점검='정수점검', 비고='Not Null default 0')
    기불공제매입세액합계_정산내역: int = ERSField(default=0, 길이=15, 누적=125, 점검='정수점검', 비고='Not Null default 0')
    가산_공제매입세액합계_정산내역: int = ERSField(default=0, 길이=15, 누적=140, 점검='정수점검', 비고='Not Null default 0')
    가산_공제매입세액합계_납부재계산: int = ERSField(default=0, 길이=15, 누적=155, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=45, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_12_공제받지못할매입세액명세서_합계_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I103300', 길이=7, 누적=9, 점검='I103300', 비고='Not Null')
    불공제사유구분: str = ERSField(길이=2, 누적=11, 점검='01,02,03,04,05,06,07', 비고='Not Null')
    세금계산서매수: int = ERSField(default=0, 길이=11, 누적=22, 점검='양수점검', 비고='Not Null default 0')
    공급가액: int = ERSField(default=0, 길이=13, 누적=35, 점검='정수점검', 비고='Not Null default 0')
    매입세액: int = ERSField(default=0, 길이=13, 누적=48, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=52, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_12_공제받지못할매입세액명세서_합계_공통매입세액안분계산내역(ERSRecord):
    자료구분: str = ERSField(default='19', 길이=2, 누적=2, 점검='19', 비고='Not Null')
    서식코드: str = ERSField(default='I103300', 길이=7, 누적=9, 점검='I103300', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공통매입공급가액: int = ERSField(default=0, 길이=13, 누적=28, 점검='정수점검', 비고='Not Null default 0')
    공통매입세액: int = ERSField(default=0, 길이=13, 누적=41, 점검='정수점검', 비고='Not Null default 0')
    총공급가액등: Decimal = ERSField(default='0', 길이=15, 누적=56, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    면세공급가액등: Decimal = ERSField(default='0', 길이=15, 누적=71, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    불공제매입세액: int = ERSField(default=0, 길이=13, 누적=84, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=16, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_12_공제받지못할매입세액명세서_합계_공통매입세액정산내역(ERSRecord):
    자료구분: str = ERSField(default='20', 길이=2, 누적=2, 점검='20', 비고='Not Null')
    서식코드: str = ERSField(default='I103300', 길이=7, 누적=9, 점검='I103300', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    총공통매입세액: int = ERSField(default=0, 길이=13, 누적=28, 점검='정수점검', 비고='Not Null default 0')
    면세사업확정비율: Decimal = ERSField(default='0', 길이=11, 누적=39, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=6)
    불공제매입세액총액: int = ERSField(default=0, 길이=13, 누적=52, 점검='정수점검', 비고='Not Null default 0')
    기불공제매입세액: int = ERSField(default=0, 길이=13, 누적=65, 점검='정수점검', 비고='Not Null default 0')
    가산_공제매입세액: int = ERSField(default=0, 길이=13, 누적=78, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=22, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_12_공제받지못할매입세액명세서_합계_납부세액환급세액재계산내역(ERSRecord):
    자료구분: str = ERSField(default='21', 길이=2, 누적=2, 점검='21', 비고='Not Null')
    서식코드: str = ERSField(default='I103300', 길이=7, 누적=9, 점검='I103300', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    재화매입세액: int = ERSField(default=0, 길이=13, 누적=28, 점검='정수점검', 비고='Not Null default 0')
    경감률_납부재계산: Decimal = ERSField(default='0', 길이=7, 누적=35, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=4)
    증가_감소면세비율: Decimal = ERSField(default='0', 길이=11, 누적=46, 점검='양의실수점검', 비고='Not Null default 0', 소수점길이=6)
    가산_공제매입세액: int = ERSField(default=0, 길이=13, 누적=59, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=41, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_13_전자화폐결제명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103500', 길이=7, 누적=9, 점검='I103500', 비고='Not Null')
    전자결제합계금액: int = ERSField(default=0, 길이=15, 누적=24, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=276, 누적=300, 점검='길이점검', 비고='SPACE')


@dataclass(kw_only=True)
class v2_13_전자화폐결제명세서_세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I103500', 길이=7, 누적=9, 점검='I103500', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    전자화폐명: str = ERSField(길이=60, 누적=75, 점검='길이점검', 비고='Not Null')
    구매자: str = ERSField(길이=60, 누적=135, 점검='', 비고='Not Null')
    결제일자: date = ERSField(길이=8, 누적=143, 점검='일자형식점검', 비고='Not Null')
    전자결제금액: int = ERSField(default=0, 길이=15, 누적=158, 점검='정수점검', 비고='Not Null default 0')
    결제처리번호: str = ERSField(길이=20, 누적=178, 점검='', 비고='Not Null')
    기타_구매자E_mail: str = ERSField(default=None, 길이=70, 누적=248, 점검='', 비고='Null 허용')
    가맹점번호: str = ERSField(길이=15, 누적=263, 점검='길이점검', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=37, 누적=300, 점검='길이점검', 비고='SPACE')


@dataclass(kw_only=True)
class v2_14_면세유류공급명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='J400100', 길이=7, 누적=9, 점검='J400100', 비고='Not Null')
    공급기간_시작일자: date = ERSField(길이=8, 누적=17, 점검='일자형식점검', 비고='Not Null')
    공급기간_종료일자: date = ERSField(길이=8, 누적=25, 점검='일자형식점검', 비고='Not Null')
    전체_수량합계: int = ERSField(default=0, 길이=11, 누적=36, 점검='정수점검', 비고='Not Null default 0')
    전체_세액합계: int = ERSField(default=0, 길이=15, 누적=51, 점검='정수점검', 비고='Not Null default 0')
    휘발유_수량합계: int = ERSField(default=0, 길이=11, 누적=62, 점검='정수점검', 비고='Not Null default 0')
    휘발유_세액합계: int = ERSField(default=0, 길이=15, 누적=77, 점검='정수점검', 비고='Not Null default 0')
    경유_수량합계: int = ERSField(default=0, 길이=11, 누적=88, 점검='정수점검', 비고='Not Null default 0')
    경유_세액합계: int = ERSField(default=0, 길이=15, 누적=103, 점검='정수점검', 비고='Not Null default 0')
    LPG_수량합계: int = ERSField(default=0, 길이=11, 누적=114, 점검='정수점검', 비고='Not Null default 0')
    LPG_세액합계: int = ERSField(default=0, 길이=15, 누적=129, 점검='정수점검', 비고='Not Null default 0')
    등유_수량합계: int = ERSField(default=0, 길이=11, 누적=140, 점검='정수점검', 비고='Not Null default 0')
    등유_세액합계: int = ERSField(default=0, 길이=15, 누적=155, 점검='정수점검', 비고='Not Null default 0')
    중유_수량합계: int = ERSField(default=0, 길이=11, 누적=166, 점검='정수점검', 비고='Not Null default 0')
    중유_세액합계: int = ERSField(default=0, 길이=15, 누적=181, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=119, 누적=300, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_14_면세유류공급명세서_세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='J400100', 길이=7, 누적=9, 점검='J400100', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    사업자_주민등록번호: str = ERSField(길이=13, 누적=28, 점검='사업자번호CHECK DIGIT+무세적 주민번호길이점검', 비고='Not Null')
    상호_법인명: str = ERSField(길이=60, 누적=88, 점검='길이점검', 비고='Not Null')
    수량합계_거래: int = ERSField(default=0, 길이=11, 누적=99, 점검='정수점검', 비고='Not Null default 0')
    금액합계_거래: int = ERSField(default=0, 길이=13, 누적=112, 점검='정수점검', 비고='Not Null default 0')
    휘발유_수량_거래: int = ERSField(default=0, 길이=11, 누적=123, 점검='정수점검', 비고='Not Null default 0')
    휘발유_세액_거래: int = ERSField(default=0, 길이=13, 누적=136, 점검='정수점검', 비고='Not Null default 0')
    경유_수량_거래: int = ERSField(default=0, 길이=11, 누적=147, 점검='정수점검', 비고='Not Null default 0')
    경유_세액_거래: int = ERSField(default=0, 길이=13, 누적=160, 점검='정수점검', 비고='Not Null default 0')
    LPG_수량_거래: int = ERSField(default=0, 길이=11, 누적=171, 점검='정수점검', 비고='Not Null default 0')
    LPG_세액_거래: int = ERSField(default=0, 길이=13, 누적=184, 점검='정수점검', 비고='Not Null default 0')
    등유_수량_거래: int = ERSField(default=0, 길이=11, 누적=195, 점검='정수점검', 비고='Not Null default 0')
    등유_세액_거래: int = ERSField(default=0, 길이=13, 누적=208, 점검='정수점검', 비고='Not Null default 0')
    중유_수량_거래: int = ERSField(default=0, 길이=11, 누적=219, 점검='정수점검', 비고='Not Null default 0')
    중유_세액_거래: int = ERSField(default=0, 길이=13, 누적=232, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=68, 누적=300, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_15_월별판매액합계표_농_축산_임_어업기자재_및_장애인보장구(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M200100', 길이=7, 누적=9, 점검='M200100', 비고='Not Null')
    월별: str = ERSField(길이=6, 누적=15, 점검='년월', 비고='Not Null')
    품명: str = ERSField(default=None, 길이=30, 누적=45, 점검='길이점검', 비고='Null 허용')
    판매수량: str = ERSField(길이=20, 누적=65, 점검='길이점검', 비고='Not Null')
    판매가액: int = ERSField(default=0, 길이=13, 누적=78, 점검='정수점검', 비고='Not Null default 0')
    판매가액_합계: int = ERSField(default=0, 길이=15, 누적=93, 점검='정수점검', 비고='Not Null default 0')
    월별판매합계표제출구분코드: str = ERSField(길이=2, 누적=95, 점검='‘01’,’02’', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=55, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_16_매입자발행세금계산서합계표_갑_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M118000', 길이=7, 누적=9, 점검='M118000', 비고='Not Null')
    매입처수: int = ERSField(default=0, 길이=7, 누적=16, 점검='양수점검', 비고='Not Null default 0')
    세금계산서매수_합계: int = ERSField(default=0, 길이=7, 누적=23, 점검='양수점검', 비고='Not Null default 0')
    공급가액_합계: int = ERSField(default=0, 길이=15, 누적=38, 점검='정수점검', 비고='Not Null default 0')
    세액_합계: int = ERSField(default=0, 길이=15, 누적=53, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=47, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_16_매입자발행세금계산서합계표_갑_세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M118000', 길이=7, 누적=9, 점검='M118000', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    거래자등록번호: str = ERSField(길이=10, 누적=25, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Not Null')
    거래자상호: str = ERSField(default=None, 길이=30, 누적=55, 점검='', 비고='Null 허용')
    세금계산서매수: int = ERSField(default=0, 길이=7, 누적=62, 점검='양수점검', 비고='Not Null default 0')
    공급가액: int = ERSField(default=0, 길이=13, 누적=75, 점검='정수점검', 비고='Not Null default 0')
    세액: int = ERSField(default=0, 길이=13, 누적=88, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=12, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_17_과세사업전환감가상각자산신고서_감가상각자산신고서면세사업자인적사항(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I102600', 길이=7, 누적=9, 점검='I102600', 비고='Not Null')
    과세사업사용_소비시기: date = ERSField(길이=8, 누적=17, 점검='일자형식점검', 비고='Not Null')
    상호_면세사업자: str = ERSField(길이=30, 누적=47, 점검='', 비고='Not Null')
    사업자등록번호_면세사업자: str = ERSField(길이=10, 누적=57, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Not Null')
    사업장소재지_면세사업자: str = ERSField(default=None, 길이=70, 누적=127, 점검='', 비고='Null 허용')
    전화번호_면세사업자: str = ERSField(default=None, 길이=14, 누적=141, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=9, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_17_과세사업전환감가상각자산신고서_감가상각자산신고서감가상각자산신고서(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I102600', 길이=7, 누적=9, 점검='I102600', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    감가상각자산_구분: str = ERSField(길이=2, 누적=17, 점검='01,02', 비고='Not Null')
    수량: int = ERSField(default=0, 길이=11, 누적=28, 점검='양수점검', 비고='Not Null default 0')
    취득일: date = ERSField(길이=8, 누적=36, 점검='일자형식점검', 비고='Not Null')
    면세불공제세액: int = ERSField(default=0, 길이=13, 누적=49, 점검='정수점검', 비고='Not Null default 0')
    과세공제매입세액: int = ERSField(default=0, 길이=13, 누적=62, 점검='정수점검', 비고='Not Null default 0')
    보관장소: str = ERSField(default=None, 길이=70, 누적=132, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=18, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_18_건물관리명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I104300', 길이=7, 누적=9, 점검='I104300', 비고='Not Null')
    일련번호구분: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    법정동코드: str = ERSField(default=None, 길이=10, 누적=25, 점검='길이점검', 비고='Null 허용')
    법정동명: str = ERSField(default=None, 길이=50, 누적=75, 점검='길이점검', 비고='Null 허용')
    산번지: str = ERSField(default=None, 길이=4, 누적=79, 점검='길이점검', 비고='Null 허용')
    번지: str = ERSField(default=None, 길이=4, 누적=83, 점검='숫자,길이점검', 비고='Null 허용')
    번지호: str = ERSField(default=None, 길이=4, 누적=87, 점검='숫자,길이점검', 비고='Null 허용')
    블록: str = ERSField(default=None, 길이=80, 누적=167, 점검='길이점검', 비고='Null 허용')
    동: str = ERSField(default=None, 길이=12, 누적=179, 점검='길이점검', 비고='Null 허용')
    동호: str = ERSField(default=None, 길이=6, 누적=185, 점검='길이점검', 비고='Null 허용')
    통: str = ERSField(default=None, 길이=4, 누적=191, 점검='숫자,길이점검', 비고='Null 허용')
    반: str = ERSField(default=None, 길이=4, 누적=193, 점검='숫자,길이점검', 비고='Null 허용')
    건물명: str = ERSField(길이=60, 누적=253, 점검='길이점검', 비고='Not Null')
    건물동명: str = ERSField(default=None, 길이=40, 누적=293, 점검='길이점검', 비고='Null 허용')
    관리비합계: int = ERSField(default=0, 길이=15, 누적=308, 점검='정수점검', 비고='Not Null default 0')
    건물소재지: str = ERSField(길이=200, 누적=508, 점검='길이점검', 비고='Not Null')
    관리건수: int = ERSField(default=0, 길이=6, 누적=514, 점검='정수점검', 비고='Not Null default 0')
    도로명코드: str = ERSField(default=None, 길이=12, 누적=526, 점검='길이점검', 비고='Null 허용')
    도로명: str = ERSField(default=None, 길이=50, 누적=576, 점검='길이점검', 비고='Null 허용')
    지하만있는_건물구분: str = ERSField(default=None, 길이=1, 누적=577, 점검='1 : 지하만 있는 경우 0 : 그외', 비고='Null 허용')
    건물번호_본번: int = ERSField(default=None, 길이=5, 누적=582, 점검='숫자,길이점검', 비고='Null 허용')
    건물번호_부번: int = ERSField(default=None, 길이=5, 누적=587, 점검='숫자,길이점검', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=13, 누적=600, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_18_건물관리명세서_세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I104300', 길이=7, 누적=9, 점검='I104300', 비고='Not Null')
    일련번호구분: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=21, 점검='숫자,길이점검', 비고='Not Null')
    집단상가층구분: str = ERSField(길이=2, 누적=23, 점검='01, 02, 03, 04, 05', 비고='Not Null')
    층: int = ERSField(default=0, 길이=4, 누적=27, 점검='숫자,길이점검', 비고='Not Null default 0')
    호실명: str = ERSField(default=None, 길이=30, 누적=57, 점검='', 비고='Null 허용')
    호번호: int = ERSField(default=0, 길이=4, 누적=61, 점검='숫자,길이점검', 비고='Not Null default 0')
    면적: Decimal = ERSField(default='0', 길이=9, 누적=70, 점검='실수숫자,길이점검', 비고='Not Null default 0', 소수점길이=1)
    사업자등록번호: str = ERSField(길이=13, 누적=83, 점검='사업자번호CHECK+무세적, 주민번호길이점검', 비고='Not Null')
    상호_성명: str = ERSField(길이=30, 누적=113, 점검='', 비고='Not Null')
    입주일: date = ERSField(default=None, 길이=8, 누적=121, 점검='일자형식점검', 비고='Null 허용')
    퇴거일: date = ERSField(default=None, 길이=8, 누적=129, 점검='일자형식점검', 비고='Null 허용')
    관리비: int = ERSField(default=0, 길이=13, 누적=142, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=58, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_19_사업자단위과세의_사업장별부가가치세과세표준및납부세액_환급세액신고명세서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103900', 길이=7, 누적=9, 점검='I103900', 비고='Not Null')
    사업자단위과세승인번호: str = ERSField(default=None, 길이=7, 누적=16, 점검='공백', 비고='')
    매출과세세금계산서과표합계: int = ERSField(default=0, 길이=15, 누적=31, 점검='정수점검', 비고='Not Null default 0')
    매출과세세금계산서세액합계: int = ERSField(default=0, 길이=15, 누적=46, 점검='정수점검', 비고='Not Null default 0')
    매출과세기타과표합계: int = ERSField(default=0, 길이=15, 누적=61, 점검='정수점검', 비고='Not Null default 0')
    매출기타세액합계: int = ERSField(default=0, 길이=15, 누적=76, 점검='정수점검', 비고='Not Null default 0')
    매출영세세금계산서과표합계: int = ERSField(default=0, 길이=15, 누적=91, 점검='정수점검', 비고='Not Null default 0')
    매출영세기타과표합계: int = ERSField(default=0, 길이=15, 누적=106, 점검='정수점검', 비고='Not Null default 0')
    과세표준합계: int = ERSField(default=0, 길이=15, 누적=121, 점검='정수점검', 비고='Not Null default 0')
    매입과세금액합계: int = ERSField(default=0, 길이=15, 누적=136, 점검='정수점검', 비고='Not Null default 0')
    매입과세세액합계: int = ERSField(default=0, 길이=15, 누적=151, 점검='정수점검', 비고='Not Null default 0')
    매입의제금액합계: int = ERSField(default=0, 길이=15, 누적=166, 점검='정수점검', 비고='Not Null default 0')
    매입의제세액합계: int = ERSField(default=0, 길이=15, 누적=181, 점검='정수점검', 비고='Not Null default 0')
    가산세액계: int = ERSField(default=0, 길이=15, 누적=196, 점검='정수점검', 비고='Not Null default 0')
    공제세액합계: int = ERSField(default=0, 길이=15, 누적=211, 점검='정수점검', 비고='Not Null default 0')
    차감납부할세액합계: int = ERSField(default=0, 길이=15, 누적=226, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=174, 누적=400, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_19_사업자단위과세의_사업장별부가가치세과세표준및납부세액_환급세액신고명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I103900', 길이=7, 누적=9, 점검='I103900', 비고='Not Null')
    단위사업장적용번호: int = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    상호_법인명: str = ERSField(default=None, 길이=60, 누적=73, 점검='', 비고='Null 허용')
    사업장소재지: str = ERSField(default=None, 길이=70, 누적=143, 점검='', 비고='Null 허용')
    매출과세세금계산서과표: int = ERSField(default=0, 길이=15, 누적=158, 점검='정수점검', 비고='Not Null default 0')
    매출과세세금계산서세액: int = ERSField(default=0, 길이=15, 누적=173, 점검='정수점검', 비고='Not Null default 0')
    매출과세기타과표: int = ERSField(default=0, 길이=15, 누적=188, 점검='정수점검', 비고='Not Null default 0')
    매출과세기타세액: int = ERSField(default=0, 길이=15, 누적=203, 점검='정수점검', 비고='Not Null default 0')
    매출영세세금계산서과표: int = ERSField(default=0, 길이=15, 누적=218, 점검='정수점검', 비고='Not Null default 0')
    매출영세기타과표: int = ERSField(default=0, 길이=15, 누적=233, 점검='정수점검', 비고='Not Null default 0')
    과세표준: int = ERSField(default=0, 길이=15, 누적=248, 점검='정수점검', 비고='Not Null default 0')
    매입과세표준: int = ERSField(default=0, 길이=15, 누적=263, 점검='정수점검', 비고='Not Null default 0')
    매입과세세액: int = ERSField(default=0, 길이=15, 누적=278, 점검='정수점검', 비고='Not Null default 0')
    매입의제표준: int = ERSField(default=0, 길이=15, 누적=293, 점검='정수점검', 비고='Not Null default 0')
    매입의제매입세액: int = ERSField(default=0, 길이=15, 누적=308, 점검='정수점검', 비고='Not Null default 0')
    가산세: int = ERSField(default=0, 길이=15, 누적=323, 점검='정수점검', 비고='Not Null default 0')
    공제세액: int = ERSField(default=0, 길이=15, 누적=338, 점검='정수점검', 비고='Not Null default 0')
    차감납부할세액: int = ERSField(default=0, 길이=15, 누적=353, 점검='정수점검', 비고='Not Null default 0')
    사업장소재지_도로명주소: str = ERSField(default=None, 길이=200, 누적=553, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=47, 누적=600, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_20_현금매출명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103700', 길이=7, 누적=9, 점검='I103700', 비고='Not Null')
    현금매출사업자구분: str = ERSField(default=None, 길이=2, 누적=11, 점검='사용않함', 비고='space')
    합계건수: int = ERSField(default=0, 길이=11, 누적=22, 점검='양수점검', 비고='Not Null default 0')
    합계금액: int = ERSField(default=0, 길이=15, 누적=37, 점검='정수점검', 비고='Not Null default 0')
    건수_세금계산서: int = ERSField(default=0, 길이=11, 누적=48, 점검='양수점검', 비고='Not Null default 0')
    금액_세금계산서: int = ERSField(default=0, 길이=15, 누적=63, 점검='정수점검', 비고='Not Null default 0')
    건수_신용카드: int = ERSField(default=0, 길이=11, 누적=74, 점검='양수점검', 비고='Not Null default 0')
    금액_신용카드: int = ERSField(default=0, 길이=15, 누적=89, 점검='정수점검', 비고='Not Null default 0')
    건수_현금영수증: int = ERSField(default=0, 길이=11, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    금액_현금영수증: int = ERSField(default=0, 길이=15, 누적=115, 점검='정수점검', 비고='Not Null default 0')
    건수_현금매출: int = ERSField(default=0, 길이=11, 누적=126, 점검='정수점검', 비고='Not Null default 0')
    금액_현금매출: int = ERSField(default=0, 길이=15, 누적=141, 점검='정수점검', 비고='Not Null default 0')
    공급대가합계금액: int = ERSField(default=0, 길이=15, 누적=156, 점검='정수점검', 비고='Not Null default 0')
    부가세합계금액: int = ERSField(default=0, 길이=15, 누적=171, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=79, 누적=250, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_20_현금매출명세서_세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I103700', 길이=7, 누적=9, 점검='I103700', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    의뢰인_주민등록번호_또는_사업자등록번호: str = ERSField(길이=13, 누적=28, 점검='사업자번호 CHECK DIGIT+무세적,주민번호 길이점검', 비고='Not Null')
    의뢰인_상호_또는_성명: str = ERSField(길이=30, 누적=58, 점검='', 비고='Not Null')
    거래일자: date = ERSField(길이=8, 누적=66, 점검='일자형식점검', 비고='Not Null')
    공급대가: int = ERSField(default=0, 길이=13, 누적=79, 점검='양수점검', 비고='Not Null default 0')
    공급가액: int = ERSField(default=0, 길이=13, 누적=92, 점검='양수점검', 비고='Not Null default 0')
    부가세: int = ERSField(default=0, 길이=13, 누적=105, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=145, 누적=250, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_21_고금_의제매입세액_공제_신고서_고금의제매입세액공제신고서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M120900', 길이=7, 누적=9, 점검='M120900', 비고='Not Null')
    품목수: int = ERSField(default=0, 길이=11, 누적=20, 점검='양수점검', 비고='Not Null default 0')
    매입현황_매입처수: int = ERSField(default=0, 길이=11, 누적=31, 점검='양수점검', 비고='Not Null default 0')
    매입현황_취득금액총액: int = ERSField(default=0, 길이=15, 누적=46, 점검='정수점검', 비고='Not Null default 0')
    매출현황_매출처수: int = ERSField(default=0, 길이=11, 누적=57, 점검='양수점검', 비고='Not Null default 0')
    매출현황_공급가액: int = ERSField(default=0, 길이=15, 누적=72, 점검='정수점검', 비고='Not Null default 0')
    매출현황_매출세액: int = ERSField(default=0, 길이=13, 누적=85, 점검='양수점검', 비고='Not Null default 0')
    당기고금매출액_합계: int = ERSField(default=0, 길이=15, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    당기고금매출액_예정분: int = ERSField(default=0, 길이=15, 누적=115, 점검='정수점검', 비고='Not Null default 0')
    당기고금매출액_확정분: int = ERSField(default=0, 길이=15, 누적=130, 점검='정수점검', 비고='Not Null default 0')
    취득가액한도계산_한도율: int = ERSField(default=0, 길이=5, 누적=135, 점검='정수점검', 비고='Not Null default 0', 소수점길이=2)
    취득가액한도계산_한도액: int = ERSField(default=0, 길이=15, 누적=150, 점검='정수점검', 비고='Not Null default 0')
    당기이전고금매입액_합계: int = ERSField(default=0, 길이=15, 누적=165, 점검='정수점검', 비고='Not Null default 0')
    당기이전고금매입액_직전기이전매입분: int = ERSField(default=0, 길이=15, 누적=180, 점검='정수점검', 비고='Not Null default 0')
    당기이전고금매입액_당기매입분: int = ERSField(default=0, 길이=15, 누적=195, 점검='정수점검', 비고='Not Null default 0')
    공제대상취득가액: int = ERSField(default=0, 길이=15, 누적=210, 점검='정수점검', 비고='Not Null default 0')
    공제대상세액_공제율_분자: int = ERSField(default=0, 길이=5, 누적=215, 점검='3', 비고='Not Null default 0')
    공제대상세액_공제율_분모: int = ERSField(default=0, 길이=5, 누적=220, 점검='103', 비고='Not Null default 0')
    공제대상세액_공제대상세액: int = ERSField(default=0, 길이=13, 누적=233, 점검='정수점검', 비고='Not Null default 0')
    납부세액: int = ERSField(default=0, 길이=13, 누적=246, 점검='정수점검', 비고='Not Null default 0')
    실제적용받을수있는매입세액: int = ERSField(default=0, 길이=13, 누적=259, 점검='정수점검', 비고='Not Null default 0')
    예정신고시공제받은매입세액: int = ERSField(default=0, 길이=13, 누적=272, 점검='정수점검', 비고='Not Null default 0')
    공제_납부할세액: int = ERSField(default=0, 길이=13, 누적=285, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=65, 누적=350, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_21_고금_의제매입세액_공제_신고서_고금_매입_매출_명세서세부내용(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M120900', 길이=7, 누적=9, 점검='M120900', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='', 비고='Not Null')
    매입일련번호: str = ERSField(길이=8, 누적=23, 점검='', 비고='Not Null')
    품목: str = ERSField(길이=30, 누적=52, 점검='', 비고='Not Null')
    품위: str = ERSField(길이=2, 누적=55, 점검='24,18,14,08,99', 비고='Not Null')
    수량: int = ERSField(길이=11, 누적=66, 점검='양수점검', 비고='Not Null')
    중량: Decimal = ERSField(default='0', 길이=13, 누적=79, 점검='정수점검', 비고='Not Null default 0', 소수점길이=2)
    매입현황_매입자_상호: str = ERSField(default=None, 길이=60, 누적=139, 점검='', 비고='')
    매입현황_주민_사업자번호: str = ERSField(길이=13, 누적=152, 점검='사업자번호 CHECK DIGIT+무세적,주민번호 길이점검 매입현황_취득가액이 없는 경우 Null허용', 비고='Not Null')
    매입현황_취득가액: int = ERSField(default=0, 길이=13, 누적=165, 점검='정수점검', 비고='Not Null default 0')
    매출현황_매출처_상호: str = ERSField(default=None, 길이=60, 누적=225, 점검='', 비고='')
    매출현황_주민_사업자번호: str = ERSField(길이=13, 누적=238, 점검='사업자번호 CHECK DIGIT+무세적,주민번호 길이점검 매출현황_공급가액이 없는 경우 Null허용', 비고='Not Null')
    매출현황_공급가액: int = ERSField(default=0, 길이=13, 누적=251, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=49, 누적=300, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_22_과세표준및세액의_결정_경정청구서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='A102700', 길이=7, 누적=9, 점검='A102700', 비고='Not Null')
    법정신고일: date = ERSField(길이=8, 누적=17, 점검='일자형식점검', 비고='Not Null')
    최초신고일: date = ERSField(길이=8, 누적=25, 점검='일자형식점검', 비고='Not Null')
    경정_결정청구이유: str = ERSField(default=None, 길이=70, 누적=95, 점검='길이점검', 비고='')
    과세표준금액_최초: int = ERSField(default=0, 길이=15, 누적=110, 점검='정수점검', 비고='Not Null default 0')
    과세표준금액_경정: int = ERSField(default=0, 길이=15, 누적=125, 점검='양수점검', 비고='Not Null default 0')
    산출세액_최초: int = ERSField(default=0, 길이=15, 누적=140, 점검='정수점검', 비고='Not Null default 0')
    산출세액_경정: int = ERSField(default=0, 길이=15, 누적=155, 점검='정수점검', 비고='Not Null default 0')
    가산세액_최초: int = ERSField(default=0, 길이=15, 누적=170, 점검='정수점검', 비고='Not Null default 0')
    가산세액_경정: int = ERSField(default=0, 길이=15, 누적=185, 점검='정수점검', 비고='Not Null default 0')
    공제및감면세액_최초: int = ERSField(default=0, 길이=15, 누적=200, 점검='정수점검', 비고='Not Null default 0')
    공제및감면세액_경정: int = ERSField(default=0, 길이=15, 누적=215, 점검='정수점검', 비고='Not Null default 0')
    납부할세액_최초: int = ERSField(default=0, 길이=15, 누적=230, 점검='정수점검', 비고='Not Null default 0')
    납부할세액_경정: int = ERSField(default=0, 길이=15, 누적=245, 점검='정수점검', 비고='Not Null default 0')
    농어촌특별세납부할세액_최초: int = ERSField(default=0, 길이=15, 누적=260, 점검='0', 비고='Not Null default 0')
    농어촌특별세납부할세액_경정: int = ERSField(default=0, 길이=15, 누적=275, 점검='0', 비고='Not Null default 0')
    교육세납부할세액_최초: int = ERSField(default=0, 길이=15, 누적=290, 점검='0', 비고='Not Null default 0')
    교육세납부할세액_경정: int = ERSField(default=0, 길이=15, 누적=305, 점검='0', 비고='Not Null default 0')
    경정청구이유코드1: str = ERSField(길이=7, 누적=312, 점검='공통분류코드 (CMN_CLSF_CD)', 비고='Not Null')
    경정청구이유코드2: str = ERSField(길이=7, 누적=319, 점검='공통분류코드 (CMN_CLSF_CD)', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=81, 누적=400, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_23_과세표준수정신고서_및_추가자진납부계산서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='A102600', 길이=7, 누적=9, 점검='A102600', 비고='Not Null')
    법정신고일: date = ERSField(길이=8, 누적=17, 점검='일자형식점검', 비고='Not Null')
    최초신고일: date = ERSField(길이=8, 누적=25, 점검='일자형식점검', 비고='Not Null')
    수정신고사유: str = ERSField(길이=70, 누적=95, 점검='길이점검', 비고='Not Null')
    과세표준금액_최초: int = ERSField(default=0, 길이=15, 누적=110, 점검='정수점검', 비고='Not Null default 0')
    과세표준금액_수정: int = ERSField(default=0, 길이=15, 누적=125, 점검='양수점검', 비고='Not Null default 0')
    산출세액_최초: int = ERSField(default=0, 길이=15, 누적=140, 점검='정수점검', 비고='Not Null default 0')
    산출세액_수정: int = ERSField(default=0, 길이=15, 누적=155, 점검='정수점검', 비고='Not Null default 0')
    가산세액_최초: int = ERSField(default=0, 길이=15, 누적=170, 점검='정수점검', 비고='Not Null default 0')
    가산세액_수정: int = ERSField(default=0, 길이=15, 누적=185, 점검='정수점검', 비고='Not Null default 0')
    공제및감면세액_최초: int = ERSField(default=0, 길이=15, 누적=200, 점검='정수점검', 비고='Not Null default 0')
    공제및감면세액_수정: int = ERSField(default=0, 길이=15, 누적=215, 점검='정수점검', 비고='Not Null default 0')
    납부할세액_최초: int = ERSField(default=0, 길이=15, 누적=230, 점검='정수점검', 비고='Not Null default 0')
    납부할세액_수정: int = ERSField(default=0, 길이=15, 누적=245, 점검='정수점검', 비고='Not Null default 0')
    기납부세액_최초: int = ERSField(default=0, 길이=15, 누적=260, 점검='정수점검', 비고='Not Null default 0')
    기납부세액_수정: int = ERSField(default=0, 길이=15, 누적=275, 점검='정수점검', 비고='Not Null default 0')
    자진납부세액_최초: int = ERSField(default=0, 길이=15, 누적=290, 점검='정수점검', 비고='Not Null default 0')
    자진납부세액_수정: int = ERSField(default=0, 길이=15, 누적=305, 점검='정수점검', 비고='Not Null default 0')
    추가자진납부세액_최초: int = ERSField(default=0, 길이=15, 누적=320, 점검='정수점검', 비고='Not Null default 0')
    추가자진납부세액_수정: int = ERSField(default=0, 길이=15, 누적=335, 점검='정수점검', 비고='Not Null default 0')
    농어촌특별세자진납부세액_최초: int = ERSField(default=0, 길이=15, 누적=350, 점검='0', 비고='Not Null default 0')
    농어촌특별세자진납부세액_수정: int = ERSField(default=0, 길이=15, 누적=365, 점검='0', 비고='Not Null default 0')
    농어촌특별세추가자진납부세액: int = ERSField(default=0, 길이=15, 누적=380, 점검='0', 비고='Not Null default 0')
    교육세자진납부세액_최초: int = ERSField(default=0, 길이=15, 누적=395, 점검='0', 비고='Not Null default 0')
    교육세자진납부세액_수정: int = ERSField(default=0, 길이=15, 누적=410, 점검='0', 비고='Not Null default 0')
    교육세추가자진납부세액: int = ERSField(default=0, 길이=15, 누적=425, 점검='0', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=5, 누적=430, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_24_전자세금계산서_발급세액공제신고서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I103100', 길이=7, 누적=9, 점검='I103100', 비고='Not Null')
    전자세금계산서발급건수: int = ERSField(default=0, 길이=7, 누적=16, 점검='양수점검', 비고='Not Null default 0')
    공제가능세액: int = ERSField(default=0, 길이=13, 누적=29, 점검='정수점검', 비고='Not Null default 0')
    해당공제세액: int = ERSField(default=0, 길이=13, 누적=42, 점검='정수점검', 비고='Not Null default 0')
    기공제세액: int = ERSField(default=0, 길이=13, 누적=55, 점검='정수점검', 비고='Not Null default 0')
    해당과세기간공제한도액: int = ERSField(default=0, 길이=13, 누적=68, 점검='정수점검', 비고='Not Null default 0')
    직전기3억미만_개인사업자_여부: str = ERSField(길이=1, 누적=69, 점검='‘Y’또는’N’', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=31, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_25_일반_간이과세전환시재고품등신고서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I102700', 길이=7, 누적=9, 점검='I102700', 비고='Not Null')
    과세유형: str = ERSField(길이=2, 누적=11, 점검='04, 05', 비고='Not Null')
    일반과세적용시기: date = ERSField(default=None, 길이=8, 누적=19, 점검='일자형식점검', 비고='Null 허용')
    일반과세적용사유: str = ERSField(default=None, 길이=2, 누적=21, 점검='01,02,03', 비고='Null 허용')
    간이과세적용기간시작일: date = ERSField(default=None, 길이=8, 누적=29, 점검='일자형식점검', 비고='Null 허용')
    간이과세적용기간종료일: date = ERSField(default=None, 길이=8, 누적=37, 점검='일자형식점검', 비고='Null 허용')
    간이과세전환통지일자: date = ERSField(default=None, 길이=8, 누적=45, 점검='일자형식점검', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=55, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_25_일반_간이과세전환시재고품등신고서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I102700', 길이=7, 누적=9, 점검='I102700', 비고='Not Null')
    과세유형: str = ERSField(길이=2, 누적=11, 점검='04, 05', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=17, 점검='숫자,길이점검', 비고='Not Null')
    품명: str = ERSField(길이=30, 누적=47, 점검='', 비고='Not Null')
    규격: str = ERSField(default=None, 길이=30, 누적=77, 점검='', 비고='Null 허용')
    수량: int = ERSField(default=0, 길이=11, 누적=88, 점검='정수점검', 비고='Not Null default 0')
    단가: int = ERSField(default=0, 길이=13, 누적=101, 점검='정수점검', 비고='Not Null default 0')
    금액: int = ERSField(default=0, 길이=13, 누적=114, 점검='정수점검', 비고='Not Null default 0')
    재고매입세액_또는_재고납부세액: int = ERSField(default=0, 길이=13, 누적=127, 점검='정수점검', 비고='Not Null default 0')
    보관장소: str = ERSField(default=None, 길이=70, 누적=197, 점검='', 비고='Null 허용')
    취득일: date = ERSField(default=None, 길이=8, 누적=205, 점검='일자형식점검', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=45, 누적=250, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_26_세액공제신청서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M100100', 길이=7, 누적=9, 점검='M100100', 비고='Not Null')
    코드: str = ERSField(길이=3, 누적=12, 점검='312', 비고='Not Null')
    공제율: Decimal = ERSField(default='0', 길이=5, 누적=17, 점검='0', 비고='Not Null default 0', 소수점길이=2)
    대상세액: int = ERSField(default=0, 길이=13, 누적=30, 점검='0', 비고='Not Null default 0')
    공제세액: int = ERSField(default=0, 길이=13, 누적=43, 점검='양수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=57, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_26_세액공제신청서_내국신용장_구매확인서전자발급명세서합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I105600', 길이=7, 누적=9, 점검='I105600', 비고='Not Null')
    건수_합계: int = ERSField(default=0, 길이=7, 누적=16, 점검='정수점검', 비고='Not Null default 0')
    해당금액_합계: int = ERSField(default=0, 길이=15, 누적=31, 점검='정수점검', 비고='Not Null default 0')
    내국신용장_건수_합계: int = ERSField(default=0, 길이=7, 누적=38, 점검='정수점검', 비고='Not Null default 0')
    내국신용장_금액_합계: int = ERSField(default=0, 길이=15, 누적=53, 점검='정수점검', 비고='Not Null default 0')
    구매확인서_건수_합계: int = ERSField(default=0, 길이=7, 누적=60, 점검='정수점검', 비고='Not Null default 0')
    구매확인서_금액_합계: int = ERSField(default=0, 길이=15, 누적=75, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=25, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_26_세액공제신청서_내국신용장_구매확인서전자발급명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I105600', 길이=7, 누적=9, 점검='I105600', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    서류구분: str = ERSField(길이=1, 누적=16, 점검='L,A', 비고='Not Null')
    서류번호: str = ERSField(길이=35, 누적=51, 점검='숫자,길이점검', 비고='Not Null')
    발급일자: date = ERSField(길이=8, 누적=59, 점검='일자점검', 비고='Not Null')
    공급받는자_사업자등록번호: str = ERSField(길이=10, 누적=69, 점검='사업자번호 CHECK DIGIT +무세적', 비고='Not Null')
    금액: int = ERSField(default=0, 길이=15, 누적=84, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=16, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_28_원산지확인서발급세액공제신고서_발급세액공제신고서합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M115900', 길이=7, 누적=9, 점검='M115900', 비고='Not Null')
    원산지확인서발급건수: int = ERSField(default=0, 길이=7, 누적=16, 점검='양수점검', 비고='Not Null default 0')
    공제가능세액: int = ERSField(default=0, 길이=13, 누적=29, 점검='정수점검', 비고='Not Null default 0')
    해당공제세액: int = ERSField(default=0, 길이=13, 누적=42, 점검='정수점검', 비고='Not Null default 0')
    기공제세액: int = ERSField(default=0, 길이=13, 누적=55, 점검='정수점검', 비고='Not Null default 0')
    해당과세기간공제한도액: int = ERSField(default=0, 길이=13, 누적=68, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=32, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_28_원산지확인서발급세액공제신고서_발급세액공제신고서명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M115900', 길이=7, 누적=9, 점검='M115900', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    원산지확인서_일련번호: str = ERSField(길이=6, 누적=21, 점검='숫자,길이점검', 비고='Not Null')
    원산지확인서_작성일: date = ERSField(길이=8, 누적=29, 점검='일자형식점검', 비고='Not Null')
    상호_법인명: str = ERSField(길이=30, 누적=59, 점검='', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=69, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Not Null')
    공급일: date = ERSField(길이=8, 누적=77, 점검='일자형식점검', 비고='Not Null')
    품명: str = ERSField(길이=30, 누적=107, 점검='', 비고='Not Null')
    수량: int = ERSField(default=0, 길이=11, 누적=118, 점검='정수점검', 비고='Not Null default 0')
    세금계산서_작성일: date = ERSField(길이=8, 누적=126, 점검='일자형식점검', 비고='Not Null')
    공급가액: int = ERSField(default=0, 길이=13, 누적=139, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=11, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_29_동물진료용역매출명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I104100', 길이=7, 누적=9, 점검='I104100', 비고='Not Null')
    면세사유구분: str = ERSField(길이=2, 누적=11, 점검='01,02,03,04,05', 비고='Not Null')
    공급건수: int = ERSField(default=0, 길이=11, 누적=22, 점검='양수점검', 비고='Not Null default 0')
    공급가액: int = ERSField(default=0, 길이=13, 누적=35, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=65, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_30_영세율매출명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I104000', 길이=7, 누적=9, 점검='I104000', 비고='Not Null')
    직접수출: int = ERSField(default=0, 길이=15, 누적=24, 점검='정수점검', 비고='Not Null default 0')
    중계무역위탁판매: int = ERSField(default=0, 길이=15, 누적=39, 점검='정수점검', 비고='Not Null default 0')
    내국신용구매확인: int = ERSField(default=0, 길이=15, 누적=54, 점검='정수점검', 비고='Not Null default 0')
    한국국제협력단: int = ERSField(default=0, 길이=15, 누적=69, 점검='정수점검', 비고='Not Null default 0')
    수탁가공무역: int = ERSField(default=0, 길이=15, 누적=84, 점검='정수점검', 비고='Not Null default 0')
    국외에서제공하는용역: int = ERSField(default=0, 길이=15, 누적=99, 점검='정수점검', 비고='Not Null default 0')
    선박항공기외국항행: int = ERSField(default=0, 길이=15, 누적=114, 점검='정수점검', 비고='Not Null default 0')
    국제복합운송계약: int = ERSField(default=0, 길이=15, 누적=129, 점검='정수점검', 비고='Not Null default 0')
    국내비거주외국법인: int = ERSField(default=0, 길이=15, 누적=144, 점검='정수점검', 비고='Not Null default 0')
    수출재화임가공용역: int = ERSField(default=0, 길이=15, 누적=159, 점검='정수점검', 비고='Not Null default 0')
    외국항행선박항공기등: int = ERSField(default=0, 길이=15, 누적=174, 점검='정수점검', 비고='Not Null default 0')
    국내주재외교공관등: int = ERSField(default=0, 길이=15, 누적=189, 점검='정수점검', 비고='Not Null default 0')
    관광진흥법에따른: int = ERSField(default=0, 길이=15, 누적=204, 점검='정수점검', 비고='Not Null default 0')
    외국인전용판매장또는: int = ERSField(default=0, 길이=15, 누적=219, 점검='정수점검', 비고='Not Null default 0')
    외교관등에게공급: int = ERSField(default=0, 길이=15, 누적=234, 점검='정수점검', 비고='Not Null default 0')
    외국인환자유치용역: int = ERSField(default=0, 길이=15, 누적=249, 점검='정수점검', 비고='Not Null default 0')
    부가세법에_따른_합계: int = ERSField(default=0, 길이=15, 누적=264, 점검='정수점검', 비고='Not Null default 0')
    방위산업물자및비상대비자원관리: int = ERSField(default=0, 길이=15, 누적=279, 점검='정수점검', 비고='Not Null default 0')
    도시철도건설용역: int = ERSField(default=0, 길이=15, 누적=294, 점검='정수점검', 비고='Not Null default 0')
    국가지방자치단체에공급사회기반시설등: int = ERSField(default=0, 길이=15, 누적=309, 점검='정수점검', 비고='Not Null default 0')
    장애인용보장구및장애인용정보통신기기등: int = ERSField(default=0, 길이=15, 누적=324, 점검='정수점검', 비고='Not Null default 0')
    농민또는임업종사자에게공급하는농축임업용기자재: int = ERSField(default=0, 길이=15, 누적=339, 점검='정수점검', 비고='Not Null default 0')
    외국인관광객등에게공급하는_재화: int = ERSField(default=0, 길이=15, 누적=354, 점검='정수점검', 비고='Not Null default 0')
    제주특별자치도면세품판매장: int = ERSField(default=0, 길이=15, 누적=369, 점검='정수점검', 비고='Not Null default 0')
    조특법및그밖의법률에_따른_합계: int = ERSField(default=0, 길이=15, 누적=384, 점검='정수점검', 비고='Not Null default 0')
    영세율적용공급실적총합계: int = ERSField(default=0, 길이=15, 누적=399, 점검='정수점검', 비고='Not Null default 0')
    군부대공급석유류: int = ERSField(default=0, 길이=15, 누적=414, 점검='정수점검', 비고='Not Null default 0')
    어민에게공급하는어업용기자재: int = ERSField(default=0, 길이=15, 누적=429, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=21, 누적=450, 점검='공란', 비고='space')


@dataclass(kw_only=True)
class v2_31_외국인관광객_면세물품_판매_및_환급실적명세서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M202300', 길이=7, 누적=9, 점검='M202300', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    면세판매장지정번호: str = ERSField(길이=8, 누적=21, 점검='', 비고='Not Null')
    합계_건수: int = ERSField(default=0, 길이=11, 누적=32, 점검='정수점검', 비고='Not Null default 0')
    합계_판매금액: int = ERSField(default=0, 길이=15, 누적=47, 점검='정수점검', 비고='Not Null default 0')
    합계_부가가치세: int = ERSField(default=0, 길이=15, 누적=62, 점검='정수점검', 비고='Not Null default 0')
    합계_개별소비세: int = ERSField(default=0, 길이=15, 누적=77, 점검='정수점검', 비고='Not Null default 0')
    합계_교육세: int = ERSField(default=0, 길이=15, 누적=92, 점검='정수점검', 비고='Not Null default 0')
    합계_농어촌특별세: int = ERSField(default=0, 길이=15, 누적=107, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=43, 누적=150, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_31_외국인관광객_면세물품_판매_및_환급실적명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M202300', 길이=7, 누적=9, 점검='M202300', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    일련번호: str = ERSField(길이=4, 누적=17, 점검='숫자,길이점검', 비고='Not Null')
    구매일련번호: str = ERSField(길이=20, 누적=37, 점검='', 비고='Not Null')
    판매일자: date = ERSField(길이=8, 누적=45, 점검='일자형식점검', 비고='Not Null')
    반출일자: date = ERSField(길이=8, 누적=53, 점검='일자형식점검', 비고='Not Null')
    반출승인번호: str = ERSField(길이=20, 누적=73, 점검='', 비고='Not Null')
    환급_송금일자: date = ERSField(길이=8, 누적=81, 점검='일자형식점검', 비고='Not Null')
    환급액: int = ERSField(default=0, 길이=15, 누적=96, 점검='정수점검', 비고='Not Null default 0')
    금액_판매금액: int = ERSField(default=0, 길이=15, 누적=111, 점검='정수점검', 비고='Not Null default 0')
    금액_부가가치세: int = ERSField(default=0, 길이=15, 누적=126, 점검='정수점검', 비고='Not Null default 0')
    금액_개별소비세: int = ERSField(default=0, 길이=15, 누적=141, 점검='정수점검', 비고='Not Null default 0')
    금액_교육세: int = ERSField(default=0, 길이=15, 누적=156, 점검='정수점검', 비고='Not Null default 0')
    금액_농어촌특별세: int = ERSField(default=0, 길이=15, 누적=171, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=29, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_32_구리스크랩등_매입세액공제신고서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M125200', 길이=7, 누적=9, 점검='M125200', 비고='Not Null')
    매입처수_합계: int = ERSField(default=0, 길이=7, 누적=16, 점검='양수점검', 비고='Not Null default 0')
    건수_합계: int = ERSField(default=0, 길이=11, 누적=27, 점검='양수점검', 비고='Not Null default 0')
    수량_합계: int = ERSField(default=0, 길이=11, 누적=38, 점검='정수점검', 비고='Not Null default 0')
    취득금액_합계: int = ERSField(default=0, 길이=15, 누적=53, 점검='정수점검', 비고='Not Null default 0')
    의제매입세액_합계: int = ERSField(default=0, 길이=15, 누적=68, 점검='정수점검', 비고='Not Null default 0')
    매입처수_영수증: int = ERSField(default=0, 길이=6, 누적=74, 점검='양수점검', 비고='Not Null default 0')
    건수_영수증: int = ERSField(default=0, 길이=11, 누적=85, 점검='양수점검', 비고='Not Null default 0')
    수량_영수증: int = ERSField(default=0, 길이=11, 누적=96, 점검='정수점검', 비고='Not Null default 0')
    취득금액_영수증: int = ERSField(default=0, 길이=15, 누적=111, 점검='정수점검', 비고='Not Null default 0')
    의제매입세액_영수증: int = ERSField(default=0, 길이=15, 누적=126, 점검='정수점검', 비고='Not Null default 0')
    매입처수_계산서: int = ERSField(default=0, 길이=6, 누적=132, 점검='양수점검', 비고='Not Null default 0')
    건수_계산서: int = ERSField(default=0, 길이=11, 누적=143, 점검='양수점검', 비고='Not Null default 0')
    수량_계산서: int = ERSField(default=0, 길이=11, 누적=154, 점검='정수점검', 비고='Not Null default 0')
    취득금액_계산서: int = ERSField(default=0, 길이=15, 누적=169, 점검='정수점검', 비고='Not Null default 0')
    의제매입세액_계산서: int = ERSField(default=0, 길이=15, 누적=184, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=16, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_32_구리스크랩등_매입세액공제신고서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M125200', 길이=7, 누적=9, 점검='M125200', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급자성명_상호: str = ERSField(default=None, 길이=60, 누적=75, 점검='', 비고='')
    공급자주민_사업자번호: str = ERSField(길이=13, 누적=88, 점검='', 비고='Not Null')
    건수: int = ERSField(default=0, 길이=11, 누적=99, 점검='양수점검', 비고='Not Null default 0')
    품명: str = ERSField(default=None, 길이=30, 누적=129, 점검='', 비고='')
    수량: int = ERSField(default=0, 길이=11, 누적=140, 점검='정수점검', 비고='Not Null default 0')
    취득금액: int = ERSField(default=0, 길이=13, 누적=153, 점검='정수점검', 비고='Not Null default 0')
    의제매입세액: int = ERSField(default=0, 길이=13, 누적=166, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=34, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_33_관세환급금등_명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I401500', 길이=7, 누적=9, 점검='I401500', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급일자: date = ERSField(길이=8, 누적=23, 점검='일자형식점검', 비고='Not Null')
    관세환급금액: int = ERSField(default=0, 길이=13, 누적=36, 점검='정수점검', 비고='Not Null default 0')
    상호_법인명: str = ERSField(길이=30, 누적=66, 점검='', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=76, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Not Null')
    내국신용장번호: str = ERSField(길이=30, 누적=106, 점검='', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=44, 누적=150, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_34_외국인물품_외교관면세판매기록표_판매_외교관면세판매기록표(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I402000', 길이=7, 누적=9, 점검='I402000', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급일자: date = ERSField(길이=8, 누적=23, 점검='일자형식점검', 비고='Not Null')
    공급받는자_성명: str = ERSField(default=None, 길이=20, 누적=43, 점검='', 비고='Null 허용')
    공급받는자_국적: str = ERSField(길이=2, 누적=45, 점검='국가코드 참조', 비고='Not Null')
    공급받는자_근무처: str = ERSField(default=None, 길이=30, 누적=75, 점검='', 비고='Null 허용')
    공급받는자_여권_외교관면세카드_주민등록번호: str = ERSField(길이=30, 누적=105, 점검='', 비고='Not Null')
    품목명: str = ERSField(길이=50, 누적=155, 점검='', 비고='Not Null')
    금액_원화: int = ERSField(default=0, 길이=13, 누적=168, 점검='정수점검', 비고='Not Null default 0')
    통화코드: str = ERSField(길이=3, 누적=171, 점검='통화코드 참조', 비고='Not Null')
    금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=186, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    공란: str = ERSField(default=None, 길이=14, 누적=200, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_35_공급가액확정명세서(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I401700', 길이=7, 누적=9, 점검='I401700', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    노선별: str = ERSField(길이=30, 누적=45, 점검='', 비고='Not Null')
    공급금액_여객수입: int = ERSField(default=0, 길이=13, 누적=58, 점검='정수점검', 비고='Not Null default 0')
    공급금액_화물수입: int = ERSField(default=0, 길이=13, 누적=71, 점검='정수점검', 비고='Not Null default 0')
    공급금액_수화물수입: int = ERSField(default=0, 길이=13, 누적=84, 점검='정수점검', 비고='Not Null default 0')
    공급금액_우편물수입: int = ERSField(default=0, 길이=13, 누적=97, 점검='정수점검', 비고='Not Null default 0')
    공급금액_기타수입: int = ERSField(default=0, 길이=13, 누적=110, 점검='정수점검', 비고='Not Null default 0')
    공급금액_합계: int = ERSField(default=0, 길이=13, 누적=123, 점검='정수점검', 비고='Not Null default 0')
    통화코드: str = ERSField(길이=3, 누적=126, 점검='통화코드 참조', 비고='Not Null')
    금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=141, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    공란: str = ERSField(default=None, 길이=59, 누적=200, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_36_선박에_의한_운송용역_공급가액일람표_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I401600', 길이=7, 누적=9, 점검='I401600', 비고='Not Null')
    소계_국내수입분: int = ERSField(default=0, 길이=13, 누적=22, 점검='정수점검', 비고='Not Null default 0')
    소계_해외수입분: int = ERSField(default=0, 길이=13, 누적=35, 점검='정수점검', 비고='Not Null default 0')
    소계_합계: int = ERSField(default=0, 길이=13, 누적=48, 점검='정수점검', 비고='Not Null default 0')
    외화입금증명서제출분_해외수입분: int = ERSField(default=0, 길이=13, 누적=61, 점검='정수점검', 비고='Not Null default 0')
    차감_해외수입분: int = ERSField(default=0, 길이=13, 누적=74, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=26, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_36_선박에_의한_운송용역_공급가액일람표_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I401600', 길이=7, 누적=9, 점검='I401600', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    선박명: str = ERSField(길이=30, 누적=45, 점검='', 비고='Not Null')
    운항기간시작일자: date = ERSField(길이=8, 누적=53, 점검='일자형식점검', 비고='Not Null')
    운항기간종료일자: date = ERSField(길이=8, 누적=61, 점검='일자형식점검', 비고='Not Null')
    운송수입금액_국내수입: int = ERSField(default=0, 길이=13, 누적=74, 점검='정수점검', 비고='Not Null default 0')
    운송수입금액_해외수입: int = ERSField(default=0, 길이=13, 누적=87, 점검='정수점검', 비고='Not Null default 0')
    운송수입금액_합계: int = ERSField(default=0, 길이=13, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    통화코드: str = ERSField(길이=3, 누적=103, 점검='통화코드 참조', 비고='Not Null')
    금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=118, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    공란: str = ERSField(default=None, 길이=32, 누적=150, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_37_외항_선박등에_제공한_재화용역일람표_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I401800', 길이=7, 누적=9, 점검='I401800', 비고='Not Null')
    선_기적완료증명서제출분금액_원화: int = ERSField(default=0, 길이=13, 누적=22, 점검='정수점검', 비고='Not Null default 0')
    선_기적완료증명서제출분금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=37, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    합계금액_원화: int = ERSField(default=0, 길이=13, 누적=50, 점검='정수점검', 비고='Not Null default 0')
    합계금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=65, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    공란: str = ERSField(default=None, 길이=35, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_37_외항_선박등에_제공한_재화용역일람표_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I401800', 길이=7, 누적=9, 점검='I401800', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급내용구분: str = ERSField(길이=2, 누적=17, 점검='01,02', 비고='Not Null')
    금액_원화: int = ERSField(default=0, 길이=13, 누적=30, 점검='정수점검', 비고='Not Null default 0')
    제출서류: str = ERSField(길이=30, 누적=60, 점검='', 비고='Not Null')
    금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=75, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    공란: str = ERSField(default=None, 길이=25, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_38_외화획득명세서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I402100', 길이=7, 누적=9, 점검='I402100', 비고='Not Null')
    영세율적용근거: str = ERSField(default=None, 길이=30, 누적=39, 점검='', 비고='Null 혀용')
    법정제출서류명: str = ERSField(default=None, 길이=50, 누적=89, 점검='', 비고='Null 혀용')
    법정서식제출불능사유: str = ERSField(default=None, 길이=50, 누적=139, 점검='', 비고='Null 혀용')
    법정서식제출가능일자: date = ERSField(default=None, 길이=8, 누적=147, 점검='일자형식점검', 비고='Null 혀용')
    공란: str = ERSField(default=None, 길이=53, 누적=200, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_38_외화획득명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I402100', 길이=7, 누적=9, 점검='I402100', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급일자: date = ERSField(길이=8, 누적=23, 점검='일자점검', 비고='Not Null')
    공급받는자_상호_성명: str = ERSField(길이=30, 누적=53, 점검='', 비고='Not Null')
    공급받는자_국가코드: str = ERSField(길이=2, 누적=55, 점검='국가코드', 비고='Not Null')
    공급내용_구분: str = ERSField(길이=2, 누적=57, 점검='‘01’,’02’', 비고='Not Null')
    공급내용_명칭: str = ERSField(길이=30, 누적=87, 점검='', 비고='Not Null')
    공급내용_금액_원화: int = ERSField(default=0, 길이=13, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    금액_외화: Decimal = ERSField(default='0', 길이=15, 누적=115, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    공란: str = ERSField(default=None, 길이=35, 누적=150, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_39_재화_용역공급기록표(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I401900', 길이=7, 누적=9, 점검='I401900', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급받는자_기관명: str = ERSField(길이=50, 누적=65, 점검='', 비고='Not Null')
    공급받는자_대표자명: str = ERSField(default=None, 길이=20, 누적=85, 점검='', 비고='Null 허용')
    품목명: str = ERSField(길이=60, 누적=145, 점검='', 비고='Not Null')
    공급금액: int = ERSField(default=0, 길이=13, 누적=158, 점검='정수점검', 비고='Not Null default 0')
    공급일자: date = ERSField(길이=8, 누적=166, 점검='일자형식검증', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=34, 누적=200, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_40_사업양도신고서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I104200', 길이=7, 누적=9, 점검='I104200', 비고='Not Null')
    양수자사업자등록번호: str = ERSField(길이=10, 누적=19, 점검='무세적체크', 비고='Not Null')
    사업장소재지주소: str = ERSField(default=None, 길이=50, 누적=69, 점검='', 비고='Null 혀용')
    사업양도일자: date = ERSField(default=None, 길이=8, 누적=77, 점검='', 비고='Null 혀용')
    공란: str = ERSField(default=None, 길이=23, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_40_사업양도신고서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I104200', 길이=7, 누적=9, 점검='I104200', 비고='Not Null')
    사업양도내용구분: str = ERSField(길이=2, 누적=11, 점검='01, 02, 03, 04', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=17, 점검='숫자,길이점검', 비고='Not Null')
    내용: str = ERSField(길이=100, 누적=117, 점검='일자점검', 비고='Not Null')
    공급내용_금액_원화: int = ERSField(default=0, 길이=13, 누적=130, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=20, 누적=150, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_41_외국인관광객_즉시환급_물품_판매_실적명세서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='I106900', 길이=7, 누적=9, 점검='I106900', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    면세판매장지정번호: str = ERSField(길이=8, 누적=21, 점검='', 비고='Not Null')
    합계_건수: int = ERSField(default=0, 길이=11, 누적=32, 점검='정수점검', 비고='Not Null default 0')
    합계_세금포함판매가격: int = ERSField(default=0, 길이=15, 누적=47, 점검='정수점검', 비고='Not Null default 0')
    합계_부가가치세: int = ERSField(default=0, 길이=15, 누적=62, 점검='정수점검', 비고='Not Null default 0')
    합계_즉시환급상당액: int = ERSField(default=0, 길이=15, 누적=77, 점검='정수점검', 비고='Not Null default 0')
    환급창구운영_사업자등록번호: str = ERSField(길이=10, 누적=87, 점검='사업자번호 CHECK', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=63, 누적=150, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_41_외국인관광객_즉시환급_물품_판매_실적명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='I106900', 길이=7, 누적=9, 점검='I106900', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    일련번호: str = ERSField(길이=4, 누적=17, 점검='숫자,길이점검', 비고='Not Null')
    구매일련번호: str = ERSField(길이=20, 누적=37, 점검='', 비고='Not Null')
    판매일자: date = ERSField(길이=8, 누적=45, 점검='일자형식점검', 비고='Not Null')
    반출승인번호: str = ERSField(길이=20, 누적=65, 점검='', 비고='Not Null')
    세금포함판매가격: int = ERSField(default=0, 길이=15, 누적=80, 점검='정수점검', 비고='Not Null default 0')
    부가가치세: int = ERSField(default=0, 길이=15, 누적=95, 점검='정수점검', 비고='Not Null default 0')
    즉시환급상당액: int = ERSField(default=0, 길이=15, 누적=110, 점검='정수점검', 비고='Not Null default 0')
    구입자성명: str = ERSField(default=None, 길이=30, 누적=140, 점검='', 비고='Null 허용')
    구입자국적: str = ERSField(default=None, 길이=50, 누적=190, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=10, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_42_평창동계올림픽_관련_사업자에_대한_의제매입세액공제_신고서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M127200', 길이=7, 누적=9, 점검='M127200', 비고='Not Null')
    매입건수_합계: int = ERSField(default=0, 길이=7, 누적=16, 점검='정수점검', 비고='Not Null default 0')
    매입가액_합계: int = ERSField(default=0, 길이=15, 누적=31, 점검='정수점검', 비고='Not Null default 0')
    매입세액공제액_합계: int = ERSField(default=0, 길이=13, 누적=44, 점검='정수점검', 비고='Not Null default 0')
    공제대상세액: int = ERSField(default=0, 길이=13, 누적=57, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_예정신고분: int = ERSField(default=0, 길이=13, 누적=70, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_월별조기분: int = ERSField(default=0, 길이=13, 누적=83, 점검='정수점검', 비고='Not Null default 0')
    공제_납부할세액: int = ERSField(default=0, 길이=13, 누적=96, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=54, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_42_평창동계올림픽_관련_사업자에_대한_의제매입세액공제_신고서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M127200', 길이=7, 누적=9, 점검='M127200', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=25, 점검='사업자번호 CHECK', 비고='Not Null')
    매입가액: int = ERSField(default=0, 길이=13, 누적=38, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=12, 누적=50, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M127300', 길이=7, 누적=9, 점검='M127300', 비고='Not Null')
    매입건수_합계: int = ERSField(default=0, 길이=7, 누적=16, 점검='정수점검', 비고='Not Null default 0')
    매입가액_합계: int = ERSField(default=0, 길이=15, 누적=31, 점검='정수점검', 비고='Not Null default 0')
    매입세액공제액_합계: int = ERSField(default=0, 길이=13, 누적=44, 점검='정수점검', 비고='Not Null default 0')
    공제대상세액: int = ERSField(default=0, 길이=13, 누적=57, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_예정신고분: int = ERSField(default=0, 길이=13, 누적=70, 점검='정수점검', 비고='Not Null default 0')
    이미공제받은세액_월별조기분: int = ERSField(default=0, 길이=13, 누적=83, 점검='정수점검', 비고='Not Null default 0')
    공제_납부할세액: int = ERSField(default=0, 길이=13, 누적=96, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=54, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M127300', 길이=7, 누적=9, 점검='M127300', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=25, 점검='사업자번호 CHECK', 비고='Not Null')
    매입가액: int = ERSField(default=0, 길이=13, 누적=38, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=12, 누적=50, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_입국경로에_설치된_보세판매장_공급실적명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M128600', 길이=7, 누적=9, 점검='M128600', 비고='Not Null')
    일련번호: str = ERSField(길이=6, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    공급일자: date = ERSField(길이=8, 누적=23, 점검='일자형식점검', 비고='Not Null')
    물품명: str = ERSField(default=None, 길이=50, 누적=73, 점검='', 비고='Null 허용')
    공급수량: int = ERSField(default=0, 길이=10, 누적=83, 점검='정수점검', 비고='Not Null default 0')
    공급가액: int = ERSField(default=0, 길이=13, 누적=96, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=4, 누적=100, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_45_소규모_개인사업자_부가가치세_감면신청서_신청서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M129200', 길이=7, 누적=9, 점검='M129200', 비고='Not Null')
    납부세액_예정분: int = ERSField(default=0, 길이=13, 누적=22, 점검='정수점검', 비고='Not Null default 0')
    납부세액_확정분: int = ERSField(default=0, 길이=13, 누적=35, 점검='정수점검', 비고='Not Null default 0')
    경감공제세액_예정분: int = ERSField(default=0, 길이=13, 누적=48, 점검='정수점검', 비고='Not Null default 0')
    경감공제세액_확정분: int = ERSField(default=0, 길이=13, 누적=61, 점검='정수점검', 비고='Not Null default 0')
    감면대상세액: int = ERSField(default=0, 길이=13, 누적=74, 점검='정수점검', 비고='Not Null default 0')
    납부할세액: int = ERSField(default=0, 길이=13, 누적=87, 점검='정수점검', 비고='Not Null default 0')
    비교세액: int = ERSField(default=0, 길이=13, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    감면세액: int = ERSField(default=0, 길이=13, 누적=113, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=37, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_45_소규모_개인사업자_부가가치세_감면신청서_신청서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M129200', 길이=7, 누적=9, 점검='M129200', 비고='Not Null')
    업종코드: str = ERSField(길이=6, 누적=15, 점검='업종코드CHECK', 비고='Not Null')
    과세표준과세금액_예정분: int = ERSField(default=0, 길이=13, 누적=28, 점검='정수점검', 비고='Not Null default 0')
    과세표준영세율금액_예정분: int = ERSField(default=0, 길이=13, 누적=41, 점검='정수점검', 비고='Not Null default 0')
    과세표준과세금액_확정분: int = ERSField(default=0, 길이=13, 누적=54, 점검='정수점검', 비고='Not Null default 0')
    과세표준영세율금액_확정분: int = ERSField(default=0, 길이=13, 누적=67, 점검='정수점검', 비고='Not Null default 0')
    공급대가: int = ERSField(default=0, 길이=13, 누적=80, 점검='정수점검', 비고='Not Null default 0')
    부가가치율: Decimal = ERSField(default='0', 길이=7, 누적=87, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    세액: int = ERSField(default=0, 길이=13, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=50, 누적=150, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_46_외국인관광객_숙박용역_환급실적명세서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M129400', 길이=7, 누적=9, 점검='M129400', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    환급창구운영_사업자등록번호: str = ERSField(길이=10, 누적=23, 점검='사업자번호 CHECK', 비고='Not Null')
    관광사업등록번호: str = ERSField(길이=20, 누적=43, 점검='', 비고='Not Null')
    합계_건수: int = ERSField(default=0, 길이=7, 누적=50, 점검='정수점검', 비고='Not Null default 0')
    합계_공급금액: int = ERSField(default=0, 길이=13, 누적=63, 점검='정수점검', 비고='Not Null default 0')
    합계_부가가치세: int = ERSField(default=0, 길이=13, 누적=76, 점검='정수점검', 비고='Not Null default 0')
    합계_환급액: int = ERSField(default=0, 길이=13, 누적=89, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=11, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_46_외국인관광객_숙박용역_환급실적명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M129400', 길이=7, 누적=9, 점검='M129400', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    환급창구운영_사업자등록번호: str = ERSField(길이=10, 누적=23, 점검='사업자번호 CHECK', 비고='Not Null')
    일련번호: str = ERSField(길이=7, 누적=30, 점검='숫자,길이점검', 비고='Not Null')
    숙박용역일련번호: str = ERSField(길이=20, 누적=50, 점검='', 비고='Not Null')
    공급일자: date = ERSField(길이=8, 누적=58, 점검='일자형식점검', 비고='Not Null')
    환급일자: date = ERSField(길이=8, 누적=66, 점검='일자형식점검', 비고='Not Null')
    환급증명서송부일자: date = ERSField(길이=8, 누적=74, 점검='일자형식점검', 비고='Not Null')
    공급금액: int = ERSField(default=0, 길이=13, 누적=87, 점검='정수점검', 비고='Not Null default 0')
    부가가치세: int = ERSField(default=0, 길이=13, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    환급액: int = ERSField(default=0, 길이=13, 누적=113, 점검='정수점검', 비고='Not Null default 0')
    투숙객국적명: str = ERSField(default=None, 길이=50, 누적=163, 점검='', 비고='Null 허용')
    투숙객여권번호: str = ERSField(default=None, 길이=20, 누적=183, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=17, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v2_47_외국인관광객_미용성형_의료용역_환급실적명세서_합계(ERSRecord):
    자료구분: str = ERSField(default='17', 길이=2, 누적=2, 점검='17', 비고='Not Null')
    서식코드: str = ERSField(default='M129300', 길이=7, 누적=9, 점검='M129300', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    환급창구운영_사업자등록번호: str = ERSField(길이=10, 누적=23, 점검='사업자번호 CHECK', 비고='Not Null')
    유치기관등록번호: str = ERSField(길이=13, 누적=36, 점검='', 비고='Not Null')
    합계_건수: int = ERSField(default=0, 길이=7, 누적=43, 점검='정수점검', 비고='Not Null default 0')
    합계_공급금액: int = ERSField(default=0, 길이=13, 누적=56, 점검='정수점검', 비고='Not Null default 0')
    합계_부가가치세: int = ERSField(default=0, 길이=13, 누적=69, 점검='정수점검', 비고='Not Null default 0')
    합계_환급액: int = ERSField(default=0, 길이=13, 누적=82, 점검='정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=18, 누적=100, 점검='길이점검', 비고='Space')


@dataclass(kw_only=True)
class v2_47_외국인관광객_미용성형_의료용역_환급실적명세서_명세(ERSRecord):
    자료구분: str = ERSField(default='18', 길이=2, 누적=2, 점검='18', 비고='Not Null')
    서식코드: str = ERSField(default='M129300', 길이=7, 누적=9, 점검='M129300', 비고='Not Null')
    종사업자일련번호: str = ERSField(길이=4, 누적=13, 점검='숫자,길이점검', 비고='Not Null')
    환급창구운영_사업자등록번호: str = ERSField(길이=10, 누적=23, 점검='사업자번호 CHECK', 비고='Not Null')
    일련번호: str = ERSField(길이=7, 누적=30, 점검='숫자,길이점검', 비고='Not Null')
    의료용역일련번호: str = ERSField(길이=20, 누적=50, 점검='', 비고='Not Null')
    공급일자: date = ERSField(길이=8, 누적=58, 점검='일자형식점검', 비고='Not Null')
    환급송금일자: date = ERSField(길이=8, 누적=66, 점검='일자형식점검', 비고='Not Null')
    환급송금증명서송부일자: date = ERSField(길이=8, 누적=74, 점검='일자형식점검', 비고='Not Null')
    공급금액: int = ERSField(default=0, 길이=13, 누적=87, 점검='정수점검', 비고='Not Null default 0')
    부가가치세: int = ERSField(default=0, 길이=13, 누적=100, 점검='정수점검', 비고='Not Null default 0')
    환급액: int = ERSField(default=0, 길이=13, 누적=113, 점검='정수점검', 비고='Not Null default 0')
    국적명: str = ERSField(default=None, 길이=50, 누적=163, 점검='', 비고='Null 허용')
    여권번호: str = ERSField(default=None, 길이=20, 누적=183, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=17, 누적=200, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_1_세금계산서합계표_표지_Head_Record(ERSRecord):
    자료구분: str = ERSField(default='7', 길이=1, 누적=1, 점검='7', 비고='Not Null')
    보고자등록번호: int = ERSField(길이=10, 누적=11, 점검='사업자번호 CHECK DIGIT +무세적', 비고='Not Null')
    보고자상호: str = ERSField(길이=30, 누적=41, 점검='', 비고='Not Null')
    보고자성명: str = ERSField(길이=15, 누적=56, 점검='', 비고='Not Null')
    보고자사업장소재지: str = ERSField(길이=45, 누적=101, 점검='', 비고='Not Null')
    보고자업태: str = ERSField(default=None, 길이=17, 누적=118, 점검='SPACE', 비고='Null 허용')
    보고자종목: str = ERSField(default=None, 길이=25, 누적=143, 점검='SPACE', 비고='Null 허용')
    거래기간: int = ERSField(길이=12, 누적=155, 점검='년(YY)월일형식', 비고='Not Null')
    작성일자: date = ERSField(길이=6, 누적=161, 점검='일자형식점검', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=9, 누적=170, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_1_세금계산서합계표_지연전송한_전자세금계산서를_여기에_적습니다(ERSRecord):
    자료구분: str = ERSField(default='3', 길이=1, 누적=1, 점검='3', 비고='Not Null')
    보고자등록번호: int = ERSField(default=None, 길이=10, 누적=11, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Null 허용')
    합계분_거래처수: int = ERSField(default=0, 길이=7, 누적=18, 점검='양수점검', 비고='Not Null default 0')
    합계분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=25, 점검='양수점검', 비고='Not Null default 0')
    합계분_공급가액: int = ERSField(default=0, 길이=15, 누적=40, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    합계분_세액: int = ERSField(default=0, 길이=14, 누적=54, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호발행분_거래처수: int = ERSField(default=0, 길이=7, 누적=61, 점검='양수점검', 비고='Not Null default 0')
    사업자번호발행분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=68, 점검='양수점검', 비고='Not Null default 0')
    사업자번호발행분_공급가액: int = ERSField(default=0, 길이=15, 누적=83, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호발행분_세액: int = ERSField(default=0, 길이=14, 누적=97, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호발행분_거래처수: int = ERSField(default=0, 길이=7, 누적=104, 점검='양수점검', 비고='Not Null default 0')
    주민번호발행분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=111, 점검='양수점검', 비고='Not Null default 0')
    주민번호발행분_공급가액: int = ERSField(default=0, 길이=15, 누적=126, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호발행분_세액: int = ERSField(default=0, 길이=14, 누적=140, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=30, 누적=170, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_1_세금계산서합계표_전자세금계산서분_매출합계_Total_Record(ERSRecord):
    자료구분: str = ERSField(default='5', 길이=1, 누적=1, 점검='5', 비고='Not Null')
    보고자등록번호: int = ERSField(default=None, 길이=10, 누적=11, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Null 허용')
    합계분_거래처수: int = ERSField(default=0, 길이=7, 누적=18, 점검='양수점검', 비고='Not Null default 0')
    합계분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=25, 점검='양수점검', 비고='Not Null default 0')
    합계분_공급가액: int = ERSField(default=0, 길이=15, 누적=40, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    합계분_세액: int = ERSField(default=0, 길이=14, 누적=54, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호발행분_거래처수: int = ERSField(default=0, 길이=7, 누적=61, 점검='양수점검', 비고='Not Null default 0')
    사업자번호발행분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=68, 점검='양수점검', 비고='Not Null default 0')
    사업자번호발행분_공급가액: int = ERSField(default=0, 길이=15, 누적=83, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호발행분_세액: int = ERSField(default=0, 길이=14, 누적=97, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호발행분_거래처수: int = ERSField(default=0, 길이=7, 누적=104, 점검='양수점검', 비고='Not Null default 0')
    주민번호발행분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=111, 점검='양수점검', 비고='Not Null default 0')
    주민번호발행분_공급가액: int = ERSField(default=0, 길이=15, 누적=126, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호발행분_세액: int = ERSField(default=0, 길이=14, 누적=140, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=30, 누적=170, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_1_세금계산서합계표_14_세액_전자세금계산서분_주민등록번호_발행분의_세액의_합계를_수록함_음수인_경우_멀티키_Multi_Key_사용_116_페이지_참고(ERSRecord):
    자료구분: str = ERSField(default='2', 길이=1, 누적=1, 점검='2', 비고='Not Null')
    보고자등록번호: int = ERSField(default=None, 길이=10, 누적=11, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Null 허용')
    일련번호: int = ERSField(길이=4, 누적=15, 점검='숫자,길이점검', 비고='Not Null')
    거래자등록번호: int = ERSField(길이=10, 누적=25, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Not Null')
    거래자상호: str = ERSField(default=None, 길이=30, 누적=55, 점검='', 비고='Null 허용')
    거래자업태: str = ERSField(default=None, 길이=17, 누적=72, 점검='SPACE', 비고='Null 허용')
    거래자종목: str = ERSField(default=None, 길이=25, 누적=97, 점검='SPACE', 비고='Null 허용')
    세금계산서매수: int = ERSField(default=0, 길이=7, 누적=104, 점검='양수점검', 비고='Not Null default 0')
    공란수: int = ERSField(default=0, 길이=2, 누적=106, 점검='0', 비고='Not Null default 0')
    공급가액: int = ERSField(default=0, 길이=14, 누적=120, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    세액: int = ERSField(default=0, 길이=13, 누적=133, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    신고자주류코드_도매: int = ERSField(길이=1, 누적=134, 점검='0,1,2,3,4,5,6,7', 비고='Not Null')
    주류코드_소매: int = ERSField(길이=1, 누적=135, 점검='0,1,2,3,4,5,6,7', 비고='Not Null')
    권번호: int = ERSField(default=0, 길이=4, 누적=139, 점검='8501', 비고='Not Null default 0')
    제출서: int = ERSField(default=None, 길이=3, 누적=142, 점검='숫자,길이점검', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=28, 누적=170, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_1_세금계산서합계표(ERSRecord):
    자료구분: str = ERSField(default='4', 길이=1, 누적=1, 점검='4', 비고='Not Null')
    보고자등록번호: int = ERSField(default=None, 길이=10, 누적=11, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Null 허용')
    합계분_거래처수: int = ERSField(default=0, 길이=7, 누적=18, 점검='양수점검', 비고='Not Null default 0')
    합계분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=25, 점검='양수점검', 비고='Not Null default 0')
    합계분_공급가액: int = ERSField(default=0, 길이=15, 누적=40, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    합계분_세액: int = ERSField(default=0, 길이=14, 누적=54, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호수취분_거래처수: int = ERSField(default=0, 길이=7, 누적=61, 점검='양수점검', 비고='Not Null default 0')
    사업자번호수취분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=68, 점검='양수점검', 비고='Not Null default 0')
    사업자번호수취분_공급가액: int = ERSField(default=0, 길이=15, 누적=83, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호수취분_세액: int = ERSField(default=0, 길이=14, 누적=97, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호수취분_거래처수: int = ERSField(default=0, 길이=7, 누적=104, 점검='양수점검', 비고='Not Null default 0')
    주민번호수취분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=111, 점검='양수점검', 비고='Not Null default 0')
    주민번호수취분_공급가액: int = ERSField(default=0, 길이=15, 누적=126, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호수취분_세액: int = ERSField(default=0, 길이=14, 누적=140, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=30, 누적=170, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_1_세금계산서합계표_전자세금계산서분_매입합계_Total_Record(ERSRecord):
    자료구분: str = ERSField(default='6', 길이=1, 누적=1, 점검='6', 비고='Not Null')
    보고자등록번호: int = ERSField(default=None, 길이=10, 누적=11, 점검='사업자번호 CHECK DIGIT+무세적', 비고='Null 허용')
    합계분_거래처수: int = ERSField(default=0, 길이=7, 누적=18, 점검='양수점검', 비고='Not Null default 0')
    합계분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=25, 점검='양수점검', 비고='Not Null default 0')
    합계분_공급가액: int = ERSField(default=0, 길이=15, 누적=40, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    합계분_세액: int = ERSField(default=0, 길이=14, 누적=54, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호수취분_거래처수: int = ERSField(default=0, 길이=7, 누적=61, 점검='양수점검', 비고='Not Null default 0')
    사업자번호수취분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=68, 점검='양수점검', 비고='Not Null default 0')
    사업자번호수취분_공급가액: int = ERSField(default=0, 길이=15, 누적=83, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    사업자번호수취분_세액: int = ERSField(default=0, 길이=14, 누적=97, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호수취분_거래처수: int = ERSField(default=0, 길이=7, 누적=104, 점검='양수점검', 비고='Not Null default 0')
    주민번호수취분_세금계산서매수: int = ERSField(default=0, 길이=7, 누적=111, 점검='양수점검', 비고='Not Null default 0')
    주민번호수취분_공급가액: int = ERSField(default=0, 길이=15, 누적=126, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    주민번호수취분_세액: int = ERSField(default=0, 길이=14, 누적=140, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=30, 누적=170, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_2_계산서합계표_제출자_대리인레코드(ERSRecord):
    레코드구분: str = ERSField(default='A', 길이=1, 누적=1, 점검='A', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=4, 점검='길이점검', 비고='Null 허용')
    제출년월일: date = ERSField(길이=8, 누적=12, 점검='일자형식점검', 비고='Not Null')
    제출자구분: int = ERSField(길이=1, 누적=13, 점검='1,2,3', 비고='Not Null')
    세무대리인관리번호: str = ERSField(default=None, 길이=6, 누적=19, 점검='길이점검', 비고='Null 허용')
    사업자등록번호: str = ERSField(길이=10, 누적=29, 점검='사업자번호 CHECK DIGIT + 무세적', 비고='Not Null')
    법인명_상호: str = ERSField(길이=40, 누적=69, 점검='', 비고='Not Null')
    주민_법인등록번호: str = ERSField(default=None, 길이=13, 누적=82, 점검='길이점검', 비고='Null 허용')
    대표자_성명: str = ERSField(길이=30, 누적=112, 점검='', 비고='Not Null')
    소재지_우편번호법정동코드: str = ERSField(default=None, 길이=10, 누적=122, 점검='길이점검', 비고='Null 허용')
    소재지_주소: str = ERSField(길이=70, 누적=192, 점검='', 비고='Not Null')
    전화번호: str = ERSField(길이=15, 누적=207, 점검='', 비고='Not Null')
    제출건수계: int = ERSField(길이=5, 누적=212, 점검='정수점검', 비고='Not Null')
    사용한한글코드종류: int = ERSField(default=None, 길이=3, 누적=215, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=15, 누적=230, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_2_계산서합계표_제출의무자인적사항레코드(ERSRecord):
    레코드구분: str = ERSField(default='B', 길이=1, 누적=1, 점검='B', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=4, 점검='길이점검', 비고='Null 허용')
    일련번호: int = ERSField(길이=6, 누적=10, 점검='숫자,길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=20, 점검='사업자번호CHECK DIGIT+무세적', 비고='Not Null')
    법인명_상호: str = ERSField(길이=40, 누적=60, 점검='', 비고='Not Null')
    대표자_성명: str = ERSField(길이=30, 누적=90, 점검='', 비고='Not Null')
    사업장_우편번호법정동코드: str = ERSField(default=None, 길이=10, 누적=100, 점검='길이점검', 비고='Null 허용')
    사업장소재지_주소: str = ERSField(길이=70, 누적=170, 점검='', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=60, 누적=230, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_2_계산서합계표_제출의무자별집계레코드_매출(ERSRecord):
    레코드구분: str = ERSField(default='C', 길이=1, 누적=1, 점검='C', 비고='Not Null')
    자료구분: int = ERSField(default='17', 길이=2, 누적=3, 점검='17', 비고='Not Null')
    기구분: str = ERSField(길이=1, 누적=4, 점검='1,2', 비고='Not Null')
    신고구분: str = ERSField(길이=1, 누적=5, 점검='1,2', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=8, 점검='길이점검', 비고='Null 허용')
    일련번호: int = ERSField(길이=6, 누적=14, 점검='숫자,길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=24, 점검='사업자번호CHECK DIGIT +무세적', 비고='Not Null')
    귀속년도: int = ERSField(길이=4, 누적=28, 점검='년도형식점검', 비고='Not Null')
    거래기간시작년월일: date = ERSField(길이=8, 누적=36, 점검='일자형식점검', 비고='Not Null')
    거래기간종료년월일: date = ERSField(길이=8, 누적=44, 점검='일자형식점검', 비고='Not Null')
    작성일자: date = ERSField(길이=8, 누적=52, 점검='일자형식점검', 비고='Not Null')
    매출처수합계: int = ERSField(default=0, 길이=6, 누적=58, 점검='양수점검', 비고='Not Null default 0')
    계산서매수합계: int = ERSField(default=0, 길이=6, 누적=64, 점검='양수점검', 비고='Not Null default 0')
    매출_수입금액합계음수표시: int = ERSField(default=0, 길이=1, 누적=65, 점검='0,1', 비고='Not Null default 0')
    매출_수입금액합계: int = ERSField(default=0, 길이=14, 누적=79, 점검='양수점검', 비고='Not Null default 0')
    사업자등록번호발행분매출처수: int = ERSField(default=0, 길이=6, 누적=85, 점검='양수점검', 비고='Not Null default 0')
    사업자등록번호발행분계산서매수: int = ERSField(default=0, 길이=6, 누적=91, 점검='양수점검', 비고='Not Null default 0')
    사업자등록번호발행분매출_수입금액음수표시: int = ERSField(default=0, 길이=1, 누적=92, 점검='0,1', 비고='Not Null default 0')
    사업자등록번호발행분매출_수입금액: int = ERSField(default=0, 길이=14, 누적=106, 점검='양수점검', 비고='Not Null default 0')
    주민등록번호발행분매출처수: int = ERSField(default=0, 길이=6, 누적=112, 점검='양수점검', 비고='Not Null default 0')
    주민등록번호발행분계산서매수: int = ERSField(default=0, 길이=6, 누적=118, 점검='양수점검', 비고='Not Null default 0')
    주민등록번호발행분매출_수입금액음수표시: int = ERSField(default=0, 길이=1, 누적=119, 점검='0,1', 비고='Not Null default 0')
    주민등록번호발행분매출_수입금액: int = ERSField(default=0, 길이=14, 누적=133, 점검='양수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=97, 누적=230, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_2_계산서합계표_지연전송한_전자계산서를_여기에_적습니다(ERSRecord):
    레코드구분: str = ERSField(default='D', 길이=1, 누적=1, 점검='D', 비고='Not Null')
    자료구분: int = ERSField(default='18', 길이=2, 누적=3, 점검='18', 비고='Not Null')
    기구분: str = ERSField(길이=1, 누적=4, 점검='1,2', 비고='Not Null')
    신고구분: str = ERSField(길이=1, 누적=5, 점검='1,2', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=8, 점검='길이점검', 비고='Null 허용')
    일련번호: int = ERSField(길이=6, 누적=14, 점검='숫자,길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=24, 점검='사업자번호CHECK DIGIT+무세적', 비고='Not Null')
    매입처사업자등록번호: str = ERSField(길이=10, 누적=34, 점검='사업자번호CHECK DIGIT+무세적', 비고='Not Null')
    매입처법인명_상호: str = ERSField(default=None, 길이=40, 누적=74, 점검='', 비고='Null 허용')
    계산서매수: int = ERSField(default=0, 길이=5, 누적=79, 점검='양수점검', 비고='Not Null default 0')
    매입금액음수표시: int = ERSField(default=0, 길이=1, 누적=80, 점검='0,1', 비고='Not Null default 0')
    매입금액: int = ERSField(default=0, 길이=14, 누적=94, 점검='양수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=136, 누적=230, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_2_계산서합계표_전자계산서_매출집계레코드_매출(ERSRecord):
    레코드구분: str = ERSField(default='E', 길이=1, 누적=1, 점검='E', 비고='Not Null')
    자료구분: int = ERSField(default='17', 길이=2, 누적=3, 점검='17', 비고='Not Null')
    기구분: str = ERSField(길이=1, 누적=4, 점검='1,2', 비고='Not Null')
    신고구분: str = ERSField(길이=1, 누적=5, 점검='1,2', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=8, 점검='길이점검', 비고='Null 허용')
    일련번호: int = ERSField(길이=6, 누적=14, 점검='숫자,길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=24, 점검='사업자번호CHECK DIGIT +무세적', 비고='Not Null')
    귀속년도: int = ERSField(길이=4, 누적=28, 점검='년도형식점검', 비고='Not Null')
    거래기간시작년월일: date = ERSField(길이=8, 누적=36, 점검='일자형식점검', 비고='Not Null')
    거래기간종료년월일: date = ERSField(길이=8, 누적=44, 점검='일자형식점검', 비고='Not Null')
    작성일자: date = ERSField(길이=8, 누적=52, 점검='일자형식점검', 비고='Not Null')
    매출처수합계: int = ERSField(default=0, 길이=6, 누적=58, 점검='양수점검', 비고='Not Null default 0')
    계산서매수합계: int = ERSField(default=0, 길이=6, 누적=64, 점검='양수점검', 비고='Not Null default 0')
    매출_수입금액합계음수표시: int = ERSField(default=0, 길이=1, 누적=65, 점검='0,1', 비고='Not Null default 0')
    매출_수입금액합계: int = ERSField(default=0, 길이=14, 누적=79, 점검='양수점검', 비고='Not Null default 0')
    사업자등록번호발행분매출처수: int = ERSField(default=0, 길이=6, 누적=85, 점검='양수점검', 비고='Not Null default 0')
    사업자등록번호발행분계산서매수: int = ERSField(default=0, 길이=6, 누적=91, 점검='양수점검', 비고='Not Null default 0')
    사업자등록번호발행분매출_수입금액음수표시: int = ERSField(default=0, 길이=1, 누적=92, 점검='0,1', 비고='Not Null default 0')
    사업자등록번호발행분매출_수입금액: int = ERSField(default=0, 길이=14, 누적=106, 점검='양수점검', 비고='Not Null default 0')
    주민등록번호발행분매출처수: int = ERSField(default=0, 길이=6, 누적=112, 점검='양수점검', 비고='Not Null default 0')
    주민등록번호발행분계산서매수: int = ERSField(default=0, 길이=6, 누적=118, 점검='양수점검', 비고='Not Null default 0')
    주민등록번호발행분매출_수입금액음수표시: int = ERSField(default=0, 길이=1, 누적=119, 점검='0,1', 비고='Not Null default 0')
    주민등록번호발행분매출_수입금액: int = ERSField(default=0, 길이=14, 누적=133, 점검='양수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=97, 누적=230, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_2_계산서합계표_제출자_대리인레코드_매입(ERSRecord):
    레코드구분: str = ERSField(default='A', 길이=1, 누적=1, 점검='A', 비고='Not Null')
    자료구분: int = ERSField(default='18', 길이=2, 누적=3, 점검='18', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=6, 점검='길이점검', 비고='Null 허용')
    제출년월일: date = ERSField(길이=8, 누적=14, 점검='일자형식점검', 비고='Not Null')
    제출자구분: int = ERSField(길이=1, 누적=15, 점검='1,2,3', 비고='Not Null')
    세무대리인관리번호: str = ERSField(길이=6, 누적=21, 점검='길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=31, 점검='사업자번호 CHECK DIGIT +무세적', 비고='Not Null')
    법인명_상호: str = ERSField(길이=40, 누적=71, 점검='', 비고='Not Null')
    주민_법인등록번호: str = ERSField(default=None, 길이=13, 누적=84, 점검='길이점검', 비고='Null 허용')
    대표자_성명: str = ERSField(길이=30, 누적=114, 점검='', 비고='Not Null')
    소재지_우편번호법정동코드: str = ERSField(default=None, 길이=10, 누적=124, 점검='길이점검', 비고='Null 허용')
    소재지_주소: str = ERSField(길이=70, 누적=194, 점검='', 비고='Not Null')
    전화번호: str = ERSField(길이=15, 누적=209, 점검='', 비고='Not Null')
    제출건수계: int = ERSField(길이=5, 누적=214, 점검='양수점검', 비고='Not Null')
    사용한한글코드종류: int = ERSField(default=None, 길이=3, 누적=217, 점검='', 비고='Null 허용')
    공란: str = ERSField(default=None, 길이=13, 누적=230, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_2_계산서합계표_매출계산서의_A레코드와_공동으로_사용함에_따라_삭제처리함_제출의무자인적사항레코드_매입(ERSRecord):
    레코드구분: str = ERSField(default='B', 길이=1, 누적=1, 점검='B', 비고='Not Null')
    자료구분: int = ERSField(default='18', 길이=2, 누적=3, 점검='18', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=6, 점검='길이점검', 비고='Null 허용')
    일련번호: int = ERSField(길이=6, 누적=12, 점검='숫자,길이점검', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=22, 점검='사업자번호 CHECK DIGIT +무세적', 비고='Not Null')
    법인명_상호: str = ERSField(길이=40, 누적=62, 점검='', 비고='Not Null')
    대표자_성명: str = ERSField(길이=30, 누적=92, 점검='', 비고='Not Null')
    사업장_우편번호법정동코드: str = ERSField(default=None, 길이=10, 누적=102, 점검='길이점검', 비고='Null 허용')
    사업장소재지_주소: str = ERSField(길이=70, 누적=172, 점검='', 비고='Not Null')
    업태: str = ERSField(길이=20, 누적=192, 점검='', 비고='Not Null')
    종목: str = ERSField(길이=30, 누적=222, 점검='', 비고='Not Null')
    공란: str = ERSField(길이=8, 누적=230, 점검='길이점검', 비고='Not Null')


@dataclass(kw_only=True)
class v3_2_계산서합계표_전자계산서_매입집계레코드(ERSRecord):
    레코드구분: str = ERSField(default='E', 길이=1, 누적=1, 점검='E', 비고='Not Null')
    자료구분: int = ERSField(default='18', 길이=2, 누적=3, 점검='18', 비고='Not Null')
    기구분: str = ERSField(길이=1, 누적=4, 점검='1,2', 비고='Not Null')
    신고구분: str = ERSField(길이=1, 누적=5, 점검='1,2', 비고='Not Null')
    세무서: str = ERSField(default=None, 길이=3, 누적=8, 점검='길이점검', 비고='Null 허용')
    일련번호: int = ERSField(길이=6, 누적=14, 점검='숫자,길이점검', 비고='Not Null')
    제출의무자_사업자_사업자등록번호: str = ERSField(길이=10, 누적=24, 점검='사업자번호 CHECK DIGIT +무세적', 비고='Not Null')
    귀속년도: int = ERSField(default=None, 길이=4, 누적=28, 점검='년도형식점검', 비고='Null 허용')
    거래기간시작년월일: date = ERSField(default=None, 길이=8, 누적=36, 점검='일자형식점검', 비고='Null 허용')
    거래기간종료년월일: date = ERSField(default=None, 길이=8, 누적=44, 점검='일자형식점검', 비고='Null 허용')
    작성일자: date = ERSField(default=None, 길이=8, 누적=52, 점검='일자형식점검', 비고='Null 허용')
    매입처수합계: int = ERSField(default=0, 길이=6, 누적=58, 점검='양수점검', 비고='Not Null default 0')
    계산서매수합계: int = ERSField(default=0, 길이=6, 누적=64, 점검='양수점검', 비고='Not Null default 0')
    매입금액합계음수표시: int = ERSField(default=0, 길이=1, 누적=65, 점검='0,1', 비고='Not Null default 0')
    매입금액합계: int = ERSField(default=0, 길이=14, 누적=79, 점검='양수점검', 비고='Not Null default 0')
    공란: str = ERSField(default=None, 길이=151, 누적=230, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_3_수출실적_명세서_전산매체_A_레코드(ERSRecord):
    자료구분_표지: str = ERSField(길이=1, 누적=1, 점검='A', 비고='Not Null')
    수출신고년월_귀속년월: str = ERSField(길이=6, 누적=7, 점검='년월형식점검', 비고='Not Null')
    신고구분: str = ERSField(길이=1, 누적=8, 점검='1,2,3,4', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=18, 점검='사업자번호 CHECK DIGIT +무세적', 비고='Not Null')
    법인명_상호: str = ERSField(길이=30, 누적=48, 점검='', 비고='Not Null')
    성명_대표자명_수출: str = ERSField(길이=15, 누적=63, 점검='', 비고='Not Null')
    사업장소재지_수출: str = ERSField(길이=45, 누적=108, 점검='', 비고='Not Null')
    업태명_수출: str = ERSField(길이=17, 누적=125, 점검='', 비고='Not Null')
    종목명_수출: str = ERSField(길이=25, 누적=150, 점검='', 비고='Not Null')
    거래기간: date = ERSField(길이=16, 누적=166, 점검='일자형식점검', 비고='Not Null')
    작성일자: date = ERSField(길이=8, 누적=174, 점검='일자형식점검', 비고='Not Null')
    공란: str = ERSField(default=None, 길이=6, 누적=180, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_3_수출실적_명세서_전산매체_B_레코드(ERSRecord):
    자료구분_합계: str = ERSField(길이=1, 누적=1, 점검='B', 비고='Not Null')
    수출신고년월_귀속년월: str = ERSField(길이=6, 누적=7, 점검='년월형식점검', 비고='Not Null')
    신고구분: str = ERSField(길이=1, 누적=8, 점검='1,2,3,4', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=18, 점검='사업자번호 CHECK DIGIT +무세적', 비고='Not Null')
    건수합계_수출: int = ERSField(default=0, 길이=7, 누적=25, 점검='양수점검', 비고='Not Null default 0')
    외화금액_합계: Decimal = ERSField(default='0', 길이=15, 누적=40, 점검='Multi-Key+실수점검', 비고='Not Null default 0', 소수점길이=2)
    원화금액_합계: int = ERSField(default=0, 길이=15, 누적=55, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    건수_재화: int = ERSField(default=0, 길이=7, 누적=62, 점검='양수점검', 비고='Not Null default 0')
    외화금액_재화: Decimal = ERSField(default='0', 길이=15, 누적=77, 점검='Multi-Key+실수점검', 비고='Not Null default 0', 소수점길이=2)
    원화금액_재화: int = ERSField(default=0, 길이=15, 누적=92, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    건수_기타: int = ERSField(default=0, 길이=7, 누적=99, 점검='양수점검', 비고='Not Null default 0')
    외화금액_기타: Decimal = ERSField(default='0', 길이=15, 누적=114, 점검='Multi-Key+실수점검', 비고='Not Null default 0', 소수점길이=2)
    원화금액_기타: int = ERSField(default=0, 길이=15, 누적=129, 점검='Multi-Key+정수점검', 비고='Not Null default 0')
    공_란: str = ERSField(default=None, 길이=51, 누적=180, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_3_수출실적_명세서_전산매체_C_레코드(ERSRecord):
    자료구분_자료: str = ERSField(길이=1, 누적=1, 점검='C', 비고='Not Null')
    수출신고년월_귀속년월: str = ERSField(길이=6, 누적=7, 점검='년월형식점검', 비고='Not Null')
    신고구분: str = ERSField(길이=1, 누적=8, 점검='1,2,3,4', 비고='Not Null')
    사업자등록번호: str = ERSField(길이=10, 누적=18, 점검='사업자번호CHECK DIGIT + 무세적', 비고='Not Null')
    수출일련번호: str = ERSField(길이=7, 누적=25, 점검='숫자,길이점검', 비고='Not Null')
    수출신고번호: str = ERSField(길이=15, 누적=40, 점검='수출신고번호CHECK DIGIT', 비고='Not Null')
    선적_기일자: date = ERSField(길이=8, 누적=48, 점검='일자형식점검', 비고='Not Null')
    수출통화코드: str = ERSField(길이=3, 누적=51, 점검='영문자,길이점검', 비고='Not Null')
    환_율: Decimal = ERSField(default='0', 길이=9, 누적=60, 점검='양의 실수점검', 비고='Not Null default 0', 소수점길이=4)
    외화금액: Decimal = ERSField(default='0', 길이=15, 누적=75, 점검='실수점검', 비고='Not Null default 0', 소수점길이=2)
    원화금액: int = ERSField(default=0, 길이=15, 누적=90, 점검='정수점검', 비고='Not Null default 0')
    공_란: str = ERSField(default=None, 길이=90, 누적=180, 점검='길이점검', 비고='')


@dataclass(kw_only=True)
class v3_4_신용카드매출전표등수령명세서_갑_을_제출자_인적사항_Header_Record(ERSRecord):
    레코드구분: str = ERSField(default='HL', 길이=2, 누적=2, 점검='HL', 비고='HL')
    귀속년도: str = ERSField(default=None, 길이=4, 누적=6, 점검='', 비고='')
    반기구분: str = ERSField(default=None, 길이=1, 누적=7, 점검='1:1기, 2:2기', 비고='1:1기, 2:2기')
    반기내월순번: str = ERSField(default=None, 길이=1, 누적=8, 점검='1,2,3,4,5,6', 비고='1,2,3,4,5,6')
    수취자_제출자사업자등록번호: str = ERSField(default=None, 길이=10, 누적=18, 점검='', 비고='')
    상호_법인명: str = ERSField(default=None, 길이=60, 누적=78, 점검='', 비고='')
    성명_대표자: str = ERSField(default=None, 길이=30, 누적=108, 점검='', 비고='')
    주민_법인등록번호: str = ERSField(default=None, 길이=13, 누적=121, 점검='', 비고='')
    제출일자: date = ERSField(default=None, 길이=8, 누적=129, 점검='', 비고='')
    공란: str = ERSField(default=None, 길이=11, 누적=140, 점검='SPACE', 비고='SPACE')


@dataclass(kw_only=True)
class v3_4_신용카드매출전표등수령명세서_갑_을_기타신용_직불카드_및_기명식선불카드_매출전표_수령금액_명세_Data_Record(ERSRecord):
    레코드구분: str = ERSField(default='DL', 길이=2, 누적=2, 점검='DL', 비고='DL')
    귀속년도: str = ERSField(default=None, 길이=4, 누적=6, 점검='', 비고='')
    반기구분: str = ERSField(default=None, 길이=1, 누적=7, 점검='1:1기, 2:2기', 비고='1:1기, 2:2기')
    반기내월_순번: str = ERSField(default=None, 길이=1, 누적=8, 점검='1,2,3,4,5,6', 비고='1,2,3,4,5,6')
    수취자_제출자사업자등록번호: str = ERSField(default=None, 길이=10, 누적=18, 점검='', 비고='')
    카드구분: str = ERSField(default=None, 길이=1, 누적=19, 점검='1,2,3,4', 비고='1,2,3,4')
    카드회원번호: str = ERSField(길이=20, 누적=39, 점검='Not Null, 숫자만 가능', 비고='Not Null, 숫자만 가능')
    공급자_가맹점사업자등록번호: str = ERSField(default=None, 길이=10, 누적=49, 점검='', 비고='')
    거래건수: int = ERSField(default=None, 길이=9, 누적=58, 점검='', 비고='')
    공급가액음수표시: str = ERSField(default=None, 길이=1, 누적=59, 점검='‘ ‘:양수 ‘- ‘:음수', 비고='‘ ‘:양수 ‘- ‘:음수')
    공급가액: int = ERSField(default=None, 길이=13, 누적=72, 점검='', 비고='')
    세액음수표시: str = ERSField(default=None, 길이=1, 누적=73, 점검='‘ ‘:양수 ‘- ‘:음수', 비고='‘ ‘:양수 ‘- ‘:음수')
    세액: int = ERSField(default=None, 길이=13, 누적=86, 점검='', 비고='')
    공란: str = ERSField(default=None, 길이=54, 누적=140, 점검='SPACE', 비고='SPACE')


@dataclass(kw_only=True)
class v3_4_신용카드매출전표등수령명세서_갑_을_신용카드등_매입내용_합계_Tail_Record(ERSRecord):
    레코드구분: str = ERSField(default='TL', 길이=2, 누적=2, 점검='TL', 비고='TL')
    귀속년도: str = ERSField(default=None, 길이=4, 누적=6, 점검='', 비고='')
    반기구분: str = ERSField(default=None, 길이=1, 누적=7, 점검='1:1기, 2:2기', 비고='1:1기, 2:2기')
    반기내월_순번: str = ERSField(default=None, 길이=1, 누적=8, 점검='1,2,3,4,5,6', 비고='1,2,3,4,5,6')
    수취자_제출자사업자등록번호: str = ERSField(default=None, 길이=10, 누적=18, 점검='', 비고='')
    DATA건수: int = ERSField(default=None, 길이=7, 누적=25, 점검='', 비고='')
    총거래건수: int = ERSField(default=None, 길이=9, 누적=34, 점검='', 비고='')
    총공급가액음수표시: str = ERSField(default=None, 길이=1, 누적=35, 점검='‘ ‘:양수 ‘- ‘:음수', 비고='‘ ‘:양수 ‘- ‘:음수')
    총공급가액: int = ERSField(default=None, 길이=15, 누적=50, 점검='', 비고='')
    총세액음수표시: str = ERSField(default=None, 길이=1, 누적=51, 점검='‘ ‘:양수 ‘- ‘:음수', 비고='‘ ‘:양수 ‘- ‘:음수')
    총세액: int = ERSField(default=None, 길이=15, 누적=66, 점검='', 비고='')
    공란: str = ERSField(default=None, 길이=74, 누적=140, 점검='SPACE', 비고='SPACE')


@dataclass(kw_only=True)
class 부가가치세신고(ERSReport):
    published_date: ClassVar[date] = date(2022, 12, 1)
    v1_1_신고서_Head_레코드: List[v1_1_신고서_Head_레코드]
    v1_2_일반과세자_신고서_레코드: List[v1_2_일반과세자_신고서_레코드]
    v1_3_간이과세자_신고서_레코드: List[v1_3_간이과세자_신고서_레코드]
    v2_3_간이과세자_신고서_레코드_사업장현황명세서: List[v2_3_간이과세자_신고서_레코드_사업장현황명세서]
    v2_3_간이과세자_신고서_레코드_신용카드매출전표_등_발행금액집계표: List[v2_3_간이과세자_신고서_레코드_신용카드매출전표_등_발행금액집계표]
    v2_3_간이과세자_신고서_레코드_영세율첨부서류제출명세서: List[v2_3_간이과세자_신고서_레코드_영세율첨부서류제출명세서]
    v2_3_간이과세자_신고서_레코드_의제매입세액공제신고서합계: List[v2_3_간이과세자_신고서_레코드_의제매입세액공제신고서합계]
    v2_3_간이과세자_신고서_레코드_의제매입세액공제신고서명세: List[v2_3_간이과세자_신고서_레코드_의제매입세액공제신고서명세]
    v2_5_재활용폐자원_및_중고자동차매입세액공제신고서_합계: List[v2_5_재활용폐자원_및_중고자동차매입세액공제신고서_합계]
    v2_5_재활용폐자원_및_중고자동차매입세액공제신고서_명세: List[v2_5_재활용폐자원_및_중고자동차매입세액공제신고서_명세]
    v2_6_일반과세전환시재고품및감가상각자산신고서: List[v2_6_일반과세전환시재고품및감가상각자산신고서]
    v2_6_일반과세전환시재고품및감가상각자산신고서_명세: List[v2_6_일반과세전환시재고품및감가상각자산신고서_명세]
    v2_7_부동산임대공급가액명세서: List[v2_7_부동산임대공급가액명세서]
    v2_7_부동산임대공급가액명세서_세부내용: List[v2_7_부동산임대공급가액명세서_세부내용]
    v2_8_간이과세전환시재고품_및_감가상각자산신고서: List[v2_8_간이과세전환시재고품_및_감가상각자산신고서]
    v2_10_사업장별부가가치세과세표준_및_납부세액_환급세액신고명세서: List[v2_10_사업장별부가가치세과세표준_및_납부세액_환급세액신고명세서]
    v2_10_사업장별부가가치세과세표준_및_납부세액_환급세액신고명세서_세부내용: List[v2_10_사업장별부가가치세과세표준_및_납부세액_환급세액신고명세서_세부내용]
    v2_11_건물등_감가상각자산_취득명세서: List[v2_11_건물등_감가상각자산_취득명세서]
    v2_12_공제받지못할매입세액명세서_합계: List[v2_12_공제받지못할매입세액명세서_합계]
    v2_12_공제받지못할매입세액명세서_합계_명세: List[v2_12_공제받지못할매입세액명세서_합계_명세]
    v2_12_공제받지못할매입세액명세서_합계_공통매입세액안분계산내역: List[v2_12_공제받지못할매입세액명세서_합계_공통매입세액안분계산내역]
    v2_12_공제받지못할매입세액명세서_합계_공통매입세액정산내역: List[v2_12_공제받지못할매입세액명세서_합계_공통매입세액정산내역]
    v2_12_공제받지못할매입세액명세서_합계_납부세액환급세액재계산내역: List[v2_12_공제받지못할매입세액명세서_합계_납부세액환급세액재계산내역]
    v2_13_전자화폐결제명세서: List[v2_13_전자화폐결제명세서]
    v2_13_전자화폐결제명세서_세부내용: List[v2_13_전자화폐결제명세서_세부내용]
    v2_14_면세유류공급명세서: List[v2_14_면세유류공급명세서]
    v2_14_면세유류공급명세서_세부내용: List[v2_14_면세유류공급명세서_세부내용]
    v2_15_월별판매액합계표_농_축산_임_어업기자재_및_장애인보장구: List[v2_15_월별판매액합계표_농_축산_임_어업기자재_및_장애인보장구]
    v2_16_매입자발행세금계산서합계표_갑_합계: List[v2_16_매입자발행세금계산서합계표_갑_합계]
    v2_16_매입자발행세금계산서합계표_갑_세부내용: List[v2_16_매입자발행세금계산서합계표_갑_세부내용]
    v2_17_과세사업전환감가상각자산신고서_감가상각자산신고서면세사업자인적사항: List[v2_17_과세사업전환감가상각자산신고서_감가상각자산신고서면세사업자인적사항]
    v2_17_과세사업전환감가상각자산신고서_감가상각자산신고서감가상각자산신고서: List[v2_17_과세사업전환감가상각자산신고서_감가상각자산신고서감가상각자산신고서]
    v2_18_건물관리명세서: List[v2_18_건물관리명세서]
    v2_18_건물관리명세서_세부내용: List[v2_18_건물관리명세서_세부내용]
    v2_19_사업자단위과세의_사업장별부가가치세과세표준및납부세액_환급세액신고명세서_합계: List[v2_19_사업자단위과세의_사업장별부가가치세과세표준및납부세액_환급세액신고명세서_합계]
    v2_19_사업자단위과세의_사업장별부가가치세과세표준및납부세액_환급세액신고명세서_명세: List[v2_19_사업자단위과세의_사업장별부가가치세과세표준및납부세액_환급세액신고명세서_명세]
    v2_20_현금매출명세서: List[v2_20_현금매출명세서]
    v2_20_현금매출명세서_세부내용: List[v2_20_현금매출명세서_세부내용]
    v2_21_고금_의제매입세액_공제_신고서_고금의제매입세액공제신고서: List[v2_21_고금_의제매입세액_공제_신고서_고금의제매입세액공제신고서]
    v2_21_고금_의제매입세액_공제_신고서_고금_매입_매출_명세서세부내용: List[v2_21_고금_의제매입세액_공제_신고서_고금_매입_매출_명세서세부내용]
    v2_22_과세표준및세액의_결정_경정청구서: List[v2_22_과세표준및세액의_결정_경정청구서]
    v2_23_과세표준수정신고서_및_추가자진납부계산서: List[v2_23_과세표준수정신고서_및_추가자진납부계산서]
    v2_24_전자세금계산서_발급세액공제신고서: List[v2_24_전자세금계산서_발급세액공제신고서]
    v2_25_일반_간이과세전환시재고품등신고서: List[v2_25_일반_간이과세전환시재고품등신고서]
    v2_25_일반_간이과세전환시재고품등신고서_명세: List[v2_25_일반_간이과세전환시재고품등신고서_명세]
    v2_26_세액공제신청서: List[v2_26_세액공제신청서]
    v2_26_세액공제신청서_내국신용장_구매확인서전자발급명세서합계: List[v2_26_세액공제신청서_내국신용장_구매확인서전자발급명세서합계]
    v2_26_세액공제신청서_내국신용장_구매확인서전자발급명세서_명세: List[v2_26_세액공제신청서_내국신용장_구매확인서전자발급명세서_명세]
    v2_28_원산지확인서발급세액공제신고서_발급세액공제신고서합계: List[v2_28_원산지확인서발급세액공제신고서_발급세액공제신고서합계]
    v2_28_원산지확인서발급세액공제신고서_발급세액공제신고서명세: List[v2_28_원산지확인서발급세액공제신고서_발급세액공제신고서명세]
    v2_29_동물진료용역매출명세서: List[v2_29_동물진료용역매출명세서]
    v2_30_영세율매출명세서: List[v2_30_영세율매출명세서]
    v2_31_외국인관광객_면세물품_판매_및_환급실적명세서_합계: List[v2_31_외국인관광객_면세물품_판매_및_환급실적명세서_합계]
    v2_31_외국인관광객_면세물품_판매_및_환급실적명세서_명세: List[v2_31_외국인관광객_면세물품_판매_및_환급실적명세서_명세]
    v2_32_구리스크랩등_매입세액공제신고서_합계: List[v2_32_구리스크랩등_매입세액공제신고서_합계]
    v2_32_구리스크랩등_매입세액공제신고서_명세: List[v2_32_구리스크랩등_매입세액공제신고서_명세]
    v2_33_관세환급금등_명세서: List[v2_33_관세환급금등_명세서]
    v2_34_외국인물품_외교관면세판매기록표_판매_외교관면세판매기록표: List[v2_34_외국인물품_외교관면세판매기록표_판매_외교관면세판매기록표]
    v2_35_공급가액확정명세서: List[v2_35_공급가액확정명세서]
    v2_36_선박에_의한_운송용역_공급가액일람표_합계: List[v2_36_선박에_의한_운송용역_공급가액일람표_합계]
    v2_36_선박에_의한_운송용역_공급가액일람표_명세: List[v2_36_선박에_의한_운송용역_공급가액일람표_명세]
    v2_37_외항_선박등에_제공한_재화용역일람표_합계: List[v2_37_외항_선박등에_제공한_재화용역일람표_합계]
    v2_37_외항_선박등에_제공한_재화용역일람표_명세: List[v2_37_외항_선박등에_제공한_재화용역일람표_명세]
    v2_38_외화획득명세서_합계: List[v2_38_외화획득명세서_합계]
    v2_38_외화획득명세서_명세: List[v2_38_외화획득명세서_명세]
    v2_39_재화_용역공급기록표: List[v2_39_재화_용역공급기록표]
    v2_40_사업양도신고서_합계: List[v2_40_사업양도신고서_합계]
    v2_40_사업양도신고서_명세: List[v2_40_사업양도신고서_명세]
    v2_41_외국인관광객_즉시환급_물품_판매_실적명세서_합계: List[v2_41_외국인관광객_즉시환급_물품_판매_실적명세서_합계]
    v2_41_외국인관광객_즉시환급_물품_판매_실적명세서_명세: List[v2_41_외국인관광객_즉시환급_물품_판매_실적명세서_명세]
    v2_42_평창동계올림픽_관련_사업자에_대한_의제매입세액공제_신고서_합계: List[v2_42_평창동계올림픽_관련_사업자에_대한_의제매입세액공제_신고서_합계]
    v2_42_평창동계올림픽_관련_사업자에_대한_의제매입세액공제_신고서_명세: List[v2_42_평창동계올림픽_관련_사업자에_대한_의제매입세액공제_신고서_명세]
    v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_합계: List[v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_합계]
    v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_명세: List[v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_명세]
    v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_입국경로에_설치된_보세판매장_공급실적명세서_명세: List[
        v2_43_2019_광주_세계수영선수권대회_관련_사업자에_대한_의제매입세액공제_신고서_입국경로에_설치된_보세판매장_공급실적명세서_명세]
    v2_45_소규모_개인사업자_부가가치세_감면신청서_신청서_합계: List[v2_45_소규모_개인사업자_부가가치세_감면신청서_신청서_합계]
    v2_45_소규모_개인사업자_부가가치세_감면신청서_신청서_명세: List[v2_45_소규모_개인사업자_부가가치세_감면신청서_신청서_명세]
    v2_46_외국인관광객_숙박용역_환급실적명세서_합계: List[v2_46_외국인관광객_숙박용역_환급실적명세서_합계]
    v2_46_외국인관광객_숙박용역_환급실적명세서_명세: List[v2_46_외국인관광객_숙박용역_환급실적명세서_명세]
    v2_47_외국인관광객_미용성형_의료용역_환급실적명세서_합계: List[v2_47_외국인관광객_미용성형_의료용역_환급실적명세서_합계]
    v2_47_외국인관광객_미용성형_의료용역_환급실적명세서_명세: List[v2_47_외국인관광객_미용성형_의료용역_환급실적명세서_명세]
    v3_1_세금계산서합계표_표지_Head_Record: List[v3_1_세금계산서합계표_표지_Head_Record]
    v3_1_세금계산서합계표_지연전송한_전자세금계산서를_여기에_적습니다: List[v3_1_세금계산서합계표_지연전송한_전자세금계산서를_여기에_적습니다]
    v3_1_세금계산서합계표_지연전송한_전자세금계산서를_여기에_적습니다: List[v3_1_세금계산서합계표_지연전송한_전자세금계산서를_여기에_적습니다]
    v3_1_세금계산서합계표_전자세금계산서분_매출합계_Total_Record: List[v3_1_세금계산서합계표_전자세금계산서분_매출합계_Total_Record]
    v3_1_세금계산서합계표_14_세액_전자세금계산서분_주민등록번호_발행분의_세액의_합계를_수록함_음수인_경우_멀티키_Multi_Key_사용_116_페이지_참고: List[
        v3_1_세금계산서합계표_14_세액_전자세금계산서분_주민등록번호_발행분의_세액의_합계를_수록함_음수인_경우_멀티키_Multi_Key_사용_116_페이지_참고]
    v3_1_세금계산서합계표: List[v3_1_세금계산서합계표]
    v3_1_세금계산서합계표_전자세금계산서분_매입합계_Total_Record: List[v3_1_세금계산서합계표_전자세금계산서분_매입합계_Total_Record]
    v3_2_계산서합계표_제출자_대리인레코드: List[v3_2_계산서합계표_제출자_대리인레코드]
    v3_2_계산서합계표_제출의무자인적사항레코드: List[v3_2_계산서합계표_제출의무자인적사항레코드]
    v3_2_계산서합계표_제출의무자별집계레코드_매출: List[v3_2_계산서합계표_제출의무자별집계레코드_매출]
    v3_2_계산서합계표_지연전송한_전자계산서를_여기에_적습니다: List[v3_2_계산서합계표_지연전송한_전자계산서를_여기에_적습니다]
    v3_2_계산서합계표_전자계산서_매출집계레코드_매출: List[v3_2_계산서합계표_전자계산서_매출집계레코드_매출]
    v3_2_계산서합계표_제출자_대리인레코드_매입: List[v3_2_계산서합계표_제출자_대리인레코드_매입]
    v3_2_계산서합계표_매출계산서의_A레코드와_공동으로_사용함에_따라_삭제처리함_제출의무자인적사항레코드_매입: List[v3_2_계산서합계표_매출계산서의_A레코드와_공동으로_사용함에_따라_삭제처리함_제출의무자인적사항레코드_매입]
    v3_2_계산서합계표_지연전송한_전자계산서를_여기에_적습니다: List[v3_2_계산서합계표_지연전송한_전자계산서를_여기에_적습니다]
    v3_2_계산서합계표_지연전송한_전자계산서를_여기에_적습니다: List[v3_2_계산서합계표_지연전송한_전자계산서를_여기에_적습니다]
    v3_2_계산서합계표_전자계산서_매입집계레코드: List[v3_2_계산서합계표_전자계산서_매입집계레코드]
    v3_3_수출실적_명세서_전산매체_A_레코드: List[v3_3_수출실적_명세서_전산매체_A_레코드]
    v3_3_수출실적_명세서_전산매체_B_레코드: List[v3_3_수출실적_명세서_전산매체_B_레코드]
    v3_3_수출실적_명세서_전산매체_C_레코드: List[v3_3_수출실적_명세서_전산매체_C_레코드]
    v3_4_신용카드매출전표등수령명세서_갑_을_제출자_인적사항_Header_Record: List[v3_4_신용카드매출전표등수령명세서_갑_을_제출자_인적사항_Header_Record]
    v3_4_신용카드매출전표등수령명세서_갑_을_기타신용_직불카드_및_기명식선불카드_매출전표_수령금액_명세_Data_Record: List[
        v3_4_신용카드매출전표등수령명세서_갑_을_기타신용_직불카드_및_기명식선불카드_매출전표_수령금액_명세_Data_Record]
    v3_4_신용카드매출전표등수령명세서_갑_을_신용카드등_매입내용_합계_Tail_Record: List[v3_4_신용카드매출전표등수령명세서_갑_을_신용카드등_매입내용_합계_Tail_Record]
