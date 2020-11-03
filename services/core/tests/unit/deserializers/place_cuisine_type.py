from src.internal.biz.deserializers.cuisine_types import CuisineTypesDeserializer, DES_CUISINE_TYPES_UPDATE
from src.internal.biz.deserializers.place_main import TEMP_GET_NULL_INT


def test_cuisine_type_deserializer_update():
    data = {'cuisine_types_ids': [1, 2, 3]}
    place_cuisine_type = CuisineTypesDeserializer.deserialize(data['cuisine_types_ids'], DES_CUISINE_TYPES_UPDATE)

    assert place_cuisine_type[0].cuisine_type.id == data['cuisine_types_ids'][0]
    assert place_cuisine_type[1].cuisine_type.id == data['cuisine_types_ids'][1]
    assert place_cuisine_type[2].cuisine_type.id == data['cuisine_types_ids'][2]

    data = {'cuisine_types_ids': [-1]}
    place_cuisine_type = CuisineTypesDeserializer.deserialize(data['cuisine_types_ids'], DES_CUISINE_TYPES_UPDATE)

    assert place_cuisine_type[0].cuisine_type.id == TEMP_GET_NULL_INT
