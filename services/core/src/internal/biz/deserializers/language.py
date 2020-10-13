from typing import Union

from asyncpg.protocol.protocol import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.language import Language

DES_LANGUAGE_FROM_DB_FULL = 'des-language-from-db-full'

LANGUAGE = 'ln'
LANGUAGE_ID = LANGUAGE + ID
LANGUAGE_CREATED_AT = LANGUAGE + CREATED_AT
LANGUAGE_EDITED_AT = LANGUAGE + EDITED_AT
LANGUAGE_NAME = LANGUAGE + 'nm'
LANGUAGE_CODE_NAME = LANGUAGE + 'cd'


class LanguageDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_LANGUAGE_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(language: Union[dict, Record]) -> Language:
        return Language(
            id=language.get(LANGUAGE_ID),
            created_at=language.get(CREATED_AT),
            edited_at=language.get(EDITED_AT),
            name=language.get(LANGUAGE_NAME),
            code_name=language.get(LANGUAGE_CODE_NAME)
        )
