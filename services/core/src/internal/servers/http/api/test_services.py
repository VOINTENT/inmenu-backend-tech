from sanic import Blueprint
from sanic.request import Request
from sanic.response import json

from src.internal.biz.services.test_service import TestService
from src.internal.servers.http.middlewares.auth import required_auth

test = Blueprint('test', url_prefix='')


@test.route('/server')
async def test_controller(request: Request):
    return json({'test': 'Successful!'})


@test.route('/db')
async def test_db(request: Request):
    return json({'result': await TestService.get_test_data()})


@test.route('/truncate_tables', methods=['POST'])
async def truncate_tables(request: Request):
    await TestService.truncate_tables()
    return json({'result': True})


@test.route('/accounts/auth/code', methods=['GET'])
@required_auth
async def get_code(request: Request, auth_account_main_id: int):
    auth_code = await TestService.get_auth_code(auth_account_main_id)
    return json({'code': auth_code.code})
