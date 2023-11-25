class Employee:
    companyName = "Apple"
    def __init__(self, name) -> None:
        self.name = name
        self.raise_amount = 0.02
    
    def showDetails(self):
        print(f"The name of Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")
    
emp1 = Employee("Faizan")
emp1.raise_amount = 0.05
emp1.companyName = "Google"
emp1.showDetails()
emp2 = Employee("Zohan")
emp2.showDetails()

# Employee.showDetails(emp1)
