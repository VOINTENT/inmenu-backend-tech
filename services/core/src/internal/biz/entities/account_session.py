from datetime import datetime
from typing import Optional

import jwt

from src.configs.internal import SECRET_KEY, ENCRYPT_ALGORITHM
from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.utils import check_value


class AccountSession(AbstractModel):
    def __init__(self,
                 id: int = None,
                 created_at: datetime = None,
                 edited_at: datetime = None,
                 account_main: AccountMain = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(account_main=account_main)
        self.__account_main = account_main

    @property
    def account_main(self) -> AccountMain:
        return self.__account_main

    @account_main.setter
    def account_main(self, value: AccountMain):
        check_value(value, AccountMain)
        self.__account_main = value

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['account_main'], AccountMain)

    def create_token(self) -> str:
        return jwt.encode(
            {
                'session_id': self.id
            }, SECRET_KEY, algorithm=ENCRYPT_ALGORITHM).decode()

    @staticmethod
    def get_session_id_from_token(token: str) -> Optional[int]:
        if not token:
            return None

        try:
            return int(jwt.decode(token, SECRET_KEY, algorithms=ENCRYPT_ALGORITHM)['session_id'])
        except:
            return None
