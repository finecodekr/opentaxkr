import ast
import json
import textwrap
from pathlib import Path

from yapf.yapflib.yapf_api import FormatCode

from opentaxkr.ers.docparser import reset_class_fields, parse, convert_type, field_options


def generate_format_files(source, json_filename, python_filename):
    doc_format = parse(source, 'LI', overrides={
        'LI02_양도소득_과세표준확정신고_기본정보': {
            '신고구분': {
                '점검': '11,13'
            }
        }
    })

    with open(json_filename, 'w', encoding='utf8') as f:
        json.dump(doc_format, f, indent=4, ensure_ascii=False)

    imports = ast.parse(textwrap.dedent(f"""\
            from dataclasses import dataclass, field
            from datetime import date
            from decimal import Decimal
            from typing import List

            from opentaxkr.ers import ERSRecord, ERSReport
            from opentaxkr.ers.양도소득_개인지방소득세 import 양도소득_개인지방소득세신고서식
            from opentaxkr.ers.양도소득세.records_20230502 import 양도소득세신고
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

    class_def = reset_class_fields(module, '양도소득_개인지방소득세신고', f"""\
        class 양도소득_개인지방소득세신고(ERSReport):
            pass
    """)
    for record in reversed(doc_format['레코드']):
        class_def.body.insert(0, ast.parse(f"{record['서식명']}: List[{record['서식명']}]").body[0])

    with open(python_filename, 'w', encoding='utf8') as f:
        f.write(FormatCode(ast.unparse(module), style_config={'column_limit': 140})[0])


generate_format_files('개인지방소득세(양도소득)_파일레이아웃_v1.2.3_20230703.html',
                      '양도소득_개인지방소득세신고서식_2023-07-03.json',
                      'records_20230703.py')
