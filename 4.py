import sys

inputNum = (int(sys.argv[1]))

def isPal(i):
    pal = str(i)
    if pal[0:int(len(pal))/2+int(len(pal))%2] == pal[int(len(pal))/2:int(len(pal))][::-1]:
        return True
    return False

def largestNum(i):
    j = ''
    for k in range(0, inputNum):
        j = j + '9'
    return int(j)

def searchForMult(length):
    maxN = largestNum(length)
    for i in xrange(maxN ** 2,0,-1):
        if isPal(i):
            for j in xrange(i-1,0,-1):
                if isPal(j):
                    iState = i % 2 * -2
                    for k in xrange(maxN,0,iState):
                        kState = k % 2 * -2
                        for l in xrange(maxN,0,kState):
                            product = k * l
                            if product <= j:
                                break
                            elif product == i:
                                return [k,l]
                    break

result = searchForMult(inputNum)
print str(result[0])+' and '+str(result[1])+' create '+str(result[0]*result[1])
