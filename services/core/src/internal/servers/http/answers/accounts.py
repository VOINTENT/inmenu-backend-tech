from sanic.response import HTTPResponse, json

from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.serializers.account_main_serializer import AccountMainSerializer, SER_FOR_AUTH_REGISTER, \
    SER_FOR_DETAIL


def get_response_register(account_main: AccountMain) -> HTTPResponse:
    return json(AccountMainSerializer.serialize(account_main, SER_FOR_AUTH_REGISTER), 201)


def get_response_auth(account_main: AccountMain) -> HTTPResponse:
    return json(AccountMainSerializer.serialize(account_main, SER_FOR_AUTH_REGISTER), 200)


def get_response_detail(account_main: AccountMain) -> HTTPResponse:
    return json(AccountMainSerializer.serialize(account_main, SER_FOR_DETAIL), 200)
