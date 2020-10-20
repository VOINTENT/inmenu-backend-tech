from typing import Tuple, Optional

import asyncpg
from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.base_dao import BaseDao
from src.internal.biz.deserializers.account_main import AccountMainDeserializer, DES_ACCOUNT_MAIN_FROM_DB_FULL, \
    ACCOUNT_MAIN_ID, ACCOUNT_MAIN_CREATED_AT, ACCOUNT_MAIN_EDITED_AT, ACCOUNT_MAIN_EMAIL, ACCOUNT_MAIN_HASH_PASSWORD, \
    ACCOUNT_MAIN_IS_ACTIVE, ACCOUNT_MAIN_IS_CONFIRMED, ACCOUNT_MAIN_BALANCE, ACCOUNT_MAIN_NAME
from src.internal.biz.entities.account_main import AccountMain


UNIQUE_EMAIL = 'unique_account_email'


class AccountMainDao(BaseDao):

    async def add(self, account_main: AccountMain) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            sql = """
                INSERT INTO account_main(email, name, hash_password, is_confirmed) VALUES
                ($1, $2, $3, $4)
                RETURNING id, created_at, edited_at;
            """
            try:
                row = await conn.fetchrow(sql, account_main.email, account_main.name, account_main.hash_password, account_main.is_confirmed)
            except asyncpg.exceptions.UniqueViolationError as exc:

                if exc.constraint_name == UNIQUE_EMAIL:
                    return None, ErrorEnum.NOT_UNIQUE_EMAIL
                else:
                    raise TypeError

            account_main.id = row['id']
            account_main.created_at = row['created_at']
            account_main.edited_at = row['edited_at']
            account_main.is_active = True
            return account_main, None

    async def get_by_email_hash_password(self, account_main: AccountMain) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(f"""
                SELECT 
                    id AS {ACCOUNT_MAIN_ID},
                    email AS {ACCOUNT_MAIN_EMAIL},
                    hash_password AS {ACCOUNT_MAIN_HASH_PASSWORD},
                    is_active AS {ACCOUNT_MAIN_IS_ACTIVE},
                    is_confirmed AS {ACCOUNT_MAIN_IS_CONFIRMED}
                FROM 
                    account_main
                WHERE 
                    email = $1 AND hash_password = $2
            """, account_main.email, account_main.hash_password)

            if row:
                return AccountMainDeserializer.deserialize(row, DES_ACCOUNT_MAIN_FROM_DB_FULL), None
            return None, None

    async def get_by_session_id(self, session_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                f"""
                    SELECT
                        account_session.account_main_id AS {ACCOUNT_MAIN_ID}
                    FROM
                        account_session
                    WHERE id = $1
                """, session_id
            )
            if not row:
                return None, None
            return AccountMainDeserializer.deserialize(row, DES_ACCOUNT_MAIN_FROM_DB_FULL), None

    async def get_by_session_id_with_confirmed(self, session_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                f"""
                    SELECT
                        account_main.id             AS {ACCOUNT_MAIN_ID},
                        account_main.is_confirmed   AS {ACCOUNT_MAIN_IS_CONFIRMED}
                    FROM
                        account_main INNER JOIN account_session ON account_main.id = account_session.account_main_id
                    WHERE account_session.id = $1
                """, session_id
            )
            if not row:
                return None, None
            return AccountMainDeserializer.deserialize(row, DES_ACCOUNT_MAIN_FROM_DB_FULL), None

    async def get_by_id(self, account_main_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                f"""
                    SELECT 
                        id AS {ACCOUNT_MAIN_ID},
                        created_at AS {ACCOUNT_MAIN_CREATED_AT},
                        edited_at AS {ACCOUNT_MAIN_EDITED_AT},
                        email AS {ACCOUNT_MAIN_EMAIL},
                        name AS {ACCOUNT_MAIN_NAME},
                        hash_password AS {ACCOUNT_MAIN_HASH_PASSWORD},
                        is_active AS {ACCOUNT_MAIN_IS_ACTIVE},
                        is_confirmed AS {ACCOUNT_MAIN_IS_CONFIRMED},
                        balance AS {ACCOUNT_MAIN_BALANCE}
                    FROM 
                        account_main
                    WHERE 
                        id = $1
                """, account_main_id
            )
            if not row:
                return None, None

            return AccountMainDeserializer.deserialize(row, DES_ACCOUNT_MAIN_FROM_DB_FULL), None

    async def get_email_by_id(self, auth_account_main_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            account_email = await conn.fetchval(
                f"""
                    SELECT
                        email
                    FROM
                        account_main
                    WHERE
                        account_main.id = $1
                """, auth_account_main_id
            )

            if not account_email:
                return None, None

            return AccountMain(email=account_email), None

    async def get_by_email(self, email: str) -> Tuple[Optional[AccountMain], Optional[Error]]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                f"""
                    SELECT
                        id              AS {ACCOUNT_MAIN_ID},
                        is_confirmed    AS {ACCOUNT_MAIN_IS_CONFIRMED},
                        is_active       AS {ACCOUNT_MAIN_IS_ACTIVE}
                    FROM
                        account_main
                    WHERE
                        account_main.email = $1
                """, email
            )

            if not row:
                return None, None

            account_main = AccountMainDeserializer.deserialize(row, DES_ACCOUNT_MAIN_FROM_DB_FULL)
            account_main.email = email

            return account_main, None
