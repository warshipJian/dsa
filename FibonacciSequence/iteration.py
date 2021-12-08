#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
0,1
1,2
2,3
'''

def fib(n):
    f = 0
    g = 1
    while n > 1:
        g = g + f
        f = g - f
        n -= 1
    return g


# 计算43 一下子就出来了哦
print(fib(43))