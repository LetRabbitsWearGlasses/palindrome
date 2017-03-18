#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in python 3.6 on: 2017-02-17
@author: G.E.Carpio
GitHub: @shaleshock
"""
def palindrome(string ,ignorecase = True, ignorespace = True):
    """Checks whether a string is a palindrome. 
       Ignores letter-case and spaces by default.
    """
    import math
    
    if ignorecase == True:
        string = string.lower()
    if ignorespace == True:
        string = string.replace(' ','')

    counter = 0
    midpoint = int(math.floor((len(string))/2))

    for e in range(midpoint):
        counter += string[e] == string[-e-1]

    if counter == midpoint:
        return True
    else:
        return False