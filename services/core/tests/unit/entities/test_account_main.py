import pytest

from src.internal.biz.entities.account_main import AccountMain


def test_empty_init():
    account_main = AccountMain()

    assert account_main.email is None
    assert account_main.password is None
    assert account_main.hash_password is None
    assert account_main.auth_token is None
    assert account_main.balance is None
    assert account_main.is_confirmed is None
    assert account_main.is_active is None


def test_correct_init():
    email = '123@gmail.com'
    password = '123'
    hash_password = 'scdkoinjviosfdisuo'
    token = 'sdhdgfiushfiudshf'
    balance = 321
    is_confirmed = False
    is_active = True

    account_main = AccountMain(
        email=email, password=password, hash_password=hash_password, auth_token=token, balance=balance,
        is_confirmed=is_confirmed, is_active=is_active
    )

    assert account_main.email == email
    assert account_main.password == password
    assert account_main.hash_password == hash_password
    assert account_main.auth_token == token
    assert account_main.balance == balance
    assert account_main.is_confirmed == is_confirmed
    assert account_main.is_active == is_active


def test_incorrect_init():
    with pytest.raises(TypeError):
        AccountMain(email=123)

    with pytest.raises(TypeError):
        AccountMain(password=123)

    with pytest.raises(TypeError):
        AccountMain(hash_password=123)

    with pytest.raises(TypeError):
        AccountMain(balance='23786')

    with pytest.raises(TypeError):
        AccountMain(is_confirmed='True')

    with pytest.raises(TypeError):
        AccountMain(is_active='False')

    with pytest.raises(TypeError):
        AccountMain(auth_token=123)


def test_correct_setters():
    hash_password = 'scdkoinjviosfdisuo'
    token = 'sdhdgfiushfiudshf'
    is_confirmed = False
    is_active = True

    account_main = AccountMain()
    account_main.hash_password = hash_password
    account_main.auth_token = token
    account_main.is_active = is_active
    account_main.is_confirmed = is_confirmed

    assert account_main.hash_password == hash_password
    assert account_main.auth_token == token
    assert account_main.is_confirmed == is_confirmed
    assert account_main.is_active == is_active


def test_hash_password():
    account_main1 = AccountMain(password='123')
    account_main1.create_hash_password()

    account_main2 = AccountMain(password='123')
    account_main2.create_hash_password()

    assert isinstance(account_main1.hash_password, str)
    assert account_main1.hash_password == account_main2.hash_password
