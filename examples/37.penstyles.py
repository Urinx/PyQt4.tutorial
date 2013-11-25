#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore
class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Penstyles')
		self.setGeometry(300,300,280,270)
		
	def paintEvent(self,e):
		qp=QtGui.QPainter()
		qp.begin(self)
		self.doDrawing(qp)
		qp.end()

	def doDrawing(self,qp):
		pen=QtGui.QPen(QtCore.Qt.black,2,QtCore.Qt.SolidLine)
		qp.setPen(pen)
		qp.drawLine(20,40,250,40)

		pen.setStyle(QtCore.Qt.DashLine)
		qp.setPen(pen)
		qp.drawLine(20,80,250,80)

		pen.setStyle(QtCore.Qt.DashDotLine)
		qp.setPen(pen)
		qp.drawLine(20,120,250,120)

		pen.setStyle(QtCore.Qt.DotLine)
		qp.setPen(pen)
		qp.drawLine(20,160,250,160)

		pen.setStyle(QtCore.Qt.DashDotDotLine)
		qp.setPen(pen)
		qp.drawLine(20,200,250,200)

		pen.setStyle(QtCore.Qt.CustomDashLine)
		pen.setDashPattern([1,3,5,4])
		qp.setPen(pen)
		qp.drawLine(20,240,250,240)

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())