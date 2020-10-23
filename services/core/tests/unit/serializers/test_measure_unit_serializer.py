from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.serializers.measure_unit import MeasureUnitSerializer, SER_MEASURE_UNIT


def test_measure_unit_serializer():
    id = 1
    name = 'name'
    short_name = 'short_name'
    measure_unit = MeasureUnit(
        id=id,
        name=name,
        short_name=short_name
    )

    data = MeasureUnitSerializer.serialize(measure_unit, SER_MEASURE_UNIT)
    data_1 = {
        'id': id,
        'name': name,
        'short_name': short_name
    }
    assert data == data_1
