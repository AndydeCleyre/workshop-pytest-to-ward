from ward import each, raises, test

from bank.bank import AccountException

from .conftest import account


@test("open account")
def _(account=account):
    assert account.name == "Richard"


@test("make deposit")
def _(account=account):
    account.make_deposit(100)
    assert account.balance == 100


@test("make withdrawal")
def _(account=account):
    account.balance = 100
    account.make_withdrawal(20)
    assert account.balance == 80


@test("make bad withdrawal")
def _(account=account):
    account.balance = 10
    with raises(AccountException):
        account.make_withdrawal(20)

    assert account.balance == 10


@test("overdraft limit")
def _(account=account):
    account.overdraft_limit = 10

    assert account.available_funds == 10


@test("withdrawal")
def _(
    account=account,
    limit=each(10, 10, 20),
    withdrawal=each(10, 5, 5),
    balance=each(-10, -5, -5),
    funds=each(0, 5, 15),
):
    account.overdraft_limit = limit
    account.make_withdrawal(withdrawal)

    assert account.balance == balance
    assert account.available_funds == funds


@test("set balance")
def _(account=account):
    with raises(AccountException):
        account.balance = -10


@test("deposit below limit")
def _(account=account):
    account._balance = -10
    account.make_deposit(5)

    assert account.balance == -5
