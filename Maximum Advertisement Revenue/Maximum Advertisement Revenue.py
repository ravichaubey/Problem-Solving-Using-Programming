#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:56:37 2020

@author: ravi
"""

import numpy as np

n = int(input())
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))
ai.sort()
bi.sort()

ai = np.array(ai)
bi = np.array(bi)

res = sum(ai*bi)
print(res)