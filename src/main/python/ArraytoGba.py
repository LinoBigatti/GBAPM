#Save to a C file.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os

from log import *

def ArraytoGBA(array, length, lengthbytes, datatype, pathtuple):
    path_basename_ = os.path.basename(pathtuple[0])[:-2]
    path_basename = path_basename_.lower()
    header_path = pathtuple[0]
    header_path = header_path[:-2] + ".h"
    trace("Array to GBA", "Header path builded. (" + header_path + ")")
    
    source = "//  GBA palette, imported by L!no\'s GBA palette manager.\n"
    source += "//  Type: " + datatype + ".\n"
    source += "//  Length: " + str(length) + ".\n"
    source += "//  Length (In bytes): " + str(lengthbytes) + ".\n"
    source += "//  File basename: " + path_basename + ".\n\n"
    trace("Array to GBA", "C file top builded. Contents: " + source)
    
    header = "//  GBA palette, imported by L!no\'s GBA palette manager.\n"
    header += "//  Type: " + datatype + ".\n"
    header += "//  Length: " + str(length) + ".\n"
    header += "//  Length (In bytes): " + str(lengthbytes) + ".\n"
    header += "//  File basename: " + path_basename + ".\n\n"
    trace("Array to GBA", "H file top builded. Contents: " + header)
    
    i = 0
    source += "const " + datatype + " " + path_basename + "Palette[" + str(length) + "] __attribute__((aligned(4))) __attribute__((visibility(\"hidden\"))) =\n"
    source += "{\n"
    source += "	"
    for num in array:
        i += 1
        if i == 8:
            i = 0
            source += "\n	"
        source += num + ", "
    source += "\n};"
    trace("Array to GBA", "C file builded. Contents: " + source)
    
    with open(pathtuple[0], 'w') as f:
        f.write(source)
        f.close()
    trace("Array to GBA", "C file saved.")
    
    header += "#ifndef " + path_basename.upper() + "_PAL_H\n"
    header += "#define " + path_basename.upper() + "_PAL_H\n\n"
    
    header += "#define " + path_basename + "PaletteLength " + str(lengthbytes) + "\n"
    header += "extern const " + datatype + " " + path_basename + "Palette[" + str(length) + "];\n\n"
    
    header += "#endif //" + path_basename.upper() + "_PAL_H"
    trace("Array to GBA", "H file builded. Contents: " + header)
    
    with open(header_path, 'w') as f:
        f.write(header)
        f.close()
    trace("Array to GBA", "H file saved.")
    
    alert = QMessageBox()
    alert.setText('Exported.')
    alert.exec_()