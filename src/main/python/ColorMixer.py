#mix and return a color.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from globals import *
from Rgb5toRgb8 import *

clr_mixer_app = QApplication([])
clr_mixer_root = QWidget()
redvalue = QLineEdit()
greenvalue = QLineEdit()
bluevalue = QLineEdit()
clr = []

def color_mixer_init():
    clr_mixer_root.setWindowTitle('GBA color mixer.')
    clr_mixer_app.setStyle('Fusion')
    clr_mixer_root.setAutoFillBackground(True)
    layout = QFormLayout()
    
    RGB5Validator = QIntValidator(0, 31)
    
    redvalue.setValidator(RGB5Validator)
    redvalue.setMaxLength(2)
    redvalue.setAlignment(Qt.AlignRight)
    redvalue.textChanged.connect(clrchanged)
    
    greenvalue.setValidator(RGB5Validator)
    greenvalue.setMaxLength(2)
    greenvalue.setAlignment(Qt.AlignRight)
    greenvalue.textChanged.connect(clrchanged)
    
    bluevalue.setValidator(RGB5Validator)
    bluevalue.setMaxLength(2)
    bluevalue.setAlignment(Qt.AlignRight)
    bluevalue.textChanged.connect(clrchanged)
    
    layout.addRow("Red", redvalue)
    layout.addRow("Green", greenvalue)
    layout.addRow("Blue", bluevalue)
    
    savebutton = QPushButton('Save')
    savebutton.clicked.connect(on_savebutton_click)
    layout.addWidget(savebutton)
    clr_mixer_root.setLayout(layout)

def clrchanged(clr):
    pal = clr_mixer_root.palette()
    clr = RGB5toRGB8(redvalue.text(), greenvalue.text(), bluevalue.text())
    pal.setColor(clr_mixer_root.backgroundRole(), QColor(clr[0], clr[1], clr[2]))
    clr_mixer_root.setPalette(pal)

def on_savebutton_click():
    global clr
    global pal
    global pal_index
    
    alert = QMessageBox()
    alert.setText('Saved.')
    if redvalue.text() != '':
        R = int(redvalue.text())
    else:
        R = 0
    if greenvalue.text() != '':
        G = int(greenvalue.text())
    else:
        G = 0
    if bluevalue.text() != '':
        B = int(bluevalue.text())
    else:
        B = 0
    
    clr = [R, G, B]
    alert.exec_()
    clr_mixer_root.hide()
    
    pal[pal_index[0]] = clr


def color_mixer(r, g, b):
    global clr

    clr = [r, g, b]
    
    redvalue.setText(str(r))
    greenvalue.setText(str(g))
    bluevalue.setText(str(b))
    
    clr_mixer_root.show()
    clr_mixer_app.exec_()