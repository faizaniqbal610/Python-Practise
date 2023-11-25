# MAP

cube = lambda x: x*x*x

print(cube(2))

l = [1, 3, 5, 2, 8]

# newl = []
# for i in l:
#     newl.append(cube(i))

newl = list(map(cube, l))

print(newl)

# FILTER

moreNewL = list(filter(lambda a:a> 4, l))

print(moreNewL)

# REDUCE

from functools import reduce

oneMoreNewL = reduce(lambda a,b:a+b, l)

print(oneMoreNewL)

