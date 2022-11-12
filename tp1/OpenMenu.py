from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class OpenMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setTitle("File")
        self.createMenu()

    def createMenu(self):
        self.addAction("New File", self.newFile, QKeySequence.New)
        self.addAction("Open File", self.openFile, QKeySequence.Open)
        
    def newFile(self):
        self.parent.parent.centralWidget.newFile()

    def openFile(self):
        self.parent.parent.centralWidget.openFile()
        
