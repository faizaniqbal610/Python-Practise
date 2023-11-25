# a = int(input("Enter your age: "))
a = 19
print("Your age is:", a)

if a > 18:
    print("You can drive")

else:
    print("You cannot drive")

applePrice = 10
budget = 200

if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apple to the cart.")

elif (budget - applePrice > 70):
    print("its okay you can buy")

else:
    print("Alexa, do not add Apple to the cart.")
