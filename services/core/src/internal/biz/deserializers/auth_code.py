from asyncpg import Record

from src.internal.biz.deserializers.account_main import ACCOUNT_MAIN, AccountMainDeserializer, \
    DES_ACCOUNT_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer
from src.internal.biz.deserializers.utils import filter_keys_by_substr
from src.internal.biz.entities.auth_code import AuthCode

DES_AUTH_CODE_FROM_DB_FULL = 'auth-code-from-db-full'

AUTH_CODE = 'ac_'
AUTH_CODE_ID = AUTH_CODE + ID
AUTH_CODE_CREATED_AT = AUTH_CODE + CREATED_AT
AUTH_CODE_EDITED_AT = AUTH_CODE + EDITED_AT
AUTH_CODE_CODE = AUTH_CODE + 'cd'


class AuthCodeDeserializer(BaseDeserializer):

    @classmethod
    def _get_deserializer(cls, format_ser: str):
        if format_ser == DES_AUTH_CODE_FROM_DB_FULL:
            return cls._from_db_full
        else:
            raise TypeError

    @staticmethod
    def _from_db_full(auth_code: Record) -> AuthCode:
        account_main_dict = filter_keys_by_substr(auth_code, ACCOUNT_MAIN)
        return AuthCode(
            id=auth_code.get(AUTH_CODE_ID),
            created_at=auth_code.get(AUTH_CODE_CREATED_AT),
            edited_at=auth_code.get(AUTH_CODE_EDITED_AT),
            account_main=AccountMainDeserializer.deserialize(account_main_dict, DES_ACCOUNT_MAIN_FROM_DB_FULL),
            code=auth_code.get(AUTH_CODE_CODE)
        )
