from typing import List

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.entities.place_cuisine_type import PlaceCuisineType

DES_CUISINE_TYPES_ADD = 'cuisine_types_add'


class CuisineTypesDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_CUISINE_TYPES_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(cuisine_types: List[int]) -> List[PlaceCuisineType]:
        return [PlaceCuisineType(cuisine_type=CuisineType(id=cuisine_type_id)) for cuisine_type_id in cuisine_types]
