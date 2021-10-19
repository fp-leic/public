#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:23:02 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


# step 1
def distance(x1, y1, x2, y2):
    return 0.0

print(distance(1, 2, 4, 6))
# When testing a function, it is useful to know the right answer.

## step 2
#def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    print("dx =", dx)
#    dy = y2 - y1
#    print("dy =", dy)
#    return 0.0
#
#print(distance(1, 2, 4, 6))

## step 3
#def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    dsquared = dx*dx + dy*dy
#    print(dsquared)
#    return 0.0
#
#print(distance(1, 2, 4, 6))

## step 4
#def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    dsquared = dx*dx + dy*dy
#    return dsquared**0.5
#
#print(distance(1, 2, 4, 6))

## another impl
#import math
#
#def distance(x1, y1, x2, y2):
#    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

print(distance(1, 2, 4, 6))
