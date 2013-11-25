#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore
class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Brushes')
		self.setGeometry(300,300,355,280)
		
	def paintEvent(self,e):
		qp=QtGui.QPainter()
		qp.begin(self)
		self.drawBrushes(qp)
		qp.end()

	def drawBrushes(self,qp):
		brush=QtGui.QBrush(QtCore.Qt.SolidPattern)
		qp.setBrush(brush)
		qp.drawRect(10,15,90,60)

		brush.setStyle(QtCore.Qt.Dense1Pattern)
		qp.setBrush(brush)
		qp.drawRect(130,15,90,60)

		brush.setStyle(QtCore.Qt.Dense2Pattern)
		qp.setBrush(brush)
		qp.drawRect(250,15,90,60)

		brush.setStyle(QtCore.Qt.Dense3Pattern)
		qp.setBrush(brush)
		qp.drawRect(10,105,90,60)

		brush.setStyle(QtCore.Qt.DiagcrossPattern)
		qp.setBrush(brush)
		qp.drawRect(10,105,90,60)

		brush.setStyle(QtCore.Qt.Dense5Pattern)
		qp.setBrush(brush)
		qp.drawRect(130,105,90,60)

		brush.setStyle(QtCore.Qt.Dense6Pattern)
		qp.setBrush(brush)
		qp.drawRect(250,105,90,60)

		brush.setStyle(QtCore.Qt.HorPattern)
		qp.setBrush(brush)
		qp.drawRect(10,195,90,60)

		brush.setStyle(QtCore.Qt.VerPattern)
		qp.setBrush(brush)
		qp.drawRect(130,195,90,60)

		brush.setStyle(QtCore.Qt.BDiagPattern)
		qp.setBrush(brush)
		qp.drawRect(250,195,90,60)

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())