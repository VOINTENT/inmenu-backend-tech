from requests import Request
from sanic import Blueprint
from sanic.response import json

from src.internal.adapters.entities.utils import get_response_with_validation_errors
from src.internal.biz.deserializers.menu_category import MenuCategoryDeserializer, DES_MENU_CATEGORY_ADD
from src.internal.biz.services.menu import MenuService
from src.internal.biz.validators.menu_category_add import MenuCategoryAddSchema
from src.internal.servers.http.middlewares.auth import required_auth_with_confirmed_email

categories = Blueprint('categories', url_prefix='/categories')


@categories.route('', methods=['POST'])
@required_auth_with_confirmed_email
async def add_category(request: Request, auth_account_main_id: int):
    errors = MenuCategoryAddSchema().validate(request.json)
    if errors:
        return get_response_with_validation_errors(errors)

    menu_category = MenuCategoryDeserializer.deserialize(request.json, DES_MENU_CATEGORY_ADD)
    menu_category, err = await MenuService.add_menu_category(menu_category, auth_account_main_id)
    if err:
        return err.get_response_with_error()

    return json({'id': menu_category.id})
