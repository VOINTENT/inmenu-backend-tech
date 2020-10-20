from sanic import Blueprint
from sanic.request import Request
from sanic.response import json

from src.internal.adapters.entities.utils import get_response_with_validation_errors
from src.internal.biz.deserializers.account_main import AccountMainDeserializer
from src.internal.biz.deserializers.base_deserializer import DES_FROM_DICT
from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.auth_code import AuthCode
from src.internal.biz.services.account_service import AccountService
from src.internal.biz.services.auth_service import AuthService
from src.internal.biz.validators.auth_gmail import AuthGmailSchema
from src.internal.biz.validators.confirm_code import ConfirmCodeSchema
from src.internal.biz.validators.register import RegisterAuthSchema
from src.internal.servers.http.answers.accounts import get_response_register, get_response_auth, get_response_detail
from src.internal.servers.http.middlewares.auth import required_auth, required_auth_with_unconfirmed_email
from src.internal.servers.http.middlewares.log import log_request

accounts = Blueprint('accounts', url_prefix='/accounts')


@accounts.route('/register', methods=['POST'])
@log_request
async def register(request: Request):
    mistakes = RegisterAuthSchema().validate(request.json)
    if mistakes:
        return get_response_with_validation_errors(mistakes)

    account_main = AccountMainDeserializer.deserialize(request.json, DES_FROM_DICT)
    account_main, err = await AuthService.register(account_main)
    if err:
        return err.get_response_with_error()

    return get_response_register(account_main)


@accounts.route('/auth/basic', methods=['POST'])
@log_request
async def auth_basic(request: Request):
    mistakes = RegisterAuthSchema().validate(request.json)
    if mistakes:
        return get_response_with_validation_errors(mistakes)

    account_main = AccountMainDeserializer.deserialize(request.json, DES_FROM_DICT)
    account_main, err = await AuthService.auth_basic(account_main)
    if err:
        return err.get_response_with_error()

    return get_response_auth(account_main)


@accounts.route('/auth/code', methods=['POST'])
@log_request
@required_auth
async def confirm_code(request: Request, auth_account_main_id: int):
    mistakes = ConfirmCodeSchema().validate(request.json)
    if mistakes:
        return get_response_with_validation_errors(mistakes)

    auth_code = AuthCode(account_main=AccountMain(id=auth_account_main_id), code=request.json.get('code'))
    _, err = await AuthService.confirm_code(auth_code)
    if err:
        return err.get_response_with_error()

    return json(True)


@accounts.route('/auth/new_code', methods=['POST'])
@log_request
@required_auth_with_unconfirmed_email
async def send_new_code(request: Request, auth_account_main_id: int):
    _, err = await AuthService.send_new_auth_code(auth_account_main_id)
    if err:
        return err.get_response_with_error()

    return json(True)


@accounts.route('/detail', methods=['GET'])
@log_request
@required_auth
async def get_detail_info(request: Request, auth_account_main_id: int):
    account_main, err = await AccountService.get_detail_account_info(auth_account_main_id)
    if err:
        return err.get_response_with_error()

    return get_response_detail(account_main)


@accounts.route('/auth/gmail/android', methods=['POST'])
@log_request
async def auth_by_google_in_android(request: Request):
    mistakes = AuthGmailSchema().validate(request.json)
    if mistakes:
        return get_response_with_validation_errors(mistakes)

    account_main = AccountMain(email=request.json['email'])
    account_main, err = await AuthService.auth_by_gmail(account_main)
    if err:
        return err.get_response_with_error()

    return get_response_auth(account_main)
