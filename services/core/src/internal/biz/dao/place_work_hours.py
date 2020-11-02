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

    async def update_work_hours(self, place_main_id, place_work_hours_list: List[PlaceWorkHours]):
        sql = """"""
        update_values = []
        for place_work_hours, i in list(zip(place_work_hours_list, range(1, len(place_work_hours_list) * 5, 5))):
            if place_work_hours.time_start is None:
                time_start = None
            else:
                time_start = place_work_hours.time_start
            if place_work_hours.time_finish is None:
                time_finish = None
            else:
                time_finish = place_work_hours.time_finish
            sql += '; ' if len(update_values) != 0 else ''
            sql += f" UPDATE place_work_hours " \
                   f" SET time_start = {f'{time_start}' if time_start else None}, " \
                   f"time_finish =  {f'{time_finish}' if time_finish else None}, " \
                   f"is_holiday = {place_work_hours.is_holiday} " \
                   f"WHERE place_main_id = {place_work_hours.place_main.id} AND week_day = '{place_work_hours.week_day}'; "
        print(sql)

        await self.conn.execute(sql)
        return None, None

