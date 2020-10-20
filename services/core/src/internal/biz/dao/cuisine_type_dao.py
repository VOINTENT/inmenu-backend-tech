from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.cuisine_type import CuisineType


class CuisineTypeDao(BaseDao):

    async def get_list_cuisine_type(self, pagination_size: int, pagination_after: int, lang_id: int):
        sql = """
            SELECT 
                cuisine_type_translate.cuisine_type_id  AS cuisine_type_translate_cuisine_type_id,
                cuisine_type_translate.name             AS cuisine_type_translate_name
            FROM
                cuisine_type_translate
            WHERE cuisine_type_translate.language_id = $1
            LIMIT $2
            OFFSET $3
            """
        if self.conn:
            data = await self.conn.fetchval(sql, lang_id, pagination_size, pagination_after)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchval(sql, lang_id, pagination_size, pagination_after)
        if not data:
            return None, ErrorEnum.CUISINE_TYPE_DOESNT_EXISTS
        cuisine_type = [CuisineType(
            id=data[i]['cuisine_type_translate_cuisine_type_id'],
            name=data[i]['cuisine_type_translate_name']
        )for i in range(len(data))]
        if not cuisine_type:
            return None, ErrorEnum.CUISINE_TYPE_DOESNT_EXISTS
        return cuisine_type, None
