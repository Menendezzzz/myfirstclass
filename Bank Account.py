from datetime import datetime
from typing import List

class Amount:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type}: {self.amount} at {self.timestamp}"

class PersonalAccount:
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions: List[Amount] = []

    def deposit(self, amount: float):
        self.balance += amount
        self.transactions.append(Amount(amount, 'Deposit'))

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Amount(amount, 'Withdrawal'))
        else:
            print("Insufficient balance")

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self) -> float:
        return self.balance

    def __str__(self):
        return f"Account #{self.account_number} held by {self.account_holder} with balance {self.balance}"

if __name__ == "__main__":
    account = PersonalAccount(20070608, 'Marsel Sharapov (VIP status)')
    account.deposit(60365.0)
    account.withdraw(300.0)
    account.print_transaction_history()
    print(f"Current balance: {account.get_balance()}")