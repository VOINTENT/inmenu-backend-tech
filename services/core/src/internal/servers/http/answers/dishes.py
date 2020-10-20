from typing import List

from sanic.response import HTTPResponse, json

from src.internal.biz.entities.dish_common import DishCommon
from src.internal.biz.serializers.dish_common import DishCommonSerializer, SER_DISH_COMMON_LIST


def get_response_get_dishes_by_menu_category_id(dish_commons: List[DishCommon]) -> HTTPResponse:
    return json([DishCommonSerializer.serialize(dish_common, SER_DISH_COMMON_LIST) for dish_common in dish_commons], 200)
