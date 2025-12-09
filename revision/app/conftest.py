import pytest

from oop.models import Person, Bank, BankAccount

# "session", "package", "module", "class", "function"
# @pytest.fixture(scope='function')
@pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='session')
def person() -> Person:
    print(11111111111111111111111111111111111111)
    return Person('test person')


@pytest.fixture(scope='class')
def person2() -> Person:
    return Person('test person 2')


@pytest.fixture(scope='class')
def bank() -> Bank:
    return Bank('mono')


@pytest.fixture(scope='class')
def bank2() -> Bank:
    return Bank('raif')


@pytest.fixture(scope='class')
def account_person(person, bank) -> BankAccount:
    return bank.open_account(person)
