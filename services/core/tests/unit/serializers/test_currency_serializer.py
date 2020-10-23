from src.internal.biz.entities.currency import Currency
from src.internal.biz.serializers.currency import CurrencySerializer, SER_CURRENCY_TYPE


def test_currency_serializer():
    id= 1
    name = 'name'
    sign = 'sign'

    currency = Currency(
        id=id,
        name=name,
        sign=sign
    )

    data = CurrencySerializer.serialize(currency, SER_CURRENCY_TYPE)
    data_1 = {
        'id' : id,
        'name': name,
        'sign': sign
    }

    assert data == data_1
