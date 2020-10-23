from typing import Optional, List

from src.internal.biz.entities.currency import Currency


def currency_serializer(dictionary: dict) -> Optional[Currency]:
    try:
        return Currency(
            id=dictionary['currency_id'],
            name=dictionary['currency_name'],
            sign=dictionary['currency_sign'])
    except:
        try:
            return Currency(
                id=dictionary['currency_id'],
                sign=dictionary['currency_sign']
            )
        except:
            raise TypeError
