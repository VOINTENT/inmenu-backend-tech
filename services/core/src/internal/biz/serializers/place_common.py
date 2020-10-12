from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.serializers.base_serializer import BaseSerializer
from src.internal.biz.serializers.place_cuisine_types import PlaceCuisineTypesSerializer, \
    SER_PLACE_CUISINE_TYPES_GET_PLACES

SER_PLACE_COMMON_GET_PLACES = 'get-places'


class PlaceCommonSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_PLACE_COMMON_GET_PLACES:
            return cls._serialize_get_places
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_places(place_common: PlaceCommon):
        place_common.place_main.photo.create_full_url()
        return {
            'id': place_common.place_main.id,
            'name': place_common.place_main.name,
            'photo_link': place_common.place_main.photo.full_url,
            'cuisine_types': PlaceCuisineTypesSerializer.serialize(place_common.place_cuisine_types, SER_PLACE_CUISINE_TYPES_GET_PLACES),
            'distance': '670 m'
        }
