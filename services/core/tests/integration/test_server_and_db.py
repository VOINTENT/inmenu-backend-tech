import requests


def test_server_and_bd():
    response = requests.get('http://127.0.0.1:8000/api/test/db')
    assert response.status_code == 200
    assert response.json() == {'result': 1}
