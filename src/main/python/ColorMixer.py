#mix and return a color.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Rgb8toRgb5 import *
from Rgb5toRgb8 import *
from log import *

def color_mixer(r, g, b):
    R, G, B = RGB5toRGB8(r, g, b)
    trace("Palette handling", "Old value RGB8: " + str([R, G, B]) + ".")
    clr_8 = QColorDialog.getColor(QColor(R, G, B))
    trace("Palette handling", "Color mixer window started.")
    clr_5 = RGB8toRGB5(clr_8.red(), clr_8.green(), clr_8.blue())
    
    return clr_5