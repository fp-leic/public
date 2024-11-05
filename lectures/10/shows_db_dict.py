#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 2024

@author: nmm
"""

"""
Lecture 10: Dictionaries

Manage a "database" of tv shows represented as a dictionary of tuples.
"""

def titles(db):
    """
    Get the titles of all shows.
    """
    keys = list(db.keys()) # keys() retrieves all keys of a dictionary as a "dict_keys" structure, let's convert to list
    # keys = list(db) # by default dictionary iteration is over keys, so this is actually equivalent
    return keys

def info(title,db):
    """
    Get the info of a show given its title.
    """
    if title in db.keys(): # tests if a key is in a dictionary
    # if title in db: # equivalent, but in doubt, call keys()
        return db[title] # dictionary look up, fails if key not in dictionary
    else: 
        return "title not found"
 
    # return db.get(title,"title not found") # the get() method looks up a key and returns a default value if absent, equivalent to code above

def years(db):
    """
    Get a list of shows with release year, as a list of tuples.
    """
    ys = []

    for title, info in db.items(): # tuple unpacking
        year, eps, gs, watched = info # tuple unpacking again
        ys.append((title,year)) # notice that this is not the same as "ys.append(title,year)", which would be an error (append() only receive has one argument)
        # ys.extend((title,year)) # what about this?

    # the same loop without unpacking
    # for entry in db.items():
    #     title = entry[0]
    #     info = entry[1]
    #     year = info[0] 
    #     ys.append((title,year))

    return ys

def watched_eps(db):
    """
    Get the total number of watched episodes.
    """
    c = 0

    for year, eps, gs, watched in db.values(): # iterate over the values(), we don't need the titles, with list unpacking
        if watched:
            c += eps

    return c

def genres(db):
    """
    Get all genres members from all shows, flattened, may repeat.
    """
    gs = []
    for info in db.values(): # iterate over the values(), we don't need the titles
        gs += info[2]
    return gs

def count_genres(db):
    """
    For each genre occurring in the database, find how many entries.
    """
    count = {} # create a dictionary to keep count for each genre
    for info in db.values():
        for genre in info[2]:
            count[genre] = count.get(genre,0) + 1 
            # without get()
            # if genre not in count.keys():
            #     count[genre] = 0 + 1
            # else:
            #     count[genre] = count[genre] + 1
    return count


def mark_watched(title,db):
    """
    Mark a given show as watched.
    """
    db[title][3] = True # this updates the value inside the info list for a show; will fail if show does not exist!
    # this is a mutator, it changes the given dictionary and returns nothing

def add_show(title,info,db):
    """
    Insert a show in the database.
    """
    db[title] = info # this assigns info to the given title; if key doesn't exist, it is created; otherwise the value is replaced
    # this is a mutator, it changes the given dictionary and returns nothing


# def genres(db):
#     gs = set()
#     for info in db.values():
#         gs = gs | set(info[2])
#     return (gs)

# def common_genres(db):
#     first = True
#     for info in db.values():
#         if first:
#             gs = set(info[2])
#             first = False
#         else: 
#             gs = gs & set(info[2])
#     return gs




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

show = "Black Mirror"
print(f"{show} info is {info(show,shows)}.")
show = "The Twilight Zone"
print(f"{show} info is {info(show,shows)}.")
print("All titles:")
for t in titles(shows):
    print(f"\t{t}")

print("Release dates:")
for t,y in years(shows):
    print(f"\t{t} ({y})")

print("All genres:")
for g in genres(shows):
    print(f"\t{g}")

print("Genre count:")
for g,c in count_genres(shows).items():
    print(f"\t{g}: {c}")

show = "Black Mirror"
mark_watched(show, shows)
print(f"{show} marked as watched.")
show = "Chernobyl"
mark_watched(show, shows)
print(f"{show} marked as watched.")

show = "The Twilight Zone"
print(f"{show} added.")
add_show(show, [1959, 156, ["Drama", "Fantasy", "Horror"], True], shows)
print(f"{show} info is {info(show,shows)}.")

print(f"Total watched eps: {watched_eps(shows)}")
