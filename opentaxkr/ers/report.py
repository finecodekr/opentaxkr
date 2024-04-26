import codecs
import csv
import difflib
import glob
import inspect
import itertools
import json
import logging
import os
import pprint
import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from io import StringIO, BytesIO
from pathlib import Path
from pkgutil import iter_modules

import dateutil.parser

FORMAT_DOC_DIR = os.path.dirname(__file__)


class 전자신고서식:
    세무프로그램코드 = '9000'

    def __init__(self, schema=None, published=None):
        self.schema = schema
        self.published = published

        self.first_record = None

    @classmethod
    def 서식_list(cls):
        for module_info in iter_modules([str(Path(__file__).parent)]):
            if '세' not in module_info.name:
                continue

            for name, value in inspect.getmembers(
                    module_info.module_finder.find_spec(module_info.name).loader.load_module()):
                if inspect.isclass(value) and issubclass(value, cls) and value != cls:
                    yield value

        # from taxreport.ntsreport import 원천징수이행상황신고, 지급명세서, 지방소득세특별징수, 부가가치세, 법인세
        # return cls.__subclasses__()

    @classmethod
    def for_name(cls, name):
        for subclass in cls.__subclasses__():
            if subclass.__name__ == name:
                return subclass

    @classmethod
    def load_histories(cls):
        cls.histories = {}
        prefix = getattr(cls, 'format_file_prefix', '')

        for filename in glob.glob(f'{os.path.dirname(inspect.getfile(cls))}/{prefix}*.json'):
            with open(filename, encoding='utf8') as f:
                published = dateutil.parser.parse(filename.split('_')[-1].split('.')[0]).date()
                cls.histories[published] = cls(json.load(f), published)

    @classmethod
    def as_of(cls, 기준일=None) -> '전자신고서식':
        for dt in sorted(cls.histories, reverse=True):
            if dt <= (기준일 or date.today()):
                break

        return cls.histories[dt]

    def detect(self, bytes):
        first_record = self.schema['레코드'][0]
        if self.match_record(first_record, bytes[:int(first_record['필드'][-1]['누적'])]):
            return self.__class__.as_of(self.extract_기준일자(bytes))

        return None

    def match_record(self, record, bytes):
        check_fields = ['레코드구분', '레코드_구분', '자료구분', '서식코드', '자료구분_표지', '자료구분_합계', '자료구분_자료', '신고구분', '제출자구분', '권번호', '세목구분코드']
        date_fields = ['제출년월일']

        checked_fields_exists = False
        for field in record['필드']:
            if field['name'] in check_fields:
                checked_fields_exists = True
                if not self.extract_field(field, bytes) in map(lambda s: s.strip(), field['점검'].split(',')):
                    return False
            elif field['name'] in date_fields:
                try:
                    datetime.strptime(self.extract_field(field, bytes), '%Y%m%d')
                except ValueError:
                    return False

            if record['서식명'] == 'v3_2_계산서합계표_제출의무자인적사항레코드':
                if field['name'] == '세무서' and 세무서명(self.extract_field(field, bytes)) is None:
                    return False
                if field['name'] == '사업자등록번호' and not validate_사업자등록번호(self.extract_field(field, bytes)):
                    return False

        return checked_fields_exists

    def extract_field(self, field, bytes):
        return bytes[int(field['누적']) - int(field['길이']):int(field['누적'])].decode('euckr')

    def unique_keys_from_records(self, records):
        raise NotImplementedError

    def filename(self, first_record):
        return f"{date.today().strftime('%Y%m%d')}{first_record['서식코드']}.{first_record.get('신고구분상세코드', first_record.get('납부구분'))}"

    def serialize_record(self, record, keep_extra_fields=True):
        """
        레코드의 필드를 스키마에 맞춰서 JSON 호환 가능한 형태로 만든다.
        :param record_name:
        :param record:
        :param keep_extra_fields: 스키마에 없는 필드를 보존할지 결정한다. 기본값은 False
        :return:
        """
        serialized = dict(record) if keep_extra_fields else dict()
        for field in self.schema_for_record_name(record['서식명'])['필드']:
            serialized[field['name']] = self.serialize_field(field, record.get(field['name']))

        for k, v in serialized.items():
            if isinstance(v, Decimal):
                serialized[k] = int(v)

        return serialized

    def serialize_field(self, field, value):
        if field['name'] in ['자료구분', '서식코드', '레코드구분', '레코드_구분']:
            value = value or field['점검']

        length = int(field['길이'])
        if field['TYPE'] == 'NUMBER':
            if not value:
                value = 0

            if isinstance(value, date):
                value = int(value.strftime('%Y%m%d')[:length])
        elif field['TYPE'] == 'CHAR':
            if isinstance(value, bool):
                value = 'Y' if value else 'N'
            elif field.get('점검') == 'Y,N':
                value = 'N' if not value else value
            elif isinstance(value, date):
                value = value.strftime('%Y%m%d')[:length]
            elif value is None:
                value = ''

        return codecs.decode(str(value).encode('euckr', errors='ignore')[:length], encoding='euckr', errors='ignore').strip()

    def deserialize_record(self, record):
        """
        JSON 호환 가능한 dict 타입의 데이터를 스키마에 맞게 파이썬에서 다루기 쉬운 자료형으로 변환한다.
        :param record_name:
        :param record:
        :param keep_extra_fields:
        :return:
        """
        for field in self.schema_for_record_name(record['서식명'])['필드']:
            if record.get(field['name']) is not None:
                record[field['name']] = self.deserialize_field(field, record[field['name']])

        return record

    def try_datetime(self, value):
        try:
            return datetime.strptime(str(value), "%Y-%m-%d")
        except ValueError:
            return value

    def deserialize_field(self, field, value):
        if field['TYPE'] == 'NUMBER':
            try:
                return self.try_datetime(Decimal(value))
            except InvalidOperation:
                return 0
            except TypeError:
                return value
        elif field['TYPE'] == 'CHAR':
            return self.try_datetime(value)

    def schema_for_record(self, **kwargs):
        for rs in self.schema['레코드']:
            if all(rs[k] == v for k, v in kwargs.items()):
                return rs
        raise Exception(f'schema not found: {kwargs}')

    def schema_for_record_name(self, record_name):
        return self.schema_for_record(서식명=record_name)

    def schema_for_record_header(self, line):
        for record in self.schema['레코드']:
            if self.match_record(record, line):
                return record

        raise Exception(f'{self} matching record not found: {line.decode("euckr")}')

    def find_field(self, record_name, field_name):
        fields = self.schema_for_record_name(record_name)['필드']
        return next(filter(lambda field: field['name'] == field_name, fields))

    def format_serialized_records(self, records, keep_custom_records=False):
        buffer = BytesIO()
        for record in records:
            schema = self.schema_for_record(서식명=record['서식명'])
            if schema.get('custom') and keep_custom_records is False:
                continue
            for field in schema['필드']:
                buffer.write(self.format_serialized_field(field, record[field['name']]))
            buffer.write(b'\r\n')

        return buffer.getvalue()

    def format_serialized_field(self, field, value):
        length = int(field['길이'])

        if field['TYPE'] == 'NUMBER':
            decimal_places = field.get('소수점길이', 0)
            if decimal_places:
                length += 1
            if 'Multi-Key+정수점검' in field.get('점검', '') and Decimal(value) < 0:
                multi_key = ['}','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
                converted = str(abs(Decimal(value)))[:-1] + multi_key[int(str(abs(Decimal(value)))[-1])]
                return converted.rjust(length, '0').encode('euckr')
            return f"{{:0{length}.{decimal_places}f}}".format(Decimal(value)).replace('.', '').encode('euckr')
        elif field['TYPE'] == 'CHAR':
            value = value.encode('euckr')
            return value + (b' ' * (length - len(value)))

    def code(self, table, key, value):
        return [code for code in self.schema['코드'][table] if code[key] == value][0]

    def split(self, stream):
        report = b''
        for line in stream.splitlines():
            first_record = self.schema['레코드'][0]
            if self.match_record(first_record, line):
                if len(report) > 0:
                    yield report
                report = b''
            report += line + b'\n'
        if len(report) > 0:
            yield report

    def parse(self, stream):
        return [self.parse_record(line)[1] for line in stream]

    def parse_record(self, line):
        """
        Line Sequential 형태에 EUC-KR로 인코딩된 bytes를 JSON에 담을 수 있는 형태의 dict로 변환한다.
        """
        line = line.replace(b'\r', b'').replace(b'\n', b'')

        record_schema = self.schema_for_record_header(line)
        record = {'서식명': record_schema['서식명']}
        col = 0

        for field in record_schema['필드']:
            try:
                if not field.get('길이', ''):
                    continue

                value = line[col:col + int(field['길이'])].decode('euckr')

                if field['TYPE'] == 'NUMBER':
                    # process crazy multi-key
                    if value[-1] in '}JKLMNOPQR':
                        value = '-' + value[:-1] + str('}JKLMNOPQR'.index(value[-1]))

                    value = str(Decimal(value.strip() or 0) / pow(10, int(field.get('소수점길이', 0))))
                elif field['TYPE'] == 'CHAR':
                    value = value.strip()

                record[field['name']] = value
                col += int(field['길이'])
            except Exception:
                logging.error('parse error', record_schema['서식명'], field['name'], field['길이'], col, line[col:col + int(field['길이'])], line)
                raise

        return record_schema, record

    def diff_record_set(self, from_records: 'RecordSet', to_records: 'RecordSet', exclude_custom_records=True):
        """
        RecordSet을 인자로 받아서 레코드 종류별로 diff를 해서 레코드 개수가 안 맞을 때도 레코드별로 diff를 보기 쉽게 한다.
        :param exclude_custom_records: diff시 custom 레코드들을 제외할 것인지 결정. 기본값은 True
        """
        result = StringIO()

        for record_schema in self.schema['레코드']:
            if exclude_custom_records and record_schema.get('custom'):
                continue
            result.write(self.diff(from_records.filter(record_schema['서식명']),
                                   to_records.filter(record_schema['서식명']),
                                   'FROM: ', 'TO: '))
        return result.getvalue()

    def diff(self, from_records, to_records, from_prefix='', to_prefix=''):
        result = StringIO()

        from_records = [(r['서식명'], self.serialize_record(r, False)) for r in from_records]
        to_records = [(r['서식명'], self.serialize_record(r, False)) for r in to_records]

        for f_record, t_record in itertools.zip_longest(from_records, to_records, fillvalue=('None', None)):
            d1 = [line + '\n' for line in pprint.pformat(f_record[1]).replace('None', '').splitlines()]
            d2 = [line + '\n' for line in pprint.pformat(t_record[1]).replace('None', '').splitlines()]

            result.writelines(difflib.unified_diff(d1, d2, fromfile=from_prefix + f_record[0], tofile=to_prefix + t_record[0]))
            result.write('\n')

        return result.getvalue()

    def field_names(self, 서식명, filter_fn=None, **kwargs):
        for field in self.schema_for_record_name(서식명)['필드']:
            if filter_fn and not filter_fn(field):
                continue

            for k in kwargs:
                if k.endswith('__in'):
                    if field[k[:-4]] not in kwargs[k]:
                        break
                elif field[k] != kwargs[k]:
                    break
            else:
                yield field['name']


class UnknownHeaderException(Exception):
    pass


def detect_report_type(bytes):
    for cls in 전자신고서식.서식_list():
        양식 = cls.as_of().detect(bytes)
        if 양식:
            return 양식

    raise UnknownHeaderException('Cannot detect 전자신고 서식 from header line:', bytes.splitlines()[0].decode('euckr'))


with open(FORMAT_DOC_DIR + '/전국세무서.csv', encoding='utf-8-sig') as f:
    전국세무서정보 = [{k: v.strip() for k, v in row.items()} for row in csv.DictReader(f)]


# TODO replace this with util.법정동코드표
with open(FORMAT_DOC_DIR + '/법정동코드_국세청홈페이지_18년6월7일.csv', encoding='utf8') as f:
    법정동코드표_국세청 = [[col for col in row] for row in csv.reader(f)]


def find_개인_법인구분(법인명_상호):
    법인명_상호 = 법인명_상호.replace('(주)', '주식회사').replace('(유)', '유한회사')
    for code in 개인_법인구분:
        if '.+' in code[0] and re.match(code[0], 법인명_상호):
            return code[1]
        elif code[0] in 법인명_상호:
            return code[1]
    return '90'


def find_세무서코드(주소):
    주소 = re.sub(' +', ' ', 주소)
    주소 = re.sub('서울시 ', '서울특별시 ', 주소) # 서울특별시로 일괄 맞춤

    시도, *나머지 = 주소.split(' ')
    match = re.match(r'([^,]*[시군구])\s+(.*)', ' '.join(나머지))
    시군구 = match.group(1) if match else ''
    시군구_이하주소 = match.group(2) if match else ' '.join(나머지)

    법정동주소_candidate = 시군구_이하주소.split(' ')[0]
    if re.match('.*로', 법정동주소_candidate) or re.match('.*길', 법정동주소_candidate):
        # 도로명주소로는 세무서를 찾을 수 없다. 괄호 안에 있는 내용을 이용함
        법정동 = re.match(r'.+?\(([^,]+\d가|[^, ()]+동|[^, ]+읍).*\)', 시군구_이하주소).group(1).replace(' ', '')
    else:
        법정동 = 시군구_이하주소.split(' ')[0]

    try:
        return next(filter(lambda row: 시도 == row[2] and row[3] == 시군구 and 법정동 == row[4], 법정동코드표_국세청))[0]
    except StopIteration:
        return next(filter(lambda row: 시도 == row[2] and row[3] == 시군구, 법정동코드표_국세청))[0]


def 세무서명(세무서코드):
    try:
        return next(filter(lambda row: row['세무서코드'] == 세무서코드, 전국세무서정보))['세무서명']
    except StopIteration:
        return None


def validate_사업자등록번호(target):
    if len(target) != 10 or not target.isdigit():
        return False

    code = "137137135"
    check_sum = sum([int(a) * int(b) for a, b in zip(code, target[:-1])])
    check_sum = (check_sum + int(target[-2]) * 5 // 10) % 10

    return int(target[-1]) == (check_sum if check_sum == 0 else 10 - check_sum)
