class Employee:
    def __init__(self, name, id) -> None:
        self.__name = name
        self._id = id

class Student(Employee):
    pass

a = Employee("Faizan", 657)
b = Employee("Rehan", 943)
# print(a.__name) # Cannot be accessed directly
print(a._Employee__name) # Can be accessed indirectly
print(a._id)
print(b._id)
print(a.__dir__())

