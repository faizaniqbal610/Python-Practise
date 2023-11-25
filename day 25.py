countries = ("Spain", "Italy", "Pakistan", "India", "England", "Germany")

temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("China", "India", "Vietnam")
# southEastAsia = countries + countries2
# print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2 ,3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(3, 4, 7)
res = len(tuple1)
print("Count of 3 in tuple1 is:", res)

