#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:58:36 2020

@author: ravi
"""

year = int(input("Please Enter Year ==> "))

if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")