#Convert to a JASC PAL file.

from Rgb5toRgb8 import *

def ArraytoJascPal(pal, length, Path):
    output = "JASC-PAL\r\n"
    output += "0100\r\n"
    output += str(length)
    
    for color in pal:
        output += "\r\n"
        clr = RGB5toRGB8(color[0], color[1], color[2])
        output += str(clr[0]) + " " + str(clr[1]) + " " + str(clr[2])
    
    with open(Path, 'w') as f:
        f.write(output)
        f.close()