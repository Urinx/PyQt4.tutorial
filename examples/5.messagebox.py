#! /usr/bin/env python
import sys
from PyQt4 import QtGui, QtCore

class MessageBox(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Message box')
	
	def closeEvent(self,event):
		reply=QtGui.QMessageBox.question(self,'Message','Are you sure to quit?',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
		if reply==QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

app=QtGui.QApplication(sys.argv)
qb=MessageBox()
qb.show()
sys.exit(app.exec_())