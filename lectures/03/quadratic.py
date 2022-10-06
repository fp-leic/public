#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:36:24 2022

@author: jlopes
"""

# Find the roots of quadratic equation ax^2 + bx + c = 0
# were a, b and c are real numbers and a <> 0

import math

# first, get the coefficients
a = float(input("give me the a: "))
b = float(input("give me the b: "))
c = float(input("give me the c: "))

if a == 0:
    print("Invalid quadratic equation!")
else:
    # second, calculate the discriminant using the formula
    delta = b*b-4*a*c

    # third, checking the 3 condition for delta
    if delta > 0:
        # for x^2 + 5x + 6 roots are "-2.0 -3.0"
        p1 = -b/(2*a)
        p2 = math.sqrt(delta)/(2*a)
        print("The roots are:", p1+p2, p1-p2)
    elif delta == 0:
        # for x^2 +2x +1 roots are "-1.0 -1.0"
        p1 = -b/(2*a)
        print("The roots are:", p1, p1)
    else:  # when the delta is less than 0
        # for 2x^2 + 2x + 1, roots are "-0.5+i0.5 -0.5-i0.5""
        p1 = -b/(2*a)
        p2 = math.sqrt(-delta)/(2*a)
        print("The roots are:", str(p1)+"+i"+str(p2), str(p1)+"-i"+str(p2))
