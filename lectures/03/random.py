#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:23:13 2018

@author: jlopes

Code adapted from the book:

Brad Miller and David Ranum, Learning with Python: Interactive Edition
"""

###### random() returns a floating point number in the range [0.0, 1.0)

import random

prob = random.random()
print(prob)

###### randrange function generates an integer between its lower and upper argument

#diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
#print(diceThrow)

###### converted the result of the method call to a number in the range [0.0, 5.0)

#prob = random.random()
#result = prob * 5
#print(result)
