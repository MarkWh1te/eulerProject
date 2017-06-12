# coding:utf-8
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def calFactorial(n):
    if n == 1:
        return 1
    return n * calFactorial(n-1)

def digitSum(n):
    if n < 10:
        return n
    return n % 10 + digitSum(n/10)




if __name__ == '__main__':
    print(digitSum(calFactorial(100)))

