import pytest


@pytest.mark.parametrize(
    "initial, interest, final",
    [
        (10, 0.1, 11),
        (-10, 0.1, -11),
        (-20, 0.1, -22),
    ]
)
def test_pay_interest(
        account,
        bank,
        initial,
        interest,
        final
):
    account.overdraft_limit = 20
    account.balance = initial
    bank.interest_rate = interest

    account.step()

    assert account.balance == final


def test_pay_all(
        account,
        bank
):
    account_2 = bank.open_account(
        "Second"
    )

    account.balance = 10
    account_2.balance = 20
    bank.interest_rate = 0.1

    bank.step()

    assert account.balance == 11
    assert account_2.balance == 22
