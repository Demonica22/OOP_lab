from enum import Enum


class AccountType(Enum):
    AccountType = 1
    Checking = 2


class BankAccount:
    next_account_number = 0

    def __init__(self):
        self.account_number = None
        self.account_balance = 0
        self.account_type = None

    def populate(self, balance: float) -> None:
        self.account_number = self.get_next_account_number()
        self.account_balance = balance
        self.account_type = AccountType.Checking

    def number(self) -> int:
        return self.account_number

    def balance(self) -> float:
        return self.account_balance

    def type(self) -> AccountType:
        return self.account_type

    def get_next_account_number(self):
        BankAccount.next_account_number += 1
        return BankAccount.next_account_number

    def deposit(self, amount: float) -> float:
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount: float) -> bool or float:
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return amount

    def transfer_from(self, acc_from, amount):
        if acc_from.withdraw(amount):
            self.deposit(amount)
            return self.balance()
        return False

    def __repr__(self):
        return f"Account #{self.account_number}\nBalance: {self.account_balance}\nAccount Type: {self.account_type}"


def new_bank_account():
    created = BankAccount()
    try:
        balance = int(input("Enter balance for your account:"))
    except Exception as x:
        print("Enter proper integer for your fields")
        return None
    created.populate(balance)
    return created


def test_deposit(acc: BankAccount) -> float or None:
    try:
        amount = int(input("Enter amount to deposit: "))
    except Exception as x:
        print("Enter proper integer for your fields")
        return None
    return acc.deposit(amount)


def test_withdraw(acc: BankAccount) -> float or None:
    try:
        amount = int(input("Enter amount to withdraw: "))
        if amount < 0:
            raise ValueError
    except Exception as x:
        print("Enter proper integer for your fields")
        return None
    return acc.withdraw(amount)


first = BankAccount()
second = BankAccount()
first.populate(100)
second.populate(100)
print("Before transfer")
print(first)
print(second)
try:
    amount = int(input("Enter transfer amount: "))
    if amount < 0:
        raise ValueError
    if first.transfer_from(second, amount):
        print("After transfer:")
        print(first)
        print(second)
    else:
        print("Not enough balance")
except Exception:
    print("Incorrect amount")
