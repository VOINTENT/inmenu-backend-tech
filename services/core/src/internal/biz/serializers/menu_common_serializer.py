from typing import Optional, List, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.entities.menu_common import MenuCommon
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.entities.language import Language
from src.internal.biz.entities.currency import Currency
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.entities.menu_main import MenuMain


def get_menu_common_serialize(menu_main: Optional[MenuMain],
                              language: Optional[Language],
                              currency: Optional[Currency],
                              menu_categories: Optional[List[MenuCategory]],
                              dishes_main: Optional[List[DishMain]],
                              dish_measures: Optional[List[DishMeasure]],
                              measure_units: Optional[List[MeasureUnit]]) -> Tuple[Optional[MenuCommon], Optional[Error]]:
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
        menu_categories=menu_categories,
        measure_units=measure_units,
        dishes_main=dishes_main,
        dish_measures=dish_measures,
        currency=Currency(
            id=currency.id,
            sign=currency.sign
        )
    )
    if not menu_common:
        return None, ErrorEnum.MENU_COMMON_DOESNT_EXISTS
    return menu_common, None
