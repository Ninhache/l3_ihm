from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TextEditor(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.createTextEditor()
        self.openedFile = ""

    def createTextEditor(self):
        self.setPlainText("")

    def openFile(self):
        self.openedFile = QFileDialog.getOpenFileName(self.parent, "Open File", "", "All Files (*)")[0]
        if self.openedFile != "":
            file = open(self.openedFile, "r")
            self.setPlainText(file.read())
            file.close()
    
    def saveFile(self):
        if self.openedFile == "":
            self.saveAsFile()
        else:
            file = open(self.openedFile, "w")
            file.write(self.toPlainText())
            file.close()

    def saveAsFile(self):
        self.openedFile = QFileDialog.getSaveFileName(self.parent, "Save File", "", "All Files (*)")[0]
        if self.openedFile != "":
            file = open(self.openedFile, "w")
            file.write(self.toPlainText())
            file.close()

    def newFile(self):
        if self.toPlainText() != "":
            msg = QMessageBox()
            msg.setText("Do you want to save the current file?")
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Save)
            ret = msg.exec_()
            if ret == QMessageBox.Save:
                self.saveFile()
            elif ret == QMessageBox.Cancel:
                return
        self.openedFile = ""
        self.setPlainText("")
