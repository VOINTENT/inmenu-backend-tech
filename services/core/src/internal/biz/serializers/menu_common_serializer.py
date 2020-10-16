from typing import Optional, List, Coroutine

from src.internal.biz.entities.menu_common import MenuCommon
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.entities.language import Language
from src.internal.biz.entities.currency import Currency
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.count_dishes import CountDishes


def get_menu_common_serialize(menu_main: Optional[MenuMain],
                              language: Optional[Language],
                              currency: Optional[Currency],
                              menu_category: Optional[List[MenuCategory]],
                              dish_main: Optional[List[DishMain]],
                              dish_measure: Optional[List[DishMeasure]],
                              measure_unit: Optional[List[MeasureUnit]],
                              count_dish_in_category: Optional[List[CountDishes]]) -> Optional[MenuCommon]:
    menu_common = MenuCommon(
        main_menu=MenuMain(
            id=menu_main.id,
            name=menu_main.name,
            photo=menu_main.photo
        ),
        language=Language(
            id=language.id,
            name=language.name
        ),
        menu_category=menu_category,
        measure_unit=measure_unit,
        dish_main=dish_main,
        dish_measures=dish_measure,
        currency=currency,
        count_dishes=count_dish_in_category
    )
    return menu_common
