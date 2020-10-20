from src.internal.biz.entities.place_location import PlaceLocation
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_PLACE_LOCATION_GET_LOCATIONS_WITH_PLACES = 'place-location-get-locs-places'
SER_PLACE_LOCATION_GET_LOCATIONS_ON_MAP = 'place-location-get-on-map'


class PlaceLocationSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_PLACE_LOCATION_GET_LOCATIONS_WITH_PLACES:
            return cls._serializer_place_location_get_locations_with_places
        elif format_ser == SER_PLACE_LOCATION_GET_LOCATIONS_ON_MAP:
            return cls._serializer_place_location_get_locations_on_map
        else:
            raise TypeError

    @staticmethod
    def _serializer_place_location_get_locations_with_places(place_location: PlaceLocation) -> dict:
        return {
            'city': place_location.city,
            'country': place_location.country,
            'count_places': place_location.count_places
        }

    @staticmethod
    def _serializer_place_location_get_locations_on_map(place_location: PlaceLocation) -> dict:
        return {
            'place_id': place_location.place_main.id,
            'place_location_id': place_location.id,
            'coords': {
                'lat': place_location.coords[0],
                'long': place_location.coords[1]
            }
        }
