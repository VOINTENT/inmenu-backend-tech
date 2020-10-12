from typing import List

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.place_location import PlaceLocation
from src.internal.biz.entities.service import Service

DES_PLACE_LOCATIONS_ADD = 'place-locations-add'


class PlaceLocationsDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_PLACE_LOCATIONS_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(place_locations: List[dict]) -> List[PlaceLocation]:
        return [
            PlaceLocation(
                full_address=place_location['full_address'],
                coords=(place_location['coords']['lat'], place_location['coords']['long'])
            ) for place_location in place_locations
        ]
