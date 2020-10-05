#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:50:08 2020

@author: ravi
"""

operations = {1:"Add",
              2:"Subtract",
              3:"Multiply",
              4:"Divide",
              5:"Exit"
    }
while True:
    print("\n")
    for i in operations.items():
        print(i)
    choice = int(input("Please select an Option ==> "))
    if choice == 1:
        a,b = map(float,input("Enter Two Numbers ==> ").split())
        print("Addition ==> ",a+b)
    elif choice == 2:
        a,b = map(float,input("Enter Two Numbers ==> ").split())        
        print("Subtraction ==> ",a-b)
    elif choice == 3:
        a,b = map(float,input("Enter Two Numbers ==> ").split())
        print("Multiplication ==> ",a*b)
    elif choice == 4:
        a,b = map(float,input("Enter Two Numbers ==> ").split())
        print("Division ==> ",a/b)
    else:
        break