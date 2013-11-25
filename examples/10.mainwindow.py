#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		self.setGeometry(400,300,350,250)
		self.setWindowTitle('mainwindow')
		
		textEdit=QtGui.QTextEdit()
		self.setCentralWidget(textEdit)

		exit=QtGui.QAction(QtGui.QIcon('apple.png'),'Exit',self)
		exit.setShortcut('Ctrl+Q')
		exit.setStatusTip('Exit application')
		exit.triggered.connect(QtGui.qApp.quit)
		
		self.statusBar()
		toolbar=self.addToolBar('Exit')
		toolbar.addAction(exit)
		menubar=self.menuBar()
		filemenu=menubar.addMenu('&File')
		filemenu.addAction(exit)

app=QtGui.QApplication(sys.argv)
mainw=MainWindow()
mainw.show()
sys.exit(app.exec_())