from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.deserializers.auth_code import AuthCodeDeserializer, DES_AUTH_CODE_FROM_DB_FULL, AUTH_CODE_ID, \
    AUTH_CODE_EDITED_AT
from src.internal.biz.entities.auth_code import AuthCode


class AuthCodeDao(BaseDao):

    async def get_by_account_main_id_code(self, auth_code: AuthCode) -> Tuple[Optional[AuthCode], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                """
                SELECT
                    id,
                    edited_at
                FROM
                    auth_code
                WHERE
                    account_main_id = $1 AND code = $2
                """, auth_code.account_main.id, auth_code.code
            )

            if not row:
                return None, None
            auth_code.id = row['id']
            auth_code.edited_at = row['edited_at']

            return auth_code, None

    async def remove_by_id(self, auth_code_id: int) -> Tuple[None, Optional[Error]]:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                DELETE
                FROM auth_code
                WHERE id = $1
                """, auth_code_id
            )

            return None, None

    async def get_by_account_main_id(self, account_main_id: int) -> Tuple[Optional[AuthCode], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                f"""
                SELECT
                    id          {AUTH_CODE_ID},
                    edited_at   {AUTH_CODE_EDITED_AT}
                FROM
                    auth_code
                WHERE
                    account_main_id = $1
                """, account_main_id
            )

            if not row:
                return None, None
            return AuthCodeDeserializer.deserialize(row, DES_AUTH_CODE_FROM_DB_FULL), None

    async def update(self, auth_code_id: int, auth_code: AuthCode) -> Tuple[Optional[AuthCode], Optional[Error]]:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                UPDATE
                    auth_code
                SET
                    edited_at = CURRENT_TIMESTAMP,
                    code = $1
                """, auth_code.code
            )

            return auth_code, None

    async def add(self, auth_code: AuthCode) -> Tuple[Optional[AuthCode], Optional[Error]]:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO auth_code(account_main_id, code) VALUES ($1, $2);
                """, auth_code.account_main.id, auth_code.code
            )

            return auth_code, None

    async def set_is_confirm(self, account_main_id: int, is_confirmed: bool) -> Tuple[None, Optional[Error]]:
        async with self.pool.acquire() as conn:
            await conn.execute(
                """
                UPDATE account_main
                SET is_confirmed = $2
                WHERE account_main.id = $1
                """, account_main_id, is_confirmed
            )
            return None, None
