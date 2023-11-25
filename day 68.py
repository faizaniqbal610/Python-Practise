class Shape:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y

class Circul(Shape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y)
        self.radius = radius
    
    def area(self):
        return 3.14 * super().area()

rec = Shape(3, 5)
c = Circul(3, 5, 7)

print(c.area())

