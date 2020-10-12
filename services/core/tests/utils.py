import json

import requests

from tests.test_config import BASE_URL_GENERAL

_data = None


def get_data() -> dict:
    global _data
    if not _data:
        with open('tests/assets/data.json', encoding='utf-8') as f:
            _data = json.load(f)
    return _data


def register(account_data: dict):
    url = f'{BASE_URL_GENERAL}/accounts/register'
    requests.post(url, data=json.dumps(account_data))


def get_user_token(account_data: dict):
    url = f'{BASE_URL_GENERAL}/accounts/register'
    response = requests.post(url, data=json.dumps(account_data))
    return response.json()['auth_token']
