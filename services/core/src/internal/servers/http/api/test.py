from sanic import Blueprint

from src.internal.servers.http.api.test_services import test

test_api = Blueprint.group(test, url_prefix='/test')
