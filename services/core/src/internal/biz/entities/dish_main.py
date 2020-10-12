from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo


class DishMain(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 name: Optional[str] = None,
                 photo: Optional[Photo] = None,
                 description: Optional[str] = None,
                 menu_main: Optional[MenuMain] = None,
                 menu_category: Optional[MenuCategory] = None,
                 measure_unit: Optional[MeasureUnit] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__name = name
        self.__photo = photo
        self.__description = description
        self.__menu_main = menu_main
        self.__menu_category = menu_category
        self.__measure_unit = measure_unit

    @property
    def name(self) -> str:
        return self.__name

    @property
    def photo(self) -> Photo:
        return self.__photo

    @property
    def description(self) -> str:
        return self.__description

    @property
    def menu_main(self) -> MenuMain:
        return self.__menu_main

    @property
    def menu_category(self) -> MenuCategory:
        return self.__menu_category

    @property
    def measure_unit(self):
        return self.__measure_unit
