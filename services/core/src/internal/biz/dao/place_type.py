from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error

from src.internal.biz.dao.base_dao import BaseDao

from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_type import PlaceType
from src.internal.biz.serializers.entities_serializer.place_type_serializer import place_type_serializer


class PlaceTypeDao(BaseDao):

    async def get_all(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[object]], Optional[Error]]:
        sql = """
            SELECT 
                place_type.id                  AS place_type_id,
                place_type_translate.name      AS place_type_translate_name
            FROM
                place_type
            INNER JOIN
                place_type_translate ON place_type.id = place_type_translate.place_type_id
            WHERE place_type_translate.language_id = $1
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

        place_types = [place_type_serializer(dictionary) for dictionary in data]

        return place_types, None
