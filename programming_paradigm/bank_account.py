# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add amount to account_balance."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Deduct amount from account_balance if funds are sufficient."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")