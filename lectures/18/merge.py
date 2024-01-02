# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:10:48 2018

@author: jlopes, pbv

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""


def merge(xs, ys):
    """ Merge sorted lists xs and ys. Return a sorted result """
    result = []
    i = 0   # index of next element of xs
    j = 0   # index of next element of ys

    while i<len(xs) and j<len(ys):
        # Both lists still have items, copy smaller item to result.
        if xs[i] <= ys[j]:
            result.append(xs[i])
            i = i + 1
        else:
            result.append(ys[j])
            j = j + 1
    # loop end
    if i>=len(xs):            # if xs list is finished
        result.extend(ys[j:]) # add remaining elements from ys
    elif j>=len(ys):          # same, but swapping roles
        result.extend(xs[i:])
    return result
        


ls1 = friends = ["Joe", "Zoe", "Brad"]
ls2 = friends = ["Angelina", "Zuki", "Thandi", "Paris"]
print()
ls1.sort()
print(ls1)
ls2.sort()
print(ls2)
print()
ls3 = merge(ls1, ls2)
print(ls3)
