from typing import Optional, List

from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure


class DishCommon:
    def __init__(self,
                 dish_main: Optional[DishMain] = None,
                 dish_measures: Optional[List[DishMeasure]] = None,
                 dish_measure: Optional[DishMeasure] = None) -> None:
        self.__dish_main = dish_main
        self.__dish_measures = dish_measures
        self.__dish_measure = dish_measure
        self.__dish_measure_price_str: Optional[str] = None
        self.__dish_measure_measure_str: Optional[str] = None

    @property
    def dish_main(self) -> Optional[DishMain]:
        return self.__dish_main

    @property
    def dish_measures(self) -> Optional[List[DishMeasure]]:
        return self.__dish_measures

    @property
    def dish_measure(self) -> Optional[DishMeasure]:
        return self.__dish_measure

    def create_measure_price_str(self) -> None:
        try:
            self.__dish_measure_price_str = f'{self.__dish_measure.price_value} {self.__dish_main.currency.sign}'
        except AttributeError or TypeError:
            return

    def create_measure_measure_str(self) -> None:
        try:
            self.__dish_measure_measure_str = f'{self.__dish_measure.measure_value} {self.__dish_main.measure_unit.short_name}'
        except AttributeError or TypeError:
            return

    @property
    def dish_measure_price_str(self):
        return self.__dish_measure_price_str

    @property
    def dish_measure_measure_str(self):
        return self.__dish_measure_measure_str
