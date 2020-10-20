from typing import Any, Iterable

from src.internal.biz.entities.dish_measure import DishMeasure


class DishMeasures(list):

    def __init__(self, initial_values: Iterable) -> None:
        for value in initial_values:
            self.__class__._check(value)
        super().__init__(initial_values)

    def append(self, dish_measure: DishMeasure) -> None:
        self.__class__._check(dish_measure)
        super().append(dish_measure)

    def pop_by_dish_main_id(self, dish_main_id: int):
        for i in range(len(self)):
            if self[i].dish_main.id == dish_main_id:
                return self.pop(i)

    @staticmethod
    def _check(value: Any):
        if not isinstance(value, DishMeasure):
            raise TypeError
