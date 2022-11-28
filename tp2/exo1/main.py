import sys
import MainWindow
from PyQt5.QtWidgets import *

def main():
	# create instance of MainWindow
	app = QApplication(sys.argv)
	window = MainWindow.MainWindow()
	
	# run the app
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	print("execution du programme")
	main()