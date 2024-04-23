import ast
import json
import re
import codecs
import textwrap
from difflib import SequenceMatcher
from pathlib import Path

import autopep8
from bs4 import BeautifulSoup
from pycodestyle import StyleGuide
from pydantic import Field
from yapf.yapflib.yapf_api import FormatCode

from opentaxkr.ers.docparser import reset_class_fields, parse


def convert_type(field):
    if field['TYPE'] == 'CHAR':
        return 'str'
    elif field['TYPE'] == 'NUMBER' and '소수점길이' in field:
        return 'Decimal'
    elif field['TYPE'] == 'NUMBER':
        return 'int'


def field_options(field):
    if field['name'] in ['자료구분', '서식코드', '레코드구분', '레코드_구분']:
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


def generate_format_files(source, json_filename, python_filename):
    doc_format = parse(source)
    with open(json_filename, 'w', encoding='utf8') as f:
        json.dump(doc_format, f, indent=4, ensure_ascii=False)

    imports = ast.parse(textwrap.dedent(f"""\
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
        """))

    if Path(python_filename).exists():
        with open(python_filename, 'r', encoding='utf8') as f:
            module = ast.parse(f.read())
    else:
        module = ast.Module(body=[], type_ignores=[])

    module.body = imports.body + [node for node in module.body
                                  if not isinstance(node, ast.ImportFrom) and not isinstance(node, ast.Import)]

    for record in doc_format['레코드']:
        class_def = reset_class_fields(module, record['서식명'], f"""\
            @dataclass(kw_only=True)
            class {record['서식명']}(ERSRecord):
                pass
        """)

        computed_fields = {node.name[len('compute_'):]: node for node in class_def.body
                           if node.name.startswith('compute_')}

        for field in reversed(record['필드']):
            if not field['name']:
                continue

            class_def.body.insert(0, ast.AnnAssign(
                target=ast.Name(field['name'], ast.Store()),
                annotation=ast.Name(convert_type(field), ast.Load()),
                value=ast.parse(field_options(field)).body[0].value,
                simple=1
            ))

    class_def = reset_class_fields(module, '양도소득세신고', f"""\
        class 양도소득세신고(양도소득세.양도소득세신고):
            pass
    """)
    for record in reversed(doc_format['레코드']):
        class_def.body.insert(0, ast.parse(f"{record['서식명']}: List[{record['서식명']}] = field(default_factory=list)").body[0])

    with open(python_filename, 'w', encoding='utf8') as f:
        f.write(FormatCode(ast.unparse(module), style_config={'column_limit': 140})[0])


generate_format_files('양도소득세 전자신고 파일설명서_V5.8_(20200224).htm',
                      '양도소득세신고서식_2020-02-24.json',
                      'records_20200224.py')
generate_format_files('양도소득세 전자신고 파일설명서_V5.13_(20230502).htm',
                      '양도소득세신고서식_2023-05-02.json',
                      'records_20230502.py')
