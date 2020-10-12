from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.currency import Currency
from src.internal.biz.entities.language import Language
from src.internal.biz.entities.photo import Photo
from src.internal.biz.entities.utils import check_value


class PlaceMain(AbstractModel):
    def __init__(self, id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 account_main: Optional[datetime] = None,
                 main_language: Optional[Language] = None,
                 name: Optional[str] = None,
                 login: Optional[str] = None,
                 photo: Optional[Photo] = None,
                 description: Optional[str] = None,
                 main_currency: Optional[Currency] = None,
                 is_draft: Optional[bool] = None,
                 is_published: Optional[bool] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(main_language=main_language, name=name, login=login, photo=photo,
                              description=description, main_currency=main_currency, is_draft=is_draft,
                              is_published=is_published)
        self.__main_language = main_language
        self.__account_main = account_main
        self.__name = name
        self.__login = login
        self.__photo = photo
        self.__description = description
        self.__main_currency = main_currency
        self.__is_draft = is_draft
        self.__is_published = is_published

    @property
    def main_language(self) -> Optional[Language]:
        return self.__main_language

    @property
    def account_main(self) -> Optional[AccountMain]:
        return self.__account_main

    @account_main.setter
    def account_main(self, value: AccountMain) -> None:
        self.__account_main = value

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @property
    def login(self) -> Optional[str]:
        return self.__login

    @property
    def photo(self) -> Optional[Photo]:
        return self.__photo

    @property
    def description(self) -> Optional[str]:
        return self.__description

    @property
    def main_currency(self) -> Optional[Currency]:
        return self.__main_currency

    @property
    def is_draft(self) -> Optional[bool]:
        return self.__is_draft

    @property
    def is_published(self) -> Optional[bool]:
        return self.__is_published

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['main_language'], Language)
        check_value(kwargs['name'], str)
        check_value(kwargs['login'], str)
        check_value(kwargs['photo'], Photo)
        check_value(kwargs['description'], str)
        check_value(kwargs['main_currency'], Currency)
        check_value(kwargs['is_draft'], bool)
        check_value(kwargs['is_published'], bool)
