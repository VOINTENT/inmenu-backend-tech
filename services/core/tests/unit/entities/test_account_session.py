import pytest

from src.internal.biz.entities.account_main import AccountMain
from src.internal.biz.entities.account_session import AccountSession


def test_empty_init():
    account_session = AccountSession()

    assert account_session.account_main is None


def test_correct_init():
    account_main = AccountMain()

    account_session = AccountSession(account_main=account_main)
    assert account_session.account_main is account_main


def test_incorrect_init():
    with pytest.raises(TypeError):
        AccountSession(account_main=123)


def test_correct_setters():
    account_main = AccountMain()

    account_session = AccountSession()
    account_session.account_main = account_main

    assert account_session.account_main is account_main


def test_incorrect_setters():
    account_session = AccountSession()

    with pytest.raises(TypeError):
        account_session.account_main = 1234
