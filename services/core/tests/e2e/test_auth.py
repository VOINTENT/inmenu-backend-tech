import json

import requests

from tests.test_config import BASE_URL_GENERAL, BASE_URL_TEST


def test_register(test_data, truncate_tables):
    request_data = test_data['user1']['auth']
    response = requests.post(f'{BASE_URL_GENERAL}/accounts/register', data=json.dumps(request_data))

    assert response.status_code == 201

    data = response.json()
    assert isinstance(data['id'], int)
    assert data['email'] == request_data['email']
    assert isinstance(data['auth_token'], str)
    assert data['is_confirmed'] is False
    assert data['is_active'] is True


def test_auth_basic(test_data, truncate_tables, user1_register):
    request_data = test_data['user1']['auth']
    response = requests.post(f'{BASE_URL_GENERAL}/accounts/auth/basic', data=json.dumps(request_data))

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data['id'], int)
    assert data['email'] == request_data['email']
    assert isinstance(data['auth_token'], str)
    assert data['is_confirmed'] is False
    assert data['is_active'] is True


def test_confirm_code(test_data, truncate_tables, user1_token):
    response = requests.get(f'{BASE_URL_TEST}/accounts/auth/code', headers={'auth-token': user1_token})
    code = response.json()

    response = requests.post(f'{BASE_URL_GENERAL}/accounts/auth/code', data=json.dumps(code), headers={'auth-token': user1_token})
    assert response.status_code == 200
    assert response.json() is True

    response = requests.post(f'{BASE_URL_GENERAL}/accounts/auth/basic', data=json.dumps(test_data['user1']['auth']))
    assert response.json()['is_confirmed'] is True

    response = requests.get(f'{BASE_URL_TEST}/accounts/auth/code', headers={'auth-token': user1_token})
    assert response.json()['code'] is None
