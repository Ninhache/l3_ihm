from enum import Enum

class State(Enum):
    IDLE = 0
    PRESSIN = 1
    PRESSOUT = 2

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Trace

class CanvasDessin(QWidget):
	def __init__(self, parent):
		super().__init__(parent)

		self.setMouseTracking(True)
		self.state = State.IDLE
		self.trace = []

	def addPoint(self, point):
		self.trace[-1].addPoint(point)

	def mousePressEvent(self, event):
		self.state = State.PRESSIN
		self.trace.append(Trace.Trace(1, QColor(0, 0, 0)))
		self.update()

	def mouseReleaseEvent(self, event):
		self.state = State.PRESSOUT

	def mouseMoveEvent(self, event):
		if self.state == State.PRESSIN:
			self.addPoint(event.pos())
		self.update()

	def leaveEvent(self, event):
		self.state = State.IDLE
		
	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		for t in self.trace:
			painter.setPen(QPen(t.color, t.width, Qt.SolidLine))
			for i in range(len(t.points) - 1):
				painter.drawLine(t.points[i], t.points[i+1])
		painter.end()
		
				
		

