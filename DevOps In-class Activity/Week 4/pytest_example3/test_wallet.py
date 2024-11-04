# test_wallet.py
# pytest -k wallet_add_cash -v [test with keyword wallet_add_cash, verbose]
# pytest -m advance -v

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.mark.xfail  # This test pass/fails will not be considered
def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 10

@pytest.mark.basic
def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

@pytest.mark.basic
def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

@pytest.mark.advance
def test_wallet_add_cash_advance(wallet):
    wallet.add_cash(800)
    assert wallet.balance == 800

@pytest.mark.xfail  # This test pass/fails will not be considered
def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

@pytest.mark.xskip  # This test will be skipped
def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)