class Person:
    name = "Faizan"
    occupation = "Software Developer"
    network = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Zohan"
a.occupation = "Game Developer"

b = Person()
b.name = "Hira"
b.occupation = "Doctor"

# print(a.name, a.occupation)
a.info()
b.info()

