#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:28:48 2020

@author: ravi
"""

n = int(input("Please enter number ==> "))
flag = 1
for i in range(2,n):
    if n%i == 0:
        flag = 0
        break
if flag:
    print("Prime Number")
else:
    print("Not a Prime Number")