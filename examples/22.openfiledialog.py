#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.textEdit=QtGui.QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()
		self.setFocus()

		openFile=QtGui.QAction(QtGui.QIcon(''),'Open',self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)

		menubar=self.menuBar()
		fileMenu=menubar.addMenu('&File')
		fileMenu.addAction(openFile)
		self.setWindowTitle('OpenFile')
		self.setGeometry(300,300,350,300)

	def showDialog(self):
		filename=QtGui.QFileDialog.getOpenFileName(self,'Open file','/home')
		f=open(filename)
		data=f.read()
		self.textEdit.setText(data)
	
if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())