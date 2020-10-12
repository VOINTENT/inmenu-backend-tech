from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel


class MeasureUnit(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 name: Optional[str] = None,
                 short_name: Optional[str] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__name = name
        self.__short_name = short_name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name
