# Content: Wallet class with spend_cash and add_cash methods
# wallet.py

class InsufficientAmount(Exception): # to signal that there is not enough cash available in the wallet to perform a spending operation.
    pass

class Wallet(object):

    def __init__(self, initial_amount=0): # initialization to create a new empty wallet
        self.balance = initial_amount

    def spend_cash(self, amount): # This method allows the user to spend a specified amount of cash from the wallet.
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount): # This method allows the user to topup amount of cash to the wallet.
        self.balance += amount