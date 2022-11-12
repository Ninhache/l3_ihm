import MenuBar
import TextEditor
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("tp1")
		self.resize(800, 600)
		self.show()

		# create menu bar
		self.menuBar = MenuBar.MenuBar(self)
		self.setMenuBar(self.menuBar)

		# create a text editor
		self.centralWidget = TextEditor.TextEditor(self)
		self.setCentralWidget(self.centralWidget)

		# add a status bar
		self.statusBar = QStatusBar(self)
		self.setStatusBar(self.statusBar)

		# add things to the status bar
		self.statusBar.showMessage("I'm useless atm")


