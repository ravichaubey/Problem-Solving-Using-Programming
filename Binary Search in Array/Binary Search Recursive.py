#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 08:37:23 2021

@author: ravi
"""

import math
## Input
n = int(input())
arr = list(map(int,input().split()))
key = int(input())

## Process
low = 0
high = len(arr) - 1

def binary_search(arr,low,high,key):
    if low > high:
        return f"Please insert element at {low}th position.."
    mid = (low + high) // 2
    if arr[mid] == key:
        return f"Element found at {mid+1}th position.."
    elif key > arr[mid]:
        return binary_search(arr, mid + 1, high, key)
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key) 

## Output
print(binary_search(arr, low, high, key))