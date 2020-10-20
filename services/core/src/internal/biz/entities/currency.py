from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.utils import check_value


class Currency(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 name: Optional[str] = None,
                 short_name: Optional[str] = None,
                 sign: Optional[str] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(name=name, sign=sign)
        self.__name = name
        self.__sign = sign
        self.__short_name = short_name

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @property
    def sign(self) -> Optional[str]:
        return self.__sign

    def short_name(self) -> Optional[str]:
        return self.__short_name

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['name'], str)
        check_value(kwargs['sign'], str)
        check_value(kwargs['short_name'], str)
