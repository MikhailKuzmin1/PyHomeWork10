from animals import Cat, Dog, Bird

class AnimalsFactory():
    def new_animal(self, type_an, name, age, spec ):
        if type_an.lower() == "cat":
            return Cat(name, age, spec)
        elif type_an.lower() == "dog":
            return Dog(name, age, spec)
        elif type_an.lower() == "bird":
            return Bird(name, age, spec)
        
factory = AnimalsFactory()
pet1 = factory.new_animal('Dog', 'Sharick', 2, 'Лает')
pet2 = factory.new_animal('bird','Galka', 1, 'Летает')   

print(pet1.get_spec())
print(pet2.get_spec())


