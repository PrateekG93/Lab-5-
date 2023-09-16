#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:45:31 2023

@author: prateekgoswami
"""
#a)

i= 1
n= int(input("Enter number of lines you want to print: "))
while i<=n:
    print("* "*i)
    i= i+1
    
    
#b)

i= 1
n= int(input("Enter number of lines you want to print: "))
a=(2*n)-1
while i<=n:
    print(" "*a,"* "*i)
    i= i+1
    a-=2
    
    
    
#c)
i= 1
n= int(input("Enter number of lines you want to print: "))
a=2*n-1
while i<=(2*n):
    print(" "*a,"* "*i)
    i= i+2
    a-=2