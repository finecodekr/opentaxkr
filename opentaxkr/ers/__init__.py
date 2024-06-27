import importlib
import itertools
import logging
import pkgutil
from dataclasses import asdict, dataclass, fields, Field, MISSING
from datetime import date, datetime
from decimal import Decimal
from functools import cache
from pathlib import Path
from types import ModuleType
from typing import List, Dict, ClassVar, get_type_hints, TypeVar, Type, BinaryIO, Iterable

import dateutil.parser


세무프로그램코드 = '9000'
REPORT_CLASS_POSTFIX = '신고'


class ERSReport:
    published_date: ClassVar[date]
    histories: ClassVar[Dict[date, 'ERSReport']]
    report_date_field: ClassVar[str]
    record_classes: ClassVar[Dict[str, Type['ERSRecord']]]

    def __init_subclass__(cls, **kwargs):
        cls.record_classes = {k: v.__args__[0] for k, v in cls.__annotations__.items() if v.__origin__ == list and issubclass(v.__args__[0], ERSRecord)}

    def __init__(self):
        """신고서의 레코드들을 빈 list로 초기화한다."""
        # self.format: 전자신고서식 = self.format_class.as_of(self.__class__.published_date)

        for field, type_hint in get_type_hints(self.__class__, include_extras=True).items():
            if type_hint._name == 'List' and type_hint.__args__ and issubclass(type_hint.__args__[0], ERSRecord):
                setattr(self, field, [])

    T = TypeVar('T', bound='ERSReport')

    @classmethod
    def as_of(cls: Type[T], report_date: date) -> T:
        """신고 시점에 따라 과거의 서식으로 신고서를 작성할 때 사용한다. report_date에 입력한 날짜가 적용되는 시점의 신고 서식 클래스를 반환한다."""
        package_path = Path(__file__).parent / cls.__name__[:-len(REPORT_CLASS_POSTFIX)]
        for m_info in sorted(filter(lambda x: x.name.startswith('records'), pkgutil.iter_modules([package_path])),
                             key=lambda x: x.name, reverse=True):
            if m_info.name[-8:] <= report_date.strftime('%Y%m%d'):
                module = importlib.import_module(f'{cls.__module__[:-len('.records_yyyymmdd')]}.{m_info.name}')
                return getattr(module, cls.__name__)

        raise ValueError(f"No records module found for {cls.__name__} as of {report_date}")

    @classmethod
    def parse(cls, fp: BinaryIO):
        """전자신고서식에 맞게 데이터를 파싱한다."""
        report = cls()
        for line in fp:
            record = cls.parse_record(line)
            getattr(report, record.__class__.__name__).append(record)

        return report

    @classmethod
    def parse_record(cls, line: bytes):
        """
        Line Sequential 형태에 EUC-KR로 인코딩된 bytes를 JSON에 담을 수 있는 형태의 dict로 변환한다.
        """
        line = line.strip()

        record_class = cls.find_record_class(line)
        data = {}
        col = 0

        field: ERSField
        for field in record_class.fields().values():
            try:
                value = line[col:col + int(field.길이)].decode('euckr', errors='ignore').strip()

                if field.type in [int, Decimal]:
                    # process crazy multi-key
                    if value and value[-1] in '}JKLMNOPQR':
                        value = '-' + value[:-1] + str('}JKLMNOPQR'.index(value[-1]))

                    value = Decimal(value or 0) / pow(10, int(field.소수점길이 or 0))

                data[field.name] = value
                col += int(field.길이)
            except Exception:
                logging.error('parse error', record_class.__name__, field.name, field.길이, col, line[col:col + int(field.길이)], line)
                raise

        return record_class(**data)

    @classmethod
    def find_record_class(cls, line: bytes):
        for record_class in cls.record_classes.values():
            if  issubclass(record_class, ERSRecord) and record_class.match(line):
                return record_class

    @classmethod
    def records_module(cls) -> ModuleType:
        raise NotImplementedError

    @classmethod
    def from_list_of_dict(cls, list_of_dict: List[Dict]):
        # TODO 날짜에 따라 맞는 모듈 찾기
        # format = cls.format.as_of(list_of_dict[0][cls.report_date_field])
        # TODO
        return cls([getattr(cls.records_module(), record_dict.pop('서식명'))(**record_dict) for record_dict in list_of_dict])

    def records(self) -> Iterable['ERSRecord']:
        return itertools.chain(*[getattr(self, cls.__name__) for cls in self.record_classes.values()])

    def serialize(self):
        return b'\r\n'.join([record.serialize() for record in self.records()])

    def serialize_and_format(self):
        return self.format.format_serialized_records(self.serialize())

    def calculate(self):
        pass


