#!/usr/bin/env python
#coding:utf8

'''
广度优先算法：
1、类似我们的朋友关系：一度朋友、二度朋友等，先从一度开始搜索
2、一度没搜索到时，搜索二度
3、用队列的方式保证搜索顺序，即将一度不符合的元素压入队列，之后肯定是按顺序弹出
4、借助了collections库的deque来做队列，一度的元素不符合条件时，压入队列，通过popleft()弹出队列
5、popleft()：左侧弹出，即先进先出FIFO
'''


from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

def search():

    # 准备数据
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom','jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    search_queue = deque()

    # 将数据装入队列，从自己开始搜索，从左到右压入
    search_queue += graph['you']
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print('find seller {}'.format(person))
                return True
            else:
                # 弹出的人不符合时，将这个人压入队列，位于尾部
                search_queue += graph[person]
                searched.append(person)
    return False

if __name__ == '__main__':
    search()