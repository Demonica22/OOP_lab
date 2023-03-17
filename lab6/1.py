from enum import Enum


class AccountType(Enum):
    AccountType = 1
    Checking = 2


class BankAccount:
    def __init__(self):
        self.account_number = None
        self.account_balance = 0
        self.account_type = None

    def populate(self, number, balance) -> None:
        self.account_number = number
        self.account_balance = balance
        self.account_type = AccountType.Checking

    def number(self) -> int:
        return self.account_number

    def balance(self) -> int:
        return self.account_balance

    def type(self) -> AccountType:
        return self.account_type

    def __repr__(self):
        return f"Account #{self.account_number}\nBalance: {self.account_balance}\nAccount Type: {self.account_type}"


def new_bank_account():
    created = BankAccount()
    try:
        number = int(input("Enter number for your account:"))
        balance = int(input("Enter balance for your account:"))
    except Exception as x:
        print("Enter proper integer for your fields")
        exit(0)
    created.populate(number, balance)
    return created


berts = BankAccount()
berts.populate(1, 10000)
print(berts)

created = new_bank_account()
print(created)
