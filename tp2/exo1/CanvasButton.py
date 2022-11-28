from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import ButtonModel

class CanvasButton(QWidget):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.createButton()
		#self.cursorOver = False
		# draw elipse
		self.bbox = QRect(0, 0, 100, 100)
		self.defaultColor = QColor(100,100,100)

		# hoverCol et pressCol 
		self.hoverCol = QColor(65, 166, 255)
		self.pressCol = QColor(71, 65, 255)

		self.setMouseTracking(True)

		self.mouseMoveEvent = self.mouseMoveEvent
		self.mousePressEvent = self.mousePressEvent
		self.mouseReleaseEvent = self.mouseReleaseEvent


		self.model = ButtonModel.ButtonModel(self)

	def createButton(self):
		self.setFixedSize(self.parent.width(), self.parent.height())

	def mouseMoveEvent(self, event):
		if (self.cursorOnEllipse(event.pos())):
			self.model.enterHover()
		else:
			self.model.leaveHover()
		self.repaint()

	def mousePressEvent(self, event):
		if (self.cursorOnEllipse(event.pos())):
			self.model.entrePress()
			self.repaint()

	def mouseReleaseEvent(self, event):
		self.model.leavePress()
		self.repaint()

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		pen = QPen()
		pen.setWidth(2)
		pen.setColor(QColor(0,0,0))
		painter.setPen(pen)
		
		if self.model.state == ButtonModel.State.IDLE:
			painter.setBrush(self.defaultColor)
		elif self.model.state == ButtonModel.State.HOVER:
			painter.setBrush(self.hoverCol)
		elif self.model.state == ButtonModel.State.PRESSIN:
			painter.setBrush(self.pressCol)
		elif self.model.state == ButtonModel.State.PRESSOUT:
			painter.setBrush(self.defaultColor)

		painter.drawEllipse(self.bbox)



		


	def cursorOnEllipse(self, point):
		return self.bbox.contains(point)
