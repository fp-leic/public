#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:39:06 2021

@author: jlopes

Code adapted from:
Geeks for Greeks 
https://www.geeksforgeeks.org/draw-clock-design-using-turtle-in-python/
"""

# import package
import turtle

# create a Screen Object
screen = turtle.Screen()

# Screen configuration
screen.setup(500, 500)

# Make turtle Object
clk = turtle.Turtle()

# set a Turtle object color
clk.color('Green')

# set a Turtle object width
clk.width(4)


# later we will talk about functions!
def draw_hour_hand():
    clk.penup()
    clk.home()
    clk.right(90)
    clk.pendown()
    clk.forward(100)


# value for numbers in clock
val = 0

# loop for print clock numbers
for i in range(12):
    # increment value by 1
    val += 1

    # move turtle in air
    clk.penup()

    # for circular motion
    clk.setheading(-30 * (i + 3) + 75)

    # move forward for space
    clk.forward(22)

    # move turtle to surface
    clk.pendown()

    # move forward for dash line
    clk.forward(15)

    # move turtle in air
    clk.penup()

    # move forward for space
    clk.forward(20)

    # write clock integer
    clk.write(str(val), align="center",
              font=("Arial", 12, "normal"))

# colored centre by setting position
# sets position of turtle at given position
clk.setpos(2, -112)
clk.pendown()
clk.width(2)

# To fill color green
clk.fillcolor('Green')

# start filling
clk.begin_fill()

# make a circle of radius 5
clk.circle(5)

# end filling
clk.end_fill()

clk.penup()
draw_hour_hand()
clk.setpos(-20, -64)
clk.pendown()
clk.penup()

# Write Clock by setting position
clk.setpos(-30, -170)
clk.pendown()
clk.write(' FP/L.EIC!', font=("Arial", 14, "normal"))
clk.hideturtle()

turtle.done()
screen.mainloop()
turtle.bye()
