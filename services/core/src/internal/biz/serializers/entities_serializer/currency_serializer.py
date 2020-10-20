from typing import re, Optional, List

from src.internal.biz.entities.currency import Currency


def currency_serializer(data: re) -> Optional[List[Currency]] or Optional[Currency]:
    try:
        currency = [Currency(
            id=data[i]['currency_id'],
            name=data[i]['currency_name'],
            short_name=data[i]['currency_short_name']
        )for i in range(len(data))]
        return currency
    except:
        try:
            currency = Currency(
                id=data['currency_id'],
                sign=data['currency_sign']
            )
            return currency
        except:
            raise TypeError
