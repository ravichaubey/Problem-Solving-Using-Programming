#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:23:47 2020

@author: ravi
"""

n = int(input("Please enter number ==> "))

fact = 1

for i in range(1,n+1):
    fact *= i
print(fact)