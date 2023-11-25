class Math:
    def __init__(self, num) -> None:
        self.num = num
    
    def addtonum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3

m = Math(5)
m.addtonum(6)
print(m.num)

