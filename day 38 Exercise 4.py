# Secret languag app

def coding(str):
    sp = str.split(" ")
    allWords = []
    for words in sp:
        if len(words)>=3:
            ch1 = "kdr"
            ch2 = "mal"
            word = ch1+words[1:]+words[0]+ch2
            allWords.append(word)
        else:
            word = words[::-1]
            allWords.append(word)
    return (" ".join(allWords))

def decoding(str):
    sp = str.split(" ")
    allWords = []
    for words in sp:
        if len(words)>=3:
            word1 = words[3:len(words)-3]
            word = word1[len(word1)-1]+word1[0:len(word1)-1]
            allWords.append(word)
        else:
            word = words[::-1]
            allWords.append(word)
    return (" ".join(allWords))

print("What you want to doing coding or decoding")
a = int(input("1 for Coding and 2 for decoding: "))

if a == 1:
    co = coding(input("Enter the massage: "))
    print(co)
elif a == 2:
    de = decoding(input("Enter the massage: "))
    print(de)
else:
    print("Your input is wrong")

