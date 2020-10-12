from typing import Optional, List

from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure


class DishCommon:
    def __init__(self,
                 dish_main: Optional[DishMain] = None,
                 dish_measures: Optional[List[DishMeasure]] = None) -> None:
        self.__dish_main = dish_main
        self.__dish_measures = dish_measures

    @property
    def dish_main(self) -> Optional[DishMain]:
        return self.__dish_main

    @property
    def dish_measures(self) -> Optional[List[DishMeasure]]:
        return self.__dish_measures
