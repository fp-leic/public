#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:51:54 2018

@author: jlopes
"""


def final_amount(p, r, n, t):
    """
    Apply the compound interest formula to p to produce the final amount.
    """
    a = p * (1 + r/n) ** (n*t)
    return a   # This is new, and makes the function fruitful.


# now that we have the function above, let us call it.
toInvest = float(input("How much do you want to invest? "))

# p = toInvest, r = 0.08, n = 2, t = 5
final = final_amount(toInvest, 0.08, 2, 5)
print("At the end of the period you'll have", final)


#def final_amount_v2(amount, rate, compounded, years):
#    """
#    The 'a' was a useless asignment. We might as well skip it.
#    """
#    return amount * (1 + rate/compounded) ** (compounded*years)
