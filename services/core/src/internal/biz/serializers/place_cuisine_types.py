from typing import List

from src.internal.biz.entities.place_cuisine_type import PlaceCuisineType
from src.internal.biz.serializers.base_serializer import BaseSerializer
from src.internal.biz.serializers.place_cuisine_type import PlaceCuisineTypeSerializer, SER_PLACE_CUISINE_TYPE_GET_PLACES

SER_PLACE_CUISINE_TYPES_GET_PLACES = 'place-cuisine-types-get-places'


class PlaceCuisineTypesSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_PLACE_CUISINE_TYPES_GET_PLACES:
            return cls._serialize_get_places
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_places(place_cuisine_types: List[PlaceCuisineType]):
        return [PlaceCuisineTypeSerializer.serialize(place_cuisine_type, SER_PLACE_CUISINE_TYPE_GET_PLACES)
                for place_cuisine_type in place_cuisine_types]
