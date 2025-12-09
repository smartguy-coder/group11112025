

# def test_person(person):
#     assert person.total_money == 0


class TestPerson:

    def test_new_person(self, person):
        print(person, 88888888888)
        assert person.name
        assert person.tin
        assert person.total_money == 0

    def test_person_unique_tin(self, person, person2):
        print(person, 9999999999999)
        assert person.tin != person2.tin


class TestPerson2:

    def test_new_person(self, person):
        print(person, 88888888888)
        assert person.name
        assert person.tin
        assert person.total_money == 0

    def test_person_unique_tin(self, person, person2):
        print(person, 9999999999999)
        assert person.tin != person2.tin