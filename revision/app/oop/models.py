import uuid
from typing import Self


class FinancialCalculator:
    def __init__(self):
        self.accounts: list[BankAccount] = []

    @property
    def total_money(self) -> float:
        money = sum([acc.balance for acc in self.accounts])
        return money


class Person(FinancialCalculator):
    def __init__(self, name: str):
        super().__init__()
        self.name = name.title()
        self.tin = uuid.uuid4().hex
        self.money = 0

    def __str__(self):
        return f"<Person {self.name}  #{self.tin}>"


class BankAccount:
    def __init__(self, owner: Person, bank: "Bank"):
        self.owner = owner
        self.balance = 0
        self.bank = bank

    def __str__(self) -> str:
        return f'BankAccount: Owner= {self.owner} #{id(self)} {self.balance} (issued by {self.bank.name})'

    __repr__ = __str__

    def deposit(self, amount: float):
        amount = abs(amount)
        self.balance += amount

    def withdraw(self, amount: float):
        amount = abs(amount)
        self.balance -= amount

    def transfer(self, amount: float, other: Self):
        amount = abs(amount)
        self.withdraw(amount)
        other.deposit(amount)


class Bank(FinancialCalculator):
    def __init__(self, name: str):
        super().__init__()
        self.name = f"PAT {name.upper()}"

    def open_account(self, client: Person) -> BankAccount:
        new_account = BankAccount(client, bank=self)
        self.accounts.append(new_account)
        client.accounts.append(new_account)

        return new_account

    def __str__(self) -> str:
        return f'<Bank: {self.name} #{id(self)} has {len(self.accounts)}>'

    __repr__ = __str__
