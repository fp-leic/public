#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 2024

@author: nmm
"""

"""
Lecture 11: Sets

Given a "database" of tv shows represented as a dictionary of tuples, get genre statistics.
"""

# version with lists, has repeated elements
# def genres(db):
#     """
#     Get all genres members from all shows, flattened, may repeat.
#     """
#     gs = []
#     for info in db.values():
#         gs += info[2]
#     return gs

def genres(db):
    """
    Get all genres members from all shows, flattened, may repeat.
    """
    gs = set() # empty set, since {} is reserved for empty dictionaries
    for info in db.values():
        gs = gs | set(info[2]) # convert current genres to set, and apply the union
    return gs

def unique_genres(db):
    """
    Get the number of unique genres.
    """
    return len(genres(db)) # len() works for sets, function composition

def common_genres(db):
    """
    Get common genres among all entries.
    """
    first = True # this is a flag to identify the first step, so that we don't apply the intersection
    for info in db.values():
        if first:
            gs = set(info[2]) # if first do not intersect
            first = False # and set the flag to false, no longer first
        else: 
            gs = gs & set(info[2]) # apply the intersection to get the common genres among all entries
    return gs

"""
ChatGPT prompt: "give me, as a Python dictionary, a list of 20 'prestige' tv shows. the key of the dictionary should should be the title, and the value a 4-list with (year, number of episodes, genres, watched status set to false)."
"""
shows = {
    "Breaking Bad": [2008, 62, ["Crime", "Drama", "Thriller"], False],
    "The Sopranos": [1999, 86, ["Crime", "Drama"], False],
    "Mad Men": [2007, 92, ["Drama", "Romance"], False],
    "Game of Thrones": [2011, 73, ["Action", "Adventure", "Drama"], False],
    "The Wire": [2002, 60, ["Crime", "Drama", "Thriller"], False],
    "Fargo": [2014, 53, ["Crime", "Drama", "Thriller"], False],
    "True Detective": [2014, 24, ["Crime", "Drama", "Mystery"], False],
    "Chernobyl": [2019, 5, ["Drama", "History", "Thriller"], False],
    "Stranger Things": [2016, 34, ["Drama", "Fantasy", "Horror"], False],
    "The Crown": [2016, 60, ["Biography", "Drama", "History"], False],
    "Better Call Saul": [2015, 63, ["Crime", "Drama", "Legal"], False],
    "Westworld": [2016, 36, ["Drama", "Sci-Fi", "Thriller"], False],
    "The Handmaid's Tale": [2017, 46, ["Drama", "Sci-Fi", "Thriller"], False],
    "House of Cards": [2013, 73, ["Drama", "Politics", "Thriller"], False],
    "Narcos": [2015, 30, ["Crime", "Drama", "Biography"], False],
    "Black Mirror": [2011, 22, ["Drama", "Sci-Fi", "Thriller"], False],
    "The Leftovers": [2014, 28, ["Drama", "Fantasy", "Mystery"], False],
    "The West Wing": [1999, 154, ["Drama", "Politics"], False],
    "Vikings": [2013, 89, ["Action", "Drama", "History"], False]
}

print(f"There are {unique_genres(shows)} unique genres.")

print("All (unique) genres:")
for g in genres(shows):
    print(f"\t{g}")

print("Common genres among all:")
for g in common_genres(shows):
    print(f"\t{g}")
