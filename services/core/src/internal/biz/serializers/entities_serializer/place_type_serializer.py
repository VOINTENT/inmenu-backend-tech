from src.internal.biz.entities.place_type import PlaceType


def place_type_serializer(dictionary: dict) -> PlaceType:
    try:
        return PlaceType(
            id=dictionary['place_type_id'],
            name=dictionary['place_type_name']
        )
    except:
        raise TypeError
