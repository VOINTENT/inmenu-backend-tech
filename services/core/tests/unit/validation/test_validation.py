from sanic.response import json

from src.internal.adapters.entities.utils import get_response_with_validation_errors
from src.internal.biz.validators.test import TestSchema


def test_empty_body():
    errors = TestSchema().validate(None)
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -101,
        "msg": "Отправлено пустое тело запроса"
    }).body


def test_excess_field():
    errors = TestSchema().validate({'test': 'test', 'field': 'value'})
    response = get_response_with_validation_errors(errors)

    assert response.status == 400
    assert response.body == json({
        "code": -102,
        "msg": "Введено неизвестное поле: field"
    }).body


def test_none_field():
    errors = TestSchema().validate({})
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -103,
        "msg": "Отсутствует поле: test"
    }).body


def test_wrong_type_field():
    errors = TestSchema().validate({'test': 123})
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -104,
        "msg": "Некорректный тип поля: test"
    }).body


def test_not_null_field():
    errors = TestSchema().validate({'test': None})
    response = get_response_with_validation_errors(errors)
    assert response.status == 400
    assert response.body == json({
        "code": -105,
        "msg": "Поле не может принимать значение null: test"
    }).body
