from typing import Optional

from src.internal.biz.serializers.base_serializer import BaseSerializer
from src.internal.biz.entities.menu_common import MenuCommon

SER_FOR_GET_MENU = 'ser-for-get-menu'


class MenuSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_FOR_GET_MENU:
            return cls._ser_for_get_menu
        else:
            raise TypeError

    @staticmethod
    def _ser_for_get_menu(menu_common: Optional[MenuCommon]):
        return {'menu_main_id': menu_common.menu.id,
                'menu_main_name': menu_common.menu.name,
                'menu_main_photo_link': menu_common.menu.photo.full_url,
                'language_id': menu_common.language.id,
                'language_name': menu_common.language.name,
                'currency_id': menu_common.currency.id,
                'currency_sign': menu_common.currency.sign,
                'categories': [MenuSerializer.categories(category, menu_common) for category in menu_common.menu_category]
                }

    @staticmethod
    def categories(category, menu_common):
        data = {
            'menu_category_id': category.id,
            'menu_category_name': category.name,
            'dishes': [MenuSerializer.dishes(dish_main, menu_common) for dish_main in menu_common.dish_main if dish_main.menu_category.id == category.id]
        }
        return data

    @staticmethod
    def dishes(dish_main, menu_common):
        data = {
            'measure_unit_id': dish_main.measure_unit.id,
            'measure_unit_name': menu_common.measure_unit[dish_main.measure_unit.id - 1].short_name,
            'dish_main_id': dish_main.id,
            'dish_main_name': dish_main.name,
            'dish_main_photo': dish_main.photo.full_url,
            'dish_main_description': dish_main.description
        }
        return data
