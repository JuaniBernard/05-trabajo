import unittest
from parameterized import parameterized
from personService import PersonService
from person import Person
from repository import Repository


class TestPersonService(unittest.TestCase):
    def setUp(self):
        personService = PersonService()
        init_repo = [
            ["federico", "gonzalez", "20"],
            ["claudio", "pico", "33"],
            ["nicolas", "pico", "40"]
                    ]
        for p in init_repo:
            per1 = Person()
            per1.name = p[0]
            per1.surname = p[1]
            per1.age = p[2]
            personService.add_person(per1)

    def tearDown(self):
        Repository.person = {}

    def test_get_personList(self):
        personService = PersonService()
        persons = {
            0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'},
            1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': '33'},
            2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': '40'}
                     }
        dictPersonList = personService.get_personList()
        self.assertDictEqual(dictPersonList, persons)

    @parameterized.expand([
        ("Juan", "Bernard", "23", 3),
        ("Pedro", "Jones", "31", 3)
    ])
    def test_add_person(self, name, surname, age, key):
        personService = PersonService()
        per1 = Person()
        per1.name = name
        per1.surname = surname
        per1.age = age
        dictPerson = per1.__dict__
        personService.add_person(per1)
        self.assertDictEqual(Repository.person[key], dictPerson)

    def test_update_person(self):
        personService = PersonService()
        key = 0
        no_update_person = Repository.person[key].copy()
        person = Person()
        person.name = "Juan"
        person.surname = "Bernard"
        person.age = "23"
        personService.update_person(key, person)
        self.assertNotEqual(Repository.person[key], no_update_person)

    def test_delete_person(self):
        personService = PersonService()
        key = 2
        personService.delete_person(key)
        self.assertNotIn(key, Repository.person)


if __name__ == "__main__":
    unittest.main()
