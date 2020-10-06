#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:34:31 2020

@author: ravi
"""

n = input("Please enter number ==> ")

if int(n) == int(n[::-1]):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")