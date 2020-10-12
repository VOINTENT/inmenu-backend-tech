from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.utils import check_value


class Service(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 name: Optional[str] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(name=name)
        self.__name = name

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['name'], str)
