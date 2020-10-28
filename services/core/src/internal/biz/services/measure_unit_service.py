from typing import List, Optional, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.measure_unit import MeasureUnitDao
from src.internal.biz.entities.measure_unit import MeasureUnit
from src.internal.biz.services.base_service import BaseService


class MeasureUnitService(BaseService):

    @staticmethod
    async def get_measure_units(pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[MeasureUnit]], Optional[Error]]:
        measure_units, error_measure_units = await MeasureUnitDao().get_measure_units(pagination_size,
                                                                                      pagination_after,
                                                                                      lang_id)
        if error_measure_units:
            return None, error_measure_units

        return measure_units, None
