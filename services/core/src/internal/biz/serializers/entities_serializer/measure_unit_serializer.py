from typing import re, List, Optional

from src.internal.biz.entities.measure_unit import MeasureUnit


def measure_unit_serializer(dictionary: dict) -> Optional[MeasureUnit]:
    try:
        return MeasureUnit(
            id=dictionary['measure_unit_id'],
            name=dictionary['measure_unit_name'],
            short_name=dictionary['measure_unit_short_name'])
    except:
        return MeasureUnit(
                id=dictionary['measure_unit_id'],
                short_name=dictionary['measure_unit_short_name'])
