import random

comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water and 2 for Gun:\n"))

def game(user, comp):
    if user == comp:
        return -1

    elif user == 0 and comp == 1:
        return 1
    
    elif user == 2 and comp == 0:
        return 1
    
    elif user == 1 and comp == 2:
        return 1
    
    else:
        return 0

points = game(user, comp)

print(f"You: {user}")
print(f"Computer: {comp}")

if (points == -1):
    print("its a draw")

elif(points == 0):
    print("You Lose")

else:
    print("You Win")

