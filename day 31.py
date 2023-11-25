# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Islamabad"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# cities3 = cities.intersection(cities2)
cities3 = cities.symmetric_difference(cities2)
# print(cities3)

names = {"Faizan", "Rehan", "Aliyan", "Zohan"}
names2 = {"Faizan", "Ibraheem", "Khan", "Zohan"}

# print(names.isdisjoint(names2))
print(names.issuperset(names2))

names3 = {"Faizan", "Rehan", "Aliyan", "Zohan"}
names4 = {"Faizan", "Zohan"}

print(names4.issubset(names3))

school = {"class1", "class2"}
school.add("class3")
school.remove("class2")
print(school)

