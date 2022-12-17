#
# A module for 2D-layout
# 3nd version: add type hints
# pbv, 2022
#
from typing import List 
import functools

#
# A box is a list of strings representing rows
# 
Box = List[str]

def printbox(box: Box) -> None:
    """Print a box."""
    for row in box:
        print(row)

def empty(w:int, h:int) -> Box:
    """An empty box of given dimensions."""
    return fill(w, h, ' ')

def fill(w:int, h:int, c:str) -> Box:
    """A box filled with a single character."""
    return [w*c for _ in range(h)]

def string(txt: str) -> Box:
    """A box with a single text string."""
    return [txt]

def width(box: Box) -> int:
    """Get the width a box."""
    return len(box[0])

def height(box: Box) -> int:
    """Get the height of a box."""
    return len(box)

def above(box1: Box, box2: Box) -> Box:
    """Place box1 above box2."""
    w1 = width(box1)
    w2 = width(box2)
    if w1 < w2:
        pad1 = (w2-w1)*' '
        box1 = [row+pad1 for row in box1]
    elif w2 < w1:
        pad2 = (w1-w2)*' '
        box2 = [row+pad2 for row in box2]
    return box1 + box2

def beside(box1:Box, box2:Box) -> Box:
    """Place box1 to the left of box2."""
    h1 = height(box1)
    h2 = height(box2)
    if h1 < h2:
        pad1 = width(box1)*' '
        box1 = box1 + (h2-h1)*[pad1]
    elif h2 < h1:
        pad2 = width(box2)*' '
        box2 = box2 + (h1-h2)*[pad2]
    return [row1+row2 for (row1,row2) in zip(box1,box2)]

def horizontal(*boxes: Box) -> Box:
    return functools.reduce(beside, boxes)

def vertical(*boxes: Box) -> Box:
    return functools.reduce(above, boxes)

def frame(box: Box) -> Box:
    """Add a frame to a box."""
    w = width(box)
    t = '+' + '-'*w + '+'
    return [t] + ['|'+row+'|' for row in box] + [t]

