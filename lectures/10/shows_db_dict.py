#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023

@author: nmm
"""

"""
Lecture 10: Dictionaries

Revisiting lecture 7, manage a "database" of tv shows represented as a dictionary of tuples.
"""


def titles(shows):
    """
    Get the titles of the shows.
    """
    return list(shows)  # iteration in dictionaries is over keys


def short(shows):
    """
    Get short version of the shows, only title and year.
    """
    result = []
    for show in shows:
        result += [(show, shows[show][0])]

    return result


def stats(shows):
    """
    Get statistics about number of episodes and cast members.
    """
    cast = 0
    eps = 0
    for title, info in shows.items():  # items() allows iterating over keys and values simultaneously
        y, e, a, g = info  # tuple unpacking
        cast = cast + len(a)
        eps = eps + e

    return (cast, eps)


def cast(shows):
    """
    Get all cast members from all shows, flattened.
    """
    res = ()
    for info in shows.values():  # values() iterates only over values of a dictionary
        res += info[2]
    return res


def loud_cast(shows):
    """
    Get all cast members from all shows in ALL CAPS, flattened.
    """
    res = ()
    res = ()
    for info in shows.values():  # values() iterates only over values of a dictionary
        for c in info[2]:
            upper_name = c.upper()
            res += (upper_name,)
    return res


def info(shows, title):
    """
    Get the info of a show given its title.
    """
    return shows[title]  # dictionary indexation


def update(shows, title, year):
    """
    Update the year of a given show in the dictionary.
    """
    info = shows[title]
    # since tuples are immutable, you need to create a new tuples with the changed year
    info = (year,) + info[1:]
    shows[title] = info
    # if a show information was instead stored as a list (mutable), you could just do
    # info[0] = year

    # this is a mutator, changes the dictionary, doesn't need to return it


shows_2000s = {"Breaking Bad": (2008, 62, ("Bryan Cranston", "Aaron Paul"), ("Crime", "Drama", "Thriller")),
               "Mad Men": (2007, 92, ("Jon Hamm",), ("Drama",)),
               "The Wire": (2002, 60, (), ("Crime", "Drama")),
               "Deadwood": (2004, 36, ("Timothy Olyphant",
                                       "Ian McShane"), ("Western", "Drama")),
               "Firefly": (2002, 14, ("Nathan Fillion", "Gina Torres", "Alan Tudyk"), ("Sci-fi", "Western"))}

# no value returned, but has a side effect in the dictionary
update(shows_2000s, "Mad Men", 9999)
print(shows_2000s)

ts = titles(shows_2000s)
ss = short(shows_2000s)
c, e = stats(shows_2000s)
qcs = cast(shows_2000s)
lcs = loud_cast(shows_2000s)

print("titles")
for i in range(len((qcs))):
    print(f"\t{i}: {qcs[i]}")

print("titles + years")
for i, t in enumerate(ss):
    print(f"\t{i}: {t[0]}, {t[1]}")

print("#eps: ", e)
print("#cast: ", c)
print("cast: ", qcs)
print("CAST: ", lcs)
