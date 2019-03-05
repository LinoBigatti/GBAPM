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
from JPAL import *
from log import *

main_app = QApplication([])
main_root = QMainWindow()
main_widget = QWidget()
pal_list = QComboBox()
pal_index_counter = 15

def main_window():
    main_root.setWindowTitle('GBA Palette Manager.')
    main_app.setStyle('Fusion')
    main_menu = main_root.menuBar()
    file_menu = main_menu.addMenu('File')
    layout0 = QHBoxLayout()
    layout1 = QHBoxLayout()
    layout = QVBoxLayout()
    
    open_json_button = QAction("Open JSON.")
    open_json_button.setStatusTip("Open a .json file.")
    open_json_button.setShortcut('Ctrl+Shift+J')
    open_json_button.triggered.connect(openjson)
    
    open_pal_button = QAction("Open PAL.")
    open_pal_button.setStatusTip("Open a .pal file.")
    open_pal_button.setShortcut('Ctrl+Shift+P')
    open_pal_button.triggered.connect(openpal)
    
    save_json_button = QAction("Save as JSON.")
    save_json_button.setStatusTip("Save as a .json file.")
    save_json_button.setShortcut('Ctrl+J')
    save_json_button.triggered.connect(savejson)
    
    save_pal_button = QAction("Save as PAL.")
    save_pal_button.setStatusTip("Save as a .pal file.")
    save_pal_button.setShortcut('Ctrl+P')
    save_pal_button.triggered.connect(savepal)
    
    export_button = QAction("Export to C.")
    export_button.setStatusTip("Export to a .c file. (GBA)")
    export_button.setShortcut('Ctrl+E')
    export_button.triggered.connect(exportfile)
    
    for i in range(0, 16):
        pal_list.addItem(str(i))
    pal_list.currentIndexChanged.connect(palindexchange)
    
    pal_size_label = QLabel("Palette size:")
    pal_size_list = QComboBox()
    pal_size_list.addItem("16")
    pal_size_list.addItem("256")
    pal_size_list.currentIndexChanged.connect(palsizechange)
    
    edit_pal_index_button = QPushButton("Edit color at current index.")
    edit_pal_index_button.clicked.connect(editpalindex)
    
    show_pal_index_button = QPushButton("Show the current palette index color.")
    show_pal_index_button.clicked.connect(showpalindex)
    
    file_menu.addAction(open_json_button)
    file_menu.addAction(open_pal_button)
    file_menu.addAction(save_json_button)
    file_menu.addAction(save_pal_button)
    file_menu.addAction(export_button)
    
    layout0.addWidget(pal_list)
    layout0.addWidget(pal_size_label)
    layout0.addWidget(pal_size_list)
    
    layout1.addWidget(edit_pal_index_button)
    layout1.addWidget(show_pal_index_button)
    
    layout.addLayout(layout0)
    layout.addLayout(layout1)
    trace("Main Window", "Layouts builded.")
    
    main_widget.setLayout(layout)
    main_root.setCentralWidget(main_widget)
    
    main_root.show()
    main_app.exec_()

def openjson():
    global pal_index_counter
    
    filedialog = QFileDialog
    filepath = filedialog.getOpenFileName(main_root, 'Open file', 'c:\\', "Json files (*.json)")
    trace("Open as JSON", "File chose. (" + filepath[0] + ")")
    
    with open(filepath[0], 'r') as f:
        data = json.load(f)
        trace("Open as JSON", "JSON loaded, contents: " + str(data))
        
        length = data["length"]
        trace("Open as JSON", "Length read. (" + str(length) + ")")
        pal_list.clear()
        pal_index_counter = length - 1
        for ii in range(0, length):
            pal_list.addItem(str(ii))
            trace("Open as JSON", "Palette list item added. (" + str(ii) + ")")
        pal_index[0] = 0
        
        pal_data = data["palette"]
        trace("Open as JSON", "Palette data loaded. Content: " + str(pal_data))
        
        pal.clear()
        
        for ii in pal_data:
            pal.append(ii)
        
        trace("Open as JSON", "File loaded successfully")

