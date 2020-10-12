from src.internal.biz.entities.place_cuisine_type import PlaceCuisineType
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_PLACE_CUISINE_TYPE_GET_PLACES = 'place-cuisine-type-get-places'


class PlaceCuisineTypeSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_PLACE_CUISINE_TYPE_GET_PLACES:
            return cls._serialize_get_places
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_places(place_cuisine_type: PlaceCuisineType):
        return {
            'id': place_cuisine_type.cuisine_type.id,
            'name': place_cuisine_type.cuisine_type.name
        }
