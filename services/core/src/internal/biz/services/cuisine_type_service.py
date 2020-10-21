from typing import Optional, List, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.cuisine_type_dao import CuisineTypeDao
from src.internal.biz.entities.cuisine_type import CuisineType
from src.internal.biz.services.base_service import BaseService


class CuisineTypeService(BaseService):

    @staticmethod
    async def get_cuisine_types(pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[CuisineType]], Optional[Error]]:
        cuisine_types, error_cuisine_types = await CuisineTypeDao().get_list_cuisine_type(pagination_size,
                                                                                          pagination_after,
                                                                                          lang_id)
        if error_cuisine_types:
            return None, error_cuisine_types
        return cuisine_types, None
