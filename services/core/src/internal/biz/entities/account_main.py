import hashlib

from datetime import datetime
from typing import Optional

from src.internal.biz.entities.abstract_model import AbstractModel
from src.internal.biz.entities.utils import check_value


class AccountMain(AbstractModel):
    def __init__(self,
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 edited_at: Optional[datetime] = None,
                 email: Optional[str] = None,
                 name: Optional[str] = None,
                 password: Optional[str] = None,
                 hash_password: Optional[str] = None,
                 auth_token: Optional[str] = None,
                 balance: Optional[int] = None,
                 is_confirmed: Optional[bool] = None,
                 is_active: Optional[bool] = None,
                 is_email_sent: Optional[bool] = None) -> None:
        super().__init__(id, created_at, edited_at)
        self.__class__._check(email=email, password=password, hash_password=hash_password, token=auth_token, balance=balance,
                              is_confirmed=is_confirmed, is_active=is_active, is_email_sent=is_email_sent)
        self.__email = email
        self.__password = password
        self.__hash_password = hash_password
        self.__auth_token = auth_token
        self.__balance = balance
        self.__is_confirmed = is_confirmed
        self.__is_active = is_active
        self.__is_email_sent = is_email_sent
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        self.__email = value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def hash_password(self) -> str:
        return self.__hash_password

    @hash_password.setter
    def hash_password(self, value: str):
        check_value(value, str)
        self.__hash_password = value

    @property
    def auth_token(self) -> str:
        return self.__auth_token

    @auth_token.setter
    def auth_token(self, value):
        check_value(value, str)
        self.__auth_token = value

    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def is_confirmed(self) -> bool:
        return self.__is_confirmed

    @is_confirmed.setter
    def is_confirmed(self, value: bool):
        check_value(value, bool)
        self.__is_confirmed = value

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @is_active.setter
    def is_active(self, value: bool):
        check_value(value, bool)
        self.__is_active = value

    @property
    def is_email_sent(self) -> bool:
        return self.__is_email_sent

    @is_email_sent.setter
    def is_email_sent(self, value: bool):
        check_value(value, bool)
        self.__is_email_sent = value

    def create_hash_password(self):
        if not self.__password:
            return
        self.__hash_password = hashlib.sha512(bytes(self.__password, 'utf-8')).hexdigest()

    def create_name_from_email(self):
        if not self.__email:
            return
        self.__name = self.__email.split('@')[0]

    @staticmethod
    def _check(**kwargs):
        check_value(kwargs['email'], str)
        check_value(kwargs['password'], str)
        check_value(kwargs['hash_password'], str)
        check_value(kwargs['token'], str)
        check_value(kwargs['balance'], int)
        check_value(kwargs['is_confirmed'], bool)
        check_value(kwargs['is_active'], bool)
        check_value(kwargs['is_email_sent'], bool)
