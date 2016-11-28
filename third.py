# coding: utf-8
from itertools import count, islice
import numpy as np

def isPrime(n):
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

