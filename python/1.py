import sys

input = map(int, sys.argv[1:])
mainNumber = input[0] - 1
numbs = input[1:]
mult = set()
for i in numbs:
    mod = int(mainNumber / i)
    if mod:
        for j in range(mod):
            mult.add(i * ( j + 1))
print reduce((lambda x, y: x + y), mult)
