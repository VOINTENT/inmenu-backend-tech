from http.client import HTTPResponse
from typing import List

from sanic.response import json

from src.internal.biz.entities.service import Service
from src.internal.biz.serializers.service import ServiceSerializer, SER_SERVICE_SIMPLE


def get_response_get_services(services: List[Service]) -> HTTPResponse:
    return json([ServiceSerializer.serialize(service, SER_SERVICE_SIMPLE) for service in services], 200)
