import sys

inputNum = int(sys.argv[1])
def hPrime(num):
    # set base value, this function uses recursion
    highestPrime = 0
    # first prime is 2
    i = 2
    # establish break case
    while i <= num:
        # collapse all recursion once found
        if highestPrime:
            print str(highestPrime) + ' was returned to me as the highest prime'
            return highestPrime
        # end case
        elif i == num:
            print str(i) + ' is the highestPrime'
            return i
            break

        # if not, we want to sub divide and find highest prime
        elif not num % i:
            print str(num) + ' is divisible by ' + str(i) + ', we must go deeper'
            highestPrime = hPrime((num / i))
        i = i + 1

print hPrime(inputNum)
