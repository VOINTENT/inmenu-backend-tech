import json

import requests

from tests.test_config import BASE_URL_GENERAL


def test_currency_type():
    headers = {'lang': 'en'}
    response = requests.get(f'{BASE_URL_GENERAL}/currency_types', headers=headers)
    data = [
        {
            "id": 1,
            "name": "Rubles",
            "sign": "₽"
        },
        {
            "id": 2,
            "name": "Dollars",
            "sign": "$"
        },
        {
            "id": 3,
            "name": "Euro",
            "sign": "€"
        },
        {
            "id": 4,
            "name": "Hryvnia",
            "sign": "₴"
        }
    ]

    assert json.loads(response.text) == data
    assert response.status_code == 200

    headers = {'lang': 'ene'}
    response = requests.get(f'{BASE_URL_GENERAL}/currency_types', headers=headers)
    assert response.status_code == 200
    assert json.loads(response.text) == []
