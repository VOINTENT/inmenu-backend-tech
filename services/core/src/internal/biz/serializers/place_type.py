from src.internal.biz.entities.place_type import PlaceType
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_PLACE_TYPE_SIMPLE = 'place-type-simple'


class PlaceTypeSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_PLACE_TYPE_SIMPLE:
            return cls._serialize_simple
        else:
            raise TypeError

    @staticmethod
    def _serialize_simple(place_type: PlaceType) -> dict:
        return {
            'id': place_type.id,
            'name': place_type.name
        }
