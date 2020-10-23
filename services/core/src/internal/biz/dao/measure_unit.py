from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.serializers.entities_serializer.measure_unit_serializer import measure_unit_serializer


class MeasureUnitDao(BaseDao):

    async def get(self, tuple_measure_unit: tuple) -> Tuple[Optional[List[MeasureUnit]], Optional[Error]]:
        sql = f"""
            SELECT 
                measure_unit.id                     AS measure_unit_id,
                measure_unit.short_name             AS measure_unit_short_name
            FROM 
                measure_unit
            WHERE 
                measure_unit.id IN {tuple_measure_unit}
                """
        if self.conn:
            data = await self.conn.fetch(sql)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetch(sql)

        if not data:
            return None, ErrorEnum.MEASURE_UNIT_DOESNT_EXISTS

        measure_units = [measure_unit_serializer(dictionary) for dictionary in data]

        if not measure_units:
            return None, ErrorEnum.MEASURE_UNIT_DOESNT_EXISTS

        return measure_units, None
