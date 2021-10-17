#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on   Tue Oct  1 17:32:44 2019

@author: jlopes

Code adapted from the book:
How to Think Like a Computer Scientist: Interactive Edition, 
runestone.academy/runestone/books
"""

import random
import turtle


def is_in_screen(w, t):
    """
    Determines if turtle t is inside the boundaries of screen w
    """
    left_bound = -w.window_width() / 2
    right_bound = w.window_width() / 2
    top_bound = w.window_height() / 2
    bottom_bound = -w.window_height() / 2

    turtle_x = t.xcor()      # get current x position
    turtle_y = t.ycor()      # get current y position

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in


wn = turtle.Screen()
wn.setup(600, 600)       # size of the screen window
wn.bgcolor("green")

tess = turtle.Turtle()
tess.shape('turtle')

while is_in_screen(wn, tess):
    coin = random.randrange(0, 2)  # throw the coin
    if coin == 0:                  # heads
        tess.left(90)
    else:                          # tails
        tess.right(90)

    tess.forward(50)

wn.mainloop()
turtle.bye()
