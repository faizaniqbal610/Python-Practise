# Strings are immutable

a = "!!! Faizan!!! !!!!"
print(len(a))

print(a.upper())
print(a.lower())

print(a.rstrip("!"))
print(a.replace("Faizan", "Rehan"))
print(a.split(" "))

blogHeading = "introduction to Python"

print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(a.count("Faizan"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str2 = "He's name is Dan. he is an honest man."
print(str2.find("is"))
print(str2.index("is"))

str3 = "WelcomeToTheConsole00"
print(str3.isalnum())
print(str3.isalpha())
print(str3.islower())
print(str3.isupper())

str4 = "We wish you a Merry Christmas\n"
print(str4.isprintable())
print(str4.isspace())
print(str3.istitle())

print(str4.swapcase())
