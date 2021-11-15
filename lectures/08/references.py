#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:45:23 2018

@author: jlopes
"""

print()

# this are strings
a = "banana"
b = "banana"

print("strings is?", a is b)

# but for lists is different
a = [1, 2, 3]
b = [1, 2, 3]

print("list ==?", a == b)
print("lists is?", a is b)

# advanced stuff
print()
print("id(a)", id(a))
print("id(b)", id(b))
print("ids ==?", id(a) == id(b))
print("is ?", a is b)
