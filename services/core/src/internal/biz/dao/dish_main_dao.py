from typing import Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.dish_main import DishMain
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.menu_category import MenuCategory
from src.internal.biz.entities.measure_unit import MeasureUnit

MEASURE_UNIT_FKEY = 'dish_main_measure_unit_id_fkey'
MENU_CATEGORY_FREY = 'dish_main_menu_category_id_fkey'
MENU_MAIN_FREY = 'dish_main_menu_main_id_fkey'


class DishMainDao(BaseDao):
    async def add(self, dish_main: DishMain) -> Tuple[Optional[DishMain], Optional[Error]]:
        sql = """
            INSERT INTO dish_main(name, photo_link, description, menu_main_id, menu_category_id, measure_unit_id)
            VALUES ($1, $2, $3, $4, $5, $6)
            RETURNING id;
        """

        try:
            dish_main_id = await self.conn.fetchval(sql, dish_main.name, dish_main.photo.short_url,
                                                    dish_main.description,
                                                    dish_main.menu_main.id, dish_main.menu_category.id,
                                                    dish_main.measure_unit.id)
        except asyncpg.exceptions.ForeignKeyViolationError as exc:
            if exc.constraint_name == MEASURE_UNIT_FKEY:
                return None, ErrorEnum.MEASURE_UNIT_DOESNT_EXISTS
            elif exc.constraint_name == MENU_CATEGORY_FREY:
                return None, ErrorEnum.MENU_CATEGORY_DOESNT_EXISTS
            elif exc.constraint_name == MENU_MAIN_FREY:
                return None, ErrorEnum.MENU_MAIN_DOESNT_EXISTS
            else:
                raise TypeError

        dish_main.id = dish_main_id
        return dish_main, None

    async def get(self, menu_id):
        sql = """
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
        if self.conn:
            data = await self.conn.fetch(sql, menu_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetch(sql, menu_id)
        if not data:
            return None, ErrorEnum.DISHES_DOESNT_EXISTS
        dish_main = [
            DishMain(
                id=data[i]['dish_main_id'],
                name=data[i]['dish_main_name'],
                photo=data[i]['dish_main_photo_link'],
                description=data[i]['dish_main_description'],
                menu_main=MenuMain(id=data[i]['dish_main_menu_main_id']),
                menu_category=MenuCategory(id=data[i]['dish_main_menu_category_id']),
                measure_unit=MeasureUnit(id=data[i]['dish_main_measure_unit_id']))
            for i in range(len(data))
        ]
        return dish_main