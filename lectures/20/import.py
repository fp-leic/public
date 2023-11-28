#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:55:14 2018

@author: pbv
"""

import html

example = html.p('This is an example list',
            html.ol(
                html.li('first item'),
                html.li('second item'),
                html.li('third item')),
                 'This is the end of the list')
print(example)
print()

def shopping_list(shoplist):
    """Build HTML for a shopping list."""
    total = sum(price for item,price in shoplist)
    args = (html.li(f'{item}: {price} EUR') for item,price in shoplist)
    result = html.p('Shopping list:',
             html.ol(*args),
             html.hline,
             f'Total: {total} EUR')
    return result

fruits = [('Apples', 2.5), ('Strawberries', 4.5), ('Pinaples', 5.5)]
print(shopping_list(fruits))        
