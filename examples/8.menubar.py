#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle('menubar')
		self.resize(350,250)
		self.move(300,300)

		exit=QtGui.QAction(QtGui.QIcon('apple.png'),'Exit',self)
		exit.setShortcut('Ctrl+Q')
		exit.setStatusTip('Exit application')
		exit.setWhatsThis('This is exit')
		exit.triggered.connect(QtGui.qApp.quit)
		
		self.statusBar()
		menubar=self.menuBar()
		filemenu=menubar.addMenu('&File')
		filemenu.addAction(exit)

app=QtGui.QApplication(sys.argv)
mainw=MainWindow()
mainw.show()
sys.exit(app.exec_())