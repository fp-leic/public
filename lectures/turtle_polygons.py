#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 2023

@author: nmm
"""

"""
Lecture 03: Program flow, conditionals, selection

Make turtles draw regular polygons.
"""

# external library, get familiar with reading documentation!
# https://docs.python.org/3/library/turtle.html
import turtle

# retrieve input values from the user
length = int(input("side length: "))
vertices = int(input("number vertices: "))

# conditionals are composed statements, act on Boolean expressions
# if length > 1000:
#     print("Too long!")
# elif vertices > 20:
#     print("Too many angles!")
# else:
#     print("Ok!")
# if the first condition holds, the second is not even tested, test for length 2000 and 50 vertices

# conditions can be any Boolean expression
# else block can be omitted
if length > 1000 or length < 0:
    print("Warning: distance out of range")
if vertices > 20 or vertices < 0:
    print("Warning: velocity out of range")

# functions from the turtle module to create the screen
window = turtle.Screen()
window.title("FP Turtles") # complex objects have associated functions (called methods)

leo = turtle.Turtle()
leo.color("Blue")
# leo.shape("turtle")
#leo.left(0) # we don't want to repeat this for every turtle!

raph = turtle.Turtle()
raph.color("Red")
# raph.shape("turtle")
#raph.left(90)

mike = turtle.Turtle()
mike.color("Orange")
# mike.shape("turtle")
#mike.left(180)

don = turtle.Turtle()
don.color("Purple")
# don.shape("turtle")
#don.left(270)

turtles = [raph,leo,mike,don] # a list with all the turtles, so that we don't have to repeat it

# This is an accumulator variable: initialized before the loop and updated at each iteration
start_angle = 0
for turt in turtles:
    turt.shape("turtle")
    turt.right(start_angle)
    start_angle = start_angle + 90

# this would work for a fixed number of vertices!
# for stp in [0,1,2,3]:
#     leo.forward(length)
#     leo.right(90)

# this works for any number of vertices but only a turtle
# for stp in range(vertices):
#     leo.forward(length)
#     leo.right(360/vertices)

# for all turtles to move all the steps, we need a nested loop
for turt in turtles:
    for vertice in range(vertices):
        turt.forward(length)
        turt.right(360/vertices)
        # nested conditional in a nested loop
        if turt.xcor() < -400 or turt.xcor() > 400 or turt.ycor() < -400 or turt.ycor() > 400:
            print("Warning: going too far!")        
    turt.hideturtle() # indentation matters! try to unindent this line or indent further!

# needed to keep window open
turtle.done()
