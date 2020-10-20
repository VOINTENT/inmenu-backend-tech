from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.dish_main import DishMainDeserializer, DES_DISH_MAIN_ADD, DISH_MAIN, \
    DES_DISH_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.dish_measure import DISH_MEASURE, DES_DISH_MEASURE_FROM_DB_FULL
from src.internal.biz.deserializers.dish_measures import DishMeasuresDeserializer, DES_DISH_MEASURES_ADD
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.dish_common import DishCommon

DES_DISH_COMMON_ADD = 'dish-common-add'
DES_DISH_COMMON_FROM_DB_FULL = 'dish-common-from-db-full'


class DishCommonDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_COMMON_ADD:
            return cls._deserialize_add
        elif format_des == DES_DISH_COMMON_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_common_dict: dict) -> DishCommon:
        return DishCommon(
            dish_main=DishMainDeserializer.deserialize(dish_common_dict, DES_DISH_MAIN_ADD),
            dish_measures=DishMeasuresDeserializer.deserialize(dish_common_dict['measures'], DES_DISH_MEASURES_ADD)
        )

    @staticmethod
    def _deserialize_from_db_full(dish_common: Union[dict, Record]) -> DishCommon:
        dish_main = filter_keys_by_substr(dish_common, DISH_MAIN)
        dish_measure = filter_keys_by_substr(dish_common, DISH_MEASURE)
        return DishCommon(
            dish_main=DishMainDeserializer.deserialize(dish_main, DES_DISH_MAIN_FROM_DB_FULL),
            dish_measure=DishMeasuresDeserializer.deserialize(dish_measure, DES_DISH_MEASURE_FROM_DB_FULL)
        )
