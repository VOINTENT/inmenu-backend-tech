from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.entities.service import Service
from src.internal.biz.entities.utils import check_value


class PlaceService(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 place_main: Optional[PlaceMain] = None,
                 service: Optional[Service] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(place_main=place_main, service=service)
        self.__place_main = place_main
        self.__service = service

    @property
    def place_main(self) -> Optional[PlaceMain]:
        return self.__place_main

    @place_main.setter
    def place_main(self, value: PlaceMain) -> None:
        self.__place_main = value

    @property
    def service(self):
        return self.__service

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['place_main'], PlaceMain)
        check_value(kwargs['service'], Service)
