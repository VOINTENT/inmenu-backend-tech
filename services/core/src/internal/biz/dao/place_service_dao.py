from typing import List, Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_service import PlaceService


SERVICE_FOREIGN_KEY = 'place_service_service_id_fkey'


class PlaceServiceDao(BaseDao):

    async def add_many(self, place_services: List[PlaceService]) -> Tuple[None, Optional[Error]]:
        sql = """
            INSERT INTO place_service(place_main_id, service_id) VALUES
        """

        inserted_values = []
        for place_service, i in list(zip(place_services, range(1, len(place_services) * 2, 2))):
            sql += ', ' if len(inserted_values) != 0 else ''
            sql += f'(${i}, ${i + 1})'
            inserted_values.append(place_service.place_main.id)
            inserted_values.append(place_service.service.id)

        if inserted_values:
            try:
                await self.conn.execute(sql, *inserted_values)
            except asyncpg.exceptions.ForeignKeyViolationError as exc:
                if exc.constraint_name == SERVICE_FOREIGN_KEY:
                    return None, ErrorEnum.WRONG_SERVICE
                else:
                    raise TypeError

        return None, None
