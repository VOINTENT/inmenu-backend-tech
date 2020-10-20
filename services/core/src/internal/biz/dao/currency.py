from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao

from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.entities.currency import Currency
from src.internal.biz.serializers.entities_serializer.currency_serializer import currency_serializer


class CurrencyDao(BaseDao):

    async def get(self, place_main_id: int) -> Tuple[Optional[Currency], Optional[Error]]:
        sql = """
        SELECT 
            currency.id                         AS currency_id,
            currency.sign                       AS currency_sign
        FROM 
            currency
        INNER JOIN
            place_main ON place_main.main_currency = currency.id
        WHERE
            place_main.main_currency = &1
            """
        if self.conn:
            data = await self.conn.fetchrow(sql, place_main_id)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchrow(sql, place_main_id)
        if not data:
            return None, ErrorEnum.CURRENCY_DOESNT_EXISTS
        currency = currency_serializer(data)
        return currency, None

    async def get_currency_type(self, pagination_size, pagination_after, lang_id) -> Tuple[Optional[List[Currency]], Optional[Error]]:
        sql = """
            SELECT 
                currency.id             AS currency_id,
                currency.name           AS currency_name, 
                currency.short_name     AS currency.short_name
            FROM
                currency
            LIMIT $1
            OFFSET &2
        """
        if self.conn:
            data = await self.conn.fetchrow(sql, pagination_size, pagination_after)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetchrow(sql)
        if not data:
            return None, ErrorEnum.CURRENCY_DOESNT_EXISTS
        currency = currency_serializer(data)
        if not currency:
            return None, ErrorEnum.CURRENCY_DOESNT_EXISTS
        return currency, None