def openpal():
    global pal_index_counter
    global pal
    
    filedialog = QFileDialog
    filepath = filedialog.getOpenFileName(main_root, 'Save file', 'c:\\', "Palette files (*.pal)")
    trace("Open as PAL", "File chose. (" + filepath[0] + ")")
    
    with open(filepath[0], 'r') as f:
        content_raw = f.read()
        trace("Open as PAL", "RAW content loaded. Content: " + content_raw)
        f.close()
    
    content = content_raw.split('\n\n')
    if content_raw.startswith('JASC-PAL\n\n0100\n\n'):
        trace("Open as PAL", "Valid PAL header.")
        pal_list.clear()
        pal = []
        pal_index[0] = 0
        
        if content[2] == "16":
            trace("Open as PAL", "Size: 16 colors.")
            pal_index_counter = 15
            pal_list.setCurrentIndex(0)
        elif content[2] == "256":
            trace("Open as PAL", "Size: 256 colors.")
            pal_index_counter = 255
            pal_list.setCurrentIndex(1)
        else:
            trace("Open as PAL", "Invalid size. Size: " + content[2])
            error = QMessageBox()
            error.setWindowTitle("Error.")
            error.setIcon(QMessageBox.Critical)
            error.setText("Invalid JASC-PAL file.")
            error.exec_()
        
        for i in range(3, len(content)):
            s_ = content[i]
            s = s_.split(' ')
            
            r = int(s[0])
            g = int(s[1])
            b = int(s[2])
            trace("Open as PAL", "RGB colors for index " + str(i - 3) + " loaded. R: " + s[0] + ". G: " + s[1] + ". B: " + s[2] + ".")
            
            clr = RGB8toRGB5(r, g, b)
            trace("Open as PAL", "RGB colors for index " + str(i - 3) + " converted to RGB5. Contents: " + str(clr))
            pal.append(clr)
            
            pal_list.addItem(str(i - 3))
        
        trace("Open as PAL", "File loaded successfully.")
    else:
        trace("Open as PAL", "Invalid PAL header. Expected: JASC-PAL\n\n0100\n\n")
        error = QMessageBox()
        error.setWindowTitle("Error.")
        error.setIcon(QMessageBox.Critical)
        error.setText("Invalid JASC-PAL file.")
        error.exec_()

def savejson():
    filedialog = QFileDialog
    filepath = filedialog.getSaveFileName(main_root, 'Save file', 'c:\\', "Json files (*.json)")
    trace("Save as JSON", "File chose. (" + filepath[0] + ")")
    
    with open(filepath[0], 'w') as f:
        data = {}
        data["length"] = pal_index_counter + 1
        data["palette"] = pal
        
        trace("Save as JSON", "JSON file built. Contents: " + str(data))
        f.write(json.dumps(data, ensure_ascii = False))
        trace("Save as JSON", "File saved successfully.")
        f.close()

def savepal():
    filedialog = QFileDialog
    filepath = filedialog.getSaveFileName(main_root, 'Save file', 'c:\\', "Palette files (*.pal)")
    trace("Save as PAL", "File chose. (" + filepath[0] + ")")
    
    ArraytoJascPal(pal, pal_index_counter + 1, filepath[0])

def exportfile():
    export_handler(pal_index_counter + 1)

def palindexchange(i):
    global pal_index
    
    pal_index[0] = i
    trace("Palette handling", "Selected index changed. New value: " + str(i))

def palsizechange(i):
    global pal
    
    trace("Palette handling", "Palette size change requested.")
    if i == 0:
        trace("Palette handling", "New palette size: 16 colors.")
        pal = pal[0:15]
        for ii in range(256, 15, -1):
            pal_list.removeItem(ii)
        pal_index_counter = 15
        if pal_index[0] >= 15:
            pal_index[0] = 15
    else:
        trace("Palette handling", "New palette size: 256 colors.")
        for ii in range(16, 256):
            pal.append([0, 0, 0])
            pal_list.addItem(str(ii))
        pal_index_counter = 255
    
    trace("Palette handling", "Palette size changed.")

def editpalindex():
    global pal
    
    trace("Palette handling", "Palette color change requested for index " + str(pal_index[0]) + ".")
    trace("Palette handling", "Old value: " + str(pal[pal_index[0]]) + ".")
    pal[pal_index[0]] = color_mixer(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])
    trace("Palette handling", "New value: " + str(pal[pal_index[0]]) + ".")
    trace("Palette handling", "New value RGB8: " + str(RGB5toRGB8(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])))

def showpalindex():
    values = "Current color: \nRed: " + str(pal[pal_index[0]][0]) + "\nGreen: " + str(pal[pal_index[0]][1]) + "\nBlue: " + str(pal[pal_index[0]][2]) + "\nHex (16 bit): " + str(RGB5tou16(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2]))
    
    trace("Palette handling", "Palette output requested for index " + str(pal_index[0]) + ".")
    trace("Palette handling", "Current values: " + values)
    alert = QMessageBox()
    alert.setAutoFillBackground(True)
    alert.setText(values)
    bgpal = alert.palette()
    clr = RGB5toRGB8(pal[pal_index[0]][0], pal[pal_index[0]][1], pal[pal_index[0]][2])
    bgpal.setColor(alert.backgroundRole(), QColor(clr[0], clr[1], clr[2]))
    alert.setPalette(bgpal)
    alert.exec_()