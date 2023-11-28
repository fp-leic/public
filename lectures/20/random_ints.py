# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:11:22 2018

@author: jlopes, pbv

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""
import random


def make_random_ints_no_dups(rng, num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    The result list cannot contain duplicates.
    """
    result = []
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result

rng = random.Random() # create a random number generator
xs = make_random_ints_no_dups(rng, 5, 1, 10000000)
print()
print(xs)

# Houston, we have problems!
#xs = make_random_ints_no_dups(rng, 10, 1, 6)
