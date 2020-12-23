#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:29:47 2020

@author: ravi
"""
#import numpy as np

n,W = map(int,input().split())
v,w = [],[]
vpw = []

for i in range(n):
    v_temp,w_temp = map(int,input().split())
    v.append(v_temp)
    w.append(w_temp)
    vpw.append(v_temp / w_temp)

A = [0 for i in range(n)]
V = 0
for i in range(n):
    if W == 0:
        break
    i_max = vpw.index(max(vpw))
    vpw[i_max] = 0
    if w[i_max] > 0 :
        a = min(w[i_max],W)
        V = V + (a*(v[i_max]/w[i_max]))
        w[i_max] = w[i_max]-a
        A[i_max] = A[i_max] + a
        W = W-a
print(round(V,4))