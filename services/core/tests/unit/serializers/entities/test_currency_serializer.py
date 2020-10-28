from src.internal.biz.entities.currency import Currency
from src.internal.biz.serializers.entities_serializer.currency_serializer import currency_serializer


def test_currency_serializer():
    data = {
        'currency_id': 1,
        'currency_name': 'name',
        'currency_sign': 'sign'
    }
    data_1 = {
        'currency_id': 2,
        'currency_sign': 'sign_2'
    }
    currency_1 = currency_serializer(data)
    currency_2 = currency_serializer(data_1)

    currency_3 = Currency(
        id=data['currency_id'],
        name=data['currency_name'],
        sign=data['currency_sign']
    )

    currency_4 = Currency(
        id=data_1['currency_id'],
        sign=data_1['currency_sign']
    )

    assert isinstance(currency_1, Currency)
    assert isinstance(currency_2, Currency)
    assert isinstance(currency_3, Currency)
    assert isinstance(currency_4, Currency)

    assert currency_2.name is None
    assert currency_1.name is not None

    assert currency_1.id == currency_3.id
    assert currency_1.name == currency_3.name
    assert currency_1.sign == currency_3.sign

    assert currency_2.id == currency_4.id
    assert currency_2.sign == currency_4.sign
