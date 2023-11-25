class Person:
    def __init__(self, name, occupation) -> None:
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Faizan", "Software Developer")

b = Person("Zohan", "Game Developer")

# print(a.name, a.occupation)
a.info()
b.info()

