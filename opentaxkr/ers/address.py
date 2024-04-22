import csv
import logging
import os
import re
from dataclasses import dataclass, field, fields

import requests

from config import settings

with open(os.path.dirname(__file__) + '/법정동코드_국세청홈페이지_18년6월7일.csv', encoding='utf8') as f:
    법정동코드표_국세청 = [[col for col in row] for row in csv.reader(f)]


@dataclass(kw_only=True)
class 도로명주소:
    전체_도로명주소: str = field(default='', metadata={'key': 'roadAddr'})
    도로명주소_참고항목_제외:str = field(metadata={'key': 'roadAddrPart1'})
    도로명주소_참고항목: str = field(default=None, metadata={'key': 'roadAddrPart2'})
    지번주소: str = field(metadata={'key': 'jibunAddr'})
    도로명주소_영문: str = field(metadata={'key': 'engAddr'})
    우편번호: str = field(metadata={'key': 'zipNo'})
    행정구역코드: str = field(metadata={'key': 'admCd'})
    도로명코드: str = field(metadata={'key': 'rnMgtSn'})
    건물관리번호: str = field(metadata={'key': 'bdMgtSn'})
    상세건물명: str = field(default=None, metadata={'key': 'detBdNmList'})
    건물명: str = field(default=None, metadata={'key': 'bdNm'})
    공동주택여부: str = field(metadata={'key': 'bdKdcd', 'help': '0: 비공동주택, 1: 공동주택'})
    시도명: str = field(metadata={'key': 'siNm'})
    시군구명: str = field(metadata={'key': 'sggNm'})
    읍면동명: str = field(metadata={'key': 'emdNm'})
    법정리명: str = field(default=None, metadata={'key': 'liNm'})
    도로명: str = field(metadata={'key': 'rn'})
    지하여부: str = field(metadata={'key': 'udrtYn', 'help': '0: 지상, 1: 지하'})
    건물본번: int = field(metadata={'key': 'buldMnnm'})
    건물부번: int = field(metadata={'key': 'buldSlno'})
    산여부: str = field(metadata={'key': 'mtYn', 'help': '0: 대지, 1: 산'})
    지번본번_번지: int = field(metadata={'key': 'lnbrMnnm'})
    지번부번_호: int = field(metadata={'key': 'lnbrSlno'})
    읍면동일련번호: str = field(metadata={'key': 'emdNo'})
    변동이력여부: str = field(metadata={'key': 'hstryYn', 'help': '0: 현행 주소정보, 1: 요청변수의 keyword(검색어)가 변동된 주소정보에서 검색된 정보'})
    관련지번: str = field(default=None, metadata={'key': 'relJibun'})
    관할주민센터: str = field(default=None, metadata={'key': 'hemdNm'})
    상세주소: str = ''
    법정동코드: str = None
    세무서코드: str = None
    특수지코드: str = None

    @classmethod
    def from_juso_response(cls, data, detail_address=''):
        return cls(**{field.name: data.get(field.metadata['key']) for field in fields(cls) if 'key' in field.metadata},
                   상세주소=detail_address)

    @staticmethod
    def split_법정동명_공동주택건물명(address):
        searched = re.search(r'\(.+\)', address)
        법정동명_건물명 = ''
        parts = []
        if searched:
            법정동명_건물명 = searched.group()
            parts = [p for p in re.split(',| ', 법정동명_건물명[1:-1]) if p]

        도로명주소 = ' '.join([p for p in re.split(r' |,', address.replace(법정동명_건물명, '')) if p])
        return 도로명주소, parts

    @staticmethod
    def parse(text):
        address, 법정동명_건물명 = 도로명주소.split_법정동명_공동주택건물명(text)
        normalized = address
        if 법정동명_건물명:
            normalized += ' (' + ', '.join(법정동명_건물명) + ')'

        parts = address.split(' ')
        try:
            for l in range(len(parts), 2, -1):
                data = 도로명주소.search(' '.join(parts[:l]))
                if data['results']['juso']:
                    juso = data['results']['juso'][0]
                    return 도로명주소.from_juso_response(juso, ' '.join(parts[l:]))
                    # return 주소(normalized, juso['siNm'], juso['sggNm'], juso['emdNm'], juso['zipNo'], juso['roadAddr'], data=data)
            else:
                return 도로명주소(normalized)
        except Exception as e:
            logging.exception(e)
            return 도로명주소(text)

    @staticmethod
    def search(address):
        return requests.get('http://www.juso.go.kr/addrlink/addrLinkApi.do', data={
            'confmKey': settings.juso_go_kr_api_key,
            'keyword': ' '.join([p for p in address.split(' ') if p]),
            'resultType': 'json'
        }, headers={
            'Accept-Language': 'ko'
        }).json()

    def __post_init__(self):
        try:
            row = next(filter(lambda row: row[2] == self.시도명 and row[3] == self.시군구명 and row[4] == self.읍면동명, 법정동코드표_국세청))
            self.세무서코드, self.법정동코드 = row[0], row[1]
        except:
            self.세무서코드 = self.법정동코드 = None

        if self.산여부 == '1':
            self.특수지코드 = '1'
        else:
            self.특수지코드 = '0'

    def __repr__(self):
        return f'{self.전체_도로명주소} [우편번호]{self.우편번호} [세무서]{self.세무서코드}'
