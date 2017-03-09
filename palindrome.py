#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in python 3.6 on: 2017-02-17
@author: G.E.Carpio
GitHub: @shaleshock
"""
def palindrome(string ,ignorecase = True, ignorespace = True):
    """Checks whether a string is a palindrome. Ignores letter-case and spaces by default."""
    import math
    
    x = str(string)
    if ignorecase == True:
        x = x.lower()     
    if ignorespace == True:
        x = x.replace(' ','')
    
    countr = 0
    half = int(math.floor((len(x))/2))
 
    for e in range(half):
        if x[e] == x[-e-1]:
            countr = countr+1

    if countr == half:
        return True
    else:
        return False