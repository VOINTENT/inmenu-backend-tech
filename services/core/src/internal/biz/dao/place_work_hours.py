from typing import List, Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_work_hours import PlaceWorkHours


class PlaceWorkHoursDao(BaseDao):

    async def add_many(self, place_work_hours_list: List[PlaceWorkHours]) -> Tuple[None, Optional[Error]]:
        sql = """
            INSERT INTO place_work_hours(place_main_id, week_day, time_start, time_finish, is_holiday) VALUES
        """

        inserted_values = []
        for place_work_hours, i in list(zip(place_work_hours_list, range(1, len(place_work_hours_list) * 5, 5))):
            sql += ', ' if len(inserted_values) != 0 else ''
            sql += f'(${i}, ${i + 1}, ${i + 2}, ${i + 3}, ${i + 4})'
            inserted_values.append(place_work_hours.place_main.id)
            inserted_values.append(place_work_hours.week_day)
            inserted_values.append(place_work_hours.time_start)
            inserted_values.append(place_work_hours.time_finish)
            inserted_values.append(place_work_hours.is_holiday)

        if inserted_values:
            await self.conn.execute(sql, *inserted_values)

        return None, None
