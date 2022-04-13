from ward import fixture

from bank.bank import Account, Bank


@fixture
def bank():
    return Bank()


@fixture
def account(bank=bank):
    return Account(name="Richard", bank=bank)
