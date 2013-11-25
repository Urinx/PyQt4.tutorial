#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		hbox=QtGui.QHBoxLayout(self)
		pixmap=QtGui.QPixmap('apple2.jpg')
		label=QtGui.QLabel(self)
		label.setPixmap(pixmap)
		
		hbox.addWidget(label)
		self.setLayout(hbox)
		self.setWindowTitle('Pixmap')
		self.setGeometry(300,300,350,300)

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())