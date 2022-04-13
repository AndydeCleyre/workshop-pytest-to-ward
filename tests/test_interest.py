from ward import each, test

from bank.bank import Account, StudentAccount

from .conftest import account, bank


@test("pay interest")
def _(
    account=account,
    bank=bank,
    initial=each(10, -10, -20),
    interest=each(0.1, 0.1, 0.1),
    final=each(11, -11, -22),
):
    account.overdraft_limit = 20
    account.balance = initial
    bank.interest_rate = interest

    account.step()

    assert account.balance == final


@test("pay all")
def _(account=account, bank=bank):
    account_2 = Account(name="Second", bank=bank)

    account.balance = 10
    account_2.balance = 20

    bank.step()

    assert account.balance == 11
    assert account_2.balance == 22


@test("student account")
def test_student_account(bank=bank, initial=each(-10, -5, 10), final=each(-10, -5, 11)):
    account = StudentAccount("Guy Young", bank=bank)

    account._balance = initial
    account.step()

    assert account._balance == final
