from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_work_hours import PlaceWorkHours
from src.internal.biz.serializers.entities_serializer.work_hours_serializer import work_hours_serializer


class WorkHoursDao(BaseDao):

    async def get_work_hours(self):
        sql = """
            SELECT
                id              AS place_work_hours_id
                week_day        AS week_day,
                time_start      AS time_start,
                time_finish     AS time_finish
            FROM
                place_work_hours
        """
        if self.conn:
            data = await self.conn.fetchval(sql)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchval(sql)

        if not data:
            return None, ErrorEnum.WORK_HOURS_DOESNT_EXISTS

        work_hours = work_hours_serializer(data)

        if not work_hours:
            return None, ErrorEnum.WORK_HOURS_DOESNT_EXISTS

        return work_hours, None
