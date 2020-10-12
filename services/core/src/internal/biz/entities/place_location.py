from datetime import datetime
from typing import Optional, Any, Tuple

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.entities.utils import check_value


class PlaceLocation(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 place_main: Optional[PlaceMain] = None,
                 full_address: Optional[str] = None,
                 coords: Optional[Tuple] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(coords=coords, full_address=full_address)
        self.__place_main = place_main
        self.__full_address = full_address
        self.__coords = coords

    @property
    def full_address(self) -> Optional[str]:
        return self.__full_address

    @property
    def coords(self) -> Optional[Any]:
        return self.__coords

    @property
    def place_main(self) -> Optional[PlaceMain]:
        return self.__place_main

    @place_main.setter
    def place_main(self, value: PlaceMain) -> None:
        self.__place_main = value

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['full_address'], str)
        check_value(kwargs['coords'], tuple)
