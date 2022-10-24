#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:27:15 2022

@author: jlopes
"""

"""
PROBLEM 1 (hello Spyder):

If the sale price of a big tv set is 1000€ and the shop gives back the
VAT (IVA) how much do you pay?
"""

sell_price = 1000.00    # start by 1000
IVA = 0.23              # it does NOT go to "Variable explorer" ?!
U = 1                   # goes to  "Variable explorer"
price = sell_price / (U + IVA)
print(round(price, 2))  # round it as currency
