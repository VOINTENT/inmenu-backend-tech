from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.utils import check_value
from src.internal.biz.services.utils import get_random_code


class AuthCode(AbstractModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 account_main: Optional[AccountMain] = None,
                 code: Optional[str] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(account_main=account_main, code=code)
        self.__account_main = account_main
        self.__code = code

    @property
    def account_main(self) -> AccountMain:
        return self.__account_main

    @property
    def code(self) -> str:
        return self.__code

    def create_random_code(self) -> None:
        self.__code = get_random_code()

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['account_main'], AccountMain)
        check_value(kwargs['code'], str)
