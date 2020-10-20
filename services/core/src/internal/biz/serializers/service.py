from src.internal.biz.entities.service import Service
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_SERVICE_SIMPLE = 'service-simple'


class ServiceSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_SERVICE_SIMPLE:
            return cls._serialize_simple
        else:
            raise TypeError

    @staticmethod
    def _serialize_simple(service: Service) -> dict:
        return {
            'id': service.id,
            'name': service.name
        }
