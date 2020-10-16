from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.language import Language
from src.internal.adapters.enums.errors import ErrorEnum


class LanguageDao(BaseDao):

    async def get_id_by_code_name(self, language_code_name: str):
        async with self.pool.acquire() as conn:
            language_id = await conn.fetchval(
                """
                SELECT id
                FROM language 
                WHERE code_name = $1
                """, language_code_name
            )

            if not language_id:
                return None, None

            return Language(id=language_id, code_name=language_code_name), None

    async def get_language_by_menu_id(self, menu_id):
        sql = """
            SELECT 
                language.id 			            AS language_id,
                language.name 			            AS language_name
            FROM 
                language
            WHERE
                language.id = (SELECT
                                    place_main.main_language    AS place_main_main_language
                                FROM 
                                    place_main
                                WHERE 
                                    place_main.id = $1)
                """
        if self.conn:
            data = await self.conn.fetchrow(sql, menu_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchrow(sql, menu_id)
        if not data:
            return None, ErrorEnum.LANGUAGE_DOESNT_EXISTS
        language = Language(
            id=data['language_id'],
            name=data['language_name']
        )
        return language
