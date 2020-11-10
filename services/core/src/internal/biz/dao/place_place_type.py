from typing import List, Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_INT
from src.internal.biz.deserializers.place_place_type import PlacePlaceTypeDeserializer, \
    DES_PLACE_PLACE_TYPE_FROM_DB_FULL
from src.internal.biz.deserializers.place_type_deserializer import PLACE_TYPE_ID, PLACE_TYPE_NAME
from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.entities.place_place_type import PlacePlaceType


PLACE_TYPE_FOREIGN_KEY = 'place_place_type_place_type_id_fkey'
UNIQUE_PLACE_PLACE_TYPE = 'unique_place_place_type'


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
            except asyncpg.exceptions.UniqueViolationError as exc:
                if exc.constraint_name == UNIQUE_PLACE_PLACE_TYPE:
                    return None, ErrorEnum.UNIQUE_PLACE_TYPE
                else:
                    raise TypeError

        return None, None

    async def get_by_place_main_id(self, place_main_id: int, lang_id: int) -> Tuple[Optional[List], Optional[Error]]:
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(f"""
                SELECT
                    place_type.id               AS {PLACE_TYPE_ID},
                    place_type_translate.name   AS {PLACE_TYPE_NAME}
                FROM
                    place_place_type
                    INNER JOIN place_type ON place_place_type.place_type_id = place_type.id
                    INNER JOIN place_type_translate ON place_type.id = place_type_translate.place_type_id AND place_type_translate.language_id = $2
                WHERE
                    place_main_id = $1
            """, place_main_id, lang_id)

            return [PlacePlaceTypeDeserializer.deserialize(row, DES_PLACE_PLACE_TYPE_FROM_DB_FULL) for row in rows], None

    async def delete(self, place_main_id: int):
        sql = f"""DELETE FROM place_place_type WHERE place_main_id = $1"""
        await self.conn.execute(sql, place_main_id)
        return None, None
