# -*- coding: utf-8 -*-

# 2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2 ** 1000?


def getDigitsSum(n,stack):
    if n == 0:
        print stack
        return sum(stack)
    else:
        stack.append(n%10)
        return getDigitsSum(n/10,stack)

print getDigitsSum(2**15,[])
print getDigitsSum(2**1000,[])


