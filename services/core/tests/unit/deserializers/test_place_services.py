from src.internal.biz.deserializers.place_common import PlaceCommonDeserializer, DES_PLACE_COMMON_UPDATE
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_INT
from src.internal.biz.deserializers.services import ServicesDeserializer, DES_SERVICES_UPDATE


def test_place_service_deserializer_update():
    data = {
        'services_ids': [1, 2, 3]
    }
    place_service = ServicesDeserializer.deserialize(data['services_ids'], DES_SERVICES_UPDATE)
    assert place_service[0].service.id == data['services_ids'][0]
    assert place_service[1].service.id == data['services_ids'][1]
    assert place_service[2].service.id == data['services_ids'][2]

    data = {'services_ids': [-1]}
    place_service = ServicesDeserializer.deserialize(data['services_ids'], DES_SERVICES_UPDATE)
    assert place_service[0].service.id == -1

    data = {}
    place_service = ServicesDeserializer.deserialize(data, DES_SERVICES_UPDATE)

    assert place_service == []

    data = {'services_ids': [1, 2, 3]}
    place_common = PlaceCommonDeserializer.deserialize(data, DES_PLACE_COMMON_UPDATE)

    assert place_common.place_services[0].service.id == data['services_ids'][0]
    assert place_common.place_services[1].service.id == data['services_ids'][1]
    assert place_common.place_services[2].service.id == data['services_ids'][2]

    data_1 = {'services_ids': None}
    data_2 = {'services_ids': []}
    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)
    place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)

    assert place_common_1.place_services[0].service.id == TEMP_GET_NULL_INT
    assert place_common_2.place_services[0].service.id == TEMP_GET_NULL_INT

    data_3 = {}
    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)

    assert place_common_3.place_services is None
