# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:06:49 2018

@author: jlopes
"""

import turtle


def make_window(color, title):
    """
    Set up the window with the given background color and title.
    Returns the new window.
    """
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window


def make_turtle(color, size):
    """
    Set up a turtle with the given color and pensize.
    Returns the new turtle.
    """
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal


wn = make_window("lightgreen", "Tess and Alex and Dave")

tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

length = 120

tess.forward(length)

alex.penup()
alex.forward(length)
alex.pendown()
alex.forward(length)

dave.penup()
dave.forward(2 * length)
dave.pendown()
dave.forward(length)

wn.mainloop()
turtle.done()
