#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 0:19:48 2018

@author: jlopes
"""

import datetime

now = datetime.datetime.now()

print()
print("Current date and time using str method of datetime object:")
print()
print(str(now))

print()
print("Current date and time using instance attributes:")
print()
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)
print("Current microsecond:", now.microsecond)
