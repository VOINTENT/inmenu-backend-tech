from asyncpg import create_pool
from asyncpg.pool import Pool
from sanic import Sanic


class AsyncPg:

    __pool_primary_db: Pool = None
    __pool_logs_db: Pool = None

    @classmethod
    def get_pool_primary_db(cls) -> Pool:
        return cls.__pool_primary_db

    @classmethod
    def get_pool_logs_db(cls) -> Pool:
        return cls.__pool_primary_db

    @classmethod
    def init_primary_db(cls, server_app: Sanic, host: str, user: str, password: str, port: int, database: str):
        @server_app.listener('before_server_start')
        async def init_primary_db(app, loop):
            cls.__pool_primary_db = await create_pool(host=host, user=user, password=password, port=port, database=database)

    @classmethod
    def init_logs_db(cls, server_app: Sanic, host: str, user: str, password: str, port: int, database: str):
        @server_app.listener('before_server_start')
        async def _init_logs_db(app, loop):
            cls.__pool_logs_db = await create_pool(host=host, user=user, password=password, port=port, database=database)
