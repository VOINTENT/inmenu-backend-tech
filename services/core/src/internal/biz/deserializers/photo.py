from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.photo import Photo


DES_PHOTO_FROM_DB_FULL = 'photo-from-db-full'

PHOTO = 'ph_'
PHOTO_ID = PHOTO + ID
PHOTO_CREATED_AT = PHOTO + CREATED_AT
PHOTO_EDITED_AT = PHOTO + EDITED_AT
PHOTO_SHORT_URL = PHOTO + 'sh'


class PhotoDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_PHOTO_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(photo: Union[dict, Record]) -> Photo:
        return Photo(
            id=photo.get(PHOTO_ID),
            created_at=photo.get(PHOTO_CREATED_AT),
            edited_at=photo.get(PHOTO_EDITED_AT),
            short_url=photo.get(PHOTO_SHORT_URL)
        )
