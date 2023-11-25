class Employee:
    name = "Faizan"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    
    def __str__(self) -> str:
        return f"The name of employee is {self.name} str"
    
    def __repr__(self):
        return f"The name of employee is {self.name} repr"

e = Employee()
print(e.name)
print(len(e))
print(e)

