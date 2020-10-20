from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.serializers.base_serializer import BaseSerializer
from src.internal.biz.serializers.place_contacts import PlaceContactsSerializer, SER_CONTACTS_SIMPLE
from src.internal.biz.serializers.place_cuisine_types import PlaceCuisineTypesSerializer, \
    SER_PLACE_CUISINE_TYPES_GET_PLACES
from src.internal.biz.serializers.place_type import PlaceTypeSerializer, SER_PLACE_TYPE_SIMPLE
from src.internal.biz.serializers.service import ServiceSerializer, SER_SERVICE_SIMPLE

SER_PLACE_COMMON_GET_PLACES = 'get-places'
SER_PLACE_COMMON_GET_PLACES_BY_NAME = 'get-places-by-name'
SER_PLACE_COMMON_GET_PLACE_LOCATION_PARTIAL_DETAIL = 'get-place-location-partial-detail'


class PlaceCommonSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_PLACE_COMMON_GET_PLACES:
            return cls._serialize_get_places
        elif format_ser == SER_PLACE_COMMON_GET_PLACES_BY_NAME:
            return cls._serialize_get_places_by_name
        elif format_ser == SER_PLACE_COMMON_GET_PLACE_LOCATION_PARTIAL_DETAIL:
            return cls._serialize_get_place_location_partial_detail
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_places(place_common: PlaceCommon) -> dict:
        place_common.place_main.photo.create_full_url()
        return {
            'id': place_common.place_main.id,
            'name': place_common.place_main.name,
            'photo_link': place_common.place_main.photo.full_url,
            'cuisine_types': PlaceCuisineTypesSerializer.serialize(place_common.place_cuisine_types, SER_PLACE_CUISINE_TYPES_GET_PLACES),
            'distance': '670 m'
        }

    @staticmethod
    def _serialize_get_places_by_name(place_common: PlaceCommon) -> dict:
        place_common.place_main.photo.create_full_url()
        return {
            'id': place_common.place_main.id,
            'name': place_common.place_main.name,
            'photo_link': place_common.place_main.photo.full_url,
            'cuisine_types': PlaceCuisineTypesSerializer.serialize(place_common.place_cuisine_types, SER_PLACE_CUISINE_TYPES_GET_PLACES)
        }

    @staticmethod
    def _serialize_get_place_location_partial_detail(place_common: PlaceCommon) -> dict:
        place_common.place_main.photo.create_full_url()
        return {
            'place_location_id': place_common.place_location.id,
            'place_id': place_common.place_main.id,
            'photo_link': place_common.place_main.photo.full_url,
            'name': place_common.place_main.name,
            'place_types': [PlaceTypeSerializer.serialize(place_place_type.place_type, SER_PLACE_TYPE_SIMPLE) for place_place_type in place_common.place_places_types],
            'services': [ServiceSerializer.serialize(place_service.service, SER_SERVICE_SIMPLE) for place_service in place_common.place_services],
            'full_address': place_common.place_location.full_address,
            'contacts': PlaceContactsSerializer.serialize(place_common.place_contacts, SER_CONTACTS_SIMPLE)
        }
