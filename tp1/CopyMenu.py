from PyQt5.QtWidgets import *

class CopyMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setTitle("Copy")

        self.createMenu()

    def createMenu(self):
        self.addAction("Copy file")
        self.actions()[0].setShortcut("Ctrl+c")
        self.actions()[0].triggered.connect(self.action)

    def action(self):
        print("copy file")

