from sanic import Blueprint
from sanic.request import Request


from src.internal.biz.services.services_service import ServicesService

from src.internal.servers.http.answers.place_types import get_response_get_place_types
from src.internal.servers.http.answers.service import get_response_get_services
from src.internal.servers.http.middlewares.request import get_pagination_params, get_lang_id

services = Blueprint('services', url_prefix='/services')


@services.route('', methods=['GET'])
@get_pagination_params
@get_lang_id
async def get_services(request: Request, pagination_size: int, pagination_after: int, lang_id: int):
    services, err = await ServicesService.get_services(pagination_size, pagination_after, lang_id)
    if err:
        return err.get_response_with_error()

    return get_response_get_services(services)
