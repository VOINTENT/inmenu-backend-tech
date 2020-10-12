from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.entities.utils import check_value


class PlaceWorkHours(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 place_main: Optional[PlaceMain] = None,
                 week_day: Optional[str] = None,
                 time_start: Optional[datetime.time] = None,
                 time_finish: Optional[datetime.time] = None,
                 is_holiday: Optional[bool] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__place_main = place_main
        self.__week_day = week_day
        self.__time_start = time_start
        self.__time_finish = time_finish
        self.__is_holiday = is_holiday

    @property
    def place_main(self):
        return self.__place_main

    @place_main.setter
    def place_main(self, value: PlaceMain):
        self.__place_main = value

    @property
    def week_day(self):
        return self.__week_day

    @week_day.setter
    def week_day(self, value: str):
        self.__week_day = value

    @property
    def time_start(self):
        return self.__time_start

    @property
    def time_finish(self):
        return self.__time_finish

    @property
    def is_holiday(self):
        return self.__is_holiday

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['place_main'], PlaceMain)
        check_value(kwargs['week_day'], str)
        check_value(kwargs['time_start'], datetime.time)
        check_value(kwargs['time_finish'], datetime.time)
        check_value(kwargs['is_holiday'], bool)
