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
            place_main.id = $1
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

    async def get_currency_type(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[Currency]], Optional[Error]]:
        sql = """
            SELECT 
                currency.id                AS currency_id,
                currency_translate.name    AS currency_name, 
                currency.sign              AS currency_sign
            FROM
                currency
            INNER JOIN
                currency_translate ON currency.id = currency_translate.currency_id
            WHERE currency_translate.language_id = $1
            LIMIT $2
            OFFSET $3
        """
        if self.conn:
            data = await self.conn.fetch(sql, lang_id, pagination_size, pagination_after)
        else:
            async with self.pool.acquire() as conn:
                data = await conn.fetch(sql, lang_id, pagination_size, pagination_after)

        if not data:
            return [], None

        currencies = [currency_serializer(dictionary) for dictionary in data]

        return currencies, None
