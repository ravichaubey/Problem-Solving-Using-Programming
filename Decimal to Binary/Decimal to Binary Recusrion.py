#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:56:35 2021

@author: ravi
"""

def dtb(n):
    assert n == int(n),"Integers only"
    if n==0:
        return 0
    else:
        return n%2 + 10*dtb(int(n/2))
    
print(dtb(10.25))