from typing import Optional

from src.internal.biz.serializers.base_serializer import BaseSerializer
from src.internal.biz.entities.menu_common import MenuCommon

SER_FOR_GET_MENU = 'ser-for-get-menu'


class MenuSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_FOR_GET_MENU:
            return cls._ser_for_get_menu

    @staticmethod
    def _ser_for_get_menu(menu_common: Optional[MenuCommon]):
        return {'menu_main_id': menu_common.menu.id,
                'menu_main_name': menu_common.menu.name,
                'menu_main_photo_link': menu_common.menu.photo,
                'language_id': menu_common.language.id,
                'language_name': menu_common.language.name,
                'currency_id': menu_common.currency.id,
                'currency_sign': menu_common.currency.sign,
                'categories': [categories(category, menu_common) for category in menu_common.menu_category]
                }


def categories(category, menu_common):
    data = {
        'menu_category_id': category.id,
        'menu_category_name': category.name,
        'dishes': [dishes(i, menu_common) for i in menu_common.dish_main if i.menu_category.id == category.id]
    }
    return data


def dishes(i, menu_common):
    data = {
        'measure_unit_id': i.measure_unit.id,
        'measure_unit_name': menu_common.measure_unit[i.measure_unit.id - 1].short_name,
        'dish_main_id': i.id,
        'dish_main_name': i.name,
        'dish_main_photo': i.photo,
        'dish_main_description': i.description
    }
    return data
