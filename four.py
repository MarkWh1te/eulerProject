# coding:utf-8
from itertools import count, islice
import numpy as np


def isPalindrome(n):
    return str(n) == str(n)[::-1]

# print isPalindrome(12321)
# print isPalindrome(113141)

def generateAllproduct():
    result = []
    for x in xrange(100,1000):
        for y in xrange(100,1000):
            result.append(x*y)
    return result

print generateAllproduct()

print max(filter(isPalindrome,generateAllproduct()))
