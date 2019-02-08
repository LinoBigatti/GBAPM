#Transform from RGB5 (GBA format) to RGB8 (Everything else format)

def RGB5toRGB8(r, g, b):
    mul = 8.22580645161
    
    if r != '':
        R = round(int(r) * mul)
    else:
        R = 0
    if g != '':
        G = round(int(g) * mul)
    else:
        G = 0
    if b != '':
        B = round(int(b) * mul)
    else:
        B = 0
    
    result = [R, G, B]
    
    return result