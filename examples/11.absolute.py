#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle('Absolute')
	 	self.resize(250,150)
		label1=QtGui.QLabel('Uricode',self)
		label1.move(15,10)
		label2=QtGui.QLabel('tutorials for programmers',self)
		label2.move(35,40)

app=QtGui.QApplication(sys.argv)
ex=Example()
ex.show()
sys.exit(app.exec_())