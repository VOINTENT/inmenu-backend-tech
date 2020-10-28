from src.internal.biz.entities.place_type import PlaceType
from src.internal.biz.serializers.entities_serializer.place_type_serializer import place_type_serializer


def test_place_type_serializer():
    data = {
        'place_type_id': 1,
        'place_type_name': 'name'
    }
    place_type = PlaceType(
        id=data['place_type_id'],
        name=data['place_type_name']
    )

    place_type_1 = place_type_serializer(data)

    assert isinstance(place_type, PlaceType)
    assert isinstance(place_type_1, PlaceType)

    assert place_type.id == place_type_1.id
    assert place_type.name == place_type_1.name
