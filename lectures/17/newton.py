#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:56:23 2019

@author: jlopes, pbv

Based in: John DeNero. Composing Programs, "1.6.5 Example: Newton's Method",
https://composingprograms.com/pages/16-higher-order-functions.html

Based in: Harold Abelson and Gerald Jay Sussman,
Structure and Interpretation of Computer Programs
"""


def improve(update, close, guess=1):
    '''Improve an approximation using a function until 
    the result is close enough.'''
    while not close(guess):
        guess = update(guess)
    return guess


def newton_update(f, df):
    '''Update an approximation using Netwon's method.
    f and df are the function and derivative of the equation's left-hand-side,
    i.e. the equation is f(x)=0.'''
    def update(x):
        return x - f(x) / df(x)
    return update


def approx_eq(x, y, tolerance=1e-15):
    '''Check if two values are close enough.'''
    return abs(x - y) < tolerance


def find_zero(f, df):
    '''Solve an equation using Newton's method.'''
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):
    """Compute square root using Newton's method."""
    def f(x):
        return x**2 - a  # x**2 - a = 0
    def df(x):
        return 2*x      # derivative of x**2-a
    return find_zero(f, df)

# tests
print(square_root_newton(2))
print(square_root_newton(3))
