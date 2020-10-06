#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:26:28 2020

@author: ravi
"""

n = int(input("Please enter number ==> "))
sumOfFactors = 0
for i in range(1,n+1):
    if n%i == 0:
        sumOfFactors += i
    
if (2*n) == sumOfFactors:
    print("Give Number is Perfect Number")
else:
    print("Give Number is not a Perfect Number")