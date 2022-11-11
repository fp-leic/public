#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:56:53 2022

Adapted from: https://www.geeksforgeeks.org/python-sets/

@author: jlopes
"""

# first, let's use a dictionary
def uncommons_d(s1, s2):
    """Find string with uncommon characters of given strings."""

    res = ""    # result
    adict = {}  # auxiliary dict for frequence table

    # store all characters of s2 in dict
    for ch in s2:
        adict[ch] = 1

    # find characters of s1 that are not present in s2
    for ch in s1:
        if (ch not in adict):
            res = res + ch
        else:
            adict[ch] = 2

    # find characters of s2 that are not present in s1
    for ch in s2:
        if (adict[ch] == 1):
            res = res + ch

    return res


# now, an alternative solution using sets
def uncommons_s(str1, str2):
    """Find string with uncommon characters of given strings."""

    # convert both strings into set
    set1 = set(str1)
    set2 = set(str2)

    # performing symmetric difference operation of sets to pull out uncommons
    uncommon = set1 ^ set2

    # join each character without space to get final string
    return ''.join(uncommon)


# driver code
print()
s1 = "abcs"
s2 = "cxzca"
s3 = "aacdb"
s4 = "gafd"
print(f"Using a dict: {uncommons_d(s1, s2)} & {uncommons_d(s3, s4)}")
print()
print(f"Using sets: {uncommons_s(s1, s2)} & {uncommons_s(s3, s4)}")
