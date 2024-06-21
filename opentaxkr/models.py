from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from addresskr import 도로명주소

세무프로그램코드 = '9000'


class 홈택스사용자구분(Enum):
    개인 = '01'
    개인사업자 = '02'
    법인 = '03'


@dataclass(kw_only=True)
class 납세자:
    납세자ID: str
    납세자명: str
    홈택스ID: str = None
    홈택스사용자번호: str = None
    휴대전화번호: str = None
    전자메일주소: str = None
    주소: str = None
    사용자구분코드: 홈택스사용자구분 = None
    사업자등록일: str = None
    대표자주민등록번호: str = None
    대표자명: str = None
    국적코드: str = 'KR'
    거주지국가코드: str = 'KR'

    도로명주소: 도로명주소 = field(default=None, init=False)

    def __post_init__(self):
        if self.사용자구분코드:
            self.사용자구분코드 = 홈택스사용자구분(self.사용자구분코드)

        self.납세자ID = self.납세자ID.replace('-', '')
        self.도로명주소 = 도로명주소.parse(self.주소)
        self.휴대전화번호 = self.휴대전화번호.replace('-', '')


@dataclass(kw_only=True)
class 세무대리인:
    대표자주민등록번호: str
    법인등록번호: str = None
    대표자성명: str
    법인명_상호: str = None
    전화번호: str
    사업자등록번호: str
    관리번호: str
    성명: str
    생년월일: date
    사업장소재지: str = None
    우편번호: str = None
    세무서코드: str = None
    법정동코드: str = None
    홈택스ID: str = None

    def __post_init__(self):
        self.전화번호 = self.전화번호.replace('-', '')
