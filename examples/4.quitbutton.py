#! /usr/bin/env python
import sys
from PyQt4 import QtGui, QtCore

class QuitButton(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Quit button')
		#QPushButton(string text, QWidget parent = None)
		quit=QtGui.QPushButton('Close',self)
		quit.setGeometry(93,57.5,64,35)
		self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))

app=QtGui.QApplication(sys.argv)
qb=QuitButton()
qb.show()
sys.exit(app.exec_())