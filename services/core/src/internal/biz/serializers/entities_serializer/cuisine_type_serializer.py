from typing import Optional, List

from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.serializers.base_serializer import BaseSerializer


def cuisine_type_serializer(dictionary: dict) -> Optional[CuisineType]:
    try:
        return CuisineType(
            id=dictionary['cuisine_type_id'],
            name=dictionary['cuisine_type_translate_name'])
    except:
        raise TypeError
