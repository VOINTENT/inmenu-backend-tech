from typing import List

from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.place_service import PlaceService
from src.internal.biz.entities.service import Service

DES_SERVICES_ADD = 'services-add'


class ServicesDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_SERVICES_ADD:
            return cls._deserialize_add
        else:
            raise TypeError

    @staticmethod
    def _deserialize_add(services: List[int]) -> List[PlaceService]:
        return [PlaceService(service=Service(id=service_type_id)) for service_type_id in services]
