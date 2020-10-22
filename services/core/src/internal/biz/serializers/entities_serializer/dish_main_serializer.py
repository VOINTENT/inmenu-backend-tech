from typing import Optional

from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.photo import Photo


def dishes_main_serializer(dictionary: dict) -> Optional[DishMain]:
    try:
        dish_main = DishMain(
                id=dictionary['dish_main_id'],
                name=dictionary['dish_main_name'],
                photo=Photo(full_url=dictionary['dish_main_photo_link']),
                description=dictionary['dish_main_description'],
                menu_main=MenuMain(id=dictionary['dish_main_menu_main_id']),
                menu_category=MenuCategory(id=dictionary['dish_main_menu_category_id']),
                measure_unit=MeasureUnit(id=dictionary['dish_main_measure_unit_id']))
        return dish_main
    except:
        raise TypeError
