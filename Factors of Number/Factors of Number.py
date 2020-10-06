#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:25:31 2020

@author: ravi
"""

n = int(input("Please enter number ==> "))
for i in range(1,n+1):
    if n%i == 0:
        print(i,end = ",")