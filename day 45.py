x = 4 # globle variable
print(x)

def hello():
    global x
    x = 5 # locak variable
    y = 1 # local variable
    print(f"The local x is {x}")
    print(y)
    print("Hello Faizan!")

print(f"The globle x is {x}")
hello()
x = 5 # globle variable
print(f"The globle x is {x}")


