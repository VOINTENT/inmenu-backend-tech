from http.client import HTTPResponse
from typing import List

from sanic.response import json

from src.internal.biz.entities.currency import Currency
from src.internal.biz.serializers.currency import CurrencySerializer, SER_CURRENCY_TYPE


def get_response_get_currency_types(currency_types: List[Currency]) -> HTTPResponse:
    return json([CurrencySerializer.serialize(currency_type, SER_CURRENCY_TYPE) for currency_type in currency_types], 200)
