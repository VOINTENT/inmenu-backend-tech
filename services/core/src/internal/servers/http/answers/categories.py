from typing import List

from sanic.response import HTTPResponse, json

from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.serializers.MenuCategorySerializer import MenuCategorySerializer, SER_MENU_CATEGORY_SIMPLE


def get_response_get_menus_by_menu_main_id(menu_categories: List[MenuCategory]) -> HTTPResponse:
    return json([MenuCategorySerializer.serialize(menu_category, SER_MENU_CATEGORY_SIMPLE) for menu_category in menu_categories], 200)
