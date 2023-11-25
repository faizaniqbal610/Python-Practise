class Employee:
    def __init__(self, name, age, id) -> None:
        self.name = name
        self.age = age
        self.id = id
    
    def showDitel(self):
        print(f"The name is {self.name}, its age is {self.age} and he has id {self.id}")

class programmer(Employee):
    def __init__(self, name, age, id, lang) -> None:
        super().__init__(name, age, id)
        self.lang = lang

Faizan = programmer("Faizan", 17, 73, "Python")
Faizan.showDitel()
