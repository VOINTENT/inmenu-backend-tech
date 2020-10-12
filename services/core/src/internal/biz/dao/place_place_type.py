from typing import List, Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_place_type import PlacePlaceType


PLACE_TYPE_FOREIGN_KEY = 'place_place_type_place_type_id_fkey'


class PlacePlaceTypeDao(BaseDao):

    async def add_many(self, place_place_types: List[PlacePlaceType]) -> Tuple[None, Optional[Error]]:
        sql = """
            INSERT INTO place_place_type(place_main_id, place_type_id) VALUES
        """

        inserted_values = []
        for place_place_type, i in list(zip(place_place_types, range(1, len(place_place_types) * 2, 2))):
            sql += ', ' if len(inserted_values) != 0 else ''
            sql += f'(${i}, ${i + 1})'
            inserted_values.append(place_place_type.place_main.id)
            inserted_values.append(place_place_type.place_type.id)

        if inserted_values:
            try:
                await self.conn.execute(sql, *inserted_values)
            except asyncpg.exceptions.ForeignKeyViolationError as exc:
                if exc.constraint_name == PLACE_TYPE_FOREIGN_KEY:
                    return None, ErrorEnum.WRONG_PLACE_TYPE
                else:
                    raise TypeError

        return None, None
