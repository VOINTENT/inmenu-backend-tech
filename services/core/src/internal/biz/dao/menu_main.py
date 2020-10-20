from typing import Tuple, Optional

from datetime import datetime

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.deserializers.menu_main import MENU_MAIN_ID, MENU_MAIN_NAME, MENU_MAIN, MenuMainDeserializer, \
    DES_MENU_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.photo import PHOTO_SHORT_URL
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

        menu_main.id = menu_id
        return menu_main, None


    async def get_by_place_main_id(self, place_main_id: int, pagination_size: int, pagination_after: int):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(f"""
                SELECT
                    menu_main.id AS {MENU_MAIN_ID},
                    menu_main.name AS {MENU_MAIN_NAME},
                    menu_main.photo_link AS {MENU_MAIN + PHOTO_SHORT_URL}
                FROM
                    menu_main
                    INNER JOIN place_main ON menu_main.place_main_id = place_main.id
                WHERE
                    place_main.id = $1
                LIMIT $2 OFFSET $3
            """, place_main_id, pagination_size, pagination_after)

            return [MenuMainDeserializer.deserialize(row, DES_MENU_MAIN_FROM_DB_FULL) for row in rows], None

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

