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
		for trace in self.trace:
			painter.setPen(QPen(trace.color, trace.width))
			path = QPainterPath()
			
			if len(trace.points) > 0:
				path.moveTo(trace.points[0])
				for point in trace.points:
					path.lineTo(point)
				painter.drawPath(path)

		painter.end()
