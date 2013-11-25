#! /usr/bin/python
import sys,random
from PyQt4 import QtGui,QtCore
class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Colors')
		self.setGeometry(300,300,350,280)
		
	def paintEvent(self,e):
		qp=QtGui.QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self,qp):
		color=QtGui.QColor(0,0,0)
		color.setNamedColor('#d4d4d4')
		qp.setPen(color)

		#drawRect(x,y,w,h)
		qp.setBrush(QtGui.QColor(255,0,0,80))
		qp.drawRect(10,15,90,60)
		qp.setBrush(QtGui.QColor(255,0,0,160))
		qp.drawRect(130,15,90,60)
		qp.setBrush(QtGui.QColor(255,0,0,255))
		qp.drawRect(250,15,90,60)
		qp.setBrush(QtGui.QColor(10,163,2,55))
		qp.drawRect(10,105,90,60)
		qp.setBrush(QtGui.QColor(160,100,0,255))
		qp.drawRect(130,105,90,60)
		qp.setBrush(QtGui.QColor(60,100,60,255))
		qp.drawRect(250,105,90,60)
		qp.setBrush(QtGui.QColor(50,50,50,255))
		qp.drawRect(10,195,90,60)
		qp.setBrush(QtGui.QColor(50,150,50,255))
		qp.drawRect(130,195,90,60)
		qp.setBrush(QtGui.QColor(223,135,19,255))
		qp.drawRect(250,195,90,60)

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())