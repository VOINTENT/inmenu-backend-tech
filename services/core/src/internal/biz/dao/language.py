from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.deserializers.language import LanguageDeserializer, DES_LANGUAGE_FROM_DB_FULL, LANGUAGE_ID, \
    LANGUAGE_NAME, LANGUAGE_CODE_NAME
from src.internal.biz.entities.language import Language
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.serializers.entities_serializer.language_serializer import language_serializer


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


    async def get_all(self, pagination_size: int, pagination_after: int) -> Tuple[Optional[List[object]], Optional[Error]]:
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(f"""
                SELECT
                    language.id         AS {LANGUAGE_ID},
                    language.name       AS {LANGUAGE_NAME},
                    language.code_name  AS {LANGUAGE_CODE_NAME}
                FROM
                    language
                LIMIT $1 OFFSET $2
            """, pagination_size, pagination_after)
            return [LanguageDeserializer.deserialize(row, DES_LANGUAGE_FROM_DB_FULL) for row in rows], None
