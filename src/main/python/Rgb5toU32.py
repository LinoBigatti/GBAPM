#Transform two RGB5 colors to a u32 (unsigned int)

from Rgb5toU16 import *

def RGB5tou32(r1, g1, b1, r2, g2, b2):
    RGB1 = RGB5tou16(r1, g1, b1)
    RGB1 = RGB1[2:]
    
    RGB2 = RGB5tou16(r2, g2, b2)
    RGB2 = RGB2[2:]
    
    print(RGB1)
    
    RGB = RGB2 + RGB1
    RGB = "0x" + RGB
    
    return RGB