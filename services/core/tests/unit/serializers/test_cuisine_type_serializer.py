from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.serializers.cuisine_type import CuisineTypeSerializer, SER_CUISINE_TYPE


def test_cuisine_type_serializer():
    id = 1
    name = 'name'

    cuisine_type = CuisineType(
        id=id,
        name=name
    )

    data = CuisineTypeSerializer.serialize(cuisine_type, SER_CUISINE_TYPE)
    data_1 = {
        'id': id,
        'name': name
    }

    assert data == data_1
