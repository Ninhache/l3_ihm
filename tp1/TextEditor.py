from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TextEditor(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.createTextEditor()

    def createTextEditor(self):
        self.setPlainText("Hello World")
