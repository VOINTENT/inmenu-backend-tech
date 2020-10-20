from typing import Tuple, Optional, List

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.language import LanguageDao
from src.internal.biz.entities.language import Language
from src.internal.biz.services.base_service import BaseService


class LanguageService(BaseService):

    @staticmethod
    async def get_all_languages(pagination_size: int, pagination_after: int) -> Tuple[Optional[List[Language]], Optional[Error]]:
        languages, err = await LanguageDao().get_all(pagination_size, pagination_after)
        if err:
            return None, err

        return languages, None
