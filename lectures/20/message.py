#
# Example using the layout module
# pbv, 2022
#

from layout import vertical, horizontal, string, empty, frame, printbox

box1 = vertical(string("Merry    "),
                string("Christmas"))

box2 = vertical(string("Happy new year!"),
                string("2023           "))


tree = vertical(string("  *  "),
                string(" /*\\ "),
                string("/***\\"),
                string("  |  "))

msg = frame(horizontal(frame(box1),
                       empty(3,4),
                       tree,
                       empty(3,4),
                       frame(box2)))

printbox(msg)                    
