#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:31:12 2023

@author: prateekgoswami
"""

N= int(input("Enter a number: "))
i=0
while i<100:
    i=i+1
    if i%N==0:
        continue
    print(i)