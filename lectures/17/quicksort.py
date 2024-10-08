#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:49:08 2018

@author: jlopes, pbv

David Mertz, Functional Programming in Python
"""

def quicksort(lst):
    """Quicksort of a list."""
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst)//2]  # mid point
        pivots = [x for x in lst if x == pivot]
        smaller = [x for x in lst if x < pivot]
        larger = [x for x in lst if x > pivot]
    return quicksort(smaller) + pivots + quicksort(larger)


l = [5, 8, 2, 9, 1, 4, 8, 9, 0, 3, 2, 7]
print('Original:',l)
print('Sorted:', quicksort(l))

