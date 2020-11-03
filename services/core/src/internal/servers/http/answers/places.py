from typing import List

from sanic.response import json, HTTPResponse

from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.entities.place_location import PlaceLocation
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.serializers.place_common import PlaceCommonSerializer, SER_PLACE_COMMON_GET_PLACES, \
    SER_PLACE_COMMON_GET_PLACES_BY_NAME, SER_PLACE_COMMON_GET_PLACE_LOCATION_PARTIAL_DETAIL
from src.internal.biz.serializers.place_location import PlaceLocationSerializer, \
    SER_PLACE_LOCATION_GET_LOCATIONS_WITH_PLACES, SER_PLACE_LOCATION_GET_LOCATIONS_ON_MAP
from src.internal.biz.serializers.place_main import PlaceMainSerializer, SER_PLACE_MAIN_GET_MY, SER_PLACE_MAIN_DEL


def get_response_get_places(place_commons: List[PlaceCommon]) -> HTTPResponse:
    return json([PlaceCommonSerializer.serialize(place_common, SER_PLACE_COMMON_GET_PLACES) for place_common in place_commons], 200)


def get_response_get_places_by_name(place_commons: List[PlaceCommon]) -> HTTPResponse:
    return json([PlaceCommonSerializer.serialize(place_common, SER_PLACE_COMMON_GET_PLACES_BY_NAME) for place_common in place_commons], 200)


def get_response_get_locations_with_places(place_locations: List[PlaceLocation]) -> HTTPResponse:
    return json([PlaceLocationSerializer.serialize(place_location, SER_PLACE_LOCATION_GET_LOCATIONS_WITH_PLACES) for place_location in place_locations], 200)


def get_response_get_place_locations_on_map(place_locations: List[PlaceLocation]) -> HTTPResponse:
    return json([PlaceLocationSerializer.serialize(place_location, SER_PLACE_LOCATION_GET_LOCATIONS_ON_MAP) for place_location in place_locations], 200)


def get_response_get_place_location_partial_detail(place_common: PlaceCommon) -> HTTPResponse:
    return json(PlaceCommonSerializer.serialize(place_common, SER_PLACE_COMMON_GET_PLACE_LOCATION_PARTIAL_DETAIL), 200)


def get_response_get_my_places(place_mains: List[PlaceMain]) -> HTTPResponse:
    return json([PlaceMainSerializer.serialize(place_main, SER_PLACE_MAIN_GET_MY) for place_main in place_mains], 200)


def get_response_del_place(response: bool) -> HTTPResponse:
    return json(PlaceMainSerializer.serialize(response, SER_PLACE_MAIN_DEL), 200)
