from http.client import HTTPResponse
from typing import List

from sanic.response import json

from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.serializers.measure_unit import MeasureUnitSerializer, SER_MEASURE_UNIT


def get_response_get_measure_units(measure_units: List[MeasureUnit]) -> HTTPResponse:
    return json([MeasureUnitSerializer.serialize(measure_unit, SER_MEASURE_UNIT) for measure_unit in measure_units], 200)
