#
# Example using the layout2 module
# pbv, 2022
#
from layout2 import empty, vertical, horizontal, string, frame, printbox

box1 = vertical(string("Merry"),
                string("Christmas"))

box2 = vertical(string("Happy new year!"),
                string("2023"))

star = vertical(string(" * "),
                string("* *"),
                string(" *  "))
             
msg = frame(vertical(horizontal(star, empty(1,1), frame(box1)),
                     horizontal(frame(box2), empty(1,1), frame(star))))

printbox(msg)                    


