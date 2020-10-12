from datetime import datetime
from typing import Optional

from src.internal.biz.entities.utils import check_value


class AbstractModel:
    """
    Абстрактная модель, содержащая в себе общие компоненты для каждой модели
    Класс должен наследоваться всеми другими моделями
    """

    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None) -> None:
        AbstractModel._check(id=id, created_at=created_at, edited_at=edited_at)
        self.__id = id
        self.__created_at = created_at
        self.__edited_at = edited_at

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value):
        check_value(value, int)
        self.__id = value

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @created_at.setter
    def created_at(self, value: datetime):
        check_value(value, datetime)
        self.__created_at = value

    @property
    def edited_at(self) -> datetime:
        return self.__edited_at

    @edited_at.setter
    def edited_at(self, value: datetime):
        check_value(value, datetime)
        self.__edited_at = value

    @property
    def created_at_timestamp(self):
        if self.created_at:
            return round(self.created_at.timestamp())
        return None

    @property
    def edited_at_timestamp(self):
        if self.edited_at:
            return round(self.edited_at.timestamp())
        return None

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['id'], int)
        check_value(kwargs['created_at'], datetime)
        check_value(kwargs['edited_at'], datetime)
