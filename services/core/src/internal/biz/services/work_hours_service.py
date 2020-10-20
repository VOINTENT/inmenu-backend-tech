from src.internal.biz.dao.work_hours_dao import WorkHoursDao
from src.internal.biz.services.base_service import BaseService


class WorkHoursService(BaseService):

    @staticmethod
    async def get_list_work_hours():
        work_hours, error_work_hours = WorkHoursDao().get_work_hours()
        if error_work_hours:
            return None, error_work_hours
        return work_hours, None
