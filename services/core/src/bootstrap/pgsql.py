from src.configs.pgsql import HOST, USER, PASSWORD, PORT, PRIMARY_DB_NAME
from src.internal.drivers.async_pg import AsyncPg
from src.internal.drivers.sanic import SanicServer


def init_pgsql_server():
    AsyncPg.init_primary_db(SanicServer.get_app(), HOST, USER, PASSWORD, PORT, PRIMARY_DB_NAME)
