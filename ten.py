# coding:utf-8

from itertools import count, islice
import numpy as np

def isPrime(n):
    # donot use xrange because number large than 2 ** 32 - 1  (which is the maximum value for a C long) would cause stackoverflow
    # xrange(2147483647+1) # OverflowError
    return n > 1 and all(n%i for i in islice(count(2), np.sqrt(n)-1))


def sumPrime(n):
    return reduce(lambda x,y:x+y, filter(isPrime,[i for i in islice(count(2),n-1)]))

print sumPrime(10)
print sumPrime(2000000)



