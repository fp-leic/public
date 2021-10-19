# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:11:01 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def area(radius):
    """ returns the area of the circle with given radius."""
    b = 3.14159 * radius**2  # b is a temp variable that helps debugging
    return b

print(area(1))  # result is Pi


##drop temp variable used for debugging
#def area(radius):
#    return 3.14159 * radius * radius
#
#print(area(1))


## dead code
#def area(radius):
#    return 3.14159 * radius * radius
#    print("Hello")  # dead code
#print(area(1))


## with multiple returns
#def absolute_value(x):
#    if x < 0:
#        return -x
#    else:
#        return x
#
#print(absolute_value(-5))


## without the else
#def absolute_value(x):
#    if x < 0:
#        return -x
#    return x
#
#print(absolute_value(-5))


## there is here one path without return
#def bad_absolute_value(x):
#    if x < 0:
#        return -x
#    elif x > 0:
#        return x
#
#print(bad_absolute_value(0))

