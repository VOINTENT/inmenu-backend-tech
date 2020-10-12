from datetime import datetime

from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.serializers.account_main_serializer import AccountMainSerializer, SER_FOR_AUTH_REGISTER


def test_for_auth_register():
    id = 321
    email = '123@gmail.com'
    token = 'dfhsiudhfds'
    is_confirmed = False
    is_active = True
    account_main = AccountMain(
        id=id,
        email=email,
        auth_token=token,
        is_confirmed=is_confirmed,
        is_active=is_active
    )

    assert AccountMainSerializer.serialize(account_main, SER_FOR_AUTH_REGISTER) == {
        'id': id,
        'email': email,
        'auth_token': token,
        'is_confirmed': is_confirmed,
        'is_active': is_active
    }
