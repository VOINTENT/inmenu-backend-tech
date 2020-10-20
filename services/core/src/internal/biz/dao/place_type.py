from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
<<<<<<< HEAD
from src.internal.biz.dao.base_dao import BaseDao
=======
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_type import PlaceType
>>>>>>> 32d607344be0c728fa040d09adeedcad389487b6


class PlaceTypeDao(BaseDao):

<<<<<<< HEAD
    async def get_all(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[object]], Optional[Error]]:
        pass
=======
    async def get_all_place_types(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[object]], Optional[Error]]:
        sql = """
            SELECT 
                place_type.id                  AS place_type_id,
                place_type_translate.name      AS place_type_translate_name
            FROM
                place_type_translate
            WHERE place_type_translate.language_id = $1
            LIMIT $2
            OFFSET $3
            """
        if self.conn:
            data = await self.conn.fetchval(sql, lang_id, pagination_size, pagination_after)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchval(sql, lang_id, pagination_size, pagination_after)
        if not data:
            return None, ErrorEnum.PLACE_TYPE_DOESNT_EXISTS
        place_types = [PlaceType(
            id=data[i]['place_type_id'],
            name=data[i]['place_type_translate_name']
        )for i in range(len(data))]
        return place_types, None
>>>>>>> 32d607344be0c728fa040d09adeedcad389487b6
