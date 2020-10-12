from typing import Tuple, Optional, List

from asyncpg import Connection
from asyncpg.pool import Pool

from src.internal.adapters.entities.error import Error
from src.internal.drivers.async_pg import AsyncPg


class BaseDao:

    def __init__(self, conn: Connection = None) -> None:
        self.pool: Pool = AsyncPg.get_pool_primary_db()
        self.conn: Connection = conn

    async def get_by_id(self, id: int) -> Tuple[Optional[object], Optional[Error]]:
        raise NotImplemented

    async def add(self, obj: object) -> Tuple[Optional[object], Optional[Error]]:
        raise NotImplemented

    async def add_many(self, objs: List[object]) -> Tuple[None, Optional[Error]]:
        raise NotImplemented

    async def remove(self, obj: object) -> Tuple[Optional[object], Optional[Error]]:
        raise NotImplemented

    async def remove_by_id(self, id: int) -> Tuple[Optional[object], Optional[Error]]:
        raise NotImplemented

    async def get_all(self) -> Tuple[Optional[List[object]], Optional[Error]]:
        raise NotImplemented

    async def update(self, id, obj: object) -> Tuple[Optional[object], Optional[Error]]:
        raise NotImplemented
