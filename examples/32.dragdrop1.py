#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Simple Drag & Drop')
		self.setGeometry(300,300,300,150)

		edit=QtGui.QLineEdit('Drag this to button',self)
		edit.setDragEnabled(True)
		edit.move(30,65)
		button=Button('Drop here',self)
		button.move(190,65)

class Button(QtGui.QPushButton):
	def __init__(self,title,parent):
		super(Button, self).__init__(title,parent)
		self.setAcceptDrops(True)
	
	def dragEnterEvent(self,e):
		if e.mimeData().hasFormat('text/plain'):
			e.accept()
		else:
			e.ignore()

	def dropEvent(self,e):
		self.setText(e.mimeData().text())

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())