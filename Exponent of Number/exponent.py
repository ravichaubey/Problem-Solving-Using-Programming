#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:56:05 2021

@author: ravi
"""

def power(base,expo):
    assert expo >= 0 and expo == int(expo),"Exponenet Must be Positivi Integers"
    if expo == 0:
        return 1
    elif expo == 1:
        return base
    else:
        return base * power(base, expo-1)
    
print(power(int(input()), int(input())))