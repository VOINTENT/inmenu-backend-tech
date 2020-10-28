import json

import requests

from tests.test_config import BASE_URL_GENERAL


def test_get_cuisine_types():
    headers = {'lang': 'en'}
    response = requests.get(f'{BASE_URL_GENERAL}/services', headers=headers)

    data = [
        {
            "id": 1,
            "name": "VIP room"
        },
        {
            "id": 2,
            "name": "Wi-Fi"
        },
        {
            "id": 3,
            "name": "Banquet"
        },
        {
            "id": 4,
            "name": "Children holidays"
        }
    ]

    assert response.status_code == 200
    assert json.loads(response.text) == data

    headers = {'lang': 'ene'}
    response = requests.get(f'{BASE_URL_GENERAL}/services', headers=headers)

    assert response.status_code == 200
    assert json.loads(response.text) == []
