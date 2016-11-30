# coding: utf-8
from itertools import count, islice
import numpy as np

def isPrime(n):
    # donot use xrange because number large than 2 ** 32 - 1  (which is the maximum value for a C long) would cause stackoverflow
    # xrange(2147483647+1) # OverflowError
    return n > 1 and all(n%i for i in islice(count(2),np.sqrt(n)-1))

def getPrimeFactor(n):
    result = []
    i = 1
    while i < np.sqrt(n)+1:
        if isPrime(i) and n % i == 0:
            result.append(i)
        i += 1
    return result

print getPrimeFactor(13195)
print max(getPrimeFactor(600851475143))

