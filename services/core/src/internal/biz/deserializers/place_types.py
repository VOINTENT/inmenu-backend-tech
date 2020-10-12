from typing import List

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.place_place_type import PlacePlaceType
from src.internal.biz.entities.place_type import PlaceType

DES_PLACE_TYPES_ADD = 'place-types-add'


class PlaceTypesDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_PLACE_TYPES_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(place_types: List[int]) -> List[PlacePlaceType]:
        return [PlacePlaceType(place_type=PlaceType(id=place_type_id)) for place_type_id in place_types]
