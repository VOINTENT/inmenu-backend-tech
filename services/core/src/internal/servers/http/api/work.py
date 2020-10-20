from sanic import Blueprint
from sanic.request import Request



from src.internal.biz.services.work_hours_service import WorkHoursService

from src.internal.servers.http.answers.place_types import get_response_get_place_types
from src.internal.servers.http.middlewares.request import get_pagination_params, get_lang_id

work_hours = Blueprint('work_hours', url_prefix='/work_hours')


@work_hours.route('', methods=['GET'])
async def get_work_hours(request: Request):
    work_hours, err = WorkHoursService.get_list_work_hours()
    if err:
        return err.get_response_with_error()

    return get_response_get_place_types(work_hours)
