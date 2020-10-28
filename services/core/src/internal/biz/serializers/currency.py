from src.internal.biz.entities.currency import Currency
from src.internal.biz.serializers.base_serializer import BaseSerializer

SER_CURRENCY_TYPE = 'ser_currency_type'


class CurrencySerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_CURRENCY_TYPE:
            return cls._serialize_get_currency_type
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_currency_type(currency_type: Currency) -> dict:
        return {
            'id': currency_type.id,
            'name': currency_type.name,
            'sign': currency_type.sign
        }
