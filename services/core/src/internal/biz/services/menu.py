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
from src.internal.biz.dao.dish_in_category_dao import DishInCategoryDao

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
        # menu_common, err = await MenuMainDao().get(menu_id)

        menu_main = await MenuMainDao().get_menu_main_by_id(menu_id)
        language = await LanguageDao().get_language_by_menu_id(menu_main.place_main.id)
        currency = await CurrencyDao().get(menu_main.place_main.id)
        menu_category = await MenuCategoryDao().get(menu_id)
        dish_main = await DishMainDao().get(menu_id)
        dish_measure = await DishMeasureDao().get(menu_id)

        arr_measure_unit = []
        for i in range(len(dish_main)):
            if dish_main[i].measure_unit.id not in arr_measure_unit:
                arr_measure_unit.append(dish_main[i].measure_unit.id)
        tuple_measure_unit = tuple(arr_measure_unit)

        measure_unit = await MeasureUnitDao().get(tuple_measure_unit)
        count_dish_in_category = await DishInCategoryDao().get(menu_id)

        menu_common = get_menu_common_serialize(menu_main,
                                                language,
                                                currency,
                                                menu_category,
                                                dish_main,
                                                dish_measure,
                                                measure_unit,
                                                count_dish_in_category)
        if not menu_common:
            return None, None
        return menu_common, None
        # if err:
        #     return None, err
        #
        # return menu_common, err
