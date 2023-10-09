#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023

@author: nmm
"""

"""
Lecture 05: Functions

Calculate areas and volumes using functions.
"""

# this a function definition: it does nothing unless it is called
def rectangle_area(length,width):
    area = width * length
    return area

def square_area(side):
    area = rectangle_area(side,side) # functions can call other functions
    return area

def prism_volume(base,height):
    volume = base * height
    return volume

def parallelepiped_volume(height,width,length):
    volume = prism_volume(rectangle_area(length,width),height) # function composition
    return volume

def cube_volume(side):
    return parallelepiped_volume(side,side,side)

def is_square(length,width): # Boolean function
    return length == width

def print_area(): # function without return value, procedure
    for square in [4,5,7,9,12]:
        res = square_area(square)
        print("area of square {} is {}".format(square,res))
        res = cube_volume(square)
        print("volume of cube {} is {}".format(square,res))

print_area()

# print(print_area()) # what will this print, function has no return?
# print(print_area) # will this work since function has no parameters?
# print(area) # will this work?

# try this in Python Tutor, https://pythontutor.com/!
# try this VS Code interactive mode, Right-click > 'Run in Interactive Window'!