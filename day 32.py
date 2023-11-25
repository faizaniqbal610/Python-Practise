info = {
    "name":"Faizan",
    "age":17,
    "eligible": True
}

print(info)
print(info["name"])

# print(info["eligible2"])
print(info.get("eligible2"))


print(info.keys())
print(info.values())

for i in info.keys():
    print(f"{i} is {info[i]}")

print(info.items())

