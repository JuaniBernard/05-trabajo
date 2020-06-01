from person import Person
from personService import PersonService

if __name__ == '__main__':

    personService = PersonService()

    # Agregamos una persona
    p0 = Person()
    p0.name = 'federico'
    p0.surname = 'gonzalez'
    p0.age = '20'
    personService.add_person(p0)

    # Agregamos una persona
    p1 = Person()
    p1.name = 'claudio'
    p1.surname = 'pico'
    p1.age = '33'
    personService.add_person(p1)

    # Agregamos al hermano
    p2 = Person()
    p2.name = 'nicolas'
    p2.surname = 'pico'
    p2.age = '40'
    personService.add_person(p2)

    print(personService.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}, 2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 40}}

    # Update FEDERICO
    p0.age = '30'
    personService.update_person(0, p0)
    print(personService.get_personList())

    # delete person
    personService.delete_person(2)

    print(personService.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}}
