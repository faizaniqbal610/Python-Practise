class Vactor:
    def __init__(self, i, j, k) -> None:
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return Vactor(self.i + x.i, self.j + x.j, self.k + x.k)
v1 = Vactor(3, 5, 6)
print(v1)
v2 = Vactor(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1+v2))
