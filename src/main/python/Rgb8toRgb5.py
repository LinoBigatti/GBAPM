#Transform from RGB8 (Everything else format) to RGB5 (GBA format)

from log import *

def RGB8toRGB5(r, g, b):
    div = 8.22580645161
    
    R = round(r / div)
    G = round(g / div)
    B = round(b / div)
    
    result = [R, G, B]
    
    trace("RGB8 to RGB5", "Transformed " + str([r, g, b]) + " into " + str(result) + ". Divisor: " + str(div) + ".")
    return result