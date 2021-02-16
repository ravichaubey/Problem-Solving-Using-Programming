#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:28:54 2021

@author: ravi
"""

def isCommon(arr1,arr2):
    if set(arr1) & set(arr2):
        return True
    return False

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

print(isCommon(a, b))