import itertools
from dataclasses import asdict, dataclass
from datetime import date
from types import ModuleType
from typing import List, Dict, ClassVar, get_type_hints

from opentaxkr.ers.report import detect_report_type, 전자신고서식


class ERSReport:
    format_class: ClassVar[전자신고서식]
    histories: ClassVar[Dict[date, 'ERSReport']]
    report_date_field: ClassVar[str]

    def __init__(self):
        self.format: 전자신고서식 = self.format_class.as_of()

        for field, type_hint in get_type_hints(self.__class__, include_extras=True).items():
            if type_hint._name == 'List' and type_hint.__args__ and issubclass(type_hint.__args__[0], ERSRecord):
                setattr(self, field, [])

    @classmethod
    def records_module(cls) -> ModuleType:
        raise NotImplementedError

    @classmethod
    def from_list_of_dict(cls, list_of_dict: List[Dict]):
        # TODO 날짜에 따라 맞는 모듈 찾기
        # format = cls.format.as_of(list_of_dict[0][cls.report_date_field])
        # TODO
        return cls([getattr(cls.records_module(), record_dict.pop('서식명'))(**record_dict) for record_dict in list_of_dict])

    def record_list(self):
        return itertools.chain(*[getattr(self, record['서식명']) for record in self.format.schema['레코드']])

    def serialize(self):
        return [self.format.serialize_record(record.asdict()) for record in self.record_list()]


@dataclass(kw_only=True)
class ERSRecord:
    def asdict(self):
        return dict(서식명=self.__class__.__name__) | asdict(self)

    def calculate(self):
        pass