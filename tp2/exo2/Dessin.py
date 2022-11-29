import CanvasDessin
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Slider(QSlider):
    def mousePressEvent(self, event):
        super(Slider, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)

    def pixelPosToRangeValue(self, pos):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

        if self.orientation() == Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == Qt.Horizontal else pr.y()
        return QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin, sliderMax - sliderMin, opt.upsideDown)


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

		self.toolbar = QToolBar("Toolbar")
		self.addToolBar(self.toolbar)
		
		self._createToolBars()

	def _createToolBars(self):
		
		# add pixmap to show actual color
		pixmap = QPixmap(16, 16)
		pixmap.fill(self.centralWidget().color)
		icon = QIcon(pixmap)
		colorButton = QPushButton()
		colorButton.setStyleSheet("QPushButton {border: none;}")
		colorButton.setIcon(icon)
		colorButton.clicked.connect(self._openColorDialog)
		self.toolbar.addWidget(colorButton)
		
		slider = Slider(Qt.Horizontal)
		slider.setMinimum(1)
		slider.setMaximum(20)
		slider.setValue(5)
		slider.valueChanged.connect(self._setWidth)
		self.toolbar.addWidget(slider)

		spinbox = QSpinBox()
		spinbox.setMinimum(1)
		spinbox.setMaximum(20)
		spinbox.setValue(5)
		spinbox.valueChanged.connect(self._setWidth)
		self.toolbar.addWidget(spinbox)

		action = QAction("Clear", self)
		action.triggered.connect(self.centralWidget().clear)
		self.toolbar.addAction(action)

	def _setWidth(self, width):
		self.centralWidget().width = width

		self.toolbar.findChild(QSpinBox).setValue(width)
		self.toolbar.findChild(QSlider).setValue(width)

	def _openColorDialog(self):
		color = QColorDialog.getColor()
		if color.isValid():
			self.centralWidget().color = color
			
			pixmap = QPixmap(16, 16)
			pixmap.fill(color)
			self.toolbar.findChild(QPushButton).setIcon(QIcon(pixmap))

		
