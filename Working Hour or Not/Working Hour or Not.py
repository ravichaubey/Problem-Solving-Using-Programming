#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:40:37 2020

@author: ravi
"""

start,end = map(int,input("Please Enter Working Hour in 24 Hour Format\nStart time and End Time ==> ").split())

if start>=9 and end<=18:
    print("Working Hour")
else:
    print("Not a Working Hour")