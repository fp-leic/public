#
# Example using the layout2 module
# pbv, 2022
#
from layout3 import empty, vertical, horizontal, string, frame, printbox

box1 = vertical(string("Merry"), 
                string("Christmas"))

                # Try introducing a type error, .e.g.
                # use "2023" instead of string("2023")
box2 = vertical(string("Happy new year!"),
                string("2023"))

star = vertical(string(" * "),
                string("* *"),
                string(" *  "))
             
msg = frame(vertical(horizontal(star, empty(1,3), frame(box1)),
                     horizontal(frame(box2), empty(1,1), frame(star))))

printbox(msg)                    


