from typing import re, Optional, List

from src.internal.biz.entities.currency import Currency


def currency_serializer(data) -> Optional[List[Currency]] or Optional[Currency]:
    try:
        return [Currency(
            id=data[i]['currency_id'],
            name=data[i]['currency_name'],
            sign=data[i]['currency_short_name']
        )for i in range(len(data))]
    except:
        return Currency(
            id=data['currency_id'],
            sign=data['currency_sign']
        )
