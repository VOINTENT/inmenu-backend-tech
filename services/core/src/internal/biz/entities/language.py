from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.utils import check_value


class Language(AbstractModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 name: Optional[str] = None,
                 code_name: Optional[str] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(name=name, code_name=code_name)
        self.__name = name
        self.__code_name = code_name

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @property
    def code_name(self) -> Optional[str]:
        return self.__code_name

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['name'], str)
        check_value(kwargs['code_name'], str)
