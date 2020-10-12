import requests


def test_sanic_server():
    response = requests.get('http://127.0.0.1:8000/api/test/server')
    assert response.status_code == 200
    assert response.json() == {'test': 'Successful!'}
