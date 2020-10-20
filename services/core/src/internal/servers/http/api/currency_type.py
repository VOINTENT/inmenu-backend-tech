from sanic import Blueprint
from sanic.request import Request

from src.internal.biz.services.currency_type_service import CurrencyTypeService
from src.internal.biz.services.work_hours_service import WorkHoursService

from src.internal.servers.http.answers.place_types import get_response_get_place_types
from src.internal.servers.http.middlewares.request import get_pagination_params, get_lang_id

currency_types = Blueprint('currency_types', url_prefix='/currency_types')


@currency_types.route('', methods=['GET'])
@get_pagination_params
@get_lang_id
async def get_work_hours(request: Request, pagination_size, pagination_after, lang_id):
    currency_types, err = CurrencyTypeService.get_currency_types(pagination_size, pagination_after, lang_id)
    if err:
        return err.get_response_with_error()

    return get_response_get_place_types(currency_types)
