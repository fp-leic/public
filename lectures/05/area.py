#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:07:36 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

import math


# known function
def distance(x1, y1, x2, y2):
    """computes the distance between 2 pints"""
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

# known function
def area(radius):
    """computes the area of a circle with radius"""
    return 3.14159 * radius**2

## step 1
#def area_of_circle(xc, yc, xp, yp):
#    radius = distance(xc, yc, xp, yp)
#    print(radius)

## step 2
#def area_of_circle(xc, yc, xp, yp):
#    radius = distance(xc, yc, xp, yp)
#    result = area(radius)
#    print(result)

## step 3
#def area_of_circle(xc, yc, xp, yp):
#    radius = distance(xc, yc, xp, yp)
#    result = area(radius)
#    return result

## step 4
#def area_of_circle(xc, yc, xp, yp):
#    return area(distance(xc, yc, xp, yp))

# center (0,0)
# perimiter (0,1)
print(area_of_circle(0, 0, 0, 1))
