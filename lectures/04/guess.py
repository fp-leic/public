#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:48:18 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

import random          # We cover random numbers in the modules chapter
rng = random.Random()  # "rng" stands for "random number generator"
number = rng.randrange(1, 1000)  # Get random number between (1 and 1000).

guesses = 0
message = ""

while True:
    guess = int(input(message + "\nGuess my number between 1 and 1000: "))
    guesses += 1
    if guess > number:
        message += str(guess) + " is too high.\n"
    elif guess < number:
        message += str(guess) + " is too low.\n"
    else:
        break
input("\nGreat, you got it in "+str(guesses)+" guesses!\n")