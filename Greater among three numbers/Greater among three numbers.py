#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:42:32 2020

@author: ravi
"""
a,b,c = map(int,input("Please Enter three numbers ==> ").split())

if a>b and a>c:
    print("First number is Greatest")
else:
    if b>c:
        print("Second Number is Greatest")
    else:
        print("Third Number is Greatest")