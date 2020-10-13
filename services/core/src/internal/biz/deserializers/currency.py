from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.currency import Currency


DES_CURRENCY_FROM_DB_FULL = 'currency-from-db-full'


CURRENCY = 'cr'
CURRENCY_ID = CURRENCY + ID
CURRENCY_CREATED_AT = CURRENCY + CREATED_AT
CURRENCY_EDITED_AT = CURRENCY + EDITED_AT
CURRENCY_NAME = CURRENCY + 'nm'
CURRENCY_SIGN = CURRENCY + 'sg'


class CurrencyDeserializer(BaseDeserializer):
    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_CURRENCY_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(currency: Union[dict, Record]) -> Currency:
        return Currency(
            id=currency.get(CURRENCY_ID),
            created_at=currency.get(CURRENCY_CREATED_AT),
            edited_at=currency.get(CURRENCY_EDITED_AT),
            name=currency.get(CURRENCY_NAME),
            sign=currency.get(CURRENCY_SIGN)
        )
