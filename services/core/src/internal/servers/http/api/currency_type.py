from sanic import Blueprint
from sanic.request import Request

from src.internal.biz.services.currency_type_service import CurrencyTypeService
from src.internal.servers.http.answers.currency_types import get_response_get_currency_types

from src.internal.servers.http.middlewares.request import get_pagination_params, get_lang_id

currency_types = Blueprint('currencies', url_prefix='/currencies')


@currency_types.route('', methods=['GET'])
@get_pagination_params
@get_lang_id
async def get_currency_types(request: Request, pagination_size: int, pagination_after: int, lang_id: int):
    currency_types, err = await CurrencyTypeService.get_currency_types(pagination_size, pagination_after, lang_id)
    if err:
        return err.get_response_with_error()

    return get_response_get_currency_types(currency_types)
