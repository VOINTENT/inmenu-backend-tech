from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.serializers.entities_serializer.measure_unit_serializer import measure_unit_serializer


def test_measure_unit_serializer():
    data = {
        'measure_unit_id': 1,
        'measure_unit_name': 'name',
        'measure_unit_short_name': 'short_name',
    }

    data_1 = {
        'measure_unit_id': 1,
        'measure_unit_short_name' : 'short_name',
    }

    measure_unit = MeasureUnit(
        id=data['measure_unit_id'],
        name=data['measure_unit_name'],
        short_name=data['measure_unit_short_name']
    )
    measure_unit_1 = MeasureUnit(
        id=data_1['measure_unit_id'],
        short_name=data_1['measure_unit_short_name']
    )

    measure_unit_2 = measure_unit_serializer(data)
    measure_unit_3 = measure_unit_serializer(data_1)

    assert isinstance(measure_unit, MeasureUnit)
    assert isinstance(measure_unit_1, MeasureUnit)
    assert isinstance(measure_unit_2, MeasureUnit)
    assert isinstance(measure_unit_3, MeasureUnit)

    assert measure_unit.id == measure_unit_2.id
    assert measure_unit.name == measure_unit_2.name
    assert measure_unit.short_name == measure_unit_2.short_name

    assert measure_unit_1.id == measure_unit_3.id
    assert measure_unit_1.name is None
    assert measure_unit_3.name is None
    assert measure_unit_1.short_name == measure_unit_3.short_name
