#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:20:14 2019

@author: silvio sampaio, 2021/22
"""

import random


def cows_bulls(seed):
    random.seed(seed)
    correct = random.randint(0, 9999)
    return lambda guess: score(correct, guess)


def score(correct, guess):
    """calculates the score of the "bulls and cows" game."""
    cows = 0     # guessed correctly in the correct place
    bulls = 0    # guessed correctly in the wrong place
    rnum = list('{0:04d}'.format(correct))  # correct as a str with 4 digits
    gnum = list('{0:04d}'.format(guess))    # ditto for guess
    # count the bulls
    for i in range(len(rnum)):
        if rnum[i] == gnum[i]:
            cows += 1         # found a cow
            rnum[i] = '*'
            gnum[i] = '+'
    # find any matches regardless of position
    for i in range(len(rnum)):
        for j in range(len(gnum)):
            if rnum[i] == gnum[j]:
                bulls += 1  # found a match
                # overwrite correct and guess so we don't count them again
                gnum[j] = '+'
                rnum[i] = '*'
    return (cows, bulls)

# a test
code = "cows_bulls(1234)(2240)"
print(code, "=>", eval(code))
