#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 15:31:52 2022

@author: jlopes
"""


"""
PROBLEM (Clock in seconds):

Given a number of minutes, how many hours, minutes and seconds there are?
"""

total_secs = int(input("How many seconds, in total? "))

hours = total_secs // 3600
secs_remaining = total_secs % 3600
minutes = secs_remaining // 60
secs_remaining = secs_remaining % 60

print("Hrs:=", hours, '/', "mins:", minutes, '/', "secs:", secs_remaining)
