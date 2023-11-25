def greet(fx):
    def mfx(*arge, **kwargs):
        print("Good Moring")
        fx(*arge, **kwargs)
        print("Thankes for using this")
    return mfx

@greet
def hello():
    print("Hello World!!!")

hello()

@greet
def add(a, b):
    print(a+b)

add(2, 1)

