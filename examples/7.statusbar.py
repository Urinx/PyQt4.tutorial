#! /usr/bin/python
import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle('statusbar')
		self.resize(250,150)
		self.move(300,300)
		#statusBar() can only be used in the QMainWindow
		self.statusBar().showMessage('Ready')

app=QtGui.QApplication(sys.argv)
mainw=MainWindow()
mainw.show()
sys.exit(app.exec_())