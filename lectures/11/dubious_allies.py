#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023

@author: nmm
"""

"""
Lecture 11: Sets

Calculate the set of dubious allies: allies that are in alliances with competitors. 

You can assume the given relationships are symmetric (if x is an ally of y, y is also registered as an ally of x).
"""


def set_of_allies(alliances, entity):
    """
    Returns the set of allies of a given entity.
    """
    allies = set()  # you cannot use {} for the empty set, that's an empty dictionary
    for h1, h2 in alliances:
        if h1 == entity:
            # this version uses a mutator, but could do allies = allies | {h2}
            allies.add(h2)
    return allies


def allies_of_competitors(alliances, conflicts, entity):
    """
    Returns the set of allies of competitors of a given entity.
    """
    allies_competitors = set()
    for h1, h2 in conflicts:
        if h1 == entity:
            allies = set_of_allies(alliances, h2)
            # this version does not use a mutator, but you could do allies_competitors.update(allies)
            allies_competitors = allies_competitors | allies
            # try to do this with lists!
    return allies_competitors


def allies_dubious(alliances, conflicts, entity):
    """
    Returns the set of allies of competitors that are also allies of a given entity.
    """
    # always reuse functions to avoid code duplication
    return set_of_allies(alliances, entity) & allies_of_competitors(alliances, conflicts, entity)


alliances = [('Eve', 'Chuck'),
             ('Arthur', 'Chuck'),
             ('Alice', 'Bob'),
             ('Arthur', 'Craig'),
             ('Carol', 'Ivan'),
             ('Alice', 'Grace'),
             ('Arthur', 'Eve'),
             ('Craig', 'Judy'),
             ('Alice', 'Chuck'),
             ('Alice', 'Dan'),
             ('Mike', 'Alice'),
             ('Grace', 'Alice'),
             ('Alice', 'Mike'),
             ('Arthur', 'Dan'),
             ('Chuck', 'Dan'),
             ('Dan', 'Chuck')]

conflicts = [('Craig', 'Judy'),
             ('Eve', 'Carol'),
             ('Bob', 'Arthur'),
             ('Bob', 'Carol'),
             ('Carol', 'Arthur'),
             ('Arthur', 'Judy'),
             ('Alice', 'Eve'),
             ('Alice', 'Arthur'),
             ('Chuck', 'Alice')]

print("allies of alice:", set_of_allies(alliances, "Alice"))
print("allies of competitors alice:",
      allies_of_competitors(alliances, conflicts, "Alice"))
print("dubious allies of alice:", allies_dubious(alliances, conflicts, "Alice"))
