def func1():
    try:
        l = [1, 3, 5, 89, 0]
        i = int(input("Enter the Index: "))
        print(l[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("i am Always Executed")
    

x = func1()
print(x)
