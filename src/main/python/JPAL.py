#Convert to a JASC PAL file.

from Rgb5toRgb8 import *
from log import *

def ArraytoJascPal(pal, length, Path):
    output = "JASC-PAL\r\n"
    output += "0100\r\n"
    output += str(length)
    trace("Save as PAL", "Header built. Contents: " + output)
    
    for color in pal:
        output += "\r\n"
        clr = RGB5toRGB8(int(color[0]), int(color[1]), int(color[2]))
        output += str(clr[0]) + " " + str(clr[1]) + " " + str(clr[2])
    trace("Save as PAL", "PAL file built. Contents: " + output)
    
    with open(Path, 'w') as f:
        f.write(output)
        f.close()
    trace("Save as PAL", "File saved successfully.")