from sanic import Blueprint
from sanic.request import Request

from src.internal.biz.services.currency_type_service import CurrencyTypeService
from src.internal.biz.services.measure_unit_service import MeasureUnitService
from src.internal.servers.http.answers.currency_types import get_response_get_currency_types
from src.internal.servers.http.answers.measure_unit import get_response_get_measure_units

from src.internal.servers.http.middlewares.request import get_pagination_params, get_lang_id

measure_units = Blueprint('measure_units', url_prefix='/measure_units')


@measure_units.route('', methods=['GET'])
@get_pagination_params
@get_lang_id
async def get_measure_units(request: Request, pagination_size: int, pagination_after: int, lang_id: int):
    measure_units, err = await MeasureUnitService.get_measure_units(pagination_size, pagination_after, lang_id)
    if err:
        return err.get_response_with_error()

    return get_response_get_measure_units(measure_units)
