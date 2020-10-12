import pytest
import requests

from tests.test_config import BASE_URL_TEST
from tests.utils import get_data, register, get_user_token


@pytest.fixture()
def truncate_tables():
    requests.post(f'{BASE_URL_TEST}/truncate_tables')
    yield
    requests.post(f'{BASE_URL_TEST}/truncate_tables')


@pytest.fixture()
def test_data():
    return get_data()


@pytest.fixture()
def user1_register(test_data):
    register(test_data['user1']['auth'])


@pytest.fixture()
def user1_token(test_data):
    return get_user_token(test_data['user1']['auth'])
