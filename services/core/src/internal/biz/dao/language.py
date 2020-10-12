from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.language import Language


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
