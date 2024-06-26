import re
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path

from bs4 import BeautifulSoup

from opentaxkr.ers.docparser import generate_record_classes, normalize_field_name, \
    find_previous_non_table_sibling, normalize_record_name
from opentaxkr.ers.util import strip


def parse(filename):
    '''
        국세청에서 배포한 전자신고 파일설명서를 **MS Word**에서 다른 형식으로 저장 - 웹 페이지로 저장해두면
        그 파일을 파싱해서 포맷 정보를 dict로 반환한다.
        전자신고 파일설명서는 홈택스 -> 자료실 에서 `원천징수`로 검색하면 나온다.
        :param filename 파일명
    '''

    data = {'line_header_length': 9}
    formats = []
    codes = {}

    대분류 = 소분류 = 중분류 = None

    with open(filename, encoding='utf8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        for table in soup.find_all('table'):
            if parse_if_code_table(table, codes):
                continue
            elif strip(table.tr.td.text) != '번호':
                continue

            title, subtitle = find_title(table)

            # print(strip(title.text), '|||||||||', strip(subtitle.text))
            if not subtitle:
                continue

            if strip(title.text) in ['1. 부가가치세 일반 및 간이 신고서', '2. 첨부서류', '3. 전산매체 테이블']:
                대분류 = strip(title.text)

            if title:
                title_text = re.sub(r'※[^.]+\.\.', '', title.text, flags=re.MULTILINE)
                if '간이과세자 신고서 레코드' in title_text:
                    title_text = re.sub(r'\([^)]+\)', '', title_text)


            if re.findall(r'^[0-9]+\) ?', strip(title_text)):
                중분류 = strip(title_text).replace('_', '')
            if re.findall(r'^[0-9]+\) ?', strip(subtitle.text)):
                중분류 = strip(subtitle.text).replace('_', '')

            소분류 = strip(subtitle.text).replace('_', '')
            if 중분류 == 소분류 or '※' in 소분류:
                소분류 = None

            for dot in ['m', '¡']:
                if dot in subtitle.text:
                    소분류 = strip(subtitle.text.replace(dot, ''))

            if 소분류 == '표지(Head Record)':
                대분류 = '3. 전산매체 테이블'
                중분류 = '1) 세금계산서합계표'

            if 중분류 == '42) 2019 광주 세계수영선수권대회 관련 사업자에 대한 의제매입세액공제 신고서':
                중분류 = '43) 2019 광주 세계수영선수권대회 관련 사업자에 대한 의제매입세액공제 신고서'

            대분류 = 대분류.replace('.', '_')
            중분류 = normalize_field_name(re.sub(r'(^[0-9]+)\)?([^ ])', r'\1_\2', 중분류.replace(' ', '')))
            서식명 = f'V{대분류[:2]}{중분류}'
            if 소분류:
                소분류 = normalize_record_name(소분류).replace('_', '')
                matches = SequenceMatcher(None, 중분류, 소분류).get_matching_blocks()
                if matches and matches[0].b == 0 and matches[0].size >= 5:
                    소분류 = 소분류[matches[0].size:]
                서식명 += '_' + 소분류

            서식명 = fix_2019_change(normalize_field_name(서식명))
            서식명 = fix_currupted(normalize_field_name(서식명))
            서식명 = normalize_record_name(서식명)
            print(서식명)
            
            record = {'서식명': 서식명, '필드': []}
            first, second, *unused = record['서식명'].split('_')
            record['order_key'] = int(first[1:]) * 100 + int(second)

            i = 0
            field_prefix = ''
            for tr in table.find_all('tr'):
                tds = tr.find_all('td')
                if tds[0].text.strip() == '번호':
                    if strip(tds[2].text) in ['신고서 항목', '신고서항목', '서식번호', '서식 항목']:
                        i = 1

                    점검_index = 6 + i if len(tds) >= 7 else 5 + i
                    continue

                field = {
                    '번호': strip(tds[0].text),
                    'name': normalize_field_name(strip(tds[1].text)),
                    '한글명': strip(tds[1].text),
                    'TYPE': strip(tds[2 + i].text),
                    '길이': strip(tds[3 + i].text),
                    '누적': strip(tds[4 + i].text),
                    '비고': strip(tds[5 + i].text),
                    '점검': strip(tds[점검_index].text),
                }

                field['name'] = field['name'].replace('_21_6_30_이전', '')
                if field['name'].startswith('과표영세율') and field['name'].endswith('_기타'):
                    field['name'] = field['name'].replace('_기타', '')
                if field['name'].startswith('매입세금계산서등공제'):
                    field['name'] = field['name'].replace('등', '')

                if not field['TYPE'] and not field['길이']:
                    if re.match(r'_[^\(\)]+', field['name']) and '시작구분자' not in field['name']:
                        field_prefix = field['name'][1:] + '_'
                    continue

                if field_prefix and field['name'] != '공란':
                    field['name'] = field_prefix + field['name']

                if field['한글명'] == '자료구분':
                    field['점검'] = record['자료구분'] = fix_자료구분(field.get('점검내용', field.get('점검')))

                if field['한글명'] == '서식코드':
                    record['서식코드'] = field.get('점검내용', field.get('점검'))
                if ',' in field['길이']:
                    field['길이'], field['소수점길이'] = field['길이'].split(',')

                # '음수처리' 필드명 예외처리
                if 서식명 == 'V3_4_신용카드매출전표등수령명세서_갑_을_기타신용직불카드및기명식선불카드매출전표수령금액명세Data':
                    if strip(tds[0].text) == '10':
                        field['name'] = "공급가액음수표시"
                    elif strip(tds[0].text) == '12':
                        field['name'] = "세액음수표시"
                if 서식명 == 'V3_4_신용카드매출전표등수령명세서_갑_을_신용카드등매입내용합계Tail':
                    if strip(tds[0].text) == '8':
                        field['name'] = "총공급가액음수표시"
                    elif strip(tds[0].text) == '10':
                        field['name'] = "총세액음수표시"

                record['필드'].append(field)

            formats.append(record)
            if 서식명 == '42) 2019 광주 세계수영선수권대회 관련 사업자에 대한 의제매입세액공제 신고서':
                break

    data['레코드'] = formats
    data['코드'] = codes
    return data


def find_title(element):
    subtitle = find_previous_non_table_sibling(element)
    if not subtitle:
        return None, None

    title = find_previous_non_table_sibling(subtitle)
    
    # 상위 제목을 발견할 수 없으면 그냥 테이블 바로 위에 있는 제목을 title로 두고 subtitle이 없다고 간주한다.
    if not title:
        return subtitle, None
    
    if not strip(title.text):
        title = find_previous_non_table_sibling(title)

    return title, subtitle


코드_map = {
    '3.가산세코드': '가산세코드',
    '3,공제감면코드': '공제감면코드',
    '2.공통은행코드': '공통은행코드'
}


def parse_if_code_table(table, codes):
    previous = table.find_previous_sibling('p')

    if not previous:
        return None

    코드명 = strip(previous.text)
    if 코드명 not in 코드_map:
        return None

    코드명 = 코드_map[코드명]

    codes[코드명] = {}
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if skip_코드_map(코드명, tds):
            continue

        key = normalize_field_name(tds[1].text.strip())
        if key in codes[코드명]:
            key += '_'
        codes[코드명][key] = tds[0].text.strip()

    return 코드명


def fix_2019_change(서식명):
    서식명_2019_2018_map = {
        'V2_2_신용카드매출전표_등_발행금액집계표': 'V2_2_신용카드매출전표_등_발행금액_집계표',
        'V3_4_신용카드매출전표등_수령명세서_갑_을_제출자_인적사항_Header_Record': 'V3_4_신용카드매출전표등수령명세서_갑_을_제출자_인적사항_Header_Record',
        'V3_4_신용카드매출전표등_수령명세서_갑_을_기타신용_직불카드_및_기명식선불카드_매출전표_수령금액_명세_Data_Record': 'V3_4_신용카드매출전표등수령명세서_갑_을_기타신용_직불카드_및_기명식선불카드_매출전표_수령금액_명세_Data_Record',
        'V3_4_신용카드매출전표등_수령명세서_갑_을_신용카드등_매입내용_합계_Tail_Record': 'V3_4_신용카드매출전표등수령명세서_갑_을_신용카드등_매입내용_합계_Tail_Record',
    }
    return 서식명_2019_2018_map.get(서식명, 서식명)


def fix_currupted(서식명):
    서식명_currupted_map = {
        'V2_15_월별판매액합계표_농축산임어업기자재_및_장애인보장구': 'V2_15_월별판매액합계표_농_축산_임_어업기자재_및_장애인보장구'
    }
    return 서식명_currupted_map.get(서식명, 서식명)


def fix_자료구분(자료구분):
    return re.sub(r'[\'‘’]', '', 자료구분).replace('Fix', '').strip()


def skip_코드_map(코드명, tds):
    if tds[0].text.strip() == '코드':
        return True
    if 코드명 == '공통은행코드':
        if tds[0].text.strip() == '은행코드':
            return True
    return False


doc_format = parse('부가가치세_전자신고_파일설명서(2022.12월)_공지.html')

generate_record_classes(doc_format, Path(__file__).parent, date(2022, 12, 1))