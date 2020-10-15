from typing import Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.menu_common import MenuCommon
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.dish_measure import DishMeasure
from src.internal.biz.entities.language import Language
from src.internal.biz.entities.currency import Currency
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.measure_unit import MeasureUnit


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
                menu_id = await self.conn.fetchval(sql, menu_main.place_main.id, menu_main.name, menu_main.photo.short_url)
            else:
                async with self.pool.acquire() as conn:
                    menu_id = await conn.fetchval(sql, menu_main.place_main.id, menu_main.name, menu_main.photo.short_url)
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
                                            language.id 					                AS language_id,
                                            language.name 					                AS language_name,
                                            currency.id                                     AS currency_id,
                                            currency.sign                                   AS currency_sign
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
                                    menu_category.menu_main_id			AS menu_category_menu_main_id
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
        if self.conn:
            main_menu = await self.conn.fetch(sql_for_main_menu, menu_id)
            menu_category = await self.conn.fetch(sql_for_menu_category, menu_id)
            dish_main = await self.conn.fetch(sql_for_dish_main, menu_id)
            dish_measure = await self.conn.fetch(sql_for_dish_measure, menu_id)
        else:
            async with self.pool.acquire() as conn:
                main_menu = await conn.fetch(sql_for_main_menu, menu_id)
                menu_category = await conn.fetch(sql_for_menu_category, menu_id)
                dish_main = await conn.fetch(sql_for_dish_main, menu_id)
                dish_measure = await conn.fetch(sql_for_dish_measure, menu_id)
        if not main_menu:
            return None, ErrorEnum.MENU_MAIN_DOESNT_EXISTS
        if not menu_category:
            return None, ErrorEnum.MENU_CATEGORY_DOESNT_EXISTS
        if not dish_main:
            return None, ErrorEnum.DISHES_DOESNT_EXISTS
        if not dish_measure:
            return None, ErrorEnum.DISH_MEASURE_VALUE_AND_PRICE_DOESNT_EXISTS
        print(main_menu)
        print(menu_category)
        print(dish_main)
        print(dish_measure)
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


        arr_for_category = []
        arr_for_measure_unit = []
        data = []
        for i in range(len(dish_main)):
            data.append({
                'menu_main_id': main_menu[0]['menu_main_id'],
                'menu_main_name': main_menu[0]['menu_main_name'],
                'menu_main_photo_link=': main_menu[0]['menu_main_photo_link'],
                'menu_main_place_main_id': main_menu[0]['menu_main_place_main_id'],
                'language_id': language_and_currency[0]['language_id'],
                'language_name' : language_and_currency[0]['language_name'],
                'currency_id': language_and_currency[0]['currency_id'],
                'currency_sign':language_and_currency[0]['currency_sign'],
                'dish_main_id': dish_main[i]['dish_main_id'],
                'dish_main_name' : dish_main[i]['dish_main_name'],
                'dish_main_photo_link': dish_main[i]['dish_main_photo_link'],
                'dish_main_description': dish_main[i]['dish_main_description'],
                'dish_main_menu_main_id' : dish_main[i]['dish_main_menu_main_id'],
                'dish_main_menu_category_id' : dish_main[i]['dish_main_menu_category_id'],
                'dish_main_measure_unit_id' : dish_main[i]['dish_main_measure_unit_id']
                    })
        array_for_category_menu = []
        for i in range(len(menu_category)):
            if menu_category[i] not in array_for_category_menu:
                array_for_category_menu.append(menu_category[i]['menu_category_id'])
        array = []
        print(len(menu_category))
        for i in range(0, len(data), 2):
            for j in range(0, len(menu_category)):
                if data[i]['dish_main_menu_category_id'] == array_for_category_menu[j]:
                    data.insert(i, {
                        'menu_category_id': menu_category[j]['menu_category_id'],
                        'menu_category_name': menu_category[j]['menu_category_name'],
                        'menu_category_menu_main_id' : menu_category[j]['menu_category_menu_main_id']
                    })
        #     else:
        #         data.insert(i, {
        #             'menu_category_id': menu_category[array[-1] - 1]['menu_category_id'],
        #             'menu_category_name': menu_category[array[-1] - 1]['menu_category_name'],
        #             'menu_category_menu_main_id': menu_category[array[-1] - 1]['menu_category_menu_main_id']
        #         })
        print(data)

        # menu_common = MenuCommon(
        #     main_menu=MenuMain(
        #         id=menu[0]['menu_main_id'],
        #         name=menu[0]['menu_main_name'],
        #         photo=menu[0]['menu_main_photo_link']
        #     ),
        #     language=Language(
        #         id=menu[0]['language_id'],
        #         name=menu[0]['language_name']
        #     ),
        #     menu_category=[
        #         MenuCategory(
        #                     id=menu[i]['menu_category_id'],
        #                     name=menu[i]['menu_category_name']
        #                     ) for i in range(len(menu))],
        #     measure_unit=[
        #         MeasureUnit(
        #                     id=menu[i]['measure_unit_id'],
        #                     name=menu[i]['measure_unit_short_name']
        #                    ) for i in range(len(menu))],
        #     dish_main=[
        #         DishMain(
        #                 id=menu[i]['dish_main_id'],
        #                 name=menu[i]['dish_main_name'],
        #                 photo=menu[i]['dish_main_photo_link'],
        #                 description=menu[i]['dish_main_description']
        #                 )for i in range(len(menu))],
        #     dish_measures=[
        #         DishMeasure(
        #                     id=menu[i]['dish_measure_id'],
        #                     price_value=menu[i]['dish_measure_price_value'],
        #                     measure_value=menu[i]['dish_measure_measure_value']
        #                     ) for i in range(len(menu))],
        #     currency=Currency(
        #         id=menu[0]['currency_id'],
        #         sign=menu[0]['currency_sign']
        #     )
        # )
        return menu_common, None
