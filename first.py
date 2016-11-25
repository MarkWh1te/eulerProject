# coding:utf-8


def m_3_5(n):
    x = 1
    result = set()
    while x < n:
        if x % 3 == 0:
            result.add(x)
        if x % 5 == 0:
            result.add(x)
        x += 1
    return sum(result)
# print m_3_5(10)
print m_3_5(1000)
