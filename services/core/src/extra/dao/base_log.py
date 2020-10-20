from typing import Tuple, Optional

from asyncpg.pool import Pool

from src.internal.adapters.entities.error import Error
from src.internal.drivers.async_pg import AsyncPg


class BaseLogsDao:

    def __init__(self) -> None:
        self.pool: Pool = AsyncPg.get_pool_logs_db()

    async def add(self, obj: object) -> Tuple[Optional[object], Optional[Error]]:
        raise NotImplemented
