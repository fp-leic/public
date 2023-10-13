#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct 2023

@author: nmm
"""

"""
Lecture 07: Tuples

Manage a "database" of tv shows represented as nested tuples.
"""

def titles(shows):
    """
    Get the titles of the shows.
    """
    result = () 
    for s in shows:
        result = result + (s[0],)
        # just s[0:2] is an error: cannot concatenate tuples with strings!
    
    # you can always iterate over the indices, but in this case they are not really necessary
    # for i in range(len(shows)):
    #     result = result + (shows[i][0],)

    return result

def short(shows):
    """
    Get short version of the shows, only title and year.
    """
    result = () 
    for s in shows:
        result += (s[0:2],) # or ((s[0],s[1]),)
        # just s[0:2] works this time, but is it what we want?

    return result

def stats(shows):
    """
    Get statististics about number of episodes and cast members.
    """
    cast = 0
    eps = 0
    # tuples can be unpacked during assignment
    # this is the same as iterating s over shows and then indexing s[2] and s[3]
    for t, y, e, a, g in shows: 
        cast = cast + len(a)
        eps = eps + e

    # return tuples when you need to pass several values
    return (cast,eps)

def cast(shows):
    """
    Get all cast members from all shows, flattened.
    """    
    res = ()
    for s in shows:
        res += s[3]
        # this will flatten the cast tuples into a single tuple
        # what if we wanted to keep them grouped by show? encapsulate in a singleton (s[3],)
    return res

def loud_cast(shows):
    """
    Get all cast members from all shows in ALL CAPS, flattened.
    """    
    res = ()
    res = ()
    for s in shows:
        for c in s[3]:
            upper_name = c.upper()
            res += (upper_name,)
        # what if we wanted to keep them grouped by show? needs an additional accumulator in the inner loop for each show
    return res


shows = (("Breaking Bad",2008,62,("Bryan Cranston", "Aaron Paul"),("Crime","Drama","Thriller")), 
         ("Mad Men",2007,92,("Jon Hamm",),("Drama",)), 
         ("The Wire",2002,60,(),("Crime","Drama")), 
         ("Deadwood",2004,36,("Timothy Olyphant", "Ian McShane"),("Western","Drama")),
         ("Firefly",2002,14,("Nathan Fillion", "Gina Torres", "Alan Tudyk"),("Sci-fi","Western")))

ts = titles(shows)
ss = short(shows)
c, e = stats(shows)
qcs = cast(shows)
lcs = loud_cast(shows)

print("titles")
# iterating over indices is useful when we want to know the position of each item
for i in range(len((qcs))):
    print(f"\t{i}: {qcs[i]}")

print("titles + years")
# you can use enumerate if you need both indices and values (and you can unpack the pair)
for i,t in enumerate(ss):
    print(f"\t{i}: {t[0]}, {t[1]}")

print("#eps: ",e)
print("#cast: ",c)
print("cast: ",qcs)
print("CAST: ",lcs) 




