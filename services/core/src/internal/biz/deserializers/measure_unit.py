from typing import Union

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.entities.measure_unit import MeasureUnit

DES_MEASURE_UNIT_FROM_DB_FULL = 'measure-unit-from-db-full'

MEASURE_UNIT = 'mu_'
MEASURE_UNIT_ID = MEASURE_UNIT + ID
MEASURE_UNIT_CREATED_AT = MEASURE_UNIT + CREATED_AT
MEASURE_UNIT_EDITED_AT = MEASURE_UNIT + EDITED_AT
MEASURE_UNIT_NAME = MEASURE_UNIT + 'nm'
MEASURE_UNIT_SHORT_NAME = MEASURE_UNIT + 'sn'


class MeasureUnitDeserializer(BaseDeserializer):
    @classmethod
    def _get_deserializer(cls, format_des: str):
        if format_des == DES_MEASURE_UNIT_FROM_DB_FULL:
            return cls._deserialize_from_db_full
        else:
            raise TypeError

    @staticmethod
    def _deserialize_from_db_full(measure_unit: Union[dict, Record]) -> MeasureUnit:
        return MeasureUnit(
            id=measure_unit.get(MEASURE_UNIT_ID),
            created_at=measure_unit.get(MEASURE_UNIT_CREATED_AT),
            edited_at=measure_unit.get(MEASURE_UNIT_EDITED_AT),
            name=measure_unit.get(MEASURE_UNIT_NAME),
            short_name=measure_unit.get(MEASURE_UNIT_SHORT_NAME)
        )
