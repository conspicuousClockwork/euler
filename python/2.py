import sys

input = int(sys.argv[1])

i = 0
count = 0
pair = [0,1]
while (pair[1] < input):
    i = pair[1]
    pair [1] += pair[0]
    pair [0] = i
    print pair [1]
    if not pair[1] % 2:
        count += pair[1]
print count
