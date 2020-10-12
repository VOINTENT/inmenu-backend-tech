from src.bootstrap.pgsql import init_pgsql_server
from src.bootstrap.servers import init_http_server, run_http_server


def init_all():

    init_http_server()
    print('[i] Http server inited')

    init_pgsql_server()
    print('[i] Pgsql server inited!')

    print('[i] Http server started...')
    run_http_server()
