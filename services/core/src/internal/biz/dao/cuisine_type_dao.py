from typing import Optional, List, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.serializers.entities_serializer.cuisine_type_serializer import cuisine_type_serializer


class CuisineTypeDao(BaseDao):

    async def get_list_cuisine_type(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[CuisineType]], Optional[Error]]:
        sql = """
            SELECT 
                cuisine_type.id                AS cuisine_type_id,
                cuisine_type_translate.name    AS cuisine_type_translate_name
            FROM
                cuisine_type
            INNER JOIN 
                cuisine_type_translate ON cuisine_type_translate.cuisine_type_id = cuisine_type.id
            WHERE 
                cuisine_type_translate.language_id = $1
            LIMIT $2
            OFFSET $3
            """
        if self.conn:
            data = await self.conn.fetch(sql, lang_id, pagination_size, pagination_after)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetch(sql, lang_id, pagination_size, pagination_after)

        if not data:
            return [], None

        cuisine_types = [cuisine_type_serializer(dictionary) for dictionary in data]

        return cuisine_types, None
