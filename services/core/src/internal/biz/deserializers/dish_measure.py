from typing import Union

from asyncpg import Record
# from loguru import logger

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.dish_main import DISH_MAIN, DishMainDeserializer, DES_DISH_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.dish_measure import DishMeasure

DES_DISH_MEASURE_ADD = 'dish-measure-add'
DES_DISH_MEASURE_FROM_DB_FULL = 'dish=measure-from-db-full'

DISH_MEASURE = 'dme_'
DISH_MEASURE_ID = DISH_MEASURE + ID
DISH_MEASURE_CREATED_AT = DISH_MEASURE + CREATED_AT
DISH_MEASURE_EDITED_AT = DISH_MEASURE + EDITED_AT
DISH_MEASURE_PRICE_VALUE = DISH_MEASURE + 'pv'
DISH_MEASURE_MEASURE_VALUE = DISH_MEASURE + 'mv'


class DishMeasureDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_MEASURE_ADD:
            return cls._deserialize_add
        elif format_des == DES_DISH_MEASURE_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_measure_dict: dict) -> DishMeasure:
        return DishMeasure(
            price_value=dish_measure_dict['price_value'],
            measure_value=dish_measure_dict['measure_value']
        )

    @staticmethod
    def _deserialize_from_db_full(dish_measure: Union[dict, Record]) -> DishMeasure:
        dish_main = filter_keys_by_substr(dish_measure, DISH_MAIN)
        return DishMeasure(
            id=dish_measure.get(DISH_MEASURE_ID),
            created_at=dish_measure.get(DISH_MEASURE_CREATED_AT),
            edited_at=dish_measure.get(DISH_MEASURE_EDITED_AT),
            price_value=dish_measure.get(DISH_MEASURE_PRICE_VALUE),
            measure_value=dish_measure.get(DISH_MEASURE_MEASURE_VALUE),
            dish_main=DishMainDeserializer.deserialize(dish_main, DES_DISH_MAIN_FROM_DB_FULL)
        )
