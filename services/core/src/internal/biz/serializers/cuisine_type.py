from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.serializers.base_serializer import BaseSerializer

SER_CUISINE_TYPE = 'ser_cuisine_type'


class CuisineTypeSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_CUISINE_TYPE:
            return cls._serialize_get_cuisine_type
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_cuisine_type(cuisine_type: CuisineType) -> dict:
        return {
            'id': cuisine_type.id,
            'name': cuisine_type.name
        }
