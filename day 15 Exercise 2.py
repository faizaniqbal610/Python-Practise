import time

time__ = time.strftime("%H:%M:%S")
print(time__)

hours = int(time.strftime("%H"))

if(hours >=0 and hours <= 12):
    print("Good Morning Sir!")

elif hours >= 12 and hours < 17:
    print("Good Afternoon Sir!")

else:
    print("Good Evening Sir")

