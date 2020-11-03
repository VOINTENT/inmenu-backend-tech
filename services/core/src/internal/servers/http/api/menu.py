from sanic import Blueprint
from sanic.request import Request
from sanic.response import json

from src.internal.adapters.entities.utils import get_response_with_validation_errors

from src.internal.biz.deserializers.menu_main import DES_MENU_ADD, MenuMainDeserializer

from src.internal.biz.services.menu import MenuService
from src.internal.biz.validators.menu_add import MenuAddSchema
from src.internal.servers.http.answers.menu import get_response_get_menu_mains_by_place_main_id
from src.internal.servers.http.middlewares.auth import required_auth
from src.internal.servers.http.middlewares.log import log_request
from src.internal.servers.http.middlewares.request import get_pagination_params

menu = Blueprint('menu', url_prefix='/menu')


@menu.route('', methods=['POST'])
@log_request
@required_auth
async def add_menu(request: Request, auth_account_main_id: int):
    errors = MenuAddSchema().validate(request.json)
    if errors:
        return get_response_with_validation_errors(errors)

    menu_main = MenuMainDeserializer.deserialize(request.json, DES_MENU_ADD)
    menu_main, err = await MenuService.add_menu(menu_main, auth_account_main_id)
    if err:
        return err.get_response_with_error()

    return json({'id': menu_main.id})


@menu.route('/places/<place_main_id:int>', methods=['GET'])
@get_pagination_params
async def get_menu_mains_by_place_main_id(request: Request, place_main_id: int, pagination_size: int,
                                          pagination_after: int):
    menu_mains, err = await MenuService.get_menu_mains_by_place_main_id(place_main_id, pagination_size,
                                                                        pagination_after)
    if err:
        return err.get_response_with_error()

    return get_response_get_menu_mains_by_place_main_id(menu_mains)
