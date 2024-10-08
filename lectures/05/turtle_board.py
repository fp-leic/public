#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2024

@author: nmm
"""

"""
Lecture 05: Functions

Draw a board with turtles using functions.
"""
import turtle

# In this program we need to draw rectangles at various points, better to define an auxiliary function.
# Defining a function does nothing until it is called, just registers its definition.
def draw_rectangle(turt,width,height,is_black):
    """
    Use turt to draw a rectangle of a certain width and height, optionally paint the rectangle black.
    Return the distance walked by the turtle.
    """
    # The string above is interepreted as the function's documentation, while this comment is just ignored (in VS Code, hover on its name).

    if width < 0 or height < 0:
        # We can have multiple returns, but as soon as one is executed, the function terminates its execution.
        return "Error"
    
    if is_black:
        turt.fillcolor("black")
    else:
        turt.fillcolor("white")
    turt.begin_fill() # this is how the turtle module fills shapes, paired with end_fill()
    for step in range(2):
        turt.forward(width)
        turt.right(90)
        turt.forward(height)
        turt.right(90)
    turt.end_fill()

    # functions can return values with return statements
    walked_rct = 2*width + 2*height
    return walked_rct
    
# We can define a function by calling other functions, use abstraction.
def draw_square(turt,side,is_black):
    """
    Use turt to draw a square of a certain side, optionally paint the square black.
    Return the distance walked by the turtle.
    """
    walked_sq = draw_rectangle(turt,side,side,is_black)
    return walked_sq
    print("This is dead code, unreachable!")

# This is a Boolean function, returns a bool value.
def color_black(i,j):
    """Whether to paint a square at position (i,j) black."""
    return (i+j)%2 == 1

# Not all functions must return values, they may just produce side-effects.
# They implicitly return a special value None
def print_walked(dist):
    print("total walked: "+str(dist))

leo = turtle.Turtle()
leo.speed(10)
# This is just to move the turtle to the top-left corner.
screen = turtle.Screen()
screen_height = screen.window_height()
screen_width = screen.window_width()
leo.teleport(-screen_width/2,screen_height/2)

# An accumulator variable to keep track of walking distance.
total_walked = 0
n_cells = 8

# To have a rectangular board (rather than square), use this.
# xdimension = int(input("x dimension: "))
# ydimension = int(input("y dimension: "))
# xcell_dimension = xdimension / n_cells # n by n board
# ycell_dimension = ydimension / n_cells # n by n board
# walked = draw_rectangle(leo,xdimension,ydimension,False)

dimension = int(input("dimension: "))
cell_dimension = dimension // n_cells # n by n board
walked = draw_square(leo,dimension,False) # draw square and get walked distance

# Note that the parameters and variables defined in a function are local, they are not known outside the function (only the return value).
# print(width) # No such variable
# print(walked_sq) # No such variable

total_walked = total_walked + walked # update total distance
# This is equivalent to the following, which updated total_walked by adding walked.
# total_walked += + walked


print_walked(total_walked) # print total distance

# Functions that do not return values actually return None, a special value 
# x = print_walked(total_walked)
# print(x)

# n by n board, nested loop, one for lines other for columns within each line
for i in range(n_cells):
    for j in range(n_cells):
        black = color_black(i,j) # bool determining whether to paint black cell
        # walked = draw_square(leo,cell_dimension,black) # draw square and get walked distance
        # total_walked = total_walked + walked # update total distance
        total_walked += draw_square(leo,cell_dimension,black) # draw square, update total_walked with the returned distance
        print_walked(total_walked) # print total distance
        leo.forward(cell_dimension)
        total_walked += cell_dimension
    leo.right(90)
    leo.forward(cell_dimension)
    total_walked += cell_dimension
    leo.left(90)
    leo.forward(-dimension)
    total_walked += dimension

# To have a rectangular board (rather than square), use this.
# for i in range(n_cells):
#     for j in range(n_cells):
#         black = color_black(i,j) # bool determining whether to paint black cell
#         # walked = draw_square(leo,cell_dimension,black) # draw square and get walked distance
#         # total_walked = total_walked + walked # update total distance
#         total_walked += draw_rectangle(leo,xcell_dimension,ycell_dimension,black) # draw square, update total_walked with the returned distance
#         print_walked(total_walked) # print total distance
#         leo.forward(xcell_dimension)
#         total_walked += xcell_dimension
#     leo.right(90)
#     leo.forward(ycell_dimension)
#     total_walked += ycell_dimension
#     leo.left(90)
#     leo.forward(-xdimension)
#     total_walked += xdimension


turtle.done()