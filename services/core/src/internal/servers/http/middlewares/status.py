from inspect import isawaitable

from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.account_status_dao import AccountStatusDao
from src.internal.biz.dao.place_account_role import PlaceAccountRoleDao


def get_status(func):
    async def wrapper(request, place_main_id, *args, **kwargs):
        place_account_role, err = await PlaceAccountRoleDao().get_by_place_main_id(place_main_id)

        if err:
            return err.get_response_with_error()

        account_status, err = await AccountStatusDao().get_owner_status()

        if err:
            return err.get_response_with_error()

        if not place_account_role.account_status.id == account_status.id:
            return ErrorEnum.STATUS_DOESNT_MATCH.get_response_with_error()

        response = func(request, place_main_id=place_main_id, *args, **kwargs)

        if isawaitable(response):
            response = await response
        return response

    return wrapper
