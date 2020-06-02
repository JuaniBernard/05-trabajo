from repository import Repository


class PersonService:
    def get_personList(self):
        return Repository.person

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person):
        key = len(Repository.person)
        while key in Repository.person:
            key = key + 1
        Repository.person[key] = person.__dict__

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_person(self, key, person):
        if key in Repository.person:
            Repository.person[key]['_name'] = person._name
            Repository.person[key]['_surname'] = person._surname
            Repository.person[key]['_age'] = person._age
        else:
            print("\n---->\tERROR: La clave no existe.")

    # Elimina persona segun key del dic person
    def delete_person(self, key):
        if key in Repository.person:
            del Repository.person[key]
        else:
            print("\n---->\tERROR: La clave no existe.")
