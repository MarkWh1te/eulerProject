# coding:utf-8
from itertools import count, islice
from math import factorial
import numpy as np

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2),np.sqrt(n)-1))

def findallprimes(n):
    result = set()
    for i in range(1,n+1):
        if isPrime(i):
            result.add(i)
    return result


def findsmallest(n):
    result = 1
    for i in findallprimes(n):
        result *= i
    return result


print findsmallest(10) * 2 * 2 * 3
print findsmallest(20) * 2 * 2 * 2 *3
