#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:06:40 2021

@author: ravi
"""

n = int(input())
arr = list(map(int,input().split()))

def selection_sort(arr,n):
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr

print(selection_sort(arr, n))