from inspect import isawaitable

from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.account_status_dao import AccountStatusDao
from src.internal.biz.dao.place_account_role import PlaceAccountRoleDao


def get_status(func):
    async def wrapper(request, place_main_id, *args, **kwargs):
        place_account_role, err = await PlaceAccountRoleDao().get_by_place_main_id(place_main_id)
        
        status_main = 1

        if err:
            return err.get_response_with_error()
        
        
        if not place_account_role.account_status.id == status_main:
            return ErrorEnum.STATUS_DOESNT_MATCH.get_response_with_error()

        response = func(request, *args, place_main_id=place_main_id, **kwargs)

        if isawaitable(response):
            response = await response
        return response

    return wrapper
