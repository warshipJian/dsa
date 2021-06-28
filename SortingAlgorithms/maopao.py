#!/usr/bin/env python
#coding:utf8

'''
冒泡排序
'''

def swap(a,left_idx,right_idx):
    left_v = a[left_idx]
    right_v = a[right_idx]
    a[left_idx] = right_v
    a[right_idx] = left_v
    return a

def sort(arr):
    max = len(arr) - 1
    for i in range(max,0,-1):
        for j in range(i):
            print(j)
            if arr[j] > arr[j+1]:
                arr = swap(arr,j,j+1)
                print(arr)
    return arr

if __name__ == '__main__':
    print(sort([1,6,7,3,2,5,4,8,9,0,-2,-99,100,98]))