# coding:utf-8

pontential = [(x,y,1000-x-y) for x in range(1,1000) for y in range(1,1000) if x+y <1000]
result = filter(lambda (x,y,z):x**2 + y **2 == z**2,pontential)

print result
