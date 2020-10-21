from typing import re, List, Optional

from src.internal.biz.entities.measure_unit import MeasureUnit


def measure_unit_serializer(data: re) -> Optional[List[MeasureUnit]]:
    try:
        return [MeasureUnit(
            id=data[i]['measure_unit_id'],
            name=data[i]['measure_unit_name'],
            short_name=data[i]['measure_unit_short_name']
        )for i in range(len(data))]
    except:
        return [
            MeasureUnit(
                id=data[i]['measure_unit_id'],
                short_name=data[i]['measure_unit_short_name'])
            for i in range(len(data))
        ]
