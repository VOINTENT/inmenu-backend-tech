from typing import Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.dish_main import DishMain


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
            dish_main_id = await self.conn.fetchval(sql, dish_main.name, dish_main.photo.short_url, dish_main.description,
                                                    dish_main.menu_main.id, dish_main.menu_category.id, dish_main.measure_unit.id)
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
