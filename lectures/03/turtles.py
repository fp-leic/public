# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:35:28 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

############
# 1st example
############

import turtle             # Allows us to use turtles

window = turtle.Screen()  # Creates a playground for turtles

alex = turtle.Turtle()    # Create a turtle, assign to alex

alex.forward(50)          # Tell alex to move forward by 50 units
alex.left(90)             # Tell alex to turn by 90 degrees
alex.forward(30)          # Complete the second side of a rectangle

window.mainloop()         # Wait for user to close window
turtle.bye()

############
# 2nd example
############

#import turtle
#
#window = turtle.Screen()
#
#window.bgcolor("lightgreen")  # Set the window background color
#window.title("Hello, Tess!")  # Set the window title
#
#tess = turtle.Turtle()
#tess.color("blue")      # Tell tess to change her color
#tess.pensize(3)         # Tell tess to set her pen width
#
#tess.forward(50)
#tess.left(120)
#tess.forward(50)
#
#window.mainloop()       # Wait for user to close window
#turtle.bye()

