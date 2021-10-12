#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:48:29 2018
@author: jlopes, from: "How to Think Like a Computer Scientist"
"""

total_secs = int(input("How many seconds, in total? "))

hours = total_secs // 3600
ecs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
