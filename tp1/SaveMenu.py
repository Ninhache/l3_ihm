from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class SaveMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setTitle("Save")
        self.createMenu()

    def createMenu(self):
        self.addAction("save", self.saveFile, QKeySequence.Save)

    def saveFile(self):
        self.parent.parent.centralWidget.saveFile()

