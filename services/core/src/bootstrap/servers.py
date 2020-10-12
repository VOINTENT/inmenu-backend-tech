from src.configs.http_server import HOST, PORT, DEBUG, SSL, ACCESS_LOG, AUTO_RELOAD, WORKERS
from src.internal.drivers.sanic import SanicServer
from src.internal.servers.http.api.main import main_api


def init_http_server():
    SanicServer.set_main_api(main_api)


def run_http_server():
    SanicServer.run_server(HOST, PORT, DEBUG, SSL, WORKERS, ACCESS_LOG, AUTO_RELOAD)
