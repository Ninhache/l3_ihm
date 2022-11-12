from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QuitMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setTitle("Quit")
        self.createMenu()

    def createMenu(self):
        self.addAction("Quit")
        self.actions()[0].setShortcut("Ctrl+q")
        self.actions()[0].triggered.connect(self.action)
        
    def action(self):
        self.parent.parent.closeEvent(QCloseEvent())
        


