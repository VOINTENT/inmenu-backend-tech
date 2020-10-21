from typing import Optional, List, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.currency import CurrencyDao
from src.internal.biz.entities.currency import Currency
from src.internal.biz.services.base_service import BaseService


class CurrencyTypeService(BaseService):

    @staticmethod
    async def get_currency_types(pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[Currency]], Optional[Error]]:
        currency_types, error_currency_types = await CurrencyDao().get_currency_type(pagination_size, pagination_after, lang_id)
        if error_currency_types:
            return None, error_currency_types
        return currency_types, None
