from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CanvasButton(QWidget):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.createButton()
		self.cursorOver = False

		self.bbox = QRect(10,10,100,100)
		self.defaultColor = QColor(0,0,0)

		self.mouseMoveEvent = self.mouseMoveEvent
		self.mousePressEvent = self.mousePressEvent
		self.mouseReleaseEvent = self.mouseReleaseEvent

	def createButton(self):
		self.setFixedSize(self.parent.width(), self.parent.height())

	def mouseMoveEvent(self, event):
		self.cursorOver = self.cursorOnEllipse(event.pos())
		if self.bbox.contains(event.pos()):
			self.defaultColor = QColor(255,0,0)
		else:
			self.defaultColor = QColor(0,0,0)
		self.repaint()

	def mousePressEvent(self, event):
		if self.bbox.contains(event.pos()):
			self.defaultColor = QColor(0,255,0)
		else:
			self.defaultColor = QColor(0,0,0)
		self.repaint()

	def mouseReleaseEvent(self, event):
		if self.bbox.contains(event.pos()):
			self.defaultColor = QColor(0,0,255)
		else:
			self.defaultColor = QColor(0,0,0)
		self.repaint()

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(self.defaultColor)
		painter.drawRect(self.bbox)

	def cursorOnEllipse(self, point):
		return self.bbox.contains(point)
