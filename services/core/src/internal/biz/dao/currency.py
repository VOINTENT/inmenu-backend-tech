from src.internal.biz.dao.base_dao import BaseDao

from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.entities.currency import Currency


class CurrencyDao(BaseDao):

    async def get(self, place_main_id):
        sql = """
        SELECT 
            currency.id                         AS currency_id,
            currency.sign                       AS currency_sign
        FROM 
            currency
        WHERE 
            currency.id = (SELECT
                                place_main.main_currency    AS place_main_main_currency
                            FROM 
                                place_main
                            WHERE 
                                place_main.id = $1)
        """
        if self.conn:
            data = await self.conn.fetchrow(sql, place_main_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchrow(sql, place_main_id)
        if not data:
            return None, ErrorEnum.CURRENCY_DOESNT_EXISTS
        currency = Currency(
            id=data['currency_id'],
            sign=data['currency_sign']
        )
        return currency
