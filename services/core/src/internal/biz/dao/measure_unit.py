from src.internal.biz.dao.base_dao import BaseDao
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.entities.measure_unit import MeasureUnit


class MeasureUnitDao(BaseDao):

    async def get(self, tuple_measure_unit):
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
        measure_unit = [
            MeasureUnit(
                id=data[i]['measure_unit_id'],
                short_name=data[i]['measure_unit_short_name'])
            for i in range(len(data))
        ]
        return measure_unit
