class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    
class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec



if __name__ == '__main__':

    pet1 = Dog('dog', 4, 'Лает')
    pet2 = Cat('cat', 2, 'Мяукает')
    pet3 = Bird('bird', 1, 'Поет')

    for pet in [pet1, pet2, pet3]:
        print(pet.get_spec())
