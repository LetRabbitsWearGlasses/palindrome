#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in python 3.6 on: 2017-02-17
@author: G.E.Carpio
GitHub: @shaleshock
"""
class CaseCheck:
    def __init__(self):
        self._result = None    #initiate "protected" variable: 'CaseCheck._result' to be used elsewhere
        
    def case_sensitivity(x):
        while True:
            user_input = input("Do you wish the results to be case sensitive (y/n)? ").lower().strip()
            user_input = user_input[0]
            if user_input in ["y","n"]:
                if user_input == "n":
                    CaseCheck._result = list(x.lower())
                else:
                    CaseCheck._result = list(x)
                break
            else:
                print("Unexpected input! Please try again.")
