# coding:utf-8
import numpy as math
# recurrentation
# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# Phi = (1 +math.sqrt(5))/ 2
# Psi = 1 - Phi

# def fib_f(n):
#     print n
#     return (Phi ** n - (Psi ** n))/math.sqrt(5)


a = b = 1
result = 0
while a < 4000000:
    if a % 2 == 0:
        result += a
    a,b = b,a+b
print result

