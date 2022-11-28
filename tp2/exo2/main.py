import sys
import Dessin
from PyQt5.QtWidgets import *

def main():

	app = QApplication(sys.argv)
	window = Dessin.Dessin()
	
	window.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	print("execution du programme")
	main()