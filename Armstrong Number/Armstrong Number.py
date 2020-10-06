#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:31:36 2020

@author: ravi
"""

n = input("Please enter number ==> ")

sumOfDigit = 0

for i in n:
    i = int(i)
    sumOfDigit += i**3 
if sumOfDigit == int(n):
    print("Armstrong Number")
else:
    print("Not a Armstrong Numbr")