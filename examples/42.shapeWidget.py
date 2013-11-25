#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class ShapeWidget(QtGui.QWidget):
	def __init__(self):
		super(ShapeWidget,self).__init__()

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		pix=QtGui.QPixmap("iphone-big-image.png","0")
		#pix=QtGui.QPixmap("iphone-big-image.png","0",QtCore.Qt.AvoidDither|QtCore.Qt.ThresholdDither|QtCore.Qt.ThresholdAlphaDither)

		self.resize(pix.size())
		self.setMask(pix.mask())
		self.dragPosition=None

	def mousePressEvent(self,event):
		if event.button()==QtCore.Qt.LeftButton:
			self.dragPosition=event.globalPos()-self.frameGeometry().topLeft()
			event.accept()

		if event.button()==QtCore.Qt.RightButton:
			self.close()

	def mouseMoveEvent(self,event):
		if event.buttons() & QtCore.Qt.LeftButton:
			self.move(event.globalPos()-self.dragPosition)
			event.accept()

	def paintEvent(self,event):
		painter=QtGui.QPainter(self)
		painter.drawPixmap(0,0,QtGui.QPixmap("iphone-big-image.png"))

app=QtGui.QApplication(sys.argv)
form=ShapeWidget()
form.show()
app.exec_()