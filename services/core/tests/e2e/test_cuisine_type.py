import json

import requests

from tests.test_config import BASE_URL_GENERAL, BASE_URL_TEST


def test_get_cuisine_types():
    headers = {'lang': 'en'}
    response = requests.get(f'{BASE_URL_GENERAL}/cuisine_types', headers=headers)

    data = [{"id": 1, "name": "Russian"},
            {"id": 2, "name": "American"},
            {"id": 3, "name": "Italian"},
            {"id": 4, "name": "Chinese"},
            {"id": 5, "name": "Japanese"},
            {"id": 6, "name": "French"}]

    assert response.status_code == 200
    assert json.loads(response.text) == data

    headers = {'lang': 'ene'}
    response = requests.get(f'{BASE_URL_GENERAL}/cuisine_types', headers=headers)

    assert response.status_code == 200
    assert json.loads(response.text) == []
