#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:33:53 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

##### students database
students = [
        ("John", ["CompSci", "Physics"]),
        ("Vusi", ["Maths", "CompSci", "Stats"]),
        ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
        ("Sara", ["InfSys", "Accounting", "Economics", "CommLaw"]),
        ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

##### Print all students with a count of their courses.

#for name, subjects in students:
#    print(name, "takes", len(subjects), "courses")

##### Count how many students are taking CompSci
    
# Now we’d like to ask how many students are taking CompSci. 
# This needs a counter, and for each student we need a
# second loop that tests each of the subjects in turn:
  
#counter = 0                      # how many, needs a counter
#for name, subjects in students:  # for each student
#    for s in subjects:           # for each subject (A nested loop!)
#        if s == "CompSci":
#            counter += 1
#            break
#print("\nThe number of students taking \"CompSci\" is", counter)
