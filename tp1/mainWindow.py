import sys
from PyQt5.QtWidgets import *

def main(args):
	app = QApplication(args)
	window = QMainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	print("execution du programme")
	main(sys.argv)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("tp1")
		self.resize(800, 600)
		self.show()