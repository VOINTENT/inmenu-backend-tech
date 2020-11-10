from sanic.response import json

from src.internal.adapters.entities.utils import get_response_with_validation_errors
from src.internal.biz.validators.patch_place import PlacePatchSchema, WeekDaySchema


def test_path_place_main_lang_id():
    data = {"main_lang_id": 'str'}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: main_lang_id'
    }).body


def test_path_place_name():
    data = {'name': 123}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: name'
    }).body


def test_path_place_description():
    data = {'description': 123}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: description'
    }).body


def test_path_place_login():
    data = {'login': 123}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: login'
    }).body


def test_path_place_photo_link():
    data = {'photo_link': 123}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: photo_link'
    }).body


def test_path_place_place_types():
    data = {'place_types_ids': {'1': 1, '2': 2, '3': 3}}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: place_types_ids'
    }).body


def test_path_place_service():
    data = {'services_ids': {'1': 1, '2': 2, '3': 3}}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: services_ids'
    }).body


def test_path_place_cuisine_types():
    data = {'cuisine_types_ids': {'1': 1, '2': 2, '3': 3}}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: cuisine_types_ids'
    }).body


def test_path_place_main_currency():
    data = {'main_currency_id': 'str'}
    errors = PlacePatchSchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": 'Некорректный тип поля: main_currency_id'
    }).body


def test_path_place_not_field_time_finish_week_day():
    data = {"is_holiday": False,
            "is_all_day": False,
            "time_start": 28800}
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -103,
        "msg": 'Отсутствует поле: time_finish'
    }).body


def test_path_place_not_field_time_start_week_day():
    data = {"is_holiday": False,
            "is_all_day": False,
            "time_finish": 72600}
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -103,
        "msg": 'Отсутствует поле: time_start'
    }).body


def test_path_place_not_field_is_all_day_week_day():
    data = {"is_holiday": False,
            "time_start": 28800,
            "time_finish": 72600}
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -103,
        "msg": 'Отсутствует поле: is_all_day'
    }).body


def test_path_place_not_field_is_holiday_week_day():
    data = {"is_all_day": False,
            "time_start": 28800,
            "time_finish": 72600}
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -103,
        "msg": 'Отсутствует поле: is_holiday'
    }).body


def test_work_on_holiday_validate_week_day():
    data = {
        "is_holiday": True,
        "is_all_day": False,
        "time_start": 28800,
        "time_finish": 79200
    }
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -107,
        "msg": 'В выходной день не может быть указано время работы: _schema'
    }).body


def test_work_in_holiday_validate_week_day():
    data = {
        "is_holiday": True,
        "is_all_day": True,
        "time_start": None,
        "time_finish": None
    }
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -110,
        "msg": 'В выходной день не может быть указан полный день работы: _schema'
    }).body


def test_work_is_all_day_validate_week_day():
    data = {
        "is_holiday": False,
        "is_all_day": True,
        "time_start": 28800,
        "time_finish": 79200
    }
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -111,
        "msg": 'В полный день работы не может быть указано время работы: _schema'
    }).body


def test_time_start_validate_week_day():
    data = {
        "is_holiday": False,
        "is_all_day": False,
        "time_start": None,
        "time_finish": 79200
    }
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -103,
        "msg": 'Отсутствует поле: time_start'
    }).body


def test_time_finish_validate_week_day():
    data = {
        "is_holiday": False,
        "is_all_day": False,
        "time_start": 28800,
        "time_finish": None
    }
    errors = WeekDaySchema().validate(data)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -103,
        "msg": 'Отсутствует поле: time_finish'
    }).body
