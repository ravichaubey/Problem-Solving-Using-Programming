#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:16:53 2021

@author: ravi
"""

#input

m,n = map(int,input().split()) #size of array1 and array2
a = list(map(int,input().split())) #array a
b = list(map(int,input().split())) #array b

#process

def polynomial_multiplication(a,b,m,n):
    prod = [0] * (m+n-1)
    #initializing product array of size m+n-1 with zeros
    
    #multiply each element of array a to array b and stroe at prod
    for i in range(m):
        for j in range(n):
            prod[i+j] += a[i]*b[j]
    return prod

#output
print(polynomial_multiplication(a, b, m, n))