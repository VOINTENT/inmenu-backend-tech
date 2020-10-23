from src.internal.biz.entities.service import Service
from src.internal.biz.serializers.service import ServiceSerializer, SER_SERVICE_SIMPLE


def test_service_serializer():
    id = 1
    name = 'name'
    serivce = Service(
        id=id,
        name=name
    )

    data = ServiceSerializer.serialize(serivce, SER_SERVICE_SIMPLE)
    data_1 = {
        'id': id,
        'name': name
    }

    assert data_1 == data
