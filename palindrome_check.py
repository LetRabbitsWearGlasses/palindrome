#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in python 3.6 on: 2017-02-17
@author: G.E.Carpio
GitHub: @shaleshock
"""
import math

def palindrome_check(x):
    countr = 0
    half = int(math.floor((len(x))/2)) #halves the lenght of the list and rounds down decimals
 
    for e in range(half):
        if x[e] == x[-e-1]:
            countr = countr+1
            print (e+1,":",x[e],"and",x[-e-1], "are equal")
        else:
            print (e+1,":",x[e],"and",x[-e-1], "are NOT equal")
    print()
    
    ### RESULTS
    if countr == half:
        return True
    else:
        return False