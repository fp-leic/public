#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  Iteration and tail-recursion by example

  Pedro Vasconcelos, 2023
"""

# Iterative factorial using a while loop
def fact_iter(n):
    acc = 1
    while n>0:
       acc = n * acc
       n = n-1
    return acc

# Usual recursive factorial
# this *not* tail-recursive 
def fact_rec(n):
   if n == 0:
      return 1
   else:
      return n * fact_rec(n-1)

# Tail recursive factorial
# Note that this function corresponds to the while loop
# of the iterative version
def fact_tailrec(n, acc):
  if n == 0:
    return acc
  else:
    return fact_tailrec(n-1, n*acc)

# "Wrapper" function 
# calls the tail-recursive factorial with initial value for the accumulator
def fact_wrapper(n):
   return fact_tailrec(n, 1)

# main program
# test the 3 versions
for n in range(10):
    print(f'fact_iter({n}) = {fact_iter(n)}')
    print(f'fact_rec({n}) = {fact_rec(n)}')
    print(f'fact_wrapper({n}) = {fact_wrapper(n)}')

