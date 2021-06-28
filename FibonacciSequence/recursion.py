#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 计算10，一下子就出来了
print(fib(10))

# 计算43，我的天，你要等很久了
# 知道为什么吗？
print(fib(43))