#to run the test, type this in cmd --> pytest -q test_wallet.py -v
# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount # wallet.py, Wallet Class and InsuffcientAmount Class


''' 
Here is a set of unit tests for the Wallet class using the pytest framework. 
Each test function checks a specific behavior or functionality of the Wallet class.

'''
def test_default_initial_amount(): # This test checks whether the new Wallet has a initial balance of 0.
    wallet = Wallet()
    assert wallet.balance == 0 # If wallet.balance == 0, the test passes.

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)