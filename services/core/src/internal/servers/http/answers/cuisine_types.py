from http.client import HTTPResponse
from typing import List

from sanic.response import json

from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.serializers.cuisine_type import CuisineTypeSerializer, SER_CUISINE_TYPE


def get_response_get_cuisine_types(cuisine_types: List[CuisineType]) -> HTTPResponse:
    return json([CuisineTypeSerializer.serialize(cuisine_type, SER_CUISINE_TYPE) for cuisine_type in cuisine_types], 200)
