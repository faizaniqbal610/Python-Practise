x = int(input("Enter the Value of X: "))
# x is the variable to match
match x:
    case 0:
        # if x is 0
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    case _:
        print(f"x is {x}")
    # Default case(will only be matched if the above cases were not mached)

