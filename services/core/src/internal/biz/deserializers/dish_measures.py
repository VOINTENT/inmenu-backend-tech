from typing import List

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.dish_measure import DishMeasureDeserializer, DES_DISH_MEASURE_ADD

DES_DISH_MEASURES_ADD = 'dish-measures-add'


class DishMeasuresDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_MEASURES_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_measures: List[dict]):
        return [DishMeasureDeserializer.deserialize(dish_measure, DES_DISH_MEASURE_ADD) for dish_measure in dish_measures]
