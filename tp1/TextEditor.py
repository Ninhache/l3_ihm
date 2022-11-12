from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TextEditor(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.createTextEditor()
        self.fileName = ""
        self.saved = True
        self.textChanged.connect(self.textChangedEvent)

    def createTextEditor(self):
        self.setPlainText("")

    def textChangedEvent(self):
        self.saved = False
        self.parent.statusBar.showMessage(self.fileName + " (unsaved)")

    def openFile(self):
        # self.file = QFileDialog.getOpenFileName(self.parent, "Open File", "", "All Files (*)")
        # open txt or html
        self.file = QFileDialog.getOpenFileName(self.parent, "Open File", "", "Text Files (*.txt);;HTML Files (*.html)")
        # get file extension
        self.fileExtension = self.file[0].split(".")[-1]
        self.fileName = self.file[0]
        print(self.file)
        print(self.fileName)
        print(self.fileExtension)

        if self.fileName != "":
            if self.fileExtension == "html":
                file = open(self.fileName, "r")
                self.setHtml(file.read())
                file.close()
            else:
                file = open(self.fileName, "r")
                self.setPlainText(file.read())
                file.close()
            self.parent.statusBar.showMessage(self.fileName)
    
    def saveFile(self):
        if self.fileName == "":
            self.saveAsFile()
        else:
            file = open(self.fileName, "w")
            file.write(self.toPlainText())
            file.close()
            self.parent.statusBar.showMessage(self.fileName)

    def saveAsFile(self):
        self.fileName = QFileDialog.getSaveFileName(self.parent, "Save File", "", "All Files (*)")[0]
        if self.fileName != "":
            file = open(self.fileName, "w")
            file.write(self.toPlainText())
            file.close()
            self.parent.statusBar.showMessage(self.fileName)

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
        self.fileName = ""
        self.setPlainText("")