@dataclass(kw_only=True)
class ERSRecord:

    @classmethod
    @cache
    def fields(cls) -> Dict[str, 'ERSField']:
        return {field.name: field for field in fields(cls)}

    def __setattr__(self, key, value):
        value = self.wrap_as_field_type(key, value)

        if self.fields()[key].default is not None and value is None:
            raise ValueError(f"{key} is required")

        super().__setattr__(key, value)

    def wrap_as_field_type(self, key, value):
        try:
            if value is None:
                return value

            if self.fields()[key].type is date and isinstance(value, str):
                return dateutil.parser.parse(value).date()

            if not isinstance(value, self.fields()[key].type):
                return self.fields()[key].type(value)

            return value
        except:
            logging.error('wrap_as_field_type error', key, value, self.fields()[key].type)
            raise

    def serialize(self) -> bytes:
        return b''.join([self.serialize_field(field) for field in self.fields().values()])

    def serialize_field(self, field: 'ERSField') -> bytes:
        value = getattr(self, field.name)

        if value is None:
            if field.name in ['자료구분', '서식코드', '레코드구분', '레코드_구분']:
                value = field.점검
            elif field.type in [int, Decimal]:
                value = 0
            elif field.type == str:
                value = ''

        if field.type == date:
            value = value.strftime('%Y%m%d')[:field.길이]
        elif field.type in [int, Decimal]:
            # 길이와 소수점길이에 맞게 포매팅한 뒤 소수점을 제거한다.
            value = f"{{:0{field.길이}.{field.소수점길이}f}}".format(value).replace('.', '').rjust(field.길이, '0')

        elif isinstance(value, bool):
            value = 'Y' if value else 'N'
        elif field.점검 == 'Y,N':
            value = 'N' if not value else value

        # return codecs.decode(str(value).encode('euckr', errors='ignore')[:field.길이], encoding='euckr', errors='ignore').strip()
        return str(value).encode('euckr', errors='ignore').ljust(field.길이, b' ')[:field.길이]

    def asdict(self):
        return dict(서식명=self.__class__.__name__) | asdict(self)

    @classmethod
    def match(cls, line: bytes):
        check_fields = ['레코드구분', '레코드_구분', '자료구분', '서식코드', '자료구분_표지', '자료구분_합계', '자료구분_자료', '신고구분',
                        '제출자구분', '권번호', '세목구분코드']
        date_fields = ['제출년월일']

        checked_fields_exists = False
        for field in cls.fields().values():
            if field.name in check_fields:
                checked_fields_exists = True
                if not cls.extract_field(field, line) in map(lambda s: s.strip(), field.점검.split(',')):
                    return False
            elif field.type == 'date':
                try:
                    datetime.strptime(cls.extract_field(field, line), '%Y%m%d')
                except ValueError:
                    return False

            # if record['서식명'] == 'v3_2_계산서합계표_제출의무자인적사항레코드':
            #     if field['name'] == '세무서' and 세무서명(self.extract_field(field, bytes)) is None:
            #         return False
            #     if field['name'] == '사업자등록번호' and not validate_사업자등록번호(self.extract_field(field, bytes)):
            #         return False

        return checked_fields_exists

    @classmethod
    def extract_field(cls, field: 'ERSField', line: bytes):
        return line[int(field.누적) - int(field.길이):int(field.누적)].decode('euckr')

    def calculate(self):
        pass


class ERSField(Field):
    def __init__(self, default=MISSING, default_factory=MISSING, 길이=None, 누적=None, 점검='', 비고='', 소수점길이=0):
        super().__init__(default=default, default_factory=default_factory,
                         init=True, repr=True, hash=None, compare=True, kw_only=True,
                         metadata=dict(길이=길이, 누적=누적, 점검=점검, 비고=비고, 소수점길이=소수점길이))

        self.길이 = 길이
        self.누적 = 누적
        self.점검 = 점검
        self.비고 = 비고
        self.소수점길이 = 소수점길이
