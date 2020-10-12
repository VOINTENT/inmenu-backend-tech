from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_main import PlaceMain


class MenuMain(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 name: Optional[str] = None,
                 photo: Optional[Photo] = None,
                 place_main: Optional[PlaceMain] = None
                 ) -> None:
        super().__init__(id, created_at, edited_at)
        self.__name = name
        self.__photo = photo
        self.__place_main = place_main

    @property
    def name(self):
        return self.__name

    @property
    def photo(self):
        return self.__photo

    @property
    def place_main(self):
        return self.__place_main
