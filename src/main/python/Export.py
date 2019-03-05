#GBA exporter

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Rgb5toU16 import *
from Rgb5toU32 import *
from globals import *
from ArraytoGba import *
from log import *

export_app = QApplication([])
export_root = QWidget()
padcheck = QCheckBox("Pad palette?")
padding = QComboBox()
datatype = QComboBox()
palette = pal
length = 0
type = 0
padto = 2

def export_init():
    export_root.setWindowTitle('GBA palette exporter.')
    export_app.setStyle('Fusion')
    layout0 = QVBoxLayout()
    layout1 = QVBoxLayout()
    layoutoptions = QHBoxLayout()
    layout = QVBoxLayout()
    
    layout0desc = QLabel()
    layout0desc.setText("Data type:")
    
    datatype.addItems(["u16", "u32"])
    datatype.currentIndexChanged.connect(datatype_changed)
    
    layout0.addWidget(layout0desc)
    layout0.addWidget(datatype)
    
    padcheck.stateChanged.connect(padcheck_changed)
    
    padding.addItems(["2", "4", "8", "16"])
    padding.setEnabled(False)
    padding.currentIndexChanged.connect(padding_changed)
    
    layout1.addWidget(padcheck)
    layout1.addWidget(padding)
    
    layoutoptions.addLayout(layout0)
    layoutoptions.addLayout(layout1)
    
    export_button = QPushButton("Export!")
    export_button.clicked.connect(export)
    
    layout.addLayout(layoutoptions)
    layout.addWidget(export_button)
    export_root.setLayout(layout)
    
    trace("Exporter", "UI builded.")
    
def datatype_changed(i):
    global type
    
    type = i
    if i == 1:
        padcheck.setChecked(True)
    trace("Exporter", "Datatype changed. New datatype: " + str(datatype.currentText()))
    
def padcheck_changed():
    trace("Exporter", "Padding enabler state changed. New state: " + str(padcheck.isChecked()))
    
    if padcheck.isChecked() == True:
        padding.setEnabled(True)
    else:
        padding.setEnabled(False)

def padding_changed():
    global padto
    
    trace("Exporter", "Padding limit changed. New limit: " + str(padding.currentText()))
    padto = int(padding.currentText())

def export():
    global palette
    
    trace("Exporter", "New export request. Handling...")
    
    export_pal = []
    
    if length % padto:
        i = padto - length % padto
        for ii in range(0, i):
            palette.append([0, 0, 0])
    trace("Exporter", "Palette padded.")
    
    if type == 0:
        for color in palette:
            export_pal.append(RGB5tou16(color[0], color[1], color[2]))
    else:
        for i in range(0, len(palette), 2):
            clr1 = palette[i]
            clr2 = palette[i + 1]
            
            export_pal.append(RGB5tou32(clr1[0], clr1[1], clr1[2], clr2[0], clr2[1], clr2[2]))
    trace("Exporter", "Palette converted to selected datatype. (" + str(datatype.currentText()) + ")")
    
    filedialog = QFileDialog
    filepath = filedialog.getSaveFileName(export_root, 'Save file', 'c:\\', "C source file (*.c)")
    trace("Exporter", "File chose. (" + filepath[0] + ")")
    
    if type == 0:
        ArraytoGBA(export_pal, len(export_pal), len(export_pal) * 2, "unsigned short", filepath)
    else:
        ArraytoGBA(export_pal, len(export_pal), len(export_pal) * 4, "unsigned int", filepath)
    
    trace("Exporter", "Exported successfully.")
    export_root.hide()

def export_handler(len):
    global length
    
    length = len
    export_root.show()
    export_app.exec_()