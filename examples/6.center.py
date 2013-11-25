#! /usr/bin/python
import sys
from PyQt4 import QtGui

class Center(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setWindowTitle('center')
		self.resize(250,150)
		self.center()
	def center(self):
		screen=QtGui.QDesktopWidget().screenGeometry()
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

app=QtGui.QApplication(sys.argv)
center=Center()
center.show()
sys.exit(app.exec_())