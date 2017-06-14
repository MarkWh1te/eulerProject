# coding:utf-8

# please run this script with python3 !!!!

# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
import numpy as np


def isAmicable(a,b):
    print(a,b)
    sum_a = np.sum(proper_divisors(a))
    sum_b = np.sum(proper_divisors(b))
    if sum_a == b and sum_b == a:
        return True
    return False

def proper_divisors(n):
    divisors = filter(lambda x:n%x==0,[i for i in range(1,n)])
    return divisors

def main(n):
    results = []
    all_num = [i for i in range(1,n)]
    for x in range(1,len(all_num)/2):
        a = all_num[x]
        if a in results:
            continue
        for y in range(len(all_num),len(all_num)/2,-1):
            b = all_num[y-1]
            if a == b:
                continue
            if isAmicable(a,b):
                results.append(a)
                results.append(b)
                print(results)
    return sum(results)


if __name__ == '__main__':
    print(isAmicable(220,284))
    print(main(10000))
