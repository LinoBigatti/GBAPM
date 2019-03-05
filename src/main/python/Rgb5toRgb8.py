#Transform from RGB5 (GBA format) to RGB8 (Everything else format)

from log import *

def RGB5toRGB8(r, g, b):
    mul = 8.22580645161
    
    R = round(r * mul)
    G = round(g * mul)
    B = round(b * mul)
    
    result = [R, G, B]
    
    trace("RGB5 to RGB8", "Transformed " + str([r, g, b]) + " into " + str(result) + ". Multiplier: " + str(mul) + ".")
    return result