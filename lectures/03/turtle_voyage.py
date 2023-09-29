#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 2023

@author: nmm
"""

"""
Lecture 03: Program flow, conditionals, selection

Make turtles travel a given distance at a given velocity.
"""

# external library, get familiar with reading documentation!
# https://docs.python.org/3/library/turtle.html
import turtle

# retrieve input values from the user
distance = int(input("travel distance: "))
steps = int(input("travel steps: "))

# conditionals are composed statements, act on Boolean expressions
# if distance > 1000:
#     print("Too long!")
# elif steps > 20:
#     print("Too fast!")
# else:
#     print("Ok!")
# if the first condition holds, the second is not even tested, test for distance 2000 and steps 50

# conditions can ben any Boolean expression
# else block can be omitted
if distance > 1000 or distance < 0:
    print("Warning: distance out of range")
if steps > 20 or steps < 0:
    print("Warning: velocity out of range")

# functions from the turtle module to create the screen
window = turtle.Screen()
window.title("FP Turtles")

leo = turtle.Turtle()
leo.color("Blue")
leo.shape("turtle")
#leo.left(0) # we don't want to repeat this for every turtle!
#leo.forward(20)

raph = turtle.Turtle()
raph.color("Red")
raph.shape("turtle")
#raph.left(90)
#raph.forward(20)

mike = turtle.Turtle()
mike.color("Orange")
mike.shape("turtle")
#mike.left(180)
#mike.forward(20)

don = turtle.Turtle()
don.color("Purple")
don.shape("turtle")
#don.left(270)
#don.forward(20)

# would work for a fixed number of steps!
# for stp in [0,1,2,3,4]:
#     leo.forward(distance)

# works for the given steps but only a single turtle
# for stp in range(steps):
#     leo.forward(distance)

direction = 0
for turt in [raph,leo,mike,don]:
    turt.left(direction)
    for step in range(steps):
        # nested conditional in a nested loop
        if turt.xcor() > -200 and turt.xcor() < 200 and turt.ycor() > -200 and turt.ycor() < 200:
            turt.forward(distance)
            turt.left(10)
    direction = direction + 90 # indentation matter! try to unindent this line or indent further!

# needed to keep window open
turtle.done()
