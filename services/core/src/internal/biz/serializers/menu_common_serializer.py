from typing import Optional

from src.internal.biz.entities.menu_common import MenuCommon
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.entities.language import Language
from src.internal.biz.entities.currency import Currency
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.count_dishes import CountDishes


def get_menu_common_serialize(menu: list, count_dish_main_for_category) -> Optional[MenuCommon]:
    menu_common = MenuCommon(
        main_menu=MenuMain(
            id=menu[0]['menu_main_id'],
            name=menu[0]['menu_main_name'],
            photo=menu[0]['menu_main_photo_link']
        ),
        language=Language(
            id=menu[0]['language_id'],
            name=menu[0]['language_name']
        ),
        menu_category=[
            MenuCategory(
                id=menu[i]['menu_category_id'],
                name=menu[i]['menu_category_name']
            ) for i in range(len(menu) - len(count_dish_main_for_category))],
        measure_unit=[
            MeasureUnit(
                id=menu[i]['measure_unit_id'],
                name=menu[i]['measure_unit_short_name']
            ) for i in range(len(menu) - len(count_dish_main_for_category))],
        dish_main=[
            DishMain(
                id=menu[i]['dish_main_id'],
                name=menu[i]['dish_main_name'],
                photo=menu[i]['dish_main_photo_link'],
                description=menu[i]['dish_main_description'],
                menu_category=menu[i]['dish_main_menu_category_id']
            ) for i in range(len(menu) - len(count_dish_main_for_category))],
        dish_measures=[
            DishMeasure(
                id=menu[i]['dish_measure_id'],
                price_value=menu[i]['dish_measure_price_value'],
                measure_value=menu[i]['dish_measure_measure_value']
            ) for i in range(len(menu) - len(count_dish_main_for_category))],
        currency=Currency(
            id=menu[0]['currency_id'],
            sign=menu[0]['currency_sign']
        ),
        count_dishes=[
            CountDishes(
                id=menu[i]['count_dish_main_id'],
                cnt=menu[i]['count_dish_main']
            )for i in range(len(menu) - len(count_dish_main_for_category), len(menu))])
    for j in range(len(menu) - len(count_dish_main_for_category)):
        print(menu_common.menu_category[j].id)
    return menu_common
