from typing import Optional

from src.internal.biz.dao.place_common import PlaceCommonDao
from src.internal.biz.dao.place_cuisine_type_dao import PlaceCuisineTypeDao
from src.internal.biz.dao.place_main_dao import PlaceMainDao
from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.services.base_service import BaseService


class PlaceService(BaseService):

    @staticmethod
    async def add_place(place_common: PlaceCommon):
        place_common, err = await PlaceCommonDao().add(place_common)
        if err:
            return None, err

        return place_common, None

    @staticmethod
    async def get_all_places(city_name: Optional[str], pagination_size: Optional[int], pagination_after: Optional[int], lang_id: Optional[int]):
        place_mains, err = await PlaceMainDao().get_all_places(city_name, pagination_size, pagination_after)
        if err:
            return None, err

        place_main_ids = [place_main.id for place_main in place_mains]

        place_cuisine_types, err = await PlaceCuisineTypeDao().get_by_ids(place_main_ids, lang_id)
        if err:
            return None, err

        place_commons = [PlaceCommon(place_main=place_main,
                                     place_cuisine_types=[place_cuisine_type
                                                          for place_cuisine_type in place_cuisine_types if place_cuisine_type.place_main.id == place_main.id])
                         for place_main in place_mains]

        return place_commons, None
