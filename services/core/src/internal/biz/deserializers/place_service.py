from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.place_main import PlaceMainDeserializer, PLACE_MAIN, DES_PLACE_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.service import SERVICE, ServiceDeserializer, DES_SERVICE_FROM_DB_FULL
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.place_service import PlaceService

DES_PLACE_SERVICE_FROM_DB_FULL = 'place-service-from-db-full'

PLACE_SERVICE = 'plsrv_'


class PlaceServiceDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_PLACE_SERVICE_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(place_service: Union[dict, Record]) -> PlaceService:
        place_main = filter_keys_by_substr(place_service, PLACE_MAIN)
        service = filter_keys_by_substr(place_service, SERVICE)
        return PlaceService(
            place_main=PlaceMainDeserializer.deserialize(place_main, DES_PLACE_MAIN_FROM_DB_FULL),
            service=ServiceDeserializer.deserialize(service, DES_SERVICE_FROM_DB_FULL)
        )
