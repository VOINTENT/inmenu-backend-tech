from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.place_main import PlaceMain


class MenuCategory(AbstractModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 menu_main: Optional[MenuMain] = None,
                 name: str = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__menu_main = menu_main
        self.__name = name

    @property
    def menu_main(self) -> MenuMain:
        return self.__menu_main

    @property
    def name(self) -> str:
        return self.__name
