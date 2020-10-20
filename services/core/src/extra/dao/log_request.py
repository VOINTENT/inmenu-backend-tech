from typing import Tuple, Optional

from src.extra.dao.base_log import BaseLogsDao
from src.extra.entities.log_request import LogRequest
from src.internal.adapters.entities.error import Error


class LogRequestDao(BaseLogsDao):

    async def add(self, log_request: LogRequest) -> Tuple[Optional[LogRequest], Optional[Error]]:
        async with self.pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO log_request(completion_time, method, url, ip, status, error_msg) 
                VALUES ($1, $2, $3, $4, $5, $6)
                """, log_request.completion_time, log_request.method, log_request.url, log_request.ip,
                               log_request.status, log_request.error_msg)

            return log_request, None
