from typing import List

from sanic.response import json

from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.serializers.place_common import PlaceCommonSerializer, SER_PLACE_COMMON_GET_PLACES


def get_response_get_places(place_commons: List[PlaceCommon]):
    return json([PlaceCommonSerializer.serialize(place_common, SER_PLACE_COMMON_GET_PLACES) for place_common in place_commons], 200)
