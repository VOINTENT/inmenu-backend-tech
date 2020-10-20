from typing import List

from sanic.response import HTTPResponse, json

from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.serializers.main_menu import MenuMainSerializer, SER_MENU_MAIN_SIMPLE


def get_response_get_menu_mains_by_place_main_id(menu_mains: List[MenuMain]) -> HTTPResponse:
    return json([MenuMainSerializer.serialize(menu_main, SER_MENU_MAIN_SIMPLE) for menu_main in menu_mains], 200)
