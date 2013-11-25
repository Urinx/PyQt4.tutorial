#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		self.setGeometry(400,300,350,250)
		self.setWindowTitle('toolbar')
		
		exit=QtGui.QAction(QtGui.QIcon('apple.png'),'Exit',self)
		exit.setShortcut('Ctrl+Q')
		exit.triggered.connect(QtGui.qApp.quit)
		
		toolbar=self.addToolBar('Exit')
		toolbar.addAction(exit)

app=QtGui.QApplication(sys.argv)
mainw=MainWindow()
mainw.show()
sys.exit(app.exec_())