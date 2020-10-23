from src.internal.biz.entities.service import Service
from src.internal.biz.serializers.entities_serializer.service_serializer import service_serializer


def test_service_serializer():
    data = {
        'service_id': 1,
        'service_name': 'name'
    }
    service = Service(
        id=data['service_id'],
        name=data['service_name']
    )

    service_1 = service_serializer(data)

    assert isinstance(service, Service)
    assert isinstance(service_1, Service)

    assert service.id == service_1.id
    assert service.name == service_1.name
