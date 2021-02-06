#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:29:23 2021

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
    if low >= high:
        return "Not Found"
    if arr[low] == key:
        return f"Found at {low+1}th Position"
    return linear_search(arr, low+1, high, key)

## Output

print(linear_search(arr, low, high, key))