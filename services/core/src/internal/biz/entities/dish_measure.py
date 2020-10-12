from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.dish_main import DishMain


class DishMeasure(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 dish_main: Optional[DishMain] = None,
                 price_value: int = None,
                 measure_value: int = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__dish_main = dish_main
        self.__price_value = price_value
        self.__measure_value = measure_value

    @property
    def dish_main(self):
        return self.__dish_main

    @dish_main.setter
    def dish_main(self, value: DishMain):
        self.__dish_main = value

    @property
    def price_value(self):
        return self.__price_value

    @property
    def measure_value(self):
        return self.__measure_value
