from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.entities.place_type import PlaceType
from src.internal.biz.entities.utils import check_value


class PlacePlaceType(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 place_main: Optional[PlaceMain] = None,
                 place_type: Optional[PlaceType] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__place_main = place_main
        self.__place_type = place_type

    @property
    def place_main(self) -> Optional[PlaceMain]:
        return self.__place_main

    @place_main.setter
    def place_main(self, value: PlaceMain) -> None:
        self.__place_main = value

    @property
    def place_type(self) -> Optional[PlaceType]:
        return self.__place_type

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['place_type'], PlaceType)
        check_value(kwargs['place_main'], PlaceMain)
