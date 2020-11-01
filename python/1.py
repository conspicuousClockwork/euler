import sys

# support variable number of arguments by using a slice
input = map(int, sys.argv[1:])
mainNumber = input[0] - 1
numbs = input[1:]
# we use a set to avoid duplicates
mult = set()

# scan through all numbers
for i in numbs:
    mod = int(mainNumber / i)
    if mod:
        for j in range(mod):
            mult.add(i * ( j + 1))

# aggregate and print data
print reduce((lambda x, y: x + y), mult)
