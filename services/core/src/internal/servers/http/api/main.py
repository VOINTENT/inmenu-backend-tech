from sanic import Blueprint

from src.internal.servers.http.api.general import general_api
from src.internal.servers.http.api.test import test_api

main_api = Blueprint.group(general_api, test_api, url_prefix='/api')
