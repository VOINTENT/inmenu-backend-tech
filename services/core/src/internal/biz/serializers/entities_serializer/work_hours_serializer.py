from typing import re, Optional, List

from src.internal.biz.entities.place_work_hours import PlaceWorkHours


def work_hours_serializer(data: re) -> Optional[List[PlaceWorkHours]]:
    try:
        work_hours = [PlaceWorkHours(
            id=data[i]['place_work_hours_id'],
            week_day=data[i]['week_day'],
            time_start=data[i]['time_start'],
            time_finish=data[i]['time_finish']
        ) for i in range(len(data))]
        return work_hours
    except:
        raise TypeError
