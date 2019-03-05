#Transform an RGB5 color to a u16 (unsigned short)

from log import *

def RGB5tou16(r, g, b):
    R = r & 0b11111
    G = g & 0b11111
    B = b & 0b11111
    trace("RGB5 to u16", "Colors clipped. (" + str([R, G, B]) + ")")
    
    RGB_ = R | (G << 5) | (B << 10)
    trace("RGB5 to u16", "Colors joined together. (" + str(RGB_) + ")")
    
    RGB = hex(RGB_)
    RGB = RGB[2:]
    trace("RGB5 to u16", "Color converted to hex. (" + RGB + ")")
    
    if len(RGB) < 4:
        RGB = ("0" * (4 - len(RGB))) + RGB
    trace("RGB5 to u16", "Color filled. (" + RGB + ")")
    
    RGB = "0x" + RGB
    trace("RGB5 to u16", "Hex symbol added. (" + RGB + ")")
    
    return RGB