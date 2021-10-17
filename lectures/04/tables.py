#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  Sun Oct  7 10:29:14 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

########################
# tables
########################

# values and 2 raised to the power of that value

print("n", '\t', "2**n")     # table column headings
print("---", '\t', "-----")

for x in range(11):          # generate values for columns
    print(x, '\t', 2 ** x)

# multiples of 2, all on one line
print()
for i in range(1, 7):
    print(2 * i, end="  ")
print("\nto be continued...")
