#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 2023

@author: nmm
"""

"""
Lecture 01: Introduction & The way of the program

Calculate the FP final grade of a student in the ordinary period ("época normal"). Does not consider participation in the supplementary examination period ("época de recurso").
"""

# this is a comment, it is ignored by the interpreter

# variable creation
grade_mt1 = 17  # MT1 grade
grade_mt2 = 16  # MT2 grade
grade_mt3 = 18  # MT3 grade (in the ordinary examination period)
grade_ac = 20   # continuous assessment grade (QTs + QPs)

num_mts = 3     # number of mini-tests

# the following causes a syntactic error: assignment statement must have a value
# num_mts =
# the following causes a runtime error: cannot divide by zero
# num_mts = 0
# the following causes a semantic error: does not calculate the average correctly
# num_mts = 4

print("FP grades (MT1 MT2 EN AC):",
      grade_mt1, grade_mt2, grade_mt3, grade_ac)

grade_mts = (grade_mt1 + grade_mt2 + grade_mt3) / num_mts

print("MT average:", grade_mts)
print("Final ordinary grade:",  0.9*grade_mts + 0.1*grade_ac)
