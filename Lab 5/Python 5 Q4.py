#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:59:20 2023

@author: prateekgoswami
"""

N= int(input("Enter the number: "))
x= int(input("Enter number: "))
count1= 0
count2=0
while x!=-999:
    if x%N==0:
        count1+=1
    else:
        count2+=1
    x= int(input("Enter number: "))
print("Number of divisible numbers: ",count1)
print("Number of non divisible numbers: ",count2)