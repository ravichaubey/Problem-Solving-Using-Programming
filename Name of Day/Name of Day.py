#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:44:41 2020

@author: ravi
"""

days = {1:"Sunday",
        2:"Monday",
        3:'Tuesday',
        4:'Wednesday',
        5:'Thursday',
        6:'Friday',
        7:'Saturday'
        }

day = int(input("Pleae Enter day starting 1 for sunday ==> "))

print(days.get(day,"Invalid Input"))