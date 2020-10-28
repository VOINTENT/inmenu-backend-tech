import json

import requests

from tests.test_config import BASE_URL_GENERAL, BASE_URL_TEST


def test_get_cuisine_types():
    headers = {'lang': 'en'}
    response = requests.get(f'{BASE_URL_GENERAL}/measure_units', headers=headers)

    data = [
        {
            "id": 1,
            "name": "grams",
            "short_name": "gr."
        },
        {
            "id": 2,
            "name": "milliliters",
            "short_name": "ml."
        },
        {
            "id": 3,
            "name": "pieces",
            "short_name": "pc."
        }
    ]

    assert response.status_code == 200
    assert json.loads(response.text) == data

    headers = {'lang': 'ene'}
    response = requests.get(f'{BASE_URL_GENERAL}/measure_units', headers=headers)

    assert response.status_code == 200
    assert json.loads(response.text) == []
