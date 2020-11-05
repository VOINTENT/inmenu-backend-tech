from src.internal.biz.deserializers.place_common import PlaceCommonDeserializer, DES_PLACE_COMMON_UPDATE
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_INT
from src.internal.biz.deserializers.place_types import DES_PLACE_TYPES_UPDATE, PlaceTypesDeserializer


def test_deserializer_update():
    data = {'place_types_ids': [1, 2, 3]}

    place_places_types = PlaceTypesDeserializer.deserialize(data['place_types_ids'], DES_PLACE_TYPES_UPDATE)
    assert place_places_types[0].place_type.id == data['place_types_ids'][0]
    assert place_places_types[1].place_type.id == data['place_types_ids'][1]
    assert place_places_types[2].place_type.id == data['place_types_ids'][2]

    data = {'place_types_ids': [-1]}
    place_places_types = PlaceTypesDeserializer.deserialize(data['place_types_ids'], DES_PLACE_TYPES_UPDATE)
    assert place_places_types[0].place_type.id == -1

    data = {}
    place_places_types = PlaceTypesDeserializer.deserialize(data, DES_PLACE_TYPES_UPDATE)

    assert place_places_types == []

