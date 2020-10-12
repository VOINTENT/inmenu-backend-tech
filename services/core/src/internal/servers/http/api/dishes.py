from sanic import Blueprint
from sanic.request import Request
from sanic.response import json

from src.internal.adapters.entities.utils import get_response_with_validation_errors
from src.internal.biz.deserializers.dish_common_deserializer import DishCommonDeserializer, DES_DISH_COMMON_ADD
from src.internal.biz.services.menu import MenuService
from src.internal.biz.validators.dish_add import DishCommonAddSchema
from src.internal.servers.http.middlewares.auth import required_auth_with_confirmed_email

dishes = Blueprint('dishes', url_prefix='/dishes')


@dishes.route('', methods=['POST'])
@required_auth_with_confirmed_email
async def add_dish(request: Request, auth_account_main_id: int):
    errors = DishCommonAddSchema().validate(request.json)
    if errors:
        return get_response_with_validation_errors(errors)

    dish_common = DishCommonDeserializer.deserialize(request.json, DES_DISH_COMMON_ADD)
    dish_common, err = await MenuService.add_dish(dish_common, auth_account_main_id)
    if err:
        return err.get_response_with_error()

    return json({'id': dish_common.dish_main.id})
