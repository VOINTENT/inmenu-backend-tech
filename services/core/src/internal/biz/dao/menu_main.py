from typing import Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.menu_common import MenuCommon
from src.internal.biz.serializers.menu_common_serializer import get_menu_common_serialize

MENU_PLACE_MAIN_FKEY = 'menu-place-main-fkey'


class MenuMainDao(BaseDao):

    async def add(self, menu_main: MenuMain) -> Tuple[Optional[MenuMain], Optional[Error]]:
        sql = """
            INSERT INTO menu_main(place_main_id, name, photo_link) VALUES
            ($1, $2, $3)
            RETURNING id;
        """

        try:
            if self.conn:
                menu_id = await self.conn.fetchval(sql, menu_main.place_main.id, menu_main.name,
                                                   menu_main.photo.short_url)
            else:
                async with self.pool.acquire() as conn:
                    menu_id = await conn.fetchval(sql, menu_main.place_main.id, menu_main.name,
                                                  menu_main.photo.short_url)
        except asyncpg.exceptions.ForeignKeyViolationError as exc:
            if exc.constraint_name == MENU_PLACE_MAIN_FKEY:
                return None, ErrorEnum.PLACE_DOESNT_EXISTS
            else:
                raise TypeError
        except Exception as exc:
            raise TypeError

        menu_main.id = menu_id
        return menu_main, None

    async def get(self, menu_id: int) -> Tuple[Optional[MenuCommon], Optional[Error]]:
        sql_for_main_menu = """
                            SELECT
                                menu_main.id 						AS menu_main_id,
                                menu_main.name 						AS menu_main_name,
                                menu_main.photo_link 				AS menu_main_photo_link,
                                menu_main.place_main_id				AS menu_main_place_main_id   
                            FROM 
                                menu_main
                            WHERE 
                                menu_main.id = $1
                       """
        sql_for_language_and_currency = """
                            SELECT 
                                language.id 			            AS language_id,
                                language.name 			            AS language_name,
                                currency.id                         AS currency_id,
                                currency.sign                       AS currency_sign
                            FROM 
                                language, currency
                            WHERE
                                language.id = (SELECT
                                                    place_main.main_language    AS place_main_main_language
                                                FROM 
                                                    place_main
                                                WHERE 
                                                    place_main.id = $1) AND 
                                currency.id = (SELECT
                                                    place_main.main_currency    AS place_main_main_currency
                                                FROM 
                                                    place_main
                                                WHERE 
                                                    place_main.id = $1)
                                        """
        sql_for_menu_category = """
                            SELECT 
                                menu_category.id                    AS menu_category_id,
                                menu_category.name                  AS menu_category_name,
                                menu_category.menu_main_id          AS menu_category_menu_main_id
                            FROM 
                                menu_category
                            WHERE
                                menu_category.menu_main_id = $1
                                """
        sql_for_dish_main = """
                            SELECT 
                                dish_main.id                        AS dish_main_id,
                                dish_main.name                      AS dish_main_name,
                                dish_main.photo_link                AS dish_main_photo_link,
                                dish_main.description               AS dish_main_description,
                                dish_main.menu_main_id				AS dish_main_menu_main_id,
                                dish_main.menu_category_id			AS dish_main_menu_category_id,
                                dish_main.measure_unit_id			AS dish_main_measure_unit_id
                            FROM 	
                                dish_main
                            WHERE 
                                dish_main.menu_main_id = $1
                            """
        sql_for_dish_measure = """
                            SELECT 
                                dish_measure.id                     AS dish_measure_id,
                                dish_measure.price_value            AS dish_measure_price_value,
                                dish_measure.measure_value          AS dish_measure_measure_value,
                                dish_measure.dish_main_id			AS dish_measure_dish_main_id
                            FROM 
                                dish_measure
                            WHERE 
                                dish_measure.dish_main_id IN(SELECT 
                                                                    dish_main.id AS dish_main_id
                                                            FROM 	
                                                                dish_main	
                                                            WHERE 
                                                                dish_main.menu_main_id = $1)
                               """
        sql_for_count_menu_category = """
                                SELECT  
                                    dish_main.menu_category_id AS dish_main_menu_category_id,
                                    COUNT(dish_main.id) AS count_dish_main_id_category
                                FROM 
                                    dish_main
                                WHERE 
                                    dish_main.menu_main_id = $1
                                GROUP BY 
                                    dish_main.menu_category_id
                                    """
        if self.conn:
            main_menu = await self.conn.fetch(sql_for_main_menu, menu_id)
            menu_category = await self.conn.fetch(sql_for_menu_category, menu_id)
            dish_main = await self.conn.fetch(sql_for_dish_main, menu_id)
            dish_measure = await self.conn.fetch(sql_for_dish_measure, menu_id)
            count_dish_main_for_category = await self.conn.fetch(sql_for_count_menu_category, menu_id)
        else:
            async with self.pool.acquire() as conn:
                main_menu = await conn.fetch(sql_for_main_menu, menu_id)
                menu_category = await conn.fetch(sql_for_menu_category, menu_id)
                dish_main = await conn.fetch(sql_for_dish_main, menu_id)
                dish_measure = await conn.fetch(sql_for_dish_measure, menu_id)
                count_dish_main_for_category = await conn.fetch(sql_for_count_menu_category, menu_id)
        if not main_menu:
            return None, ErrorEnum.MENU_MAIN_DOESNT_EXISTS
        if not menu_category:
            return None, ErrorEnum.MENU_CATEGORY_DOESNT_EXISTS
        if not dish_main:
            return None, ErrorEnum.DISHES_DOESNT_EXISTS
        if not dish_measure:
            return None, ErrorEnum.DISH_MEASURE_VALUE_AND_PRICE_DOESNT_EXISTS

        arr_measure_unit = []
        for i in range(len(dish_main)):
            if dish_main[i]['dish_main_measure_unit_id'] not in arr_measure_unit:
                arr_measure_unit.append(dish_main[i]['dish_main_measure_unit_id'])
        tuple_measure_unit = tuple(arr_measure_unit)
        place_main_id = main_menu[0]['menu_main_place_main_id']

        sql_for_measure_unit = f"""
                            SELECT 
                                measure_unit.id                     AS measure_unit_id,
                                measure_unit.short_name             AS measure_unit_short_name
                            FROM 
                                measure_unit
                            WHERE 
                                measure_unit.id IN {tuple_measure_unit}
                                """

        if self.conn:
            language_and_currency = await self.conn.fetch(sql_for_language_and_currency, place_main_id)
            measure_unit = await self.conn.fetch(sql_for_measure_unit)
        else:
            async with self.pool.acquire() as conn:
                language_and_currency = await conn.fetch(sql_for_language_and_currency, place_main_id)
                measure_unit = await conn.fetch(sql_for_measure_unit)
        if not language_and_currency:
            return None, ErrorEnum.LANGUAGE_AND_CURRENCY_DOESNT_EXISTS
        if not measure_unit:
            return None, ErrorEnum.MEASURE_UNIT_DOESNT_EXISTS()

        menu = []
        for i in range(len(dish_main)):
            menu.append({
                'menu_main_id': main_menu[0]['menu_main_id'],
                'menu_main_name': main_menu[0]['menu_main_name'],
                'menu_main_photo_link': main_menu[0]['menu_main_photo_link'],
                'menu_main_place_main_id': main_menu[0]['menu_main_place_main_id'],
                'language_id': language_and_currency[0]['language_id'],
                'language_name': language_and_currency[0]['language_name'],
                'currency_id': language_and_currency[0]['currency_id'],
                'currency_sign': language_and_currency[0]['currency_sign'],
                # 'menu_category_id': menu_category[int(dish_main[i]['dish_main_menu_category_id'] - count_dish_main_for_category[dish_main[i]['dish_main_menu_category_id'] - 1]['dish_main_menu_category_id'])][
                #     'menu_category_id'],
                # 'menu_category_name': menu_category[int(dish_main[i]['dish_main_menu_category_id'] - count_dish_main_for_category[dish_main[i]['dish_main_menu_category_id'] - 1]['dish_main_menu_category_id'])][
                #     'menu_category_name'],
                # 'menu_category_menu_main_id': menu_category[int(dish_main[i]['dish_main_menu_category_id'] - count_dish_main_for_category[dish_main[i]['dish_main_menu_category_id'] - 1]['dish_main_menu_category_id'])][
                #     'menu_category_menu_main_id'],
                'menu_category_id': dish_main[i]['dish_main_menu_category_id'],
                'menu_category_name': menu_category[dish_main[i]['dish_main_menu_category_id'] - len(count_dish_main_for_category) - 1]['menu_category_name'],
                'menu_category_menu_main_id': dish_main[i]['dish_main_menu_main_id'],
                'dish_main_id': dish_main[i]['dish_main_id'],
                'dish_main_name': dish_main[i]['dish_main_name'],
                'dish_main_photo_link': dish_main[i]['dish_main_photo_link'],
                'dish_main_description': dish_main[i]['dish_main_description'],
                'dish_main_menu_main_id': dish_main[i]['dish_main_menu_main_id'],
                'dish_main_menu_category_id': dish_main[i]['dish_main_menu_category_id'],
                'dish_main_measure_unit_id': dish_main[i]['dish_main_measure_unit_id'],
                'measure_unit_id': measure_unit[int(dish_main[i]['dish_main_measure_unit_id'] - 1)]['measure_unit_id'],
                'measure_unit_short_name': measure_unit[int(dish_main[i]['dish_main_measure_unit_id'] - 1)][
                    'measure_unit_short_name'],
                'dish_measure_id': dish_measure[i]['dish_measure_id'],
                'dish_measure_price_value': dish_measure[i]['dish_measure_price_value'],
                'dish_measure_measure_value': dish_measure[i]['dish_measure_measure_value']
            })
            print(menu)
        for i in range(len(count_dish_main_for_category)):
            menu.append({
                'count_dish_main_id': count_dish_main_for_category[int(menu_category[i]['menu_category_id']) - len(count_dish_main_for_category) - 1]['dish_main_menu_category_id'],
                'count_dish_main': count_dish_main_for_category[int(menu_category[i]['menu_category_id']) - len(count_dish_main_for_category) - 1]['count_dish_main_id_category']})
        print(menu)
        menu_common = get_menu_common_serialize(menu, count_dish_main_for_category)
        return menu_common, None
