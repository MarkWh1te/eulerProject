# coding:utf-8

def findDivisor(n):
    return filter(lambda x:n%x==0,[i for i in xrange(1,n+1)])

# print(findFactors(21))

def getTriangular(n):
    return reduce(lambda x,y:x+y,[i for i in xrange(1,n+1)])

# print(getTriangular(7))

def getHighlyDivisorTriangular(n):
    i = 2 * 3 * 5* 7 * 11* 13 *17*19
    DivisorNumber = 1
    while DivisorNumber < n:
        print i
        print DivisorNumber
        DivisorNumber = len(findDivisor(getTriangular(i)))
        i += 1
    return getTriangular(i-1)

print(getHighlyDivisorTriangular(500))
