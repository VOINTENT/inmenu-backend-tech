from typing import Tuple, Optional

from src.internal.adapters.entities.error import Error
from src.internal.biz.dao.account_main_dao import AccountMainDao
from src.internal.biz.entities.account_main import AccountMain


class AccountService:

    @staticmethod
    async def get_detail_account_info(account_main_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        account_main, err = await AccountMainDao().get_by_id(account_main_id)
        if err:
            return None, err

        return account_main, None
