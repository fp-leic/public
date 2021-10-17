#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:59:05 2018

@author: jlopes

Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

########################
# some examples to be interpreted
########################

##### break

#for i in [12, 16, 17, 24, 29]:
#    if i % 2 == 1:   # If the number is odd
#        break        # ... immediately exit the loop
#    print(i)
#print("done")

##### middle-test loop

#total = 0
#while True:
#    response = input("Enter the next number (Leave blank to end): ")
#    if response == "" or response == "-1":
#        break
#    total += int(response)
#print("\nThe total of the numbers you entered is: ", total)

##### Post-test loop

#while True:
#    print("play_the_game_once()")
#    response = input("Play again? (yes or no) ")
#    if response != "yes":
#        break
#print("Goodbye!")

