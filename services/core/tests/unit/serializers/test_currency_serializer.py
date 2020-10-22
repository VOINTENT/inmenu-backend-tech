from src.internal.biz.entities.currency import Currency
from src.internal.biz.serializers.entities_serializer.currency_serializer import currency_serializer


def test_currency_serializer():
    data = {
        'currency_id': 1,
        'currency_translate_name': 'name',
        'currency_sign': 'sign'
    }
    data_1 = {
        'currency_id': 2,
        'currency_sign': 'sign_2'
    }
    currency_1 = currency_serializer(data)
    currency_2 = currency_serializer(data_1)

    assert isinstance(currency_1, Currency)
    assert isinstance(currency_2, Currency)

    assert currency_2.name is None
    assert currency_1.name is not None
