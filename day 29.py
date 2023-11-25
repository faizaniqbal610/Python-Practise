# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

def fibonacci(f):
    if f==0:
        return 0
    elif f==1:
        return 1
    else:
        return fibonacci(f-1) + fibonacci(f-2)

print(fibonacci(10))

