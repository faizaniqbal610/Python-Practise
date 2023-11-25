list1 = [["Which Progarming language you use now", "C++", "Java", "Python", "JavaScript", "c"],
        ["Which Progarming language you use now", "C++", "Java", "Python", "JavaScript", "c"],
        ["Which Progarming language you use now", "C++", "Java", "Python", "JavaScript", "c"],
        ["Which Progarming language you use now", "C++", "Java", "Python", "JavaScript", "c"],
        ]

# print(list1[0][0])

money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
win_money = 0
i=0

while True:
    if i<len(list1):
        print(list1[i][0])
        print("a.", list1[i][1], end="                  ")
        print("b.", list1[i][2])
        print("c.", list1[i][3], end="                  ")
        print("d.", list1[i][4])
        answer = input("Enter the answer in a, b, c, d: ")

        if answer == list1[i][5]:
            print(f"\nyou win {money[i]} reeps\n")
            win_money = win_money + money[i]
        else:
            print("Your answer is wrong you loss")
            print("\nYour Total money is", win_money, "\n")
            break
        i = i+1
        
    else:
        print("Congratulation You Complete all Levels")
        print("\nYour Total money is", win_money, "\n")
        break
    

