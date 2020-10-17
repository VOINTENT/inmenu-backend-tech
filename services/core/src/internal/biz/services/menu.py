from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.dish_common_dao import DishCommonDao
from src.internal.biz.dao.menu_category import MenuCategoryDao
from src.internal.biz.dao.menu_main import MenuMainDao
from src.internal.biz.dao.place_account_role import PlaceAccountRoleDao
from src.internal.biz.dao.place_main_dao import PlaceMainDao
from src.internal.biz.entities.dish_common import DishCommon
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.services.base_service import BaseService
from src.internal.biz.dao.dish_main_dao import DishMainDao
from src.internal.biz.dao.language import LanguageDao
from src.internal.biz.dao.currency import CurrencyDao
from src.internal.biz.dao.dish_measure_dao import DishMeasureDao
from src.internal.biz.dao.measure_unit import MeasureUnitDao

from src.internal.biz.serializers.menu_common_serializer import get_menu_common_serialize



class MenuService(BaseService):

    @staticmethod
    async def add_menu(menu: MenuMain, auth_account_main_id: int) -> Tuple[Optional[MenuMain], Optional[Error]]:

        account_main, err = await PlaceMainDao().get_place_owner(menu.place_main.id)
        if err:
            return None, err

        if not account_main:
            return None, ErrorEnum.PLACE_DOESNT_EXISTS

        if account_main.id != auth_account_main_id:
            return None, ErrorEnum.PLACE_FORBIDDEN

        menu_main, err = await MenuMainDao().add(menu)
        if err:
            return None, err

        return menu, None

    @staticmethod
    async def add_menu_category(menu_category: MenuCategory, auth_account_main_id: int):
        place_account_role, err = await PlaceAccountRoleDao().get_by_menu_main_id(menu_category.menu_main.id, auth_account_main_id)
        if err:
            return None, err

        if not place_account_role or place_account_role.account_status.id not in (1, 2):
            return None, ErrorEnum.PLACE_FORBIDDEN

        menu_category, err = await MenuCategoryDao().add(menu_category)
        if err:
            return None, err

        return menu_category, None

    @staticmethod
    async def add_dish(dish_common: DishCommon, auth_account_main_id: int):
        place_account_role, err = await PlaceAccountRoleDao().get_by_menu_main_id(dish_common.dish_main.menu_main.id, auth_account_main_id)
        if err:
            return None, err

        if not place_account_role or place_account_role.account_status.id not in (1, 2):
            return None, ErrorEnum.PLACE_FORBIDDEN

        dish_common, err = await DishCommonDao().add(dish_common)
        if err:
            return None, err

        return dish_common, err

    @staticmethod
    async def get_menu(menu_id: int):

        menu_main, error_menu_main = await MenuMainDao().get_menu_main_by_id(menu_id)
        if error_menu_main:
            return None, error_menu_main

        language, error_language = await LanguageDao().get_language_by_menu_id(menu_main.place_main.id)
        if error_language:
            return None, error_language

        currency, error_currency = await CurrencyDao().get(menu_main.place_main.id)
        if error_currency:
            return None, error_currency

        menu_category, error_menu_category = await MenuCategoryDao().get(menu_id)
        if error_menu_category:
            return None, error_menu_category

        dish_main, error_dish_main = await DishMainDao().get(menu_id)
        if error_dish_main:
            return None, error_dish_main

        dish_measure, error_dish_measure = await DishMeasureDao().get(menu_id)
        if error_dish_measure:
            return None, error_dish_measure

        arr_measure_unit = []
        for i in range(len(dish_main)):
            if dish_main[i].measure_unit.id not in arr_measure_unit:
                arr_measure_unit.append(dish_main[i].measure_unit.id)
        tuple_measure_unit = tuple(arr_measure_unit)

        measure_unit, error_measure_unit = await MeasureUnitDao().get(tuple_measure_unit)
        if error_measure_unit:
            return None, error_measure_unit

        menu_common = get_menu_common_serialize(menu_main,
                                                language,
                                                currency,
                                                menu_category,
                                                dish_main,
                                                dish_measure,
                                                measure_unit)
        if not menu_common:
            return None, None
        return menu_common, None
