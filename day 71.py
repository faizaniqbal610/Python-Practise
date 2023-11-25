class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made my animal")
    
class Dog(Animal):
    def __init__(self, name, species, breed) -> None:
        super().__init__(name, species)
        self.breed = breed

d = Dog("Dog", "Dog", "Dog")
d.make_sound()
