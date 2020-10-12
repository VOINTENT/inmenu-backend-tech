from src.internal.biz.entities.auth_code import AuthCode
from src.internal.drivers.async_pg import AsyncPg


class TestService:

    @staticmethod
    async def get_test_data() -> int:
        async with AsyncPg.get_pool_primary_db().acquire() as conn:
            return await conn.fetchval(
                """
                    SELECT id FROM test LIMIT 1;
                """
            )

    @staticmethod
    async def truncate_tables() -> None:
        async with AsyncPg.get_pool_primary_db().acquire() as conn:
            await conn.execute(
                """
                    TRUNCATE TABLE account_main CASCADE;
                    TRUNCATE TABLE account_session CASCADE;
                """
            )

    @staticmethod
    async def get_auth_code(auth_account_main_id: int) -> AuthCode:
        async with AsyncPg.get_pool_primary_db().acquire() as conn:
            code = await conn.fetchval(
                """
                SELECT code
                FROM auth_code
                WHERE account_main_id = $1
                """, auth_account_main_id
            )
            return AuthCode(code=code)
