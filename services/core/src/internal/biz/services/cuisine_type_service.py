from src.internal.biz.dao.cuisine_type_dao import CuisineTypeDao
from src.internal.biz.services.base_service import BaseService


class CuisineTypeService(BaseService):

    async def get_cuisine_types(self, pagination_size: int, pagination_after: int, lang_id: int):
        cuisine_types, error_cuisine_types = CuisineTypeDao.get_list_cuisine_type(pagination_size, pagination_after, lang_id)
        if error_cuisine_types:
            return None, error_cuisine_types
        return cuisine_types, None
