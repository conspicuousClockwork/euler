import sys
from math import sqrt
inputNum = (int(sys.argv[1]))

def getPrimes(pRange):
    primes = [2]
    for i in xrange(3, pRange + 1):
        primed = True
        for j in primes:
            print 'Checking ' + str(i) + ' against ' + str(j)
            if not i % j:
                primed = False
                break
            elif j >= sqrt(i):
                break
        if primed:
            primes.append(i)
    return primes


print getPrimes(inputNum)
