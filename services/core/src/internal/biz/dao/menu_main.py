from typing import Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.menu_main import MenuMain


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
