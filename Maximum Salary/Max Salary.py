#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:59:21 2020

@author: ravi
"""

n = int(input())
lst = [int(i) for i in input().split()]


def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largestnumber(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer

print(''.join([str(i) for i in largestnumber(lst)]))