from person import Person
from personService import PersonService


class App:
    def menu_person(self):
        print("\n\n\tMENU - Persona")
        print("\n1.\tListar personas")
        print("2.\tAgregar persona")
        print("3.\tModificar persona")
        print("4.\tEliminar persona")
        print("  \tSalir (otra tecla)")
        return int(input("\n\tElija una opción: "))


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

    # Delete person
    personService.delete_person(2)

    print(personService.get_personList())  # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '30'}, 1: {'_name': 'CLAUDIO', '_surname': 'PICO', '_age': 33}}

    # Ahora trabajamos con el menú
    app = App()
    while True:
        opcion_persona = app.menu_person()
        if opcion_persona == 1:
            print(personService.get_personList())
        if opcion_persona == 2:
            _name = input("\n----> \tIngrese el nombre: ").upper()
            _surname = input("\n----> \tIngrese el apellido: ").upper()
            _age = input("\n----> \tIngrese la edad: ")
            per1 = Person(_name, _surname, _age)
            personService.add_person(per1)

        if opcion_persona == 3:
            key = int(
                input("\n----> \tIngrese la key de la persona a modificar: ")
                     )
            _name = input("\n----> \tIngrese el nuevo nombre: ").upper()
            _surname = input("\n----> \tIngrese el nuevo apellido: ").upper()
            _age = input("\n----> \tIngrese la nueva edad: ")
            per1 = Person(_name, _surname, _age)
            personService.update_person(key, per1)
        if opcion_persona == 4:
            key = int(
                input("\n----> \tIngrese la key de la persona a eliminar: ")
                     )
            personService.delete_person(key)
        if opcion_persona < 1 or opcion_persona > 4:
            break
