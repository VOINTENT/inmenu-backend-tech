from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.service import Service

DES_SERVICE_FROM_DB_FULL = 'service-from-db-full'

SERVICE = 'srv_'
SERVICE_ID = SERVICE + ID
SERVICE_CREATED_AT = SERVICE + CREATED_AT
SERVICE_EDITED_AT = SERVICE + EDITED_AT
SERVICE_NAME = SERVICE + 'nm'


class ServiceDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_SERVICE_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(service: Union[dict, Record]) -> Service:
        return Service(
            id=service.get(SERVICE_ID),
            created_at=service.get(SERVICE_CREATED_AT),
            edited_at=service.get(SERVICE_EDITED_AT),
            name=service.get(SERVICE_NAME)
        )
