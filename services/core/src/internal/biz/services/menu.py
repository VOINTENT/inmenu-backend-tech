from typing import Tuple, Optional, List

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
from src.internal.biz.dao.dish_measure_dao import DishMeasureDao



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
        place_account_role, err = await PlaceAccountRoleDao().get_by_menu_main_id(menu_category.menu_main.id,
                                                                                  auth_account_main_id)
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
        place_account_role, err = await PlaceAccountRoleDao().get_by_menu_main_id(dish_common.dish_main.menu_main.id,
                                                                                  auth_account_main_id)
        if err:
            return None, err

        if not place_account_role or place_account_role.account_status.id not in (1, 2):
            return None, ErrorEnum.PLACE_FORBIDDEN

        dish_common, err = await DishCommonDao().add(dish_common)
        if err:
            return None, err

        return dish_common, None

    @staticmethod
    async def get_menu_mains_by_place_main_id(place_main_id: int, pagination_size: int, pagination_after: int) -> Tuple[
        Optional[List[MenuMain]], Optional[Error]]:
        place_categories, err = await MenuMainDao().get_by_place_main_id(place_main_id, pagination_size,
                                                                         pagination_after)
        if err:
            return None, err

        return place_categories, None

    @staticmethod
    async def get_menu_categories_by_menu_category_id(menu_main_id: int) -> Tuple[Optional[List[MenuCategory]], Optional[Error]]:
        menu_categories, err = await MenuCategoryDao().get_by_menu_main_id(menu_main_id)
        if err:
            return None, err

        return menu_categories, None

    @staticmethod
    async def get_dishes_by_menu_category_id(menu_category_id, pagination_size: int, pagination_after: int) -> Tuple[Optional[List[DishCommon]], Optional[Error]]:
        dish_mains, err = await DishMainDao().get_by_menu_category_id(menu_category_id, pagination_size,
                                                                      pagination_after)
        if err:
            return None, err

        dish_main_ids = [dish_main.id for dish_main in dish_mains]

        dish_measures, err = await DishMeasureDao().get_by_dish_main_ids(dish_main_ids)
        if err:
            return None, err

        return [
                   DishCommon(dish_main=dish_main, dish_measure=dish_measures.pop_by_dish_main_id(dish_main.id))
                   for dish_main in dish_mains
               ], None

        return dish_common, err
