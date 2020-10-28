from sanic import Blueprint
from sanic.request import Request

from src.internal.biz.services.cuisine_type_service import CuisineTypeService
from src.internal.servers.http.answers.cuisine_types import get_response_get_cuisine_types
from src.internal.servers.http.middlewares.request import get_pagination_params, get_lang_id

cuisine_types = Blueprint('cuisine_types', url_prefix='/cuisine_types')


@cuisine_types.route('', methods=['GET'])
@get_pagination_params
@get_lang_id
async def get_cuisine_types(request: Request, pagination_size: int, pagination_after: int, lang_id: int):
    cuisine_types, err = await CuisineTypeService.get_cuisine_types(pagination_size, pagination_after, lang_id)
    if err:
        return err.get_response_with_error()

    return get_response_get_cuisine_types(cuisine_types)
