#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in python 3.6 on: 2017-02-17
@author: G.E.Carpio
GitHub: @shaleshock
"""
from case_sensitivity import CaseCheck
from palindrome_check import palindrome_check

CaseCheck.case_sensitivity(input("Please enter a string of characters: "))

if palindrome_check(CaseCheck._result) == True:
    print ("Your input is a palindrome!")
else:
    print ("Your input is not a plaindrome!")