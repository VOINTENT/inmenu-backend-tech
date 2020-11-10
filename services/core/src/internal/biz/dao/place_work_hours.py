import datetime
from datetime import time
from typing import List, Tuple, Optional

import asyncpg

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.place_work_hours import PlaceWorkHours


class PlaceWorkHoursDao(BaseDao):

    async def add_many(self, place_work_hours_list: List[PlaceWorkHours]) -> Tuple[None, Optional[Error]]:
        sql = """
            INSERT INTO place_work_hours(place_main_id, week_day, time_start, time_finish, is_holiday, is_all_day) VALUES
        """

        inserted_values = []
        for place_work_hours, i in list(zip(place_work_hours_list, range(1, len(place_work_hours_list) * 6, 6))):
            sql += ', ' if len(inserted_values) != 0 else ''
            sql += f'(${i}, ${i + 1}, ${i + 2}, ${i + 3}, ${i + 4}, ${i + 5})'
            inserted_values.append(place_work_hours.place_main.id)
            inserted_values.append(place_work_hours.week_day)
            inserted_values.append(place_work_hours.time_start)
            inserted_values.append(place_work_hours.time_finish)
            inserted_values.append(place_work_hours.is_holiday)
            inserted_values.append(place_work_hours.is_all_day)

        if inserted_values:
            await self.conn.execute(sql, *inserted_values)

        return None, None

    async def delete(self, place_main_id):
        sql = """DELETE FROM place_work_hours WHERE place_main_id = $1"""
        await self.conn.execute(sql, place_main_id)
        return None, None
