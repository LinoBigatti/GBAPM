#Save to a C file.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os

def ArraytoGBA(array, length, lengthbytes, datatype, pathtuple):
    path_basename_ = os.path.basename(pathtuple[0])[:-2]
    path_basename = path_basename_.lower()
    header_path = pathtuple[0]
    header_path = header_path[:-2] + ".h"
    
    source = "//  GBA palette, imported by L!no\'s GBA palette manager.\n"
    source += "//  Type: " + datatype + ".\n"
    source += "//  Length: " + str(length) + ".\n"
    source += "//  Length (In bytes): " + str(lengthbytes) + ".\n"
    source += "//  File basename: " + path_basename + ".\n\n"
    
    header = "//  GBA palette, imported by L!no\'s GBA palette manager.\n"
    header += "//  Type: " + datatype + ".\n"
    header += "//  Length: " + str(length) + ".\n"
    header += "//  Length (In bytes): " + str(lengthbytes) + ".\n"
    header += "//  File basename: " + path_basename + ".\n\n"
    
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
    
    with open(pathtuple[0], 'w') as f:
        f.write(source)
        f.close()
    
    header += "#ifndef " + path_basename.upper() + "_PAL_H\n"
    header += "#define " + path_basename.upper() + "_PAL_H\n\n"
    
    header += "#define " + path_basename + "PaletteLength " + str(lengthbytes) + "\n"
    header += "extern const " + datatype + " " + path_basename + "Palette[" + str(length) + "];\n\n"
    
    header += "#endif //" + path_basename.upper() + "_PAL_H"
    
    with open(header_path, 'w') as f:
        f.write(header)
        f.close()
    
    alert = QMessageBox()
    alert.setText('Exported.')
    alert.exec_()