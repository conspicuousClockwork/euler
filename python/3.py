import sys

inputNum = int(sys.argv[1])
def hPrime(num):
    highestPrime = 0
    i = 2
    while i <= num:
        if highestPrime:
            print str(highestPrime) + ' was returned to me as the highest prime'
            return highestPrime
        elif i == num:
            print str(i) + ' is the highestPrime'
            return i
            break
        elif not num % i:
            print str(num) + ' is divisible by ' + str(i) + ', we must go deeper'
            highestPrime = hPrime((num / i))
        i = i + 1

print hPrime(inputNum)
