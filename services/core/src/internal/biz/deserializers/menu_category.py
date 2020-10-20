from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.menu_main import MENU_MAIN, MenuMainDeserializer, DES_MENU_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain

DES_MENU_CATEGORY_ADD = 'menu-category-add'
DES_MENU_CATEGORY_FROM_DB_FULL = 'menu-main-category-from-db-full'

MENU_CATEGORY = 'mc_'
MENU_CATEGORY_ID = MENU_CATEGORY + ID
MENU_CATEGORY_CREATED_AT = MENU_CATEGORY + CREATED_AT
MENU_CATEGORY_EDITED_AT = MENU_CATEGORY + EDITED_AT
MENU_CATEGORY_NAME = MENU_CATEGORY + 'nm'


class MenuCategoryDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_MENU_CATEGORY_ADD:
            return cls._deserialize_add
        elif format_des == DES_MENU_CATEGORY_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(menu_category_dict: dict) -> MenuCategory:
        return MenuCategory(
            name=menu_category_dict['name'],
            menu_main=MenuMain(id=menu_category_dict['menu_id'])
        )

    @staticmethod
    def _deserialize_from_db_full(menu_category: Union[dict, Record]) -> MenuCategory:
        menu_main = filter_keys_by_substr(menu_category, MENU_MAIN)
        return MenuCategory(
            id=menu_category.get(MENU_CATEGORY_ID),
            created_at=menu_category.get(MENU_CATEGORY_CREATED_AT),
            edited_at=menu_category.get(MENU_CATEGORY_EDITED_AT),
            name=menu_category.get(MENU_CATEGORY_NAME),
            menu_main=MenuMainDeserializer.deserialize(menu_main, DES_MENU_MAIN_FROM_DB_FULL)
        )
