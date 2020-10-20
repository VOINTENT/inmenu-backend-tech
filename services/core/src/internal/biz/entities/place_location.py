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
                 coords: Optional[Tuple] = None,
                 city: Optional[str] = None,
                 country: Optional[str] = None,
                 count_places: Optional[int] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(coords=coords, full_address=full_address, city=city, country=country)
        self.__place_main = place_main
        self.__full_address = full_address
        self.__city = city
        self.__country = country
        self.__coords = coords
        self.__count_places = count_places

    @property
    def full_address(self) -> Optional[str]:
        return self.__full_address

    @property
    def count_places(self):
        return self.__count_places

    @count_places.setter
    def count_places(self, value: int) -> None:
        self.__count_places = value

    @property
    def coords(self) -> Optional[Any]:
        return self.__coords

    @property
    def place_main(self) -> Optional[PlaceMain]:
        return self.__place_main

    @place_main.setter
    def place_main(self, value: PlaceMain) -> None:
        self.__place_main = value

    @property
    def city(self) -> str:
        return self.__city

    @property
    def country(self) -> str:
        return self.__country

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['full_address'], str)
        check_value(kwargs['coords'], tuple)
        check_value(kwargs['city'], str)
        check_value(kwargs['country'], str)
