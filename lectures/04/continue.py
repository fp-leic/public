#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:58:38 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

for i in [12, 16, 17, 22, 25, 27]:
    if i % 2 == 1:      # If the number is odd
        continue        # Don't process it
    print(i)
print("\nDone.")
