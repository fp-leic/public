#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 2023

@author: nmm
"""

"""
Lecture 02: Variables, expressions, statements & Simple Data

Calculate the time to travel a given distance at a given velocity.
"""

# retrieve input values from the user
input_distance = input("travel distance (km): ")
input_velocity = input("travel velocity (km/h): ")
# inputs from the terminal are always strings, but we need number for arithmetic
distance = int(input_distance)
velocity = int(input_velocity)

# print the type of the variables
print("variable input_distance type:", type(input_distance))
print("variable distance type:", type(distance))

# the following throws an error: cannot divide strings
# hours = input_distance / input_velocity

# division returns a float
hours = distance / velocity
print("variable hours type now:", type(hours))
# let's simplify and use full hours (integers)
# we can re-assign variables, right-hand expression calculated first
hours = int(hours)
print("variable hours type now:", type(hours))

# integer division to retrieve how many years fit in the calculated hours
years = hours // (24 * 365)
# integer remainder to retrieve the remaining hours after taking the years
hours = hours % (24 * 365)
# integer division to retrieve how many days fit in the remaining hours
days = hours // 24
# integer remainder to retrieve the remaining hours after taking the days
hours = hours % 24

print("travel time in years, days, hours:", years, days, hours)

# the following throws an error: cannot concatenate integers with strings
# years_textual = years + " years"

# prepare better output, must concatenate strings
# assignment to new variables, original variables remain integers
years_textual = str(years) + " years"
days_textual = str(days) + " days"
hours_textual = str(hours) + " hours"

print("travel time:", years_textual, days_textual, hours_textual)

# or a more visual representation, duplication of strings
print(years*"Y")
print(days*"D")
print(hours*"H")

# the following throws an error: cannot "multiply" strings with strings
# print(years_textual*"Y")
