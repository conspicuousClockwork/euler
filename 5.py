import sys

inputNum = (int(sys.argv[1]))

#Returns true if a prime number
def isPrime(i):
    for j in xrange(2, i):
        #only checks up to a little over half the number
        if j == int(i/2 + 1):
            return True
        elif not i % j:
            return False

#Returns list of all prime numbers in range
def prdPrime(input):
    #Initialize list with 2
    primed = [2]
    for i in xrange(3, input + 1):
        if isPrime(i):
            primed.append(i)
    return primed

#Returns list of all simplified numbers in range
def prdSimp(input, primes):
    #Set of numbers that are multiples of higher numbers in range
    simped = set()
    #List of highest factored elements
    notSimped = []
    #For every number, check lower numbers if they are divisible or not
    for i in xrange(input, 1,-1):
        #If i is in primes, ignore it
        if i in simped or i in primes:
            continue
        #Check all lower numbers if they are divisible or not
        for j in xrange(i - 1, 1, -1):
            #If it is divisible and not already in the set simped, add to simp
            if not i % j and not j in simped:
                simped.add(j)
        #If i is not in simped or in primes, add to list notSimped
        if not i in simped or i in primes:
            notSimped.append(i)
    return notSimped

def prdCombine(primes, simps):
    #For every prime, check if values in list simps is divisible by said prime
    for i in primes:
        #For every element in list simps, check if previous prime can be divided
        for index, j in enumerate(simps):
            #If it is divisible, divide and update value
            if not j % i:
                #If value is 2, ignore it
                if j/i == 2:
                    simps[index] = 1
                else:
                    simps[index] = j/i
    print simps
    #Return product of both lists
    return reduce((lambda x, y: x * y), primes) * reduce((lambda x, y: x * y), simps)

primeSet = prdPrime(inputNum)
simpSet = prdSimp(inputNum, primeSet)
print prdCombine(primeSet,simpSet)
