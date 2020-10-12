from typing import Tuple, Optional, List

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.place_main import PlaceMain


UNIQUE_PLACE_LOGIN = 'unique_place_login'
LANGUAGE_FOREIGN_KEY = 'place_main_main_language_fkey'
CURRENCY_FOREIGN_KEY = 'place_main_main_currency_fkey'


class PlaceMainDao(BaseDao):

    async def add(self, place_main: PlaceMain) -> Tuple[Optional[PlaceMain], Optional[Error]]:

        sql = """
            INSERT INTO place_main(account_main_id, main_language, name, login, photo_link, description, main_currency, is_draft, is_published)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
            RETURNING id
        """

        try:
            place_main_id = await self.conn.fetchval(
                sql, place_main.account_main.id, place_main.main_language.id, place_main.name, place_main.login, place_main.photo.short_url,
                place_main.description, place_main.main_currency.id, place_main.is_draft, place_main.is_published
            )
        except asyncpg.exceptions.UniqueViolationError as exc:
            if exc.constraint_name == UNIQUE_PLACE_LOGIN:
                return None, ErrorEnum.NOT_UNIQUE_PLACE_LOGIN
            else:
                raise TypeError
        except asyncpg.exceptions.ForeignKeyViolationError as exc:
            if exc.constraint_name == LANGUAGE_FOREIGN_KEY:
                return None, ErrorEnum.WRONG_LANGUAGE
            if exc.constraint_name == CURRENCY_FOREIGN_KEY:
                return None, ErrorEnum.WRONG_CURRENCY
            else:
                raise TypeError

        place_main.id = place_main_id
        return place_main, None

    async def get_place_owner(self, place_main_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            account_main_id = await conn.fetchval(
                """
                SELECT account_main_id
                FROM place_main
                WHERE id = $1
                """, place_main_id
            )
            if not account_main_id:
                return None, None

            return AccountMain(id=account_main_id), None

    async def get_all_places(self, city: Optional[str], pagination_size: Optional[int], pagination_after: Optional[int]) -> Tuple[Optional[List[PlaceMain]], Optional[Error]]:
        async with self.pool.acquire() as conn:
            sql = """
                SELECT
                    place_main.id,
                    place_main.name,
                    place_main.photo_link
                FROM
                    place_main
                    INNER JOIN place_location ON place_main.id = place_location.place_main_id
            """
            inserted_values = []

            if city:
                sql += ' WHERE ' if not inserted_values else ' AND '
                sql += f'city = ${len(inserted_values) + 1}'
                inserted_values.append(city)

            sql += f"""
            LIMIT ${len(inserted_values) + 1} OFFSET ${len(inserted_values) + 2}
            """
            inserted_values.append(pagination_size)
            inserted_values.append(pagination_after)

            rows = await conn.fetch(sql, *inserted_values)

            return [PlaceMain(
                id=row['id'],
                name=row['name'],
                photo=Photo(short_url=row['photo_link'])
            ) for row in rows], None
