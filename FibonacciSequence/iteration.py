#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(n):
    f = 1
    g = 1
    for v in range(n-1):
        a = f
        b = g
        f = b
        g = a + b
    return f

# 计算43 一下子就出来了哦
print(fib(43))