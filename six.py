# coding:utf-8


def sumSquare(n):
    return sum([x ** 2 for x in xrange(1,n+1)])

def squareSum(n):
    return sum([x for x in xrange(1,n+1)]) ** 2

def square_sum_difference(n):
    return abs(squareSum(n) - sumSquare(n))
print square_sum_difference(10)
print square_sum_difference(100)
