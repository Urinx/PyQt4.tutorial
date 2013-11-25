#! /usr/bin/python
import sys,random
from PyQt4 import QtGui,QtCore
class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Points')
		self.setGeometry(300,300,250,150)
		
	def paintEvent(self,e):
		qp=QtGui.QPainter()
		qp.begin(self)
		self.drawPoints(qp)
		qp.end()

	def drawPoints(self,qp):
		qp.setPen(QtCore.Qt.red)
		#qp.setPen(QtGui.QColor(0,0,255))
		size=self.size()
		for i in range(1000):
			x=random.randint(1,size.width()-1)
			y=random.randint(1,size.height()-1)
			qp.drawPoint(x,y)

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())