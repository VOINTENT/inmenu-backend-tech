from typing import List, Union

from asyncpg import Record

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.dish_measure import DishMeasureDeserializer, DES_DISH_MEASURE_ADD, \
    DES_DISH_MEASURE_FROM_DB_FULL
from src.internal.biz.entities.dish_measures import DishMeasures

DES_DISH_MEASURES_ADD = 'dish-measures-add'
DES_DISH_MEASURES_FROM_DB_FULL = 'dish-measure-from-db-full'


class DishMeasuresDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_MEASURES_ADD:
            return cls._deserialize_add
        elif format_des == DES_DISH_MEASURES_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_measures: List[dict]):
        return [DishMeasureDeserializer.deserialize(dish_measure, DES_DISH_MEASURE_ADD) for dish_measure in dish_measures]

    @staticmethod
    def _deserialize_from_db_full(dish_measures: List[Union[dict, Record]]) -> DishMeasures:
        return DishMeasures([DishMeasureDeserializer.deserialize(dish_measure, DES_DISH_MEASURE_FROM_DB_FULL)
                             for dish_measure in dish_measures])
