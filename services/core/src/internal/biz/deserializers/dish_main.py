from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.currency import CurrencyDeserializer, DES_CURRENCY_FROM_DB_FULL, CURRENCY
from src.internal.biz.deserializers.measure_unit import MEASURE_UNIT, MeasureUnitDeserializer, \
    DES_MEASURE_UNIT_FROM_DB_FULL
from src.internal.biz.deserializers.menu_category import MenuCategoryDeserializer, MENU_CATEGORY, \
    DES_MENU_CATEGORY_FROM_DB_FULL
from src.internal.biz.deserializers.menu_main import MENU_MAIN, MenuMainDeserializer, DES_MENU_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.photo import PHOTO, PhotoDeserializer, DES_PHOTO_FROM_DB_FULL
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo

DES_DISH_MAIN_ADD = 'dish-main-add'
DES_DISH_MAIN_FROM_DB_FULL = 'dish-main-from-db-full'

DISH_MAIN = 'dma_'
DISH_MAIN_ID = DISH_MAIN + ID
DISH_MAIN_CREATED_AT = DISH_MAIN + CREATED_AT
DISH_MAIN_EDITED_AT = DISH_MAIN + EDITED_AT
DISH_MAIN_NAME = DISH_MAIN + 'nm'
DISH_MAIN_DESCRIPTION = DISH_MAIN + 'ds'


class DishMainDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_DISH_MAIN_ADD:
            return cls._deserialize_add
        elif format_des == DES_DISH_MAIN_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(dish_main_dict: dict) -> DishMain:
        return DishMain(
            name=dish_main_dict['name'],
            photo=Photo(short_url=dish_main_dict['photo_link']),
            description=dish_main_dict['description'],
            menu_main=MenuMain(id=dish_main_dict['menu_id']),
            menu_category=MenuCategory(id=dish_main_dict['category_id']),
            measure_unit=MeasureUnit(id=dish_main_dict['measure_unit_id'])
        )

    @staticmethod
    def _deserialize_from_db_full(dish_main: Union[dict, Record]) -> DishMain:
        menu_main = filter_keys_by_substr(dish_main, MENU_MAIN)
        menu_category = filter_keys_by_substr(dish_main, MENU_CATEGORY)
        measure_unit = filter_keys_by_substr(dish_main, MEASURE_UNIT)
        currency = filter_keys_by_substr(dish_main, CURRENCY)
        photo= filter_keys_by_substr(dish_main, PHOTO)
        return DishMain(
            id=dish_main.get(DISH_MAIN_ID),
            created_at=dish_main.get(DISH_MAIN_CREATED_AT),
            edited_at=dish_main.get(DISH_MAIN_EDITED_AT),
            name=dish_main.get(DISH_MAIN_NAME),
            description=dish_main.get(DISH_MAIN_DESCRIPTION),
            menu_main=MenuMainDeserializer.deserialize(menu_main, DES_MENU_MAIN_FROM_DB_FULL),
            menu_category=MenuCategoryDeserializer.deserialize(menu_category, DES_MENU_CATEGORY_FROM_DB_FULL),
            measure_unit=MeasureUnitDeserializer.deserialize(measure_unit, DES_MEASURE_UNIT_FROM_DB_FULL),
            currency=CurrencyDeserializer.deserialize(currency, DES_CURRENCY_FROM_DB_FULL),
            photo=PhotoDeserializer.deserialize(photo, DES_PHOTO_FROM_DB_FULL)
        )
