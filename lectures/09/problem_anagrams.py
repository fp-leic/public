#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 26 out 2022 21:31:10 WEST

@author: jlopes
"""

"""
Given a list of strings, write a Python function `anagrams(alist)`
that groups anagrams together and returns them in a nested list.

An anagram is a word or phrase formed by rearranging the letters of
another word or phrase by using all the original letters exactly
once.

Note that you can add and/or remove white spaces between the letters
to form the anagrams and that case is irrelevant.

The output list as well as its nested lists should be sorted
alphabetically.
"""


# the function to use as sorting criteria
def case_insensitive(item):
    return item.lower()


# define the function
def anagrams(alist):
    """Return a group of anagrams as a nested list."""

    keys = []    # sorted, lower case and without spaces
    groups = []  # the groups in the order of the corrresponding keys

    # for each string in the list find the key and the grouping
    for s in sorted(alist, key=case_insensitive):

        s_key = ''.join(sorted(s.lower())).replace(" ", "")  # the key

        if s_key not in keys:   # the key is a new one
            keys.append(s_key)  # append the new key
            groups.append([s])  # append the original word

        else:                   # the key is an old one
            index = keys.index(s_key)  # find the key
            groups[index].append(s)    # append the original word

    return groups


# drive code
print()
s1 = ["lives", "Elvis"]
print(anagrams(s1))
# [['Elvis', 'lives']]

print()
s2 = ["sentence", "ten scene", "bat", "CE sennet"]
print(anagrams(s2))
# [[['bat'], ['CE sennet', 'sentence', 'ten scene']]

print()
s3 = ["they see", "eat", "The eyes", "ate", "tea", "Always"]
print(anagrams(s3))
# [['Always'], ['ate', 'eat', 'tea'], ['The eyes', 'they see']]
