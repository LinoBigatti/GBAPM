#Transform an RGB5 color to a u16 (unsigned short)

def RGB5tou16(r, g, b):
    R = r & 0b11111
    G = g & 0b11111
    B = b & 0b11111
    
    RGB_ = R | (G << 5) | (B << 10)
    
    RGB = hex(RGB_)
    
    RGB = RGB[2:]
    
    if len(RGB) < 4:
        RGB = ("0" * (4 - len(RGB))) + RGB
    
    RGB = "0x" + RGB
    
    return RGB