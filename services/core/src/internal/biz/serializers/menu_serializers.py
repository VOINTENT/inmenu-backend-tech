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
        print(len(menu_common.menu_category))
        print(len(menu_common.count_dishes))
        # data = {'menu_main_id': menu_common.menu.id,
        #         'menu_main_name': menu_common.menu.name,
        #         'menu_main_photo_link': menu_common.menu.photo,
        #         'language_id': menu_common.language.id,
        #         'language_name': menu_common.language.name,
        #         'currency_id': menu_common.currency.id,
        #         'currency_sign': menu_common.currency.sign,
        #         'categories': [iter(
        #             {
        #                 'menu_category_id': menu_common.menu_category[j].id,
        #                 'menu_category_name': menu_common.menu_category[j].name,
        #                 'dishes': [
        #                     {
        #                         'measure_unit_id': menu_common.measure_unit[i].id,
        #                         'measure_unit_name': menu_common.measure_unit[i].name,
        #                         'dish_main_id': menu_common.dish_main[i].id,
        #                         'dish_main_name': menu_common.dish_main[i].name,
        #                         'dish_main_photo': menu_common.dish_main[i].photo,
        #                         'dish_main_description': menu_common.dish_main[i].description
        #                     }
        #                     for i in range(len(menu_common.count_dishes))
        #                 ]
        #             }
        #             for j in range(len(menu_common.menu_category))
        #         )]
        #         }
        # print(data)
        return {'menu_main_id': menu_common.menu.id,
                'menu_main_name': menu_common.menu.name,
                'menu_main_photo_link': menu_common.menu.photo,
                'language_id': menu_common.language.id,
                'language_name': menu_common.language.name,
                'currency_id': menu_common.currency.id,
                'currency_sign': menu_common.currency.sign,
                'categories': categories(menu_common)
                #     {
                #         'menu_category_id': menu_common.menu_category[j].id,
                #         'menu_category_name': menu_common.menu_category[j].name,
                #         'dishes': [
                #             {
                #                 'measure_unit_id': menu_common.measure_unit[j + menu_common.count_dishes[i].cnt].id,
                #                 'measure_unit_name': menu_common.measure_unit[j + menu_common.count_dishes[i].cnt].name,
                #                 'dish_main_id': menu_common.dish_main[j + menu_common.count_dishes[i].cnt].id,
                #                 'dish_main_name': menu_common.dish_main[j + menu_common.count_dishes[i].cnt].name,
                #                 'dish_main_photo': menu_common.dish_main[j + menu_common.count_dishes[i].cnt].photo,
                #                 'dish_main_description': menu_common.dish_main[j + menu_common.count_dishes[i].cnt].description
                #             }
                #             for i in range(0, len(menu_common.count_dishes))
                #         ]
                #     }
                #     for j in range(0, len(menu_common.menu_category))
                # ]
                }


def categories(menu_common):
    data = []
    for i in range(len(menu_common.menu_category)):
        data.append({
            'menu_category_id': menu_common.menu_category[i].id,
            'menu_category_name': menu_common.menu_category[i].name,
            'dishes': dishes(menu_common, menu_common.count_dishes[i].cnt)
        })


def dishes(menu_common, menu_count):
    data = []
    for i in range(menu_count):
        data.append({
                'measure_unit_id': menu_common.measure_unit[i].id,
                'measure_unit_name': menu_common.measure_unit[i].name,
                'dish_main_id': menu_common.dish_main[i].id,
                'dish_main_name': menu_common.dish_main[i].name,
                'dish_main_photo': menu_common.dish_main[i].photo,
                'dish_main_description': menu_common.dish_main[i].description
        })
