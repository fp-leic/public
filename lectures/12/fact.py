#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:39:02 2019

@author: jlopes, pbv
"""


# iteractive version
def factorial_iter(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact


# recursive version
def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)


# Drive code
n = int(input("Enter a positive integer: "))
print("Factorial_iter of {0} is {1}".format(n, factorial_iter(n)))
print("Factorial_rec of {0} is {1}".format(n, factorial_rec(n)))
