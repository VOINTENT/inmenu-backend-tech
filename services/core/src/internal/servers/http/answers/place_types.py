from typing import List

from sanic.response import HTTPResponse, json

from src.internal.biz.entities.place_type import PlaceType
from src.internal.biz.serializers.place_type import PlaceTypeSerializer, SER_PLACE_TYPE_SIMPLE


def get_response_get_place_types(place_types: List[PlaceType]) -> HTTPResponse:
    return json([PlaceTypeSerializer.serialize(place_type, SER_PLACE_TYPE_SIMPLE) for place_type in place_types], 200)
