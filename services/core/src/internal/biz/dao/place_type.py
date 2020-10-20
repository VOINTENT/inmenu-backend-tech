from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.base_dao import BaseDao


class PlaceTypeDao(BaseDao):

    async def get_all(self, pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[object]], Optional[Error]]:
        pass
