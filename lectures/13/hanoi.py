#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:26:44 2018

@author: jlopes, pbv

Recursive Python function to solve tower of Hanoi

Adapted from:
    https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
"""


def tower_of_hanoi(height, from_pole, to_pole, aux_pole):
    if height == 1:
        # base case
        move_disk(from_pole, to_pole)
    else:
        # recursive case
        # move n-1 disks from source to auxiliary, so they are out of the wa
        tower_of_hanoi(height-1, from_pole, aux_pole, to_pole)
        # move the nth disk from source to target
        move_disk(from_pole, to_pole)
        # move the n-1 disks that we left on auxiliary onto target
        tower_of_hanoi(height-1, aux_pole, to_pole, from_pole)


# Display our progress
def move_disk(fp, tp):
    print(f"Moving top disk from {fp} to {tp}")


# Initiate calls from source A to target C with auxiliary B
# print("2 =========")
# tower_of_hanoi(2, "A", "C", "B")

#print("3 =========")
tower_of_hanoi(3, "A", "C", "B")

#print("4 =========")
#tower_of_hanoi(4, "A", "C", "B")

#print("5 =========")
#tower_of_hanoi(5, "A", "C", "B")
