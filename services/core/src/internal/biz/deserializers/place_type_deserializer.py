from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.place_type import PlaceType

DES_PLACE_TYPE_FROM_DB_FULL = 'place-type-from-db-full'

PLACE_TYPE = 'pltp_'
PLACE_TYPE_ID = PLACE_TYPE + ID
PLACE_TYPE_CREATED_AT = PLACE_TYPE + CREATED_AT
PLACE_TYPE_EDITED_AT = PLACE_TYPE + EDITED_AT
PLACE_TYPE_NAME = PLACE_TYPE + 'nm'


class PlaceTypeDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_PLACE_TYPE_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(place_type: Union[dict, Record]) -> PlaceType:
        return PlaceType(
            id=place_type.get(PLACE_TYPE_ID),
            created_at=place_type.get(PLACE_TYPE_CREATED_AT),
            edited_at=place_type.get(PLACE_TYPE_EDITED_AT),
            name=place_type.get(PLACE_TYPE_NAME)
        )
