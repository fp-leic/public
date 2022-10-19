# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:38:21 2018

@author: jlopes, pbv
"""

def calculator(expr):
    '''Computes the results of the given expression tree.

    An *expression tree* is either
    - a number (integer or floating point);
    - a triple of a left-hand-side expression, an operator and 
      a right-hand-side expression
    
    >>> calculator((1, '+', 2))
    3
    >>> calculator(((1, '+', 2), '*', 3))
    9
    >>> calculator(((2, '*', ((4, '-', 2), '*', 10)), '-', (5, '*', 2)))
    30
    >>> calculator(((2, '+', (4, '*', 2)), '*', (7, '-', 3)))
    40

    >>> calculator(((6, '-', ((3, '+', 1), '*', (9, '-', 2)))))
    -22
    >>> calculator(((9, '*', 2), '-', ((3, '+', 1), '*', (9, '-', 2))))
    -10
    >>> calculator(((9, '*', (2, '-', 0)), '-', (((2, '*', 3), '+', 1), '*', (9, '-', 2))))
    -31
    >>> calculator((1, '+', 1))
    2
    '''
    # base case
    if type(expr) is int or type(expr) is float:
        return expr

    # otherwise it must be a triple
    lhs, op, rhs = expr
    # recursive calls
    val1 = calculator(lhs)
    val2 = calculator(rhs)
    if op == '+':
        return val1 + val2
    if op == '-':
        return val1 - val2
    if op == '*':
        return val1 * val2
    if op == '/':
        return val1 / val2


# the tests
fun = calculator
def yaml_tests(inputs, fun):
    for i in inputs:
        print("{0} => {1}".format(i, fun(*i)))
inputs = [
          [(1, '+', 2)],
          [((1, '+', 2), '*', 3)],
          [(10, '-', 10)],
          [(6, '-', (3, '*', 2))],
          [(6, '-', ((3, '+', 1), '*', (9, '-', 2)))],
          [(6, '-', (2, '*', 3))],
          [((9, '-', 2), '*', (2, '*', 3))],
          [((1, '/', 2), '+', 3)]
         ]
yaml_tests(inputs, fun)
