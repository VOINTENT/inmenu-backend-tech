from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.place_main import PlaceMain
from src.internal.biz.entities.utils import check_value


class PlaceContacts(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 place_main: Optional[PlaceMain] = None,
                 phone_number: Optional[str] = None,
                 email: Optional[str] = None,
                 site_link: Optional[str] = None,
                 vk_link: Optional[str] = None,
                 instagram_link: Optional[str] = None,
                 facebook_link: Optional[str] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__place_main = place_main
        self.__phone_number = phone_number
        self.__email = email
        self.__site_link = site_link
        self.__vk_link = vk_link
        self.__instagram_link = instagram_link
        self.__facebook_link = facebook_link

    @property
    def place_main(self) -> PlaceMain:
        return self.__place_main

    @place_main.setter
    def place_main(self, value: PlaceMain) -> None:
        self.__place_main = value

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @property
    def email(self) -> str:
        return self.__email

    @property
    def site_link(self) -> str:
        return self.__site_link

    @property
    def vk_link(self) -> str:
        return self.__vk_link

    @property
    def instagram_link(self) -> str:
        return self.__instagram_link

    @property
    def facebook_link(self) -> str:
        return self.__facebook_link

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['place_main'], PlaceMain)
        check_value(kwargs['phone_number'], str)
        check_value(kwargs['email'], str)
        check_value(kwargs['site_link'], str)
        check_value(kwargs['vk_link'], str)
        check_value(kwargs['instagram_link'], str)
        check_value(kwargs['facebook_link'], str)
