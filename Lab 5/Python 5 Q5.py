#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:47:39 2023

@author: prateekgoswami
"""

a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
minimum= min(a,b)
i=2
j=1
while i>0:
    if i<=minimum:
        if a%i==0 and b%i==0:
            
            j=i
            print("LCM is", j)
            break
        else:
            i+=1
    else:
        LCM = (a*b)/j
        print("LCM is",LCM)
        break

