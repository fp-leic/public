# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:43:30 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(list(range(5, 60, 2)))

tess.up()                       # this is new

for size in range(5, 60, 2):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)          # move tess along
    tess.right(24)              # and turn her

wn.mainloop()
turtle.bye()
