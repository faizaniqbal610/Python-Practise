a = input("Enter the number: ")
print(f"The Multiplcation Table of {a} is")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some line of code")
print("End of Program")

