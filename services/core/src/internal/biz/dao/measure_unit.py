from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.serializers.entities_serializer.measure_unit_serializer import measure_unit_serializer


class MeasureUnitDao(BaseDao):

    async def get_measure_units(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[MeasureUnit]], Optional[Error]]:
        sql = """
            SELECT
                measure_unit.id                     AS measure_unit_id,
                measure_unit_translate.name         AS measure_unit_name, 
                measure_unit_translate.short_name   AS measure_unit_short_name
            FROM
                measure_unit
            INNER JOIN
                measure_unit_translate ON measure_unit.id = measure_unit_translate.measure_unit_id
            WHERE measure_unit_translate.language_id = $1
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

        measure_units = [measure_unit_serializer(dictionary) for dictionary in data]

        return measure_units, None
