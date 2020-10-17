from typing import Tuple, Optional

from datetime import datetime

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.menu_main import MenuMain
from src.internal.biz.entities.place_main import PlaceMain
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

    async def get_menu_main_by_id(self, menu_id: int) -> Tuple[Optional[MenuMain], Optional[Error]]:
        sql = """
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
        if self.conn:
            data = await self.conn.fetchrow(sql, menu_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchrow(sql, menu_id)
        if not data:
            return None, ErrorEnum.MENU_MAIN_DOESNT_EXISTS
        menu_main = MenuMain(
                    id=data['menu_main_id'],
                    name=data['menu_main_name'],
                    photo=data['menu_main_photo_link'],
                    place_main=PlaceMain(id=data['menu_main_place_main_id']))
        return menu_main, None
