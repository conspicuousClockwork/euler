import sys
from math import sqrt
inputNum = (int(sys.argv[1]))

def getPrimes(pRange):
    primes = [2]
    primeCount = 1
    currentPrime = 2
    i = 3
    while primeCount < pRange:
        primed = True
        for j in primes:
            if not i % j:
                primed = False
                break
            elif j >= sqrt(i):
                break
        if primed:
            primeCount = primeCount + 1
            currentPrime = i
            primes.append(i)
        i = i + 1
    return currentPrime


print getPrimes(inputNum)
