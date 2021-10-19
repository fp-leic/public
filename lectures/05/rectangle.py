#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:15:42 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

import turtle


def draw_rectangle(animal, width, height):
    """Get animal to draw a rectangle of given width and height."""
    for _ in range(2):
        animal.forward(width)
        animal.left(90)
        animal.forward(height)
        animal.left(90)


wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)

draw_rectangle(tess, 200, 80)


def draw_square(animal, size):   # A new version of draw_square
    draw_rectangle(animal, size, size)


def move_n_draw(animal, x, y):
    """ Get an animal to go to (x,y) and draw a square 80x80 """
    animal.penup()
    animal.goto(x, y)
    animal.pendown()
    draw_square(animal, 80)


move_n_draw(tess, 120, 100)
move_n_draw(tess, 120, -100)
move_n_draw(tess, 0, -100)
move_n_draw(tess, 0, 100)
move_n_draw(tess, -100, 0)

wn.mainloop()
turtle.done() 
