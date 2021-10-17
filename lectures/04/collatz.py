#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  Sat Oct  6 22:34:52 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

########################
# The Collatz 3n + 1 sequence
########################

n = 102737123

while n != 1:
    print(n, end=", ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
print(n, end=".\n")

# Collatz conjecture:
# “All positive integers will eventually converge to 1 using the Collatz rules”
