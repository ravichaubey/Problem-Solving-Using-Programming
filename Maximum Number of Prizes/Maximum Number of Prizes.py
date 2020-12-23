#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:37:03 2020

@author: ravi
"""
def optimal_summands(n):

    summands = [1]
    n -= 1
    while n:
        last_element = summands[-1]

        if (last_element + 1) * 2 <= n:
            n -= last_element + 1
            summands.append(last_element + 1)
        else:
            if last_element >= n:
                n += summands.pop()
            summands.append(n)
            n = 0

    return summands


if __name__ == "__main__":
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")