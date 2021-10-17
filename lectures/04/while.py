#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  Oct  6 22:05:57 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

########################
# some examples to be interpreted
########################

##### accumulated sum

n = 6

current_sum = 0
i = 0
while i <= n:
   current_sum += i
   i += 1
print(current_sum)

##### accumulated sum with for

#n = 6
#
#current_sum = 0
#for i in range(n+1):
#    current_sum += i
#print(current_sum)

##### accumulated sum with sum()

#n = 6
#print(sum(range(n + 1)))

