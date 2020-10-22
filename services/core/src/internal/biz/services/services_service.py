from typing import List, Optional, Tuple

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.services_dao import ServicesDao
from src.internal.biz.entities.service import Service
from src.internal.biz.services.base_service import BaseService


class ServicesService(BaseService):

    @staticmethod
    async def get_services(pagination_size: int, pagination_after: int, lang_id: int) -> Tuple[Optional[List[Service]], Optional[Error]]:
        services, error_services = await ServicesDao().get_service(pagination_size, pagination_after, lang_id)

        if error_services:
            return None, error_services

        return services, None
