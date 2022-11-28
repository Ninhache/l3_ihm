import CanvasDessin
from PyQt5.QtWidgets import *

class Dessin(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("tp2")
		self.resize(400, 400)
		self.setMinimumSize(400, 400)
		self.setMaximumSize(400, 400)
		self.setWindowTitle("Dessin")
		self.show()
		self.setCentralWidget(CanvasDessin.CanvasDessin(self))