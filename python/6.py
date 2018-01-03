import sys

inputNum = (int(sys.argv[1]))


def sumSquare(inputRange):
    squares = []
    skip = []
    for i in xrange(2, inputRange + 1):
        if not i in skip:
            j = i**2
            squares.append(j)
            while j <= inputRange:
                skip.append(j)
                j = j**2
                squares.append(j)
    return reduce((lambda x, y: x+y),squares) + 1

def squareSum(inputRange):
    return sum(xrange(1, inputRange+1))**2


print squareSum(inputNum) - sumSquare(inputNum)
