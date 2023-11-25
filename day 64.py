class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

srting = "Faizan-320"
e1 = Employee.fromStr(srting)
print(e1.name)
print(e1.salary)
