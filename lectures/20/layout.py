#
# A module for simple 2D-layout
#
# pbv, 2022
#
import functools

# ---------------------------------------------------
# BOXES
# ---------------------------------------------------
# A 2D "box" is a list of strings representing rows;
# for example the boxes
#
#  AAAA     BBB
#  AAAA     BBB
#           BBB
#
# are represented by
#
# ['AAAA', 'AAAA'] and ['BBB', 'BBB', 'BBB']
#
# Properties of boxes:
# - number of rows and columns may be different
# - every row has exactly the same width
# - at least 1 row and 1 column
#

# Utility functions 

def printbox(box):
    """Print a box."""
    for row in box:
        print(row)

# Create simple boxes        
        
def empty(w, h):
    """An empty box of given dimensions."""
    return fill(w, h, ' ')

def fill(w, h, c):
    """A box filled with a single character."""
    return [w*c for _ in range(h)]

def string(txt):
    """A box with a single text string."""
    return [txt]

# Get the dimensions of a box

def width(box):
    """Get the width a box."""
    return len(box[0])


def height(box):
    """Get the height of a box."""
    return len(box)

# Combine two boxes vertically, i.e.:
# 
#  above(AAAA , BBBB) = AAAA     
#       (AAAA   BBBB    AAAA
#               BBBB    BBBB
#                       BBBB
#                       BBBB
#  

def above(box1, box2):
    """Place box1 above box2."""
    assert width(box1) == width(box2)  # for now only
    return box1 + box2

# Combine two boxes horizontally, i.e.
#
#  beside(AAAA, BB) = AAAABB
#         AAAA  BB    AAAABB


def beside(box1, box2):
    """Place box1 to the left of box2."""
    assert height(box1) == height(box2) # for now only
    return [ row1+row2 for (row1,row2) in zip(box1,box2)]

# Combine lists of boxes

def horizontal(*boxes):
    return functools.reduce(beside, boxes)

def vertical(*boxes):
    return functools.reduce(above, boxes)

# Add a frame to a box

def frame(box):
    """Add a frame to a box."""
    w = width(box)
    top = '+' + '-'*w + '+'
    return [top] + ['|'+row+'|' for row in box] + [top]

