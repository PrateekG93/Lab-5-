#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:56:29 2023

@author: prateekgoswami
"""

i= 1
n= int(input("Enter number of lines you want to print: "))
a=n
while i<=(n):
    while a>0:
        print(" "*a,"* "*i)
        i= i+1
        a-=1
