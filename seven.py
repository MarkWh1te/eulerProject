# coding:utf-8

from itertools import count, islice
import numpy as np

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2),np.sqrt(n)-1))

def findNstprime(n):
    result = []
    i = 2
    while len(result) <= n:
        if isPrime(i):
            result.append(i)
        i += 1
    return result[n-1]

print findNstprime(10001)
