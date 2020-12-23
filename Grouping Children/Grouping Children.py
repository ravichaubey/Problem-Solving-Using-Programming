#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:35:19 2020

@author: ravi
"""

n = int(input())
x = list(map(float,input().split()))

#1 2 3 4 5 6

def minGroups(x):
    R = []
    i = 0
    while i<n:
        l,r = x[i],x[i]+1
        R.append((l,r))
        i += 1
        while i<n and x[i]<=r:
            i+=1
    return R

print(minGroups(x))
            
       
    