from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.place_main import PLACE_MAIN, PlaceMainDeserializer, DES_PLACE_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.place_type_deserializer import PLACE_TYPE, PlaceTypeDeserializer, \
    DES_PLACE_TYPE_FROM_DB_FULL
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.place_place_type import PlacePlaceType

DES_PLACE_PLACE_TYPE_FROM_DB_FULL = 'place-place-type-from-db-full'

PLACE_PLACE_TYPE = 'ppt_'
PLACE_PLACE_TYPE_ID = PLACE_PLACE_TYPE + ID
PLACE_PLACE_TYPE_CREATED_AT = PLACE_PLACE_TYPE + CREATED_AT
PLACE_PLACE_TYPE_EDITED_AT = PLACE_PLACE_TYPE + EDITED_AT


class PlacePlaceTypeDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_PLACE_PLACE_TYPE_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(place_place_type: Union[dict, Record]) -> PlacePlaceType:
        place_main = filter_keys_by_substr(place_place_type, PLACE_MAIN)
        place_type = filter_keys_by_substr(place_place_type, PLACE_TYPE)
        return PlacePlaceType(
            place_main=PlaceMainDeserializer.deserialize(place_main, DES_PLACE_MAIN_FROM_DB_FULL),
            place_type=PlaceTypeDeserializer.deserialize(place_type, DES_PLACE_TYPE_FROM_DB_FULL)
        )
