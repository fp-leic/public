#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 2023

@author: nmm
"""

"""
Lecture 04: Iteration

Make turtles race each other with random actions.
"""

import turtle
import random # this library allows us to generate random numbers

distance = int(input("insert travel distance: "))

# while loops executes until condition becomes False
# condition can be any arbitrary expression  
while distance > 1000 or distance < 0:
    print("invalid distance!")
    distance = int(input("insert travel distance: ")) # comment this to see you first infinite loop!

window = turtle.Screen()
window.title("Race FP")
# this is just to draw the limits of the track
judge = turtle.Turtle()
judge.color("Black")
judge.hideturtle()
judge.speed(0)
judge.penup()
judge.sety(10)
judge.pendown()
judge.forward(distance)
judge.right(90)
judge.forward(20)
judge.right(90)
judge.forward(distance)

# create our turtles
leo = turtle.Turtle()
leo.color("Blue")
leo.speed(0.6)

mike = turtle.Turtle()
mike.color("Orange")
mike.speed(0.6)

ralph = turtle.Turtle()
ralph.color("Red")
ralph.speed(0.6)

don = turtle.Turtle()
don.color("Purple")
don.speed(0.6)

# starting with a single turtle ...

# # for loop only works if we knew the number of steps needed to cross the line
# for st in range(100):
#     dist = random.randint(1, 10)
#     leo.forward(dist)
#     rota = random.randint(-5, 5)
#     leo.left(rota)

# # while loop allows us to wait until leo finishes regardless of the number of steps
# while leo.xcor() < 200:
#     dist = random.randint(1, 10)
#     leo.forward(dist)
#     rota = random.randint(-5, 5)
#     leo.left(rota)

# # let's make a more complex condition to avoid going off track
# # while leo.xcor() < 200 and not leo.ycor() > 10 and not leo.ycor() < -10: # this works, but is there a simpler way?
# while leo.xcor() < 200 and abs(leo.ycor()) <= 10: # abs gets the absolute value of a number
# # while leo.xcor() < 200 or abs(leo.ycor()) <= 10: # careful with the Boolean operators, what is happening here?
#     dist = random.randint(1, 10)
#     leo.forward(dist)
#     rota = random.randint(-5, 5)
#     leo.left(rota)
#     print("leo position: ", leo.xcor(), leo.ycor()) # use prints to "debug" your code!
#     print("x and y conditions: ", leo.xcor() < 200, abs(leo.ycor()) <= 10)

# let's add the other turtles

# this looks more like a time trial than a race!
# for turt in [leo,mike,ralph,don]:
#     while turt.xcor() < 200 and abs(turt.ycor()) <= 10:
#         dist = random.randint(1, 10)
#         turt.forward(dist)
#         rota = random.randint(-5, 5)
#         turt.left(rota)
#         print("turtle position: ", turt.xcor(), turt.ycor()) 

# # now this is a race
# # do we want this...
# # while (leo.xcor() < 200 and abs(leo.ycor()) <= 10) and (ralph.xcor() < 200 and abs(ralph.ycor()) <= 10) and (don.xcor() < 200 and abs(don.ycor()) <= 10) and (mike.xcor() < 200 and abs(mike.ycor()) <= 10):
# # or this? careful with the precedences
# while (leo.xcor() < 200 and abs(leo.ycor()) <= 10) or (ralph.xcor() < 200 and abs(ralph.ycor()) <= 10) or (don.xcor() < 200 and abs(don.ycor()) <= 10) or (mike.xcor() < 200 and abs(mike.ycor()) <= 10):
#     for turt in [leo,mike,ralph,don]:
#         dist = random.randint(1, 10)
#         turt.forward(dist)
#         rota = random.randint(-5, 5)
#         turt.left(rota)
#         print("turtle position: ", turt.xcor(), turt.ycor()) 

# that worked, but the solution was not elegant (what if more turtles joined the race?)
# let's use an accumulator variable, it's value is updated along the loop
finished = False
while not finished: # same as finished == False, same as finished != True
    for turt in [leo,mike,ralph,don]:
        dist = random.randint(1, 10)
        turt.forward(dist)
        rota = random.randint(-5, 5)
        turt.left(rota)
        if turt.xcor() >= 200 or abs(turt.ycor()) > 10: # notice the negated test: assume not finished until anyone finished
            finished = True
        print("turtle position: ", turt.xcor(), turt.ycor()) 

        
# but we really want everyone to finish...
# finished = False
# while not finished: 
#     finished = True
#     for turt in [leo,mike,ralph,don]:
#         dist = random.randint(1, 10)
#         turt.forward(dist)
#         rota = random.randint(-5, 5)
#         turt.left(rota)
#         if turt.xcor() < 200 and abs(turt.ycor()) <= 10: # negated again: assume finished unless someone still racing
#             finished = False
#         print("turtle position: ", turt.xcor(), turt.ycor()) 

turtle.done()
