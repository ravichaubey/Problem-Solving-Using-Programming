#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:36:02 2020

@author: ravi
"""

m,n = map(int,input("Please Enter two numbers ==> ").split())

while True:
    if m == n:
        print(m)
        break
    elif m>n:
        m = m-n
    else:
        n = n-m