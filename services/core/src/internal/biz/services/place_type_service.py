from src.internal.biz.dao.place_type import PlaceTypeDao
from src.internal.biz.services.base_service import BaseService


class PlaceTypeService(BaseService):

    @staticmethod
    async def get_all_place_types(pagination_size: int, pagination_after: int, lang_id: int):
        place_types, error_place_types = await PlaceTypeDao().get_all(pagination_size,
                                                                      pagination_after,
                                                                      lang_id)
        if error_place_types:
            return None, error_place_types

        return place_types, None
