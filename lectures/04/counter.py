#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  Sat Oct  6 23:47:10 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

########################
# counter
########################

##### counts the number of decimal digits in a positive integer

n = 3029
count = 0
while n != 0:
    count = count + 1
    n = n // 10
print(count)

##### only count digits that are either 0 or 5

#n = 2574301453
#count = 0
#while n > 0:
#    digit = n % 10
#    if digit == 0 or digit == 5:
#        count = count + 1
#    n = n // 10
#print(count)
