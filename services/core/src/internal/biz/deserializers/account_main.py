from typing import Union, Dict

from asyncpg import Record

from src.internal.biz.deserializers.base_constants import ID, CREATED_AT, EDITED_AT
from src.internal.biz.deserializers.base_deserializer import BaseDeserializer, DES_FROM_DICT
from src.internal.biz.entities.account_main import AccountMain


DES_ACCOUNT_MAIN_FROM_DB_FULL = 'account-main-from-db-full'

ACCOUNT_MAIN = 'acm_'
ACCOUNT_MAIN_ID = ACCOUNT_MAIN + ID
ACCOUNT_MAIN_CREATED_AT = ACCOUNT_MAIN + CREATED_AT
ACCOUNT_MAIN_EDITED_AT = ACCOUNT_MAIN + EDITED_AT
ACCOUNT_MAIN_EMAIL = ACCOUNT_MAIN + 'em'
ACCOUNT_MAIN_HASH_PASSWORD = ACCOUNT_MAIN + 'hp'
ACCOUNT_MAIN_BALANCE = ACCOUNT_MAIN + 'bl'
ACCOUNT_MAIN_IS_CONFIRMED = ACCOUNT_MAIN + 'ic'
ACCOUNT_MAIN_IS_ACTIVE = ACCOUNT_MAIN + 'ia'


class AccountMainDeserializer(BaseDeserializer):

    @classmethod
    def deserialize(cls, obj_record: Union[Record, Dict], format_ser: str) -> AccountMain:
        return super().deserialize(obj_record, format_ser)

    @classmethod
    def _get_deserializer(cls, format_ser: str):
        if format_ser == DES_FROM_DICT:
            return super()._deserializer_from_dict(AccountMain)
        elif format_ser == DES_ACCOUNT_MAIN_FROM_DB_FULL:
            return cls._from_db_full
        else:
            return TypeError

    @staticmethod
    def _from_db_full(account_main_record: Union[Record, Dict]):
        return AccountMain(
            id=account_main_record.get(ACCOUNT_MAIN_ID),
            created_at=account_main_record.get(ACCOUNT_MAIN_CREATED_AT),
            edited_at=account_main_record.get(ACCOUNT_MAIN_EDITED_AT),
            email=account_main_record.get(ACCOUNT_MAIN_EMAIL),
            hash_password=account_main_record.get(ACCOUNT_MAIN_HASH_PASSWORD),
            balance=account_main_record.get(ACCOUNT_MAIN_BALANCE),
            is_confirmed=account_main_record.get(ACCOUNT_MAIN_IS_CONFIRMED),
            is_active=account_main_record.get(ACCOUNT_MAIN_IS_ACTIVE)
        )
