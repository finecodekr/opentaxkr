import ast
import codecs
import re
import textwrap

from bs4 import BeautifulSoup

from opentaxkr.ers.util import strip


def parse(filename, prefix, overrides=None):
    '''
        국세청에서 배포한 전자신고 파일설명서 DOCX를 MS WORD에서 웹 페이지로 저장.
        그 파일을 파싱해서 포맷 정보를 dict로 반환한다.
        :param filename 파일명
    '''

    data = {'line_header_length': 9}
    formats = {}
    codes = {}

    대분류 = 소분류 = 중분류 = None

    index = 0
    with codecs.open(filename, encoding='utf8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

        for table in soup.find_all('table'):
            if table.tr.td.text.strip() != '번호':
                continue

            title = find_previous_non_table_sibling(table)

            if title and '○ ' in title.text:
                index += 1
            else:
                continue

            서식명 = normalize_field_name(f'{prefix}{index:02}_{title.text.replace("○ ", "").replace('테이블', '').replace('레코드', '')}')
            print(서식명)

            formats.setdefault(서식명, {'서식명': 서식명, '필드': []})
            record = formats[서식명]

            i = 0
            field_prefix = ''
            for tr in table.find_all('tr'):
                tds = tr.find_all('td')
                if tds[0].text.strip() == '번호':
                    if strip(tds[2].text) in ['신고서 항목', '신고서항목', '서식번호', '서식 항목', '영문명']:
                        i = 1

                    점검_index = 6 + i if len(tds) >= 7 else 5 + i
                    점검_index += sum(int(td.get('colspan', 1)) - 1 for td in tds)

                    continue

                if tds[0].text.strip() == '삭제':
                    continue

                점검_index_diff = -sum(int(td.get('colspan', 1)) - 1 for td in tds)

                if not tds[0].text.strip()[:2].isnumeric() or not strip(tds[1].text.replace('\xa0', '')):
                    break

                field_name = normalize_field_name(strip(tds[1].text))
                if any(f for f in record['필드'] if f['name'] == field_name):
                    field_name = f'{field_name}2'

                field = {
                    '번호': strip(tds[0].text),
                    'name': field_name,
                    '한글명': strip(tds[1].text),
                    'TYPE': strip(tds[2 + i].text),
                    '길이': strip(tds[3 + i].text),
                    '누적': strip(tds[4 + i].text),
                    '비고': strip(tds[5 + i].text),
                    '점검': strip(tds[점검_index + 점검_index_diff].text),
                }

                if field['한글명'] == '자료구분':
                    record['자료구분'] = fix_자료구분(field.get('점검내용', field.get('점검')))
                if field['한글명'] == '서식코드':
                    record['서식코드'] = field.get('점검내용', field.get('점검'))
                if ',' in field['길이']:
                    field['길이'], field['소수점길이'] = field['길이'].split(',')

                if overrides and overrides.get(서식명, {}).get(field['name']):
                    field.update(overrides[서식명][field['name']])

                record['필드'].append(field)

    data['레코드'] = list(formats.values())
    data['코드'] = codes
    return data


def normalize_field_name(field_name):
    """
    서식 문서의 서식명, 필드명 등을 python, javascript에서 identifier로 쓸 수 있는 형태로 변환.
    이 코드를 수정한 후에는 모든 신고서의 docparser를 돌려서 결과 json을 비교해볼 것.
    TODO docparser를 일일이 안 돌려봐도 되도록 테스트 케이스 작성할 것.
    """
    normalized = field_name.strip()
    normalized = normalized.replace('\x9f', '_')
    normalized = re.sub(r'\([^\(]+\([^\)]+\)[^\)]+\)', r'', normalized)
    normalized = re.sub(r'\(([0-9]+)\)', r'', normalized)
    normalized = re.sub(r'\(([^0-9\)]+)\)', r'_\1', normalized)
    normalized = re.sub(r'^([0-9]+)', r'_\1', normalized)
    normalized = re.sub(r'[一-龥]+', r'', normalized)
    normalized = re.sub(r'[㉮-㉲]+', r'', normalized)
    normalized = re.sub(r'[①-⑳]', lambda m: '_' + str(ord(m.group(0)) - ord('①') + 1) + '_', normalized)
    normalized = re.sub(r'\[([^\]]+)\]', r'_\1_', normalized)
    normalized = re.sub(r'\<([^\>]+)\>', r'', normalized) # <2019_03_07_공지> 등
    normalized = re.sub(r"\( *[`’‘]([^\]]+)\)", r'', normalized) # 농어촌특별세납부할세액_최초 (’15.9.7. 추가)	등
    normalized = re.sub(r"\(([^\]]+)\)", r'_\1_', normalized)
    normalized = re.sub(r"\>=([0-9]+)", r'gte\1', normalized) # 감면대상소득비율_감면대상사업소득비율>=80인_경우
    normalized = re.sub(r"\<([0-9]+)", r'lt\1', normalized) # 감면대상소득비율_감면대상사업소득비율<80인_경우
    normalized = re.sub(r'[:–\-_\s\t,\.+·･․‧【】•∙%`「」\(\)²\&\/\*]+', r'_', normalized) # 위의 규칙들에서 처리되지 않은 괄호()는 여기서 변환
    normalized = re.sub(r'^[^가-힣_0-9a-zA-Z]+', '', normalized)
    normalized = re.sub(r'_+$', '', normalized)
    return normalized


def find_title(element):
    subtitle = find_previous_non_table_sibling(element)
    if not subtitle:
        return None, None

    title = find_previous_non_table_sibling(subtitle)
    parent_title = find_previous_non_table_sibling(title)

    return parent_title, title, subtitle


def find_previous_non_table_sibling(element):
    previous = element.find_previous_sibling('p')
    if not previous or previous.name == 'table':
        return None

    text = strip(previous.text)
    if previous.name == 'p' and text and not re.match(r'^\(.+\)$', text):
        return previous

    return find_previous_non_table_sibling(previous)


def fix_자료구분(자료구분):
    return re.sub(r'[\'‘’]', '', 자료구분).replace('Fix', '').strip()


def reset_class_fields(module: ast.Module, class_name: str, default_code: str):
    try:
        class_def = next(filter(lambda node: isinstance(node, ast.ClassDef) and node.name == class_name,
                                module.body))
        class_def.body = [node for node in class_def.body if not isinstance(node, ast.AnnAssign)]
    except:
        class_def = ast.parse(textwrap.dedent(default_code)).body[0]
        class_def.body = []
        module.body.append(class_def)

    return class_def


def convert_type(field):
    if field['점검'] == '일자형식점검':
        return 'date'
    elif field['TYPE'] == 'CHAR':
        return 'str'
    elif field['TYPE'] == 'NUMBER' and '소수점길이' in field:
        return 'Decimal'
    elif field['TYPE'] == 'NUMBER':
        return 'int'


def field_options(field):
    if field['name'] in ['자료구분', '서식코드', '레코드구분', '레코드_구분', '세목구분코드']:
        default_expression = f"default='{field['점검']}', "
    elif 'Not Null' not in field['비고']:
        default_expression = 'default=None, '
    elif 'default' in field['비고']:
        default_value = re.findall(r'default ([^ ]+)', field['비고'])[0]
        if convert_type(field) == 'int':
            default_expression = f'default={default_value}, '
        else:
            default_expression = f"default='{default_value}', "
    else:
        default_expression = ''

    options = {
        'max_length': int(field['길이']),
        '점검': field['점검'],
        '비고': field['비고']
    }
    if '소수점길이' in field:
        options['decimal_places'] = int(field['소수점길이'])

    # TODO 점검 값으로 제한하기
    # if ',' in field['점검']:
    #     return " = Literal['" + "', '".join(field['점검'].split(',')) + "']"

    return f"field({default_expression}metadata={repr(options)})"
