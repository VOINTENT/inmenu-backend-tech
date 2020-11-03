import requests
import json

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.dao.menu_main import MenuMainDao
from src.internal.biz.services.place_service import PlaceService
from tests.test_config import BASE_URL_GENERAL
from src.internal.drivers.async_pg import AsyncPg

PLACE_MAIN_ID = 1
PLACE_MAIN_ID_FOR_MISTAKE = 43421
SQL_FOR_PLACE_MAIN = """
    SELECT place_main.id
    FROM place_main
    WHERE place_main.id = $1
"""

SQL_FOR_MENU_MAIN = """
    SELECT menu_main.id
    FROM menu_main
    WHERE place_main_id = $1
"""

SQL_FOR_MENU_CATEGORY = """
    SELECT menu_category_id
    FROM menu_category
    WHERE menu_main_1 = $1 
"""

SQL_FOR_DISH_MAIN = """
    SELECT dish_main.id
    FROM dish_main
    WHERE menu_main_id = $1
"""

SQL_FOR_DISH_MEASURE = """
    SELECT dish_measure.id
    FROM dish_measure
    WHERE dish_main_id IN $1
"""


class TestPlaceMain:

    @staticmethod
    def tuple_dishes(dishes_main_id):
        list_dishes_main_id = [dishes_main_id[i]['id'] for i in range(len(dishes_main_id))]
        tuple_dishes_main_id = tuple(list_dishes_main_id)
        return tuple_dishes_main_id

    @staticmethod
    async def del_place():
        req = requests.delete(f"{BASE_URL_GENERAL}/places/{PLACE_MAIN_ID}")
        async with AsyncPg.get_pool_primary_db().acquire() as conn:
            place_main_id = await conn.fetchval(SQL_FOR_PLACE_MAIN, PLACE_MAIN_ID)
            menu_main_id = await conn.fetchval(SQL_FOR_MENU_MAIN, PLACE_MAIN_ID)
            menu_category_id = await conn.fetchval(SQL_FOR_MENU_CATEGORY, menu_main_id)
            dish_main_id = await conn.fetchval(SQL_FOR_DISH_MAIN, menu_main_id)
        list_dishes_main_id = [dish_main_id[i]['id'] for i in range(len(dish_main_id))]
        tuple_dishes_main_id = tuple(list_dishes_main_id)
        async with AsyncPg.get_pool_primary_db().acquire() as conn:
            dish_measure_id = await conn.fetchval(SQL_FOR_DISH_MEASURE, tuple_dishes_main_id)

        assert place_main_id is None
        assert menu_main_id is None
        assert menu_category_id is None
        assert dish_main_id is None
        assert dish_measure_id is None

        assert json.loads(req.text) == {"Status": True}
        assert req.status_code == 200
