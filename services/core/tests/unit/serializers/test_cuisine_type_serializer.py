from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.serializers.entities_serializer.cuisine_type_serializer import cuisine_type_serializer


def test_cuisine_type_serializer():
    data = {
        'cuisine_type_id': 1,
        'cuisine_type_translate_name': 'name'
    }
    cuisine_type = cuisine_type_serializer(data)
    cuisine_type_1 = CuisineType(id=data['cuisine_type_id'],
                                 name=data['cuisine_type_translate_name'])
    assert isinstance(cuisine_type, CuisineType)
    assert isinstance(cuisine_type_1, CuisineType)

    assert cuisine_type.id == data['cuisine_type_id']
    assert cuisine_type.name == data['cuisine_type_translate_name']
