#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:30:08 2020

@author: ravi
"""

d = int(input("Enter Distance from A to B ==> ")) #distance from A to B
m = int(input("Enter Atmost Distance Car can travel with full tank ==> ")) #Atmost distance that car #can travel with full tank

n = int(input("Enter Number of Fuel Station between A and B ==> ")) #Number of Stops for Fuel Station

fuelStations = list(map(int,input().split("Enter Fuel Station ==> ")))
fuelStations.insert(0,0)
fuelStations.append(d)


def minRefills(fuelStations,n,m):
    minRefillsNum = 0
    currentRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while(currentRefill <= n and (fuelStations[currentRefill + 1] - fuelStations[lastRefill])<=m):
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill<=n:
            minRefillsNum+=1
    return minRefillsNum
        
print(minRefills(fuelStations,n,m))
