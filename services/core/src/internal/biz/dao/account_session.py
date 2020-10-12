from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.entities.account_session import AccountSession


class AccountSessionDao(BaseDao):

    async def add(self, account_session: AccountSession) -> Tuple[Optional[AccountSession], Optional[Error]]:
        async with self.pool.acquire() as conn:
            session_id = await conn.fetchval(
                """
                    INSERT INTO account_session(account_main_id) VALUES ($1)
                    RETURNING id;
                """, account_session.account_main.id
            )

            account_session.id = session_id
            return account_session, None
