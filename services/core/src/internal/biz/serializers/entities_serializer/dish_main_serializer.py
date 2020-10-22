from typing import re, Optional, List

from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain


def dishes_main_serializer(data) -> Optional[List[DishMain]]:
    try:
        dishes_main = [
            DishMain(
                id=data[i]['dish_main_id'],
                name=data[i]['dish_main_name'],
                photo=data[i]['dish_main_photo_link'],
                description=data[i]['dish_main_description'],
                menu_main=MenuMain(id=data[i]['dish_main_menu_main_id']),
                menu_category=MenuCategory(id=data[i]['dish_main_menu_category_id']),
                measure_unit=MeasureUnit(id=data[i]['dish_main_measure_unit_id']))
            for i in range(len(data))
        ]
        return dishes_main
    except:
        raise TypeError

