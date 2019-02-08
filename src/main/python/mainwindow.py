#The main window.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

from ColorMixer import *
from Rgb5toU16 import *
from Rgb5toU32 import *
from globals import *
from Export import *

main_app = QApplication([])
main_root = QWidget()
pal_list = QComboBox()
pal_index_counter = 0

def main_window():
    main_root.setWindowTitle('GBA Palette Manager.')
    main_app.setStyle('Fusion')
    layout0 = QHBoxLayout()
    layout1 = QHBoxLayout()
    layout2 = QHBoxLayout()
    layout3 = QHBoxLayout()
    layout = QVBoxLayout()
    
    open_file_button = QPushButton("Open.")
    open_file_button.clicked.connect(openfile)
    
    pal_list.addItem("0")
    pal_list.currentIndexChanged.connect(palindexchange)
    
    add_pal_index_button = QPushButton("Add palette index.")
    add_pal_index_button.clicked.connect(addpalindex)
    
    rem_pal_index_button = QPushButton("Remove palette index.")
    rem_pal_index_button.clicked.connect(rempalindex)
    
    edit_pal_index_button = QPushButton("Edit color at current index.")
    edit_pal_index_button.clicked.connect(editpalindex)
    
    show_pal_index_button = QPushButton("Show the current palette index color.")
    show_pal_index_button.clicked.connect(showpalindex)
    
    save_file_button = QPushButton("Save.")
    save_file_button.clicked.connect(savefile)
    
    export_button = QPushButton("Export.")
    export_button.clicked.connect(exportfile)
    
    layout0.addWidget(open_file_button)
    
    layout1.addWidget(pal_list)
    layout1.addWidget(add_pal_index_button)
    layout1.addWidget(rem_pal_index_button)
    
    layout2.addWidget(edit_pal_index_button)
    layout2.addWidget(show_pal_index_button)
    
    layout3.addWidget(save_file_button)
    layout3.addWidget(export_button)
    
    layout.addLayout(layout0)
    layout.addLayout(layout1)
    layout.addLayout(layout2)
    layout.addLayout(layout3)
    
    main_root.setLayout(layout)
    
    main_root.show()
    main_app.exec_()

def openfile():
    global pal_index_counter
    
    filedialog = QFileDialog
    filepath = filedialog.getOpenFileName(main_root, 'Open file', 'c:\\', "Json files (*.json)")
    with open(filepath[0], 'r') as f:
        data = json.load(f)
        
        length = data["length"]
        pal_list.clear()
        pal_index_counter = length - 1
        for ii in range(0, length):
            pal_list.addItem(str(ii))
        pal_index[0] = 0
        
        pal_data = data["palette"]
        
        pal.clear()
        
        for ii in pal_data:
            pal.append(ii)
            print(ii)

def savefile():
    filedialog = QFileDialog
    filepath = filedialog.getSaveFileName(main_root, 'Save file', 'c:\\', "Json files (*.json)")
    with open(filepath[0], 'w') as f:
        data = {}
        data["length"] = pal_index_counter + 1
        data["palette"] = pal
        
        f.write(json.dumps(data, ensure_ascii = False))
        
        f.close()

def exportfile():
    export_handler(pal_index_counter + 1)

def palindexchange(i):
    global pal_index
    
    pal_index[0] = i

def addpalindex():
    global pal_index_counter
    
    pal_index_counter += 1
    pal_list.addItem(str(pal_index_counter))
    pal.append([0, 0, 0])

def rempalindex():
    global pal_index_counter
    
    pal_list.removeItem(pal_index_counter)
    pal_index_counter -= 1
    pal.pop()

def editpalindex():
    color_mixer(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])

def showpalindex():
    global pal
    global pal_index
    
    alert = QMessageBox()
    alert.setAutoFillBackground(True)
    alert.setText('Current color: \nRed: ' + str(pal[pal_index[0]][0]) + '\nGreen: ' + str(pal[pal_index[0]][1]) + '\nBlue: ' + str(pal[pal_index[0]][2]) + '\nHex (16 bit): ' + str(RGB5tou16(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])))
    bgpal = alert.palette()
    clr_ = RGB5toRGB8(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])
    bgpal.setColor(alert.backgroundRole(), QColor(clr_[0], clr_[1], clr_[2]))
    alert.setPalette(bgpal)
    alert.exec_()