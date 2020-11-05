import datetime

from src.internal.biz.deserializers.place_common import DES_PLACE_COMMON_UPDATE, PlaceCommonDeserializer
from src.internal.biz.deserializers.place_work_hours_week import PlaceWorkHoursWeekDeserializer, \
    DES_WORK_HOURS_WEEK_UPDATE


def test_place_work_hours_deserializer():
    data_1 = {"work_hours": {
        "mo": {
            "is_holiday": False,
            "is_all_day": False,
            "time_start": 28800,
            "time_finish": 79200
        }
    }
    }

    place_work_hours = PlaceWorkHoursWeekDeserializer.deserialize(data_1['work_hours'], DES_WORK_HOURS_WEEK_UPDATE)

    assert isinstance(place_work_hours, list)

    assert place_work_hours[0].week_day == 'mo'
    assert place_work_hours[0].is_holiday == data_1['work_hours']['mo']['is_holiday']
    assert place_work_hours[0].is_all_day == data_1['work_hours']['mo']['is_all_day']
    # assert place_work_hours[0].time_start == datetime.time(data_1['work_hours']['mo']['time_start'])
    # assert place_work_hours[0].time_finish == datetime.time(data_1['work_hours']['mo']['time_finish'])

    data_2 = {'work_hours': {}}

    place_work_hours = PlaceWorkHoursWeekDeserializer.deserialize(data_2['work_hours'], DES_WORK_HOURS_WEEK_UPDATE)

    assert place_work_hours[0].week_day is None
    assert place_work_hours[0].is_holiday is None
    assert place_work_hours[0].is_all_day is None
    assert place_work_hours[0].time_start is None
    assert place_work_hours[0].time_finish is None

    data_3 = {'work_hours': None}

    try:
        place_work_hours = PlaceWorkHoursWeekDeserializer.deserialize(data_3['work_hours'], DES_WORK_HOURS_WEEK_UPDATE)
    except AttributeError:
        assert 1 == 1
