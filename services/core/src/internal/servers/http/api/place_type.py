from sanic import Blueprint
from sanic.request import Request


from src.internal.biz.services.place_type_service import PlaceTypeService

from src.internal.servers.http.answers.place_types import get_response_get_place_types
from src.internal.servers.http.middlewares.request import get_pagination_params, get_lang_id

place_types = Blueprint('place_types', url_prefix='/place_types')


@place_types.route('/', methods=['GET'])
@get_pagination_params
@get_lang_id
async def get_place_types(request: Request, pagination_size: int, pagination_after: int, lang_id: int):
    place_type, err = await PlaceTypeService.get_all_place_types(pagination_size, pagination_after, lang_id)
    if err:
        return err.get_response_with_error()

    return get_response_get_place_types(place_type)

