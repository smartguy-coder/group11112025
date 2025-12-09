




class TestPerson2:

    def test_new_person(self, person):
        print(person, 88888888888)
        assert person.name == "Test Person"
        assert person.tin
        assert person.total_money == 0

    def test_person_unique_tin(self, person, person2):
        print(person, 9999999999999)
        assert person.tin != person2.tin


class TestPerson:

    def test_new_person(self, person):
        print(person, 88888888888)
        assert person.name == "Test Person"
        assert person.tin
        assert person.total_money == 0

        person.name = "Test Person married"
        assert person.name == "Test Person married"

    def test_person_unique_tin(self, person, person2):
        print(person, 9999999999999)
        assert person.tin != person2.tin


class TestAccountFlow:
    def test_balance_new_account(self, account_person):
        assert account_person.balance == 0

    def test_deposit_money_to_account(self, account_person):
        account_person.deposit(5000)
        assert account_person.balance == 5000
        account_person.deposit(5000)
        assert account_person.balance == 10000
        assert account_person.owner.total_money == 10000
        assert account_person.bank.total_money == 10000

    def test_open_account(self, bank, person2):
        acc = bank.open_account(person2)
        acc.withdraw(500)
        assert bank.total_money == 9500


def test_person(person):
    assert person.total_money == 0