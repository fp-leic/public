#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:36:12 2022

@author: jlopes
"""

"""Problem:
Write a Python function translate(a_string, table) that translates.
a given string a_string using a translation table.
The translation table, table, is a nested tuple with an arbitrary
number of translation pairs/tuples (in_value, out_value).
"""


def translate(a_string, table):
    """Translates a given string using a translation table."""

# unzip the translation table
    intab, outtab = zip(*table)

# use the accumulator
    result = ''

# traverse the original string
    for ch in a_string:
        # print(ch)

        # do the translation
        if ch in intab:

            # 1. find the index
            index = intab.index(ch)

            # 2. translate the char at the index
            new_char = str(outtab[index])

            # 3. accumulate
            result += new_char

            # in one line!
            # result += str(outtab[intab.index(ch)])

        # do not translate
        else:
            result += ch

    # return value
    return result


# drive code to test the function
table1 = (('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5), ('!', ' :)'))
table2 = ((' ', '--'), ('.', '!'), ('i', 'o'), ('t', 'tt'))
s1 = "Hello world!"
s2 = "Testing this string..."

print()
print("Original string:", s1)
print("Translated w t1:", translate(s1, table1))

# print()
# print("Original string:", s2)
# print("Translated w t1:", translate(s2, table1))

# print()
# print("Original string:", s1)
# print("Translated w t2:", translate(s1, table2))

# print()
# print("Original string:", s2)
# print("Translated w t2:", translate(s2, table2))
