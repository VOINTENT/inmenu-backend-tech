from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.account_status import AccountStatus
from src.internal.biz.entities.place_main import PlaceMain


class PlaceAccountRole(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 place_main: Optional[PlaceMain] = None,
                 account_main: Optional[AccountMain] = None,
                 account_status: Optional[AccountStatus] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__place_main = place_main
        self.__account_main = account_main
        self.__account_status = account_status

    @property
    def place_main(self):
        return self.__place_main

    @property
    def account_main(self):
        return self.__account_main

    @property
    def account_status(self):
        return self.__account_status
