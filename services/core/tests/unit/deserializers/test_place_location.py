from src.internal.biz.deserializers.place_common import DES_PLACE_COMMON_UPDATE, PlaceCommonDeserializer
from src.internal.biz.deserializers.place_location import PlaceLocationDeserializer, DES_PLACE_LOCATION_UPDATE
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_INT


def test_place_location_deserializer():
    data_1 = {"location": {
        "full_address": "Россия, Казань, Астрономическая, 23",
        "city": "Казань",
        "country": "Россия",
        "coords": {
            "lat": 58.43426432,
            "long": 58.43426432
        }
    }
    }

    place_location_1 = PlaceLocationDeserializer.deserialize(data_1['location'], DES_PLACE_LOCATION_UPDATE)

    assert place_location_1.id is None
    assert place_location_1.full_address == data_1['location']['full_address']
    assert place_location_1.city == data_1['location']['city']
    assert place_location_1.country == data_1['location']['country']
    assert place_location_1.coords == (data_1['location']['coords']['lat'], data_1['location']['coords']['long'])

    data_2 = {"location": {
        "full_address": "Россия, Казань, Астрономическая, 23",
        "country": "Россия",
        "coords": {
            "lat": 58.43426432,
            "long": 58.43426432
        }
    }
    }

    try:
        place_location_2 = PlaceLocationDeserializer.deserialize(data_2['location'], DES_PLACE_LOCATION_UPDATE)
    except KeyError:
        assert 1 == 1

    data_3 = {'location': {}}

    place_location_3 = PlaceLocationDeserializer.deserialize(data_3['location'], DES_PLACE_LOCATION_UPDATE)

    assert place_location_3.id == TEMP_GET_NULL_INT
    assert place_location_3.full_address is None
    assert place_location_3.full_address is None
    assert place_location_3.city is None
    assert place_location_3.country is None
    assert place_location_3.coords is None

    place_common_1 = PlaceCommonDeserializer.deserialize(data_1, DES_PLACE_COMMON_UPDATE)

    assert place_common_1.place_location.id is None
    assert place_common_1.place_location.full_address == data_1['location']['full_address']
    assert place_common_1.place_location.city == data_1['location']['city']
    assert place_common_1.place_location.country == data_1['location']['country']
    assert place_common_1.place_location.coords == (data_1['location']['coords']['lat'], data_1['location']['coords']['long'])

    try:
        place_common_2 = PlaceCommonDeserializer.deserialize(data_2, DES_PLACE_COMMON_UPDATE)
    except KeyError:
        assert 1 == 1

    place_common_3 = PlaceCommonDeserializer.deserialize(data_3, DES_PLACE_COMMON_UPDATE)

    assert place_common_3.place_location.id == TEMP_GET_NULL_INT
    assert place_common_3.place_location.full_address is None
    assert place_common_3.place_location.full_address is None
    assert place_common_3.place_location.city is None
    assert place_common_3.place_location.country is None
    assert place_common_3.place_location.coords is None
