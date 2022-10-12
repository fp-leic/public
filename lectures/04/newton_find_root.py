#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:16:35 2022

@author: jlopes
"""

"""
Newton's method for finding roots.
https://en.wikipedia.org/wiki/Newton%27s_method

is a root-finding algorithm which produces successively better
approximations to the roots (or zeroes) of a real-valued function.
The most basic version starts with a single-variable function f
defined for a real variable x, the function's derivative f′,
and an initial guess x0 for a root of f. If the function satisfies
sufficient assumptions and the initial guess is close

The initial guess will be x0 = 1
and the function will be f(x) = x^2 − 2
so that f′(x) = 2x
"""

# def f(x):
#     return x**2 - 2      # f(x) = x^2 - 2

# def fprime(x):
#     return 2*x           # f'(x) = 2x

x0 = 1                    # the initial guess
tolerance = 0.0000000001  # the accuracy desired
max_iterations = 100+1    # the maximum number of iterations to execute

for i in range(max_iterations):
    y = x0**2 - 2  # f(x0)
    yprime = 2*x0  # fprime(x0)

    if abs(yprime) == 0:              # stop if the denominator is zero
        print("Mathematical error)")  # Newton's method did not converge
        break

    x1 = x0 - y / yprime            # do Newton's computation

    if abs(x1 - x0) <= tolerance:   # stop when the result is within the desired tolerance
        print(x1)                   # x1 is a solution within tolerance and maximum number of iterations
        break

    x0 = x1                         # update x0 to start the process again

print(i, "iterations")
if i == max_iterations-1:
    print("Max number iterations")  # Newton's method did not converge
    