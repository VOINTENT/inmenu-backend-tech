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
