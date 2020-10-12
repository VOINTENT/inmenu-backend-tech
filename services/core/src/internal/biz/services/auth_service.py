from typing import Tuple, Optional

from src.configs.internal import LIFETIME_CODE, SEND_CODE_INTERVAL
from src.internal.adapters.entities.error import Error
from src.internal.adapters.enums.errors import ErrorEnum
from src.internal.biz.dao.account_main_dao import AccountMainDao
from src.internal.biz.dao.account_session import AccountSessionDao
from src.internal.biz.dao.auth_code import AuthCodeDao
from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.account_session import AccountSession
from src.internal.biz.entities.auth_code import AuthCode
from src.internal.biz.services.base_service import BaseService
from src.internal.biz.services.utils import get_passed_time
from src.internal.drivers.mail import Mail, EMAIL_CODE_TYPE


class AuthService(BaseService):

    @staticmethod
    async def register(account_main: AccountMain) -> Tuple[Optional[AccountMain], Optional[Error]]:
        account_main.create_hash_password()
        account_main, err = await AccountMainDao().add(account_main)
        if err:
            return None, err

        account_session = AccountSession(account_main=account_main)
        account_session, err = await AccountSessionDao().add(account_session)
        if err:
            return None, err

        account_main.auth_token = account_session.create_token()

        auth_code = AuthCode(account_main=account_main)
        auth_code.create_random_code()

        _, err = await AuthCodeDao().add(auth_code)

        account_main.is_email_sent = Mail.send_email(EMAIL_CODE_TYPE, account_main.email, auth_code.code)

        return account_main, None

    @staticmethod
    async def auth_basic(account_main: AccountMain) -> Tuple[Optional[AccountMain], Optional[Error]]:
        account_main.create_hash_password()
        account_main, err = await AccountMainDao().get_by_email_hash_password(account_main)
        if err:
            return None, err

        if not account_main:
            return None, ErrorEnum.WRONG_EMAIL_PASSWORD

        account_session = AccountSession(account_main=account_main)
        account_session, err = await AccountSessionDao().add(account_session)
        if err:
            return None, err

        account_main.auth_token = account_session.create_token()

        return account_main, None

    @staticmethod
    async def get_account_main_by_session_id(session_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        account_main, err = await AccountMainDao().get_by_session_id(session_id)
        if err:
            return None, err

        return account_main, None

    @staticmethod
    async def get_account_main_by_session_id_with_confirmed(session_id: int) -> Tuple[Optional[AccountMain], Optional[Error]]:
        account_main, err = await AccountMainDao().get_by_session_id_with_confirmed(session_id)
        if err:
            return None, err

        return account_main, None

    @staticmethod
    async def confirm_code(code: AuthCode) -> Tuple[None, Optional[Error]]:
        auth_code_dao = AuthCodeDao()
        code, err = await auth_code_dao.get_by_account_main_id_code(code)
        if err:
            return None, err

        if not code:
            return None, ErrorEnum.UNKNOWN_CODE

        if get_passed_time(code.edited_at) > LIFETIME_CODE:
            return None, ErrorEnum.LIFETIME_CODE_OUT

        _, err = await AuthCodeDao().set_is_confirm(True)
        if err:
            return None, err

        _, err = await auth_code_dao.remove_by_id(code.id)
        if err:
            return None, err

        return None, None

    @staticmethod
    async def send_new_auth_code(auth_account_main_id: int):
        previous_code, err = await AuthCodeDao().get_by_account_main_id(auth_account_main_id)
        if err:
            return None, err

        if previous_code and get_passed_time(previous_code.edited_at) < SEND_CODE_INTERVAL:
            return None, ErrorEnum.SEND_CODE_TOO_OFTEN

        auth_code = AuthCode(account_main=AccountMain(id=auth_account_main_id))
        auth_code.create_random_code()

        if previous_code:
            _, err = await AuthCodeDao().update(previous_code.id, auth_code)
        else:
            _, err = await AuthCodeDao().add(auth_code)

        return None, None
