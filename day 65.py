class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

p = Person("Faizan", 17)

print(p.__dict__)

x = [1, 2, 3]
print(dir(x))

print(help(Person))

