#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 08:45:12 2021

@author: ravi
"""

n = int(input())
arr = list(map(int,input().split()))
key = int(input())

low = 0
high = n-1

def binary_search(arr,low,high,key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return f"Element Found at {mid+1}th position.."
        elif key > arr[mid]:
            low = mid+1
        elif key < arr[mid]:
            high = mid -1
    return f"Pleae insert element at {low}th position.."

print(binary_search(arr, low, high, key))