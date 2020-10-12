from inspect import isawaitable

from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.entities.account_session import AccountSession
from src.internal.biz.services.auth_service import AuthService


def required_auth(func):
    async def wrapper(request, *args, **kwargs):
        if not request.headers.get('auth-token'):
            return ErrorEnum.FORBIDDEN.get_response_with_error()

        session_id = AccountSession.get_session_id_from_token(request.headers.get('auth-token'))
        if not session_id:
            return ErrorEnum.INVALID_OR_OUTDATED_TOKEN.get_response_with_error()

        account_main, err = await AuthService.get_account_main_by_session_id(session_id)
        if err:
            return err.get_response_with_error()

        if not account_main:
            return ErrorEnum.INVALID_OR_OUTDATED_TOKEN.get_response_with_error()

        response = func(request, *args, auth_account_main_id=account_main.id, **kwargs)
        if isawaitable(response):
            response = await response
        return response

    return wrapper


def required_auth_with_confirmed_email(func):
    async def wrapper(request, *args, **kwargs):
        if not request.headers.get('auth-token'):
            return ErrorEnum.FORBIDDEN.get_response_with_error()

        session_id = AccountSession.get_session_id_from_token(request.headers.get('auth-token'))
        if not session_id:
            return ErrorEnum.INVALID_OR_OUTDATED_TOKEN.get_response_with_error()

        account_main, err = await AuthService.get_account_main_by_session_id_with_confirmed(session_id)
        if err:
            return err.get_response_with_error()

        if not account_main:
            return ErrorEnum.INVALID_OR_OUTDATED_TOKEN.get_response_with_error()

        if not account_main.is_confirmed:
            return ErrorEnum.EMAIL_IS_NOT_CONFIRMED.get_response_with_error()

        response = func(request, *args, auth_account_main_id=account_main.id, **kwargs)
        if isawaitable(response):
            response = await response
        return response

    return wrapper
