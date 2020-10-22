from typing import Optional, List, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.service import Service
from src.internal.biz.serializers.entities_serializer.service_serializer import service_serializer


class ServicesDao(BaseDao):

    async def get_service(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[Service]], Optional[Error]]:
        sql = """
            SELECT 
                service.id              AS service_id,
                service_translate.name  AS service_translate_name
            FROM 
                service
            INNER JOIN 
                service_translate ON service_translate.service_id = service.id
            WHERE language_id = $1
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

        services = [service_serializer(dictionary) for dictionary in data]

        return services, None
