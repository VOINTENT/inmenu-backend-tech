from datetime import datetime

from src.internal.biz.deserializers.account_main import AccountMainDeserializer, ACCOUNT_MAIN_IS_ACTIVE, \
    ACCOUNT_MAIN_ID, ACCOUNT_MAIN_CREATED_AT, ACCOUNT_MAIN_EDITED_AT, ACCOUNT_MAIN_EMAIL, ACCOUNT_MAIN_HASH_PASSWORD, \
    ACCOUNT_MAIN_BALANCE, ACCOUNT_MAIN_IS_CONFIRMED, DES_ACCOUNT_MAIN_FROM_DB_FULL
from src.internal.biz.deserializers.base_deserializer import DES_FROM_DICT


def test_des_from_dict():

    account_main_dict = {
        "email": "email@gmail.com",
        "password": "password"
    }

    account_main = AccountMainDeserializer.deserialize(account_main_dict, DES_FROM_DICT)
    assert account_main.email == account_main_dict['email']
    assert account_main.password == account_main_dict['password']


def test_des_from_db_full():
    account_main_record = {
        ACCOUNT_MAIN_ID: 12,
        ACCOUNT_MAIN_CREATED_AT: datetime.now(),
        ACCOUNT_MAIN_EDITED_AT: datetime.now(),
        ACCOUNT_MAIN_EMAIL: 'email@mail.com',
        ACCOUNT_MAIN_HASH_PASSWORD: 'dsoijfiosjdf',
        ACCOUNT_MAIN_BALANCE: 321,
        ACCOUNT_MAIN_IS_CONFIRMED: False,
        ACCOUNT_MAIN_IS_ACTIVE: True
    }

    account_main = AccountMainDeserializer.deserialize(account_main_record, DES_ACCOUNT_MAIN_FROM_DB_FULL)

    assert account_main_record[ACCOUNT_MAIN_ID] == account_main.id
    assert account_main_record[ACCOUNT_MAIN_CREATED_AT] == account_main.created_at
    assert account_main_record[ACCOUNT_MAIN_EDITED_AT] == account_main.edited_at
    assert account_main_record[ACCOUNT_MAIN_EMAIL] == account_main.email
    assert account_main_record[ACCOUNT_MAIN_HASH_PASSWORD] == account_main.hash_password
    assert account_main_record[ACCOUNT_MAIN_BALANCE] == account_main.balance
    assert account_main_record[ACCOUNT_MAIN_IS_CONFIRMED] == account_main.is_confirmed
    assert account_main_record[ACCOUNT_MAIN_IS_ACTIVE] == account_main.is_active
