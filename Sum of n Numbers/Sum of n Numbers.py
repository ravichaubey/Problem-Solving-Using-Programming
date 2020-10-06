#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:22:24 2020

@author: ravi
"""

n = int(input("Please enter number ==> "))

res = 0

for i in range(n+1):
    res += i
print("Sum is ",res)