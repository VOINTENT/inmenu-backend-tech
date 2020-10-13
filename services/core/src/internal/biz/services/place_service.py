from typing import Optional, Tuple, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.place_common import PlaceCommonDao
from src.internal.biz.dao.place_cuisine_type_dao import PlaceCuisineTypeDao
from src.internal.biz.dao.place_main_dao import PlaceMainDao
from src.internal.biz.entities.place_common import PlaceCommon
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.services.base_service import BaseService


class PlaceService(BaseService):

    @staticmethod
    async def add_place(place_common: PlaceCommon) -> Tuple[Optional[PlaceCommon], Optional[Error]]:
        place_common, err = await PlaceCommonDao().add(place_common)
        if err:
            return None, err

        return place_common, None

    @classmethod
    async def get_all_places(cls, city_name: Optional[str], pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[PlaceCommon]], Optional[Error]]:
        place_mains, err = await PlaceMainDao().get_all_places(city_name, pagination_size, pagination_after)
        if err:
            return None, err

        place_commons, err = await cls._get_place_commons_with_place_cuisine_types_by_place_mains(place_mains, lang_id)
        if err:
            return None, err

        return place_commons, None

    @classmethod
    async def get_places_by_name(cls, city_name: Optional[str], place_name: str, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[PlaceCommon]], Optional[Error]]:
        place_mains, err = await PlaceMainDao().get_places_by_name(city_name, place_name, pagination_size, pagination_after)
        if err:
            return None, err

        place_commons, err = await cls._get_place_commons_with_place_cuisine_types_by_place_mains(place_mains, lang_id)
        if err:
            return None, err

        return place_commons, None

    @staticmethod
    def _get_place_commons_by_place_main_and_place_cuisine_types(place_mains: List[PlaceMain], place_cuisine_types) -> List[PlaceCommon]:
        return [PlaceCommon(
            place_main=place_main,
            place_cuisine_types=[place_cuisine_type
                                 for place_cuisine_type in place_cuisine_types if
                                 place_cuisine_type.place_main.id == place_main.id])
                for place_main in place_mains]

    @classmethod
    async def _get_place_commons_with_place_cuisine_types_by_place_mains(cls, place_mains: List[PlaceMain], lang_id: int) -> Tuple[Optional[List[PlaceCommon]], Optional[Error]]:
        place_main_ids = [place_main.id for place_main in place_mains]

        place_cuisine_types, err = await PlaceCuisineTypeDao().get_by_main_ids(place_main_ids, lang_id)
        if err:
            return None, err

        place_commons = cls._get_place_commons_by_place_main_and_place_cuisine_types(place_mains, place_cuisine_types)

        return place_commons, None
