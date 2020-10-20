from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.serializers.base_serializer import BaseSerializer


SER_FOR_AUTH_REGISTER = 'ser-for-auth-register'
SER_FOR_DETAIL = 'ser-for-detail'


class AccountMainSerializer(BaseSerializer):

    @classmethod
    def _get_serializer(cls, format_ser: str):
        if format_ser == SER_FOR_AUTH_REGISTER:
            return cls._ser_for_register
        elif format_ser == SER_FOR_DETAIL:
            return cls._ser_for_detail
        else:
            return TypeError

    @staticmethod
    def _ser_for_register(account_main: AccountMain) -> dict:
        return {
            'id': account_main.id,
            'email': account_main.email,
            'auth_token': account_main.auth_token,
            'is_confirmed': account_main.is_confirmed,
            'is_active': account_main.is_active,
            'is_email_sent': account_main.is_email_sent if account_main.is_email_sent is not None else False
        }

    @staticmethod
    def _ser_for_detail(account_main: AccountMain) -> dict:
        return {
            'id': account_main.id,
            'created_at': account_main.created_at_timestamp,
            'edited_at': account_main.edited_at_timestamp,
            'email': account_main.email,
            'name': account_main.name,
            'is_confirmed': account_main.is_confirmed,
            'is_active': account_main.is_active,
            'balance': account_main.balance
        }
