from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.serializers.base_serializer import BaseSerializer

SER_MEASURE_UNIT = 'ser_measure_unit'


class MeasureUnitSerializer(BaseSerializer):
    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_MEASURE_UNIT:
            return cls._serialize_get_measure_units
        else:
            raise TypeError

    @staticmethod
    def _serialize_get_measure_units(measure_unit: MeasureUnit) -> dict:
        return {
            'id': measure_unit.id,
            'name': measure_unit.name,
            'short_name': measure_unit.short_name
        }
