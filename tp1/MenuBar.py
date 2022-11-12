import OpenMenu
import SaveMenu
import CopyMenu
import QuitMenu
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MenuBar(QMenuBar):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.createMenuBar()

	def createMenuBar(self):
		self.openMenu = self.addMenu(OpenMenu.OpenMenu(self))
		self.saveMenu = self.addMenu(SaveMenu.SaveMenu(self))
		self.copyMenu = self.addMenu(CopyMenu.CopyMenu(self))
		self.quitMenu = self.addMenu(QuitMenu.QuitMenu(self))
