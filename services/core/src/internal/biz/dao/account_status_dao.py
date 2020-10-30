from typing import Optional, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.account_status import AccountStatus


class AccountStatusDao(BaseDao):

    async def get_owner_status(self) -> Tuple[Optional[AccountStatus], Optional[Error]]:
        async with self.pool.acquire() as conn:
            account_status_id = await conn.fetchval("""
                SELECT account_status.id
                FROM account_status
                WHERE account_status.id = 1
            """)
            if not account_status_id:
                raise TypeError

            return AccountStatus(id=account_status_id), None
