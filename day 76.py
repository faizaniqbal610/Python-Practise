import time

def usingWhile():
    i = 0
    # while i<50000:
    while i<100:
        i = i+1
        print(i, end=", ")

def usingFor():
    # for i in range(50000):
    for i in range(100):
        print(i, end=", ")

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print("While in", time.time() - init, "Secoud")
print("For in", t1, "Second")

time.sleep(3)
print("this is print after 3 sec")

t = time.localtime()
forMatted = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(forMatted)
