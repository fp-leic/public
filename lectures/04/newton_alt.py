#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023

@author: nmm
"""

"""
Lecture 04: Iteration

Use Newton's Method to find roots (or zeroes) of a function.
"""

x0 = 100000000 # initial guess, arbitrary but should be close to the solution; large number to see more iterations! try this with 0 to find a non-converging point
epsilon = 0.00000000000001 # algorithm will stop once the the difference between approximations is smaller than this
maxtries = 10000 # maximum number of tries, since the algorithm may start looping between guesses and never converge
gotresult = False
goterror = False
counter = 0
while not goterror and not gotresult and counter < maxtries :
    fx = x0**2 - 2      # try x0**3 - 2*x0 + 2 with initial guess 0 to see it loop!
    fprimex = 2*x0      # try 3*x0**2 - 2 with initial guess 0 to see it loop!

    if fprimex == 0:
        goterror = True
        continue        # this skips the rest of the body to avoid division by zero
                        # putting the rest of the body in an "else" block would also work!
    #else: # try this instead of the "continue"
    x1 = x0 - fx / fprimex
    print("approximation at iteration {}: {}".format(counter,x1))

    if abs(x1 - x0) < epsilon:
        gotresult = True

    x0 = x1
    counter = counter + 1

if gotresult:
    print("found a good approximation in {} iterations: {}".format(counter,x1))
else:
    print("made {} iterations but did not converse to good approximation".format(counter))

# # alternative version that relies on "for" loop and "break" statements instead
# # flow is harder to understand, how to identify what caused the loop to stop?

# for counter in range(maxtries) :
#     fx = x0**2 - 2      # try x0**3 - 2*x0 + 2 with initial guess 0 to see it loop!
#     fprimex = 2*x0      # try 3*x0**2 - 2 with initial guess 0 to see it loop!

#     if fprimex == 0:
#         break

#     x1 = x0 - fx / fprimex
#     print("guess at {}: {}".format(counter,x1))

#     if abs(x1 - x0) < epsilon:
#         break

#     x0 = x1

