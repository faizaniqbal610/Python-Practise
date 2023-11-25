class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
    
    def showDitals(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("Default language is Python")

e1 = Employee("Rehan", 356)
e2 = Programmer("Faizan", 406)

e2.showDitals()
e2.showLanguage()

