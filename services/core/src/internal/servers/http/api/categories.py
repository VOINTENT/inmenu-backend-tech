from requests import Request
from sanic import Blueprint
from sanic.response import json

from src.internal.adapters.entities.utils import get_response_with_validation_errors
from src.internal.biz.deserializers.menu_category import MenuCategoryDeserializer, DES_MENU_CATEGORY_ADD
from src.internal.biz.services.menu import MenuService
from src.internal.biz.validators.menu_category_add import MenuCategoryAddSchema
from src.internal.servers.http.answers.categories import get_response_get_menus_by_menu_main_id
from src.internal.servers.http.middlewares.auth import required_auth
from src.internal.servers.http.middlewares.log import log_request

categories = Blueprint('categories', url_prefix='/categories')


@categories.route('', methods=['POST'])
@log_request
@required_auth
async def add_category(request: Request, auth_account_main_id: int):
    errors = MenuCategoryAddSchema().validate(request.json)
    if errors:
        return get_response_with_validation_errors(errors)

    menu_category = MenuCategoryDeserializer.deserialize(request.json, DES_MENU_CATEGORY_ADD)
    menu_category, err = await MenuService.add_menu_category(menu_category, auth_account_main_id)
    if err:
        return err.get_response_with_error()

    return json({'id': menu_category.id})


@categories.route('/menus/<menu_main_id:int>')
@log_request
async def get_menus_by_menu_main_id(request: Request, menu_main_id: int):
    menu_categories, err = await MenuService.get_menu_categories_by_menu_category_id(menu_main_id)
    if err:
        return err.get_response_with_error()

    return get_response_get_menus_by_menu_main_id(menu_categories)
