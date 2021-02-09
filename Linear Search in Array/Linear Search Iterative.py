#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:33:53 2021

@author: ravi
"""

##Input
n = int(input())
arr = list(map(int,input().split()))
key = int(input())

## Process
low = 0
high = n

def linear_search(arr,low,high,key):
    flag = 0
    for i in range(low,high):
        if arr[i] == key:
            flag = 1
            return f"Found at {i+1}th Position"
    if flag == 0:
        return "Not Found"
    
## Output

print(linear_search(arr, low, high, key))