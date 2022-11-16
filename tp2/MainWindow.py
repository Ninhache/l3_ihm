import CanvasButton
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("tp2")
		self.resize(800, 600)
		self.show()
		self.setCentralWidget(CanvasButton.CanvasButton(self))
